#sets with string values
fruits = {"Apple", "Banana", "Carrot", "Mango"}
print(f"Fruits set: {fruits}")

#set with numbers
num = {1, 2, 3, 4, 5}
print(f"Number set: {num}")

#set with mixed data types
mixed = {"Archie", True, 3, 9.56}
print(f"Mixed Values: {mixed}")

#creating a set from a list
#automatically removing duplicates
my_list = [1, 2, 3, 2, 1, 4, 5, 4]
Unique = set(my_list)
print(f"Unique elements from List: {Unique}")

#empty dictionary
empty_braces ={}
print(f"Type of {{}}: {type(empty_braces)}")

#this is an empty set
empty_set = set()
print(f"Type of set(): {type(empty_set)}")

#counting unique words in a sentence
sentence = "python is great and python is easy"
unique_words = list(set(sentence.split()))
print(len(unique_words))
print(unique_words)