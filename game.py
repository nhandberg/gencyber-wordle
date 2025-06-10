from random import choice

words = []

with open("words.txt", "r") as f:
    words = [x.strip() for x in f.readlines()]

word = choice(words)

done = False
while not done:
    guess = input("Enter a five letter word: ")

    #Check if word is in the list
    if guess not in words:
        print("Invalid word")
        continue

    if guess == word:
        print("Nice work!")
        done = True

    #If word isn't right, check each letter
    else:
        result = ""
        for i in range(len(guess)):
            if guess[i] == word[i]:
                result += 'G'
            elif guess[i] in word:
                result += 'Y'
            else:
                result += '?'
        print(result)