words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to the spelling bee")
    print("Your letters are: A I P C R H G")
    points = 0

    while len(words) > 0:
        print(f"You have {len(words)} words left")
        guess = input("Guess a word: ").upper()
        
        # Check if the guess is in the words dictionary
        if guess == "GRAPHIC":
            print(f"You Fund the super word: {guess} Congratulations!")
            words.clear()
        elif guess in words.keys():
            print(f"You guessed {guess} correctly! +{words[guess]} points")
            points += words.pop(guess)
            
        else:
            print(f"You guessed {guess} incorrectly!")

    print(f"You won with{points} points! Game over.")

main()
