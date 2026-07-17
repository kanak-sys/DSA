"""

calculate average:
given a list of numbers,
use a loop to calculate
and print their average
you can use len()
to get the count of elements in the list
but avoid using sum()
format the average to 2 decimal places

"""



def calculate_average(listt):
    n = len(listt)
    total = 0
    for num in listt:
        total += num
    return total/n

listt = [10, 7, 34, 20, 4, 45, 86, 2, 90, 51, 1, 99]
avg = calculate_average(listt)
print(f"Average: {avg:.2f}")
