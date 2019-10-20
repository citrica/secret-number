import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0
list_wrong_guesses = []

with open("score_list.txt", "r") as score_file:
    a = score_file.read()
    score_list = json.loads(a)
    print("List: " + str(score_list))

# sort the list of dicts per attempts
new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

for score_dict in new_score_list:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}"\
        .format(score_dict.get("name"), str(score_dict.get("attempts")), score_dict.get("date"),
                score_dict.get("secret number"), score_dict.get("wrong"))

    print(score_text)

user_name = input("Enter your name: ")
while True:

    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        current_time = str(datetime.datetime.now())
        score_data = {"name": user_name, "secret number": secret, "attempts": attempts, "wrong": list_wrong_guesses,
                      "date": current_time}
        print(current_time)
        score_list.append(score_data)

        with open("score_list.txt", "w") as score_file:
            b = json.dumps(score_list)
            score_file.write(b)
        break
    elif guess > secret:
        list_wrong_guesses.append(guess)
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        list_wrong_guesses.append(guess)
        print("Your guess is not correct... try something bigger")