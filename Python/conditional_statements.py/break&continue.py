"""
break statement::
immediately stops the loop and exists it
even if the condition is still true or 
there are items left in sequence
"""

#break in while loop
num = 1
while num <= 10:
    if num == 5:
        break
    print(num)
    num += 1

#break in for loop
for i in range(1, 11):
    if i == 6:
        break
    print(i)

"""
continue statement::
skips rest of the current itration and jumps straight to the next one.
loop doesn't stops skips particular cycle

"""

i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

