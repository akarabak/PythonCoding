

def pascal(rows):
    for i in range(rows):
        coef = 1
        exponent = i
        print(1, "", end="")
        for position in range(1, i + 1):
            coef = coef * (rows - position) // position
            exponent -= 1
            print(coef, "", end="")
        print()


def permutations(perm: str, available: str):
    if len(available) == 0:
        print(perm)
        return
    for i in range(len(available)):
        perm += available[i]
        available = available[:i] + available[i+1:]
        permutations(perm, available)
        available += perm[-1]
        perm = perm[:-1]


def combinations(comb: [str], available: [str]):
    pass

if __name__ == '__main__':
    permutations('', 'abc')
    #pascal(5)
