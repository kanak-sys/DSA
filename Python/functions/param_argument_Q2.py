"""
write a function called rectangle_area
that takes length and breadth as parameter
prints the area

"""
def rectangle_area(length, breadth):
    Area = length * breadth
    print(f"Area of Rectangle: {Area}")

l1 = int(input("enter length of rec. "))
b1 = int(input("enter breadth of rec. "))
rectangle_area(l1, b1)