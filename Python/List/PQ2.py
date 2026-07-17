"""
wap that takes a list and a target number
use a loop to determine
if the target number exist in the list
do not use the in operator
"""
listt = [10, 7, 34, 20, 4, 45, 86, 2, 90, 51, 1, 99]
def does_target_exist(listt, target_number):
    for num in listt:
        if target_number == num:
            return True
    return False
print(does_target_exist(listt, 18))
print(does_target_exist(listt, 20))
print(does_target_exist(listt, 99))
print(does_target_exist(listt, 100))
