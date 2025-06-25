def get_number():
    """
    this function is used to get a number
    :return: the number
    """
    num = int(input("enter a number you want to get its sqrt"))
    if num is str:
        raise TypeError ("you didn't enter an integer")
    if num is   None:
        raise TypeError ("you didn't enter an integer")
    return num


def check_if_possible(num):
    """
    this function is used to check if a number is possible
    :param num: the number
    :return: an error message if not possible
    """
    if num is str:
        raise TypeError ("cant do a sqrt on a string")
    if num <= 0:
        raise TypeError ("cant do a sqrt on a negative number")


def get_sqrt(num):
    """
    this function is used to get the square root of the number
    :param num: the number
    :return: an error message if not possible
    """
    check_if_possible(num)
    for number in range(num):
        if number * number == num:
            print("that is the sqrt!")
            print(number)
            return number
        else:
            number += 1
    print("that is not a sqrt")
    raise ValueError("the sqrt is not an integer")


def main():
    get_sqrt(get_number())


if __name__ == "__main__":
    main()