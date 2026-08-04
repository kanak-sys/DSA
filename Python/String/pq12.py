"Sorted Names"
#take a list of names as input comma separated
#split them, sort them , alphabetically
#and join them back with "|" separator

def sort_names(names:str):
    split_names = names.split(",")
    
    split_names.sort()

    result = " | ".join(split_names)
    print(result)

names = input("Enter names separated by comma only: ")
sort_names(names)