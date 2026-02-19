n = int(input(" enter no of element: "))
arr = list(map(int, input("enter elements: ").split()))
missing_ele = []

sun_total = n * (n + 1) // 2
actual_sum = sum(arr)
missing_ele.append(sun_total - actual_sum)

print("missing element: ", missing_ele)