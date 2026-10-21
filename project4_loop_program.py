import random
hidden_number=random.randint(1,100)
number_guess = random.randint
# for loop is part of lines 6 to 12
for i in range (10):
    number_guess = int(input("guess a number between 1 and 100"))
    if hidden_number > number_guess:
        input("too low try again by pressing enter")
    if hidden_number < number_guess:
        input ("too high try again by pressing enter")
    if hidden_number == number_guess:
        print ("You won have a great day and if I dont see you good evening, good night,and good morning.")



 