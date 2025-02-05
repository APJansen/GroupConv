from keras import ops

from groco import utils


class Group:
    """
    Class representing a group along with its actions on a grid.

    Args:
        name: string, name of the group.
        order: int, the number of elements in the group.
        inverses: 1d tensor indicating the inverse of element i at position i.
        composition: 2d tensor with entry composition[r][c] the index of the group element
            obtained by composing the inverse of the rth element with the cth element.
        subgroup: dictionary from subgroup strings to indices representing the elements in
            the subgroup.
        cosets: dictionary from subgroup strings to indices representing the elementary coset
            representatives of the corresponding subgroup.
        action: callable, the action of the group on a signal on the grid.
        parent: Group, the parent group of the group.

    Methods:
        action: performs the action of the whole group on a signal on the grid
            or on the group itself.
    """

    def __init__(
        self,
        name: str,
        order: int,
        inverses=None,
        composition=None,
        subgroup=None,
        cosets=None,
        action=None,
        parent=None,
    ):
        self.name = name
        self.order = order
        self.parent = parent
        self.composition = self._compute_composition(composition)
        self.inverses = self._compute_inverses(inverses)
        self.subgroup = self._compute_subgroup(subgroup)
        self.cosets = self._compute_cosets(cosets)
        self._action = self._compute_action(action)

    def action(
        self,
        signal,
        spatial_axes: tuple = (1, 2),
        new_group_axis: int = 0,
        group_axis=None,
        acting_group: str = "",
        domain_group: str = "",
    ):
        """
        The action of the group on a given signal.

        Args:
            signal: The tensor to act on.
            spatial_axes: Tuple indicating which are the spatial axes, defaults to (1, 2).
            new_group_axis: Which axis in the output to concatenate the group elements' actions
                on, defaults to 0.
            group_axis: The group axis of the input, defaults to None, meaning a signal only
                on the grid.
            acting_group: Name of subgroup with which to act, defaults to None meaning
                the whole group.
            domain_group: Name of subgroup signal lives on, defaults to None meaning
                the whole group.

        Returns:
            Tensor of the signal acted on by the group.
        """
        acting_group, domain_group = self.parse_subgroups(acting_group, domain_group)
        action = self._action_on_group if domain_group else self._action_on_grid
        signal = action(
            signal,
            spatial_axes=spatial_axes,
            new_group_axis=new_group_axis,
            group_axis=group_axis,
            acting_group=acting_group,
            domain_group=domain_group,
        )
        return signal

    def _action_on_grid(
        self,
        signal,
        new_group_axis: int,
        spatial_axes: tuple,
        acting_group: str,
        **kwargs,
    ):
        signal = self._action(signal, spatial_axes=spatial_axes, new_group_axis=new_group_axis)
        signal = ops.take(signal, axis=new_group_axis, indices=self.subgroup[acting_group])
        return signal

    def _action_on_group(
        self,
        signal,
        new_group_axis: int,
        spatial_axes: tuple,
        acting_group: str,
        group_axis: int,
        domain_group: str,
    ):
        """
        Act on a signal on the group.

        If acting_group is set to a subgroup, only act with that subgroup on a signal on
        the whole group.
        If domain_group is set to a subgroup, act with whole group on a signal on the subgroup,
        where the signal is set to 0 outside of the subgroup.
        """
        acting_group_order = len(self.subgroup[acting_group])
        domain_group_order = len(self.subgroup[domain_group])
        # fill in zeroes outside of domain group if necessary
        if domain_group_order < self.order:
            signal = self.upsample(signal, group_axis, domain_group)

        # action on grid
        signal = self._action_on_grid(
            signal, new_group_axis=group_axis, spatial_axes=spatial_axes, acting_group=acting_group
        )

        # act on point group:
        signal = utils.merge_axes(signal, group_axis, group_axis + 1)
        composition_indices = self._composition_flat_indices(acting_group, domain_group)
        signal = ops.take(signal, axis=group_axis, indices=composition_indices)
        signal = utils.split_axes(signal, acting_group_order, group_axis)

        signal = ops.moveaxis(signal, group_axis, new_group_axis)

        return signal

    def upsample(self, signal, group_axis, domain_group):
        domain_group_indices = self.subgroup[domain_group]
        zeros = ops.zeros(
            shape=signal.shape[:group_axis] + (1,) + signal.shape[group_axis + 1 :],
            dtype=signal.dtype,
        )
        filled_signal = []
        index_to_subgroup = {val: index for index, val in enumerate(domain_group_indices)}
        for i in range(self.order):
            if i in domain_group_indices:
                x = ops.take(signal, axis=group_axis, indices=[index_to_subgroup[i]])
            else:
                x = zeros
            filled_signal.append(x)
        return ops.concatenate(filled_signal, axis=group_axis)

    def _composition_flat_indices(self, acting_group, domain_group):
        acting_inv_indices = [self.inverses[i] for i in self.subgroup[acting_group]]
        subgroup_composition = ops.take(self.composition, axis=0, indices=acting_inv_indices)
        subgroup_composition = ops.take(
            subgroup_composition, axis=1, indices=self.subgroup[domain_group]
        )
        group_composition_indices = ops.cast(
            [[i * self.order + c for c in row] for i, row in enumerate(subgroup_composition)],
            dtype="int32",
        )
        return ops.reshape(group_composition_indices, [-1])

    def _compute_inverses(self, inverses):
        if inverses is not None:
            return ops.cast(inverses, dtype="int32")
        return [
            [c for c in range(self.order) if self.composition[r][c] == 0][0]
            for r in range(self.order)
        ]

    def _compute_composition(self, composition):
        """Compute the composition induced by the parent group."""
        if composition is not None:
            return ops.cast(composition, dtype="int32")

        parent_indices = self.parent.subgroup[self.name]
        composition = ops.take(self.parent.composition, indices=parent_indices, axis=0)
        composition = ops.take(composition, indices=parent_indices, axis=1)
        composition = ops.convert_to_numpy(composition)
        composition = [
            self._external_to_internal_indices(composition[r]) for r in range(self.order)
        ]
        return ops.cast(composition, dtype="int32")

    def _compute_action(self, action):
        if action is not None:
            return action

        def subgroup_action(signal, spatial_axes, new_group_axis):
            signal = self.parent._action(signal, spatial_axes, new_group_axis)
            signal = ops.take(signal, indices=self.parent.subgroup[self.name], axis=new_group_axis)
            return signal

        return subgroup_action

    def _compute_subgroup(self, subgroup):
        if subgroup is not None:
            return subgroup
        parent_subgroups = self.parent.subgroup
        this_subgroup = set(parent_subgroups[self.name])
        subgroups = {
            name: self._external_to_internal_indices(indices)
            for name, indices in parent_subgroups.items()
            if set(indices).issubset(this_subgroup)
        }
        return subgroups

    def _compute_cosets(self, cosets):
        if cosets is not None:
            return cosets
        parent_cosets = self.parent.cosets
        this_subgroup = set(self.parent.subgroup[self.name])
        cosets = {
            name: self._external_to_internal_indices([i for i in indices if i in this_subgroup])
            for name, indices in parent_cosets.items()
            if name in self.subgroup.keys()
        }
        return cosets

    def _external_to_internal_indices(self, external_indices):
        """
        Translate indices of elements in parent group, to indices within the subgroup.

        Args:
            external_indices: 1d tensor of indices of subgroup elements viewed from within the
                parent group.

        Returns:
            1d tensor of indices of the same elements, but viewed from within the subgroup.
        """
        # the relation between a subgroup's internal indices and its indices from within the parent
        # group is that the internal indices are simply a range from 0 to the order, and they
        # correspond to the indices in the parent group as given by the subgroup_external_indices.
        # e.g.:
        # subgroup_external_indices: [0, 3, 5, 7]
        # subgroup_internal_indices: [0, 1, 2, 3]
        # external_indices: [7, 3]
        # internal_indices: [3, 1]
        subgroup_external_indices = self.parent.subgroup[self.name]
        subgroup_internal_indices = list(range(self.order))

        external_to_internal = {
            e: v for e, v in zip(subgroup_external_indices, subgroup_internal_indices)
        }
        internal_indices = [external_to_internal[i] for i in external_indices]
        return internal_indices

    def parse_subgroup(self, subgroup):
        parser = {None: None, "": self.name}
        return subgroup if subgroup else parser[subgroup]

    def parse_subgroups(self, *subgroups):
        parser = {None: None, "": self.name}
        return tuple(subgroup if subgroup else parser[subgroup] for subgroup in subgroups)
