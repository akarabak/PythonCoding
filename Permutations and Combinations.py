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


def combinations(available: str, comb: str='', length=0):
    if length > 0 and len(comb) == length:
        print(comb)
    elif length == 0 and len(available) == 0:
        print(comb)
    if len(available) == 0:
        return
    for i in range(len(available)):
        comb += available[i]
        combinations(available[i+1:], comb, length)
        comb = comb[:-1]


class Telephone:
    number_pad = [
        ['0'],
        ['1'],
        ['a','b','c'],
        ['d','e','f'],
        ['g','h','i'],
        ['j','k','l'],
        ['m','n','o'],
        ['p','q','r', 's'],
        ['t','u','v'],
        ['w','x','y','z']
    ]
    def __init__(self, phone):
        self.phone = list(phone)

    def print(self):
        word = [j for j in self.phone]
        self.print_word(word, 0)

    def print_word(self, word, position):
        if len(word) == position:
            print(''.join(word))
            return
        current_num = int(self.phone[position])
        for l in Telephone.number_pad[current_num]:
            word[position] = l
            self.print_word(word, position + 1)


if __name__ == '__main__':
    print('Permutations of abc:')
    permutations('abc')
    print('Combinations of abc:')
    combinations('abc')
    print('Phones:')
    Telephone('8182573553').print()
    #pascal(5)
