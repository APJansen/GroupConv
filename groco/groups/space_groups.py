import itertools

from keras import ops

from groco.groups import Group

Oh_flip_axes = [[], [1, 2], [0, 2], [0, 1], [2], [1], [0], [0, 1, 2]]
Oh_permutation_tuples = [(0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1), (2, 1, 0), (1, 0, 2)]
Oh_parameters = list(itertools.product(Oh_permutation_tuples, Oh_flip_axes))


def Oh_action(signal, spatial_axes=(0, 1, 2), new_group_axis=3):
    offset = spatial_axes[0]
    prefix = tuple(range(offset))
    suffix = tuple(range(offset + 3, ops.ndim(signal)))
    Oh_params = [
        (prefix + tuple(p + offset for p in perm) + suffix, [f + offset for f in flip])
        for (perm, flip) in Oh_parameters
    ]
    transformed_signals = []
    for perm, flip in Oh_params:
        transformed_signal = signal
        for f in flip:
            transformed_signal = ops.flip(transformed_signal, axis=f)
        transformed_signal = ops.expand_dims(
            ops.transpose(transformed_signal, perm), axis=new_group_axis
        )
        transformed_signals.append(transformed_signal)
    transformed_signals = ops.concatenate(transformed_signals, axis=new_group_axis)
    return transformed_signals


