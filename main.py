import random

jokes = [
    (
        "Tank",
        "You're welcome."
    ),
    (
        "Says",
        "Says me."
    ),
    (
        "Nobel",
        "Nobel…that’s why I knocked!"
    )
]

print("Knock Knock game!\nAnswer to play!\n")

random_joke = random.choice(jokes)

right_answer = False

while not right_answer:
    user_input = input(f"Knock Knock.\n").lower()

    if user_input == "who's there?":
        right_answer = True

right_answer = False

while not right_answer:
    user_input = input(f"{random_joke[0]}\n").lower()

    if user_input == f"{random_joke[0]} who?".lower():
        right_answer = True

print(random_joke[1])
