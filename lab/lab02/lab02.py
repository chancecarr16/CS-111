def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    counter = 1
    total = n
    if k == 0:
        total = 1
    while counter < k:
        total *= (n - counter)
        counter += 1
    return total


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    num_list = str(y)
    add_sum = 0
    for character in num_list:
        add_sum += int(character)
    return add_sum


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    eight_string = str(n)

    def check_eights():
        eight_count = 0
        while eight_count < len(eight_string):
            if eight_string[eight_count] == '8' == eight_string[eight_count + 1]:
                return True
            eight_count += 1
        return False

    if len(eight_string) < 2:
        return False
    if check_eights():
        return True
    else:
        return False
