"""
Blackjack
"""


def calculate_score(n1: int, n2: int, n3: int):
    if n1 > 11 or n2 > 11 or n3 > 11:
        return "Sorry, one of the numbers is more than 11, it's too high."
    else:
        n4 = n1+n2+n3
        if n4 <= 21:
            return n4
        else:
            if n4 > 21:
                if n1 == 11 or n2 == 11 or n3 == 11:
                    n4 -= 10
                    if n4 > 21:
                        return "BUST"
                    else:
                        return n4
                else:
                    return "BUST"


print(calculate_score(9, 9, 9))
print(calculate_score(2, 8, 11))
print(calculate_score(3, 8, 11))
print(calculate_score(11, 11, 11))

"""
Even Numbers
"""


def even_positive_numbers(list_input: list) -> list:
    new_list = []
    for i in list_input:
        if i >= 0 and i % 2 == 0:
            new_list.append(i)
    return new_list


if __name__ == '__main__':
    print(even_positive_numbers([1, 2, 3]))
    print(even_positive_numbers([10, 22, 31, 24, 35, 36]))
    print(even_positive_numbers([-10, -22, 31, 24, 35, 36]))
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")
