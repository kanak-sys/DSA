#make a new list  from 1 to 10 [1, 2, 3, 4, ..., 10]
list = []
for i in range(1, 11):
    list.append(i)
print(list)

#comprehension
listt = [i for i in range(1, 11)]
print(listt)

#make a new list from 10 to 1
list1 = [i for i in range(10, 0, -1)]
print(list1)

#make a new list 1 to 10 of all squares
list2 = [i*i for i in range(1, 11)]
print(list2)

#make a list containning elements divisible by 3 and 7 both
list3 = [i for i in range(1, 31) if i % 3 == 0 and i % 7 == 0]
print(list3)

#make a list of all prime numbers from 1 to 100
def is_prime(num12):
    factors = 0
    for i in range(1, num12+1):
        if num12 % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False
list4 = [i for i in range(1, 101) if is_prime(i)]
print(list4)

#make a list of marks use list comprehension to create new list that contain only the marks that are above 75
marks = [87, 45, 23, 87, 12, 8, 43, 70, 98]
list5 = [num for num in marks if num >= 75]
print(list5, id(list5))
print(marks, id(marks))