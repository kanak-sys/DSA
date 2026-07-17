squares = {}
for i in range(1,6):
    squares[i] = i*i
print(squares)

cubes = {i: i*i*i for i in range(1,6)}
print(cubes)

marks = {"maths": 87, "english": 87, "hindi": 62, "physics": 19}
top = {sub: mark for sub, mark in marks.items() if mark>80}
print(top)

doubled = {sub: mark*mark for sub, mark in marks.items()}
print(doubled)

#creating a dict from two lists
subjects = ["maths", "science", "english"]
scores = [85, 92, 78]
result = {s: sc for s, sc in zip(subjects, scores)}
print(result)