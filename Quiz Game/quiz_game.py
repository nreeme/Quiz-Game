print("Welcome to Quiz Bowl!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    print("Good Bye")

print("Okay let's play!")

score = 0

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Sorry try again")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Sorry try again")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Sorry try again")

print("You got " + str(score) + " of 3 Correct!")
print(str((score/ 3) * 100) + "%")