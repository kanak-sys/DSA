"file type check"
#take a filename as input 
#check if it ends with .pdf
#.docx, .txt and print the file type

def check_file(file:str):
    if file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".txt"):
        print(file)
file = input("Enter file name: ")
check_file(file)