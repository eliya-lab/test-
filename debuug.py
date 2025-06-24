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
    for number in list1:
        sum_list += number
    return sum_list


def amount_in_list(list1):
    """
    this function gets a list
    :param list1: list to count
    :return: amount of list1
    """
    amount = 0
    for amount in list1:
        amount += 1
    return amount

def average_lists(sum_list, amount):
    """
    this function gets the average of list1
    :param sum_list: list to average
    :param amount: amount of param in list1
    :return: average of list1
    """
    average = sum_list / amount
    print(f"the average is:  {average}")
    return average

def main():
    """

    :return:
    """
    average_lists(sum_lists(combine_lists([1, 2, 3, 4, 5], [6, 7, 8, 9])), amount_in_list(combine_lists([1, 2, 3, 4, 5], [6, 7, 8, 9])))

if __name__ == '__main__':
    main()