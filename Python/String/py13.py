"Longest Word"
#take a sentence as input 
#print the longest word

def check_sentence(sentence:str):
    static = 0
    static_word = " "
    split_sen = sentence.split(" ")
    for word in split_sen:
        n = len(word)
        if n >= static:
            static = n
            static_word = word
    print(f"Longest word in sentence: {static_word} of length: {static}")

sentence = input("enter sentence as input: ")
check_sentence(sentence)