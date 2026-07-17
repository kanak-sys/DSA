"Define a dictionary with 5 subjects"
"and their respective marks"
"utilize the get method to try accessing a subject that is not in the dictionary"
"ensuring it prints not available as default"

dictt = {"maths": 78,
        "physics": 87,
        "chemistry": 87,
        "hindi": 67,
        "english": 89}
print(dictt.get("maths", "not available"))
print(dictt.get("biology", "not available"))