
from quiz import question1, question2, question3, question4
from quiz import repense1, repense2, repense3, repense4

print("\n====================")
print("Welcome to the programme!")
print("Q/A")
print("====================\n")

score = 0

print(question1())
repense = input("Your answer: ")

if repense == repense1():
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is:", repense1())


print(question2())
repense = input("Your answer: ")

if repense == repense2():
    
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is:", repense2())


print(question3())
repense = input("Your answer: ")

if repense == repense3():
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is:", repense3())


print(question4())
repense = input("Your answer: ")

if repense == repense4():
    score += 1
    print("Correct!")
else:
    print("Incorrect!")
    print("The correct answer is:", repense4())


print("\nQuiz completed!")
print("Your score is:", score, "/ 4")