Oh = Group(
    name="Oh",
    order=48,
    composition=[
        [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
        ],
        [
            1,
            0,
            3,
            2,
            5,
            4,
            7,
            6,
            10,
            11,
            8,
            9,
            14,
            15,
            12,
            13,
            19,
            18,
            17,
            16,
            23,
            22,
            21,
            20,
            25,
            24,
            27,
            26,
            29,
            28,
            31,
            30,
            35,
            34,
            33,
            32,
            39,
            38,
            37,
            36,
            42,
            43,
            40,
            41,
            46,
            47,
            44,
            45,
        ],
        [
            2,
            3,
            0,
            1,
            6,
            7,
            4,
            5,
            11,
            10,
            9,
            8,
            15,
            14,
            13,
            12,
            17,
            16,
            19,
            18,
            21,
            20,
            23,
            22,
            27,
            26,
            25,
            24,
            31,
            30,
            29,
            28,
            34,
            35,
            32,
            33,
            38,
            39,
            36,
            37,
            41,
            40,
            43,
            42,
            45,
            44,
            47,
            46,
        ],
        [
            3,
            2,
            1,
            0,
            7,
            6,
            5,
            4,
            9,
            8,
            11,
            10,
            13,
            12,
            15,
            14,
            18,
            19,
            16,
            17,
            22,
            23,
            20,
            21,
            26,
            27,
            24,
            25,
            30,
            31,
            28,
            29,
            33,
            32,
            35,
            34,
            37,
            36,
            39,
            38,
            43,
            42,
            41,
            40,
            47,
            46,
            45,
            44,
        ],
        [
            4,
            5,
            6,
            7,
            0,
            1,
            2,
            3,
            14,
            15,
            12,
            13,
            10,
            11,
            8,
            9,
            21,
            20,
            23,
            22,
            17,
            16,
            19,
            18,
            29,
            28,
            31,
            30,
            25,
            24,
            27,
            26,
            38,
            39,
            36,
            37,
            34,
            35,
            32,
            33,
            44,
            45,
            46,
            47,
            40,
            41,
            42,
            43,
        ],
        [
            5,
            4,
            7,
            6,
            1,
            0,
            3,
            2,
            12,
            13,
            14,
            15,
            8,
            9,
            10,
            11,
            22,
            23,
            20,
            21,
            18,
            19,
            16,
            17,
            28,
            29,
            30,
            31,
            24,
            25,
            26,
            27,
            37,
            36,
            39,
            38,
            33,
            32,
            35,
            34,
            46,
            47,
            44,
            45,
            42,
            43,
            40,
            41,
        ],
        [
            6,
            7,
            4,
            5,
            2,
            3,
            0,
            1,
            13,
            12,
            15,
            14,
            9,
            8,
            11,
            10,
            20,
            21,
            22,
            23,
            16,
            17,
            18,
            19,
            30,
            31,
            28,
            29,
            26,
            27,
            24,
            25,
            36,
            37,
            38,
            39,
            32,
            33,
            34,
            35,
            45,
            44,
            47,
            46,
            41,
            40,
            43,
            42,
        ],
        [
            7,
            6,
            5,
            4,
            3,
            2,
            1,
            0,
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            23,
            22,
            21,
            20,
            19,
            18,
            17,
            16,
            31,
            30,
            29,
            28,
            27,
            26,
            25,
            24,
            39,
            38,
            37,
            36,
            35,
            34,
            33,
            32,
            47,
            46,
            45,
            44,
            43,
            42,
            41,
            40,
        ],
        [
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
        ],
        [
            9,
            8,
            11,
            10,
            13,
            12,
            15,
            14,
            18,
            19,
            16,
            17,
            22,
            23,
            20,
            21,
            3,
            2,
            1,
            0,
            7,
            6,
            5,
            4,
            33,
            32,
            35,
            34,
            37,
            36,
            39,
            38,
            43,
            42,
            41,
            40,
            47,
            46,
            45,
            44,
            26,
            27,
            24,
            25,
            30,
            31,
            28,
            29,
        ],
        [
            10,
            11,
            8,
            9,
            14,
            15,
            12,
            13,
            19,
            18,
            17,
            16,
            23,
            22,
            21,
            20,
            1,
            0,
            3,
            2,
            5,
            4,
            7,
            6,
            35,
            34,
            33,
            32,
            39,
            38,
            37,
            36,
            42,
            43,
            40,
            41,
            46,
            47,
            44,
            45,
            25,
            24,
            27,
            26,
            29,
            28,
            31,
            30,
        ],
        [
            11,
            10,
            9,
            8,
            15,
            14,
            13,
            12,
            17,
            16,
            19,
            18,
            21,
            20,
            23,
            22,
            2,
            3,
            0,
            1,
            6,
            7,
            4,
            5,
            34,
            35,
            32,
            33,
            38,
            39,
            36,
            37,
            41,
            40,
            43,
            42,
            45,
            44,
            47,
            46,
            27,
            26,
            25,
            24,
            31,
            30,
            29,
            28,
        ],
        [
            12,
            13,
            14,
            15,
            8,
            9,
            10,
            11,
            22,
            23,
            20,
            21,
            18,
            19,
            16,
            17,
            5,
            4,
            7,
            6,
            1,
            0,
            3,
            2,
            37,
            36,
            39,
            38,
            33,
            32,
            35,
            34,
            46,
            47,
            44,
            45,
            42,
            43,
            40,
            41,
            28,
            29,
            30,
            31,
            24,
            25,
            26,
            27,
        ],
        [
            13,
            12,
            15,
            14,
            9,
            8,
            11,
            10,
            20,
            21,
            22,
            23,
            16,
            17,
            18,
            19,
            6,
            7,
            4,
            5,
            2,
            3,
            0,
            1,
            36,
            37,
            38,
            39,
            32,
            33,
            34,
            35,
            45,
            44,
            47,
            46,
            41,
            40,
            43,
            42,
            30,
            31,
            28,
            29,
            26,
            27,
            24,
            25,
        ],
        [
            14,
            15,
            12,
            13,
            10,
            11,
            8,
            9,
            21,
            20,
            23,
            22,
            17,
            16,
            19,
            18,
            4,
            5,
            6,
            7,
            0,
            1,
            2,
            3,
            38,
            39,
            36,
            37,
            34,
            35,
            32,
            33,
            44,
            45,
            46,
            47,
            40,
            41,
            42,
            43,
            29,
            28,
            31,
            30,
            25,
            24,
            27,
            26,
        ],
        [
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            23,
            22,
            21,
            20,
            19,
            18,
            17,
            16,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
            0,
            39,
            38,
            37,
            36,
            35,
            34,
            33,
            32,
            47,
            46,
            45,
            44,
            43,
            42,
            41,
            40,
            31,
            30,
            29,
            28,
            27,
            26,
            25,
            24,
        ],
        [
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
        ],
        [
            17,
            16,
            19,
            18,
            21,
            20,
            23,
            22,
            2,
            3,
            0,
            1,
            6,
            7,
            4,
            5,
            11,
            10,
            9,
            8,
            15,
            14,
            13,
            12,
            41,
            40,
            43,
            42,
            45,
            44,
            47,
            46,
            27,
            26,
            25,
            24,
            31,
            30,
            29,
            28,
            34,
            35,
            32,
            33,
            38,
            39,
            36,
            37,
        ],
        [
            18,
            19,
            16,
            17,
            22,
            23,
            20,
            21,
            3,
            2,
            1,
            0,
            7,
            6,
            5,
            4,
            9,
            8,
            11,
            10,
            13,
            12,
            15,
            14,
            43,
            42,
            41,
            40,
            47,
            46,
            45,
            44,
            26,
            27,
            24,
            25,
            30,
            31,
            28,
            29,
            33,
            32,
            35,
            34,
            37,
            36,
            39,
            38,
        ],
        [
            19,
            18,
            17,
            16,
            23,
            22,
            21,
            20,
            1,
            0,
            3,
            2,
            5,
            4,
            7,
            6,
            10,
            11,
            8,
            9,
            14,
            15,
            12,
            13,
            42,
            43,
            40,
            41,
            46,
            47,
            44,
            45,
            25,
            24,
            27,
            26,
            29,
            28,
            31,
            30,
            35,
            34,
            33,
            32,
            39,
            38,
            37,
            36,
        ],
        [
            20,
            21,
            22,
            23,
            16,
            17,
            18,
            19,
            6,
            7,
            4,
            5,
            2,
            3,
            0,
            1,
            13,
            12,
            15,
            14,
            9,
            8,
            11,
            10,
            45,
            44,
            47,
            46,
            41,
            40,
            43,
            42,
            30,
            31,
            28,
            29,
            26,
            27,
            24,
            25,
            36,
            37,
            38,
            39,
            32,
            33,
            34,
            35,
        ],
        [
            21,
            20,
            23,
            22,
            17,
            16,
            19,
            18,
            4,
            5,
            6,
            7,
            0,
            1,
            2,
            3,
            14,
            15,
            12,
            13,
            10,
            11,
            8,
            9,
            44,
            45,
            46,
            47,
            40,
            41,
            42,
            43,
            29,
            28,
            31,
            30,
            25,
            24,
            27,
            26,
            38,
            39,
            36,
            37,
            34,
            35,
            32,
            33,
        ],
        [
            22,
            23,
            20,
            21,
            18,
            19,
            16,
            17,
            5,
            4,
            7,
            6,
            1,
            0,
            3,
            2,
            12,
            13,
            14,
            15,
            8,
            9,
            10,
            11,
            46,
            47,
            44,
            45,
            42,
            43,
            40,
            41,
            28,
            29,
            30,
            31,
            24,
            25,
            26,
            27,
            37,
            36,
            39,
            38,
            33,
            32,
            35,
            34,
        ],
        [
            23,
            22,
            21,
            20,
            19,
            18,
            17,
            16,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
            0,
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            47,
            46,
            45,
            44,
            43,
            42,
            41,
            40,
            31,
            30,
            29,
            28,
            27,
            26,
            25,
            24,
            39,
            38,
            37,
            36,
            35,
            34,
            33,
            32,
        ],
        [
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
        ],
        [
            25,
            24,
            27,
            26,
            29,
            28,
            31,
            30,
            42,
            43,
            40,
            41,
            46,
            47,
            44,
            45,
            35,
            34,
            33,
            32,
            39,
            38,
            37,
            36,
            1,
            0,
            3,
            2,
            5,
            4,
            7,
            6,
            19,
            18,
            17,
            16,
            23,
            22,
            21,
            20,
            10,
            11,
            8,
            9,
            14,
            15,
            12,
            13,
        ],
        [
            26,
            27,
            24,
            25,
            30,
            31,
            28,
            29,
            43,
            42,
            41,
            40,
            47,
            46,
            45,
            44,
            33,
            32,
            35,
            34,
            37,
            36,
            39,
            38,
            3,
            2,
            1,
            0,
            7,
            6,
            5,
            4,
            18,
            19,
            16,
            17,
            22,
            23,
            20,
            21,
            9,
            8,
            11,
            10,
            13,
            12,
            15,
            14,
        ],
        [
            27,
            26,
            25,
            24,
            31,
            30,
            29,
            28,
            41,
            40,
            43,
            42,
            45,
            44,
            47,
            46,
            34,
            35,
            32,
            33,
            38,
            39,
            36,
            37,
            2,
            3,
            0,
            1,
            6,
            7,
            4,
            5,
            17,
            16,
            19,
            18,
            21,
            20,
            23,
            22,
            11,
            10,
            9,
            8,
            15,
            14,
            13,
            12,
        ],
        [
            28,
            29,
            30,
            31,
            24,
            25,
            26,
            27,
            46,
            47,
            44,
            45,
            42,
            43,
            40,
            41,
            37,
            36,
            39,
            38,
            33,
            32,
            35,
            34,
            5,
            4,
            7,
            6,
            1,
            0,
            3,
            2,
            22,
            23,
            20,
            21,
            18,
            19,
            16,
            17,
            12,
            13,
            14,
            15,
            8,
            9,
            10,
            11,
        ],
        [
            29,
            28,
            31,
            30,
            25,
            24,
            27,
            26,
            44,
            45,
            46,
            47,
            40,
            41,
            42,
            43,
            38,
            39,
            36,
            37,
            34,
            35,
            32,
            33,
            4,
            5,
            6,
            7,
            0,
            1,
            2,
            3,
            21,
            20,
            23,
            22,
            17,
            16,
            19,
            18,
            14,
            15,
            12,
            13,
            10,
            11,
            8,
            9,
        ],
        [
            30,
            31,
            28,
            29,
            26,
            27,
            24,
            25,
            45,
            44,
            47,
            46,
            41,
            40,
            43,
            42,
            36,
            37,
            38,
            39,
            32,
            33,
            34,
            35,
            6,
            7,
            4,
            5,
            2,
            3,
            0,
            1,
            20,
            21,
            22,
            23,
            16,
            17,
            18,
            19,
            13,
            12,
            15,
            14,
            9,
            8,
            11,
            10,
        ],
        [
            31,
            30,
            29,
            28,
            27,
            26,
            25,
            24,
            47,
            46,
            45,
            44,
            43,
            42,
            41,
            40,
            39,
            38,
            37,
            36,
            35,
            34,
            33,
            32,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
            0,
            23,
            22,
            21,
            20,
            19,
            18,
            17,
            16,
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
        ],
        [
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
        ],
        [
            33,
            32,
            35,
            34,
            37,
            36,
            39,
            38,
            26,
            27,
            24,
            25,
            30,
            31,
            28,
            29,
            43,
            42,
            41,
            40,
            47,
            46,
            45,
            44,
            9,
            8,
            11,
            10,
            13,
            12,
            15,
            14,
            3,
            2,
            1,
            0,
            7,
            6,
            5,
            4,
            18,
            19,
            16,
            17,
            22,
            23,
            20,
            21,
        ],
        [
            34,
            35,
            32,
            33,
            38,
            39,
            36,
            37,
            27,
            26,
            25,
            24,
            31,
            30,
            29,
            28,
            41,
            40,
            43,
            42,
            45,
            44,
            47,
            46,
            11,
            10,
            9,
            8,
            15,
            14,
            13,
            12,
            2,
            3,
            0,
            1,
            6,
            7,
            4,
            5,
            17,
            16,
            19,
            18,
            21,
            20,
            23,
            22,
        ],
        [
            35,
            34,
            33,
            32,
            39,
            38,
            37,
            36,
            25,
            24,
            27,
            26,
            29,
            28,
            31,
            30,
            42,
            43,
            40,
            41,
            46,
            47,
            44,
            45,
            10,
            11,
            8,
            9,
            14,
            15,
            12,
            13,
            1,
            0,
            3,
            2,
            5,
            4,
            7,
            6,
            19,
            18,
            17,
            16,
            23,
            22,
            21,
            20,
        ],
        [
            36,
            37,
            38,
            39,
            32,
            33,
            34,
            35,
            30,
            31,
            28,
            29,
            26,
            27,
            24,
            25,
            45,
            44,
            47,
            46,
            41,
            40,
            43,
            42,
            13,
            12,
            15,
            14,
            9,
            8,
            11,
            10,
            6,
            7,
            4,
            5,
            2,
            3,
            0,
            1,
            20,
            21,
            22,
            23,
            16,
            17,
            18,
            19,
        ],
        [
            37,
            36,
            39,
            38,
            33,
            32,
            35,
            34,
            28,
            29,
            30,
            31,
            24,
            25,
            26,
            27,
            46,
            47,
            44,
            45,
            42,
            43,
            40,
            41,
            12,
            13,
            14,
            15,
            8,
            9,
            10,
            11,
            5,
            4,
            7,
            6,
            1,
            0,
            3,
            2,
            22,
            23,
            20,
            21,
            18,
            19,
            16,
            17,
        ],
        [
            38,
            39,
            36,
            37,
            34,
            35,
            32,
            33,
            29,
            28,
            31,
            30,
            25,
            24,
            27,
            26,
            44,
            45,
            46,
            47,
            40,
            41,
            42,
            43,
            14,
            15,
            12,
            13,
            10,
            11,
            8,
            9,
            4,
            5,
            6,
            7,
            0,
            1,
            2,
            3,
            21,
            20,
            23,
            22,
            17,
            16,
            19,
            18,
        ],
        [
            39,
            38,
            37,
            36,
            35,
            34,
            33,
            32,
            31,
            30,
            29,
            28,
            27,
            26,
            25,
            24,
            47,
            46,
            45,
            44,
            43,
            42,
            41,
            40,
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
            0,
            23,
            22,
            21,
            20,
            19,
            18,
            17,
            16,
        ],
        [
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
        ],
        [
            41,
            40,
            43,
            42,
            45,
            44,
            47,
            46,
            34,
            35,
            32,
            33,
            38,
            39,
            36,
            37,
            27,
            26,
            25,
            24,
            31,
            30,
            29,
            28,
            17,
            16,
            19,
            18,
            21,
            20,
            23,
            22,
            11,
            10,
            9,
            8,
            15,
            14,
            13,
            12,
            2,
            3,
            0,
            1,
            6,
            7,
            4,
            5,
        ],
        [
            42,
            43,
            40,
            41,
            46,
            47,
            44,
            45,
            35,
            34,
            33,
            32,
            39,
            38,
            37,
            36,
            25,
            24,
            27,
            26,
            29,
            28,
            31,
            30,
            19,
            18,
            17,
            16,
            23,
            22,
            21,
            20,
            10,
            11,
            8,
            9,
            14,
            15,
            12,
            13,
            1,
            0,
            3,
            2,
            5,
            4,
            7,
            6,
        ],
        [
            43,
            42,
            41,
            40,
            47,
            46,
            45,
            44,
            33,
            32,
            35,
            34,
            37,
            36,
            39,
            38,
            26,
            27,
            24,
            25,
            30,
            31,
            28,
            29,
            18,
            19,
            16,
            17,
            22,
            23,
            20,
            21,
            9,
            8,
            11,
            10,
            13,
            12,
            15,
            14,
            3,
            2,
            1,
            0,
            7,
            6,
            5,
            4,
        ],
        [
            44,
            45,
            46,
            47,
            40,
            41,
            42,
            43,
            38,
            39,
            36,
            37,
            34,
            35,
            32,
            33,
            29,
            28,
            31,
            30,
            25,
            24,
            27,
            26,
            21,
            20,
            23,
            22,
            17,
            16,
            19,
            18,
            14,
            15,
            12,
            13,
            10,
            11,
            8,
            9,
            4,
            5,
            6,
            7,
            0,
            1,
            2,
            3,
        ],
        [
            45,
            44,
            47,
            46,
            41,
            40,
            43,
            42,
            36,
            37,
            38,
            39,
            32,
            33,
            34,
            35,
            30,
            31,
            28,
            29,
            26,
            27,
            24,
            25,
            20,
            21,
            22,
            23,
            16,
            17,
            18,
            19,
            13,
            12,
            15,
            14,
            9,
            8,
            11,
            10,
            6,
            7,
            4,
            5,
            2,
            3,
            0,
            1,
        ],
        [
            46,
            47,
            44,
            45,
            42,
            43,
            40,
            41,
            37,
            36,
            39,
            38,
            33,
            32,
            35,
            34,
            28,
            29,
            30,
            31,
            24,
            25,
            26,
            27,
            22,
            23,
            20,
            21,
            18,
            19,
            16,
            17,
            12,
            13,
            14,
            15,
            8,
            9,
            10,
            11,
            5,
            4,
            7,
            6,
            1,
            0,
            3,
            2,
        ],
        [
            47,
            46,
            45,
            44,
            43,
            42,
            41,
            40,
            39,
            38,
            37,
            36,
            35,
            34,
            33,
            32,
            31,
            30,
            29,
            28,
            27,
            26,
            25,
            24,
            23,
            22,
            21,
            20,
            19,
            18,
            17,
            16,
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
            0,
        ],
    ],
    subgroup={
        "Oh": list(range(48)),
        "O": [
            0,
            1,
            2,
            3,
            8,
            9,
            10,
            11,
            16,
            17,
            18,
            19,
            28,
            29,
            30,
            31,
            36,
            37,
            38,
            39,
            44,
            45,
            46,
            47,
        ],
        "D4h": [0, 1, 2, 3, 4, 5, 6, 7, 40, 41, 42, 43, 44, 45, 46, 47],
        "D4": [0, 1, 2, 3, 44, 45, 46, 47],
    },
    cosets={
        "Oh": [0],
        "O": [0, 4],  # 4 is a reflection in the depth axis (third spatial axis)
        "D4h": [
            0,
            24,
            32,
        ],  # 24, 32 are permutation of second and third axis, and first and third axes, respectively
        "D4": [
            0,
            24,
            32,
            4,
            28,
            36,
        ],  # last 3 are first 3 multiplied on the right by the depth reflection
    },
    action=Oh_action,
)

O = Group(name="O", order=24, parent=Oh)
D4h = Group(name="D4h", order=16, parent=Oh)
D4 = Group(name="D4", order=8, parent=Oh)


space_group_dict = {"Oh": Oh, "O": O, "D4h": D4h, "D4": D4}
