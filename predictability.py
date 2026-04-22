def question_one(n):
    score = 0

    if n % 2 == 1:        # odd
        score += 1
    if n > 10:            # not too small
        score += 1
    if n % 10 != 0:       # not round
        score += 1
    if n in [37, 73, 67, 21]:     # classic picks
        score += 2

    return score
print("Question one")
print()

user = int(input("Pick a number from 1–100: "))
score = question_one(user)

print("Predictability score:", score)

if score >= 4:
    print("Very predictable")
elif score >= 2:
    print("Somewhat predictable")
else:
    print("Unusual choice!")

print()

print("Question two")
print()
