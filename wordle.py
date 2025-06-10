import requests
import json

date = input("Enter a date (YYYY-MM-DD): ")
r = requests.get(f"https://www.nytimes.com/svc/wordle/v2/{date}.json").json()
word = r['solution']

#Guessing game
done = False
tries = 0

while not done and tries < 6:
	guess = input("Enter a guess: ").lower()
	tries += 1

	# Is the word valid?
	if len(guess) != 5:
		print("Invalid word")
		continue

	# Word is correct
	if guess == word:
		print("Correct!")
		done = True

	# Word is incorrect
	else:
		result = ""
		#Check each letter
		for i in range(len(guess)):
			# Correct letter
			if guess[i] == word[i]:
				result += 'G'
			# Letter in word, but wrong spot
			elif guess[i] in word:
				result += 'Y'
			# Letter is not in word
			else:
				result += '?'

		print(result)


if tries == 6:
	print("Game over!")

