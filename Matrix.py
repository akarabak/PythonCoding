def rotate_current(m, layer):
    first = layer
    second = len(m) - 1 - layer

    for i in range(0, second - first):
        temp1 = m[first][second - i]
        m[first][second - i] = m[first + i][first]

        temp2 = m[second - i][second]
        m[second - i][second] = temp1

        temp1 = m[second][first + i]
        m[second][first + i] = temp2

        m[first + i][first] = temp1


def rotate(m):
    for i in range(0, len(m) // 2):
        rotate_current(m, i)
    return m



