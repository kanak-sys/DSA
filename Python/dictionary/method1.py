#case method
marks = {"maths": 99,
         "hindi": 98,
         "english": 93, 
         "history": 45}
print(marks.keys())
total = 0
for sub in marks.keys():
    print(f"subject ={sub}, and marks ={marks[sub]}")
    total += marks[sub]
print(f"total marks scored: {total}")

#key
for key in marks:
    print(key)

#values method
print(marks.values())
total = 0
for mark in marks.values():
    print(f"marks= {mark}")
    total += mark
print(f"total marks: {total}")

#items
print(marks.items())
for detail in marks.items():
    print(f"tuple: {detail}")
    print(f"only key i.e at 0 index in eeach tuple: {detail[0]}")
    print(f"only marks at 1 index in tuple: {detail[1]}")


#using unpacking
for sub, marks in marks.items():
    print(sub, marks)