def combine_lists(list1, list2):
    """
    this function combines list1 and list2
    :param list1: list to be combined
    :param list2: list to be combined
    :return: the combined list
    """
    for num in list2:
        list1.append(num)
    return list1


def sum_lists(list1):
    """
    this function gets the sum of list1
    :param list1: list to sum
    :return: sum of list1
    """
    sum_list = 0
    amount = 0
    for number in list1:
        sum_list += number
        amount += 1
    average = sum_list / amount
    print(f"the average is:  {average}")
    return average


def main():
    list1 = [1, 2, 3 ,4 ,5]
    list2 = [6, 7, 8, 9, 10]
    sum_lists(combine_lists(list1, list2))


if __name__ == '__main__':
    main()