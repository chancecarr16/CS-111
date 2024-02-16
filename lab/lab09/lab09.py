import random


def in_range1(n):
    """Write a function that checks to see if n is 
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    """
    "*** YOUR CODE HERE ***"
    if 0 < n < 101:
        return True
    return False


def main():
    """Write code in the main function that generates 1000 
    random numbers between 1 and 101 and calls the generated 
    function to validate the number generated."""
    "*** YOUR CODE HERE ***"
    for x in range(1000):
        random_number = random.randint(1, 101)
        try:
            print(f"{random_number} is {in_range2(random_number)}")
        except ValueError as e:
            print(f"{e}! {random_number} is not in the range.")
            return False


def in_range2(num):
    """Redo in_range1, but throw an exception instead of 
    throwing false
    """
    "*** YOUR CODE HERE ***"
    if 0 < num < 101:
        return True
    else:
        raise ValueError(f"Your bad")


main()
