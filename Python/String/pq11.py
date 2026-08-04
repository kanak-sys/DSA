"vowel starting words"
#take a sentence as input
#split it into words and print
#how many words start with vowel

def vowel_check(sentence:str):
    count = 0
    vowel = 'aeiouAEIOU'
    split_words = sentence.split(" ")
    print(split_words)
    for word in split_words:
        if word[0] in vowel:
            count += 1
    return count

sentence = input("Enter sentence: ")
ans = vowel_check(sentence)
print(ans)