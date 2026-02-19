n = int(input("enter no of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(" enter element: ")))
freq = {}
for i in arr:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print("frequency of elements: ", freq)