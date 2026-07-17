pythonmarks = {"maths": 78, "hindi": 67, "science": 85, "computer": 83, "english": 89}

#len- number of key-value pair
n = len(pythonmarks)
print(n)

#sum-calculate sum on values
total = sum(pythonmarks.values())
print(total)

#min & max- minimum and maximum on values
mini = min(pythonmarks.values())
maxi = max(pythonmarks.values())
print(mini, maxi)

#min & max- minimum and maximum on keys by default sorted values
minim = min(pythonmarks)
maxim = max(pythonmarks)
print(minim, maxim)

#sorted- on keys returns a soreted list of keys
sorting = sorted(pythonmarks)
print(sorting)

#sorted- for dictionary
sorting2  = dict(sorted(pythonmarks.items()))
print(sorting2)
