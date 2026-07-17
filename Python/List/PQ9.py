"""Given a list remove all duplicate elements while preserving
the original order of the unique items"""

def remove_dupli(list):
    result = []
    for num in list:
        if num not in result:
            result.append(num)

    return result
list = [1, 1, 2, 4, 7, 9, 1, 4, 1, 5, 3, 7]
print(remove_dupli(list))