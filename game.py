# from random import choice
import requests
import json

#Get list of valid words
words = []
with open("words.txt", "r") as f:
    words = [x.strip() for x in f.readlines()]

# API call
# date = "2025-06-10"
date = input("Enter date (YYYY-MM-DD): ")
res = requests.get(f"https://www.nytimes.com/svc/wordle/v2/{date}.json").json()
word = res['solution']

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