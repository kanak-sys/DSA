#add() for single elements
#update() for multiple elements

fruits = {"Apple", "Banana"}
fruits.add("cherry")
print(fruits)

fruits.update(["grapes","kiwi","Apple"])
print(fruits)

#remove() -  removes the value raises keyerror if value not found
#discard() - removes the value and no error if value not found safer
#pop() - removes and returns a random element
#clear() -  removes everything

fruits.remove("cherry")
print(fruits)

fruits.discard("cherry")
fruits.discard("Apple")
print(fruits)

removed = fruits.pop()
print(removed)

fruits.clear()
print(fruits)

