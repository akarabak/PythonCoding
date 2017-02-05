

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


def permutations(available: str, perm: str=''):
    if len(available) == 0:
        print(perm)
        return
    for i in range(len(available)):
        c = available[i]
        available = available[:i] + available[i+1:]
        permutations(available, perm + c)
        available += c


def combinations_wrapper(word: str):
    for i in range(len(word)):
        combinations(word[i:])


def combinations(available: str, comb: str=''):
    if len(comb) > 0:
        print(comb)
    if len(available) == 0:
        return
    else:
        comb += available[0]
        combinations(available[1:], comb)
        comb = comb[:-1]

if __name__ == '__main__':
    #permutations('abc')
    combinations_wrapper('abc')
    #pascal(5)
