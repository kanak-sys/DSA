name, age, gender = 'rahul', 25, "male"
is_student = True
print("hello", name," you are ", age, " years old and your gender is ", gender)
print("hello" + name + " you are " + str(age) + " years old") # we can't concatenate string 
                                                            #with int so we need to convert int to string
                                                            #  using str() function when +
#end
print(name, end= " ")
print(age)
print(gender)

#F-strings
print(f"hello {name} you are {age * 10} years old and your gender is {gender} and you are a student: {is_student}")





