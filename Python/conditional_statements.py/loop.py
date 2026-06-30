"""
without writing anything again and again we can use loops to repeat a block of code
print hello 10 times
1. while loop-
    it is used to execute a block of code
    repeatedly as long as a given condition is true
"""

#infinite loop
"""
while 99 > 3:       #since the condition is true every time the block will run infinitely
    print("hello")  #after executing loops runs continuously use ctrl+c to stop the execution
    print("done")   #throws keyboard interrupt error 
"""

"""
i = 1
while i <= 10:      #i = 1 true, excute 1 <=10 true,  again i =1 true,....
    print("hello")
"""

#normal loop
i = 1
while i <= 10:
    print("hello")
    i += 1      #i = i + 1

