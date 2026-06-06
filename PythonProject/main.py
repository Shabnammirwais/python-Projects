# name = input("What is your name? ")
# length_of_name = len(name)
# print("The number of  letters in your name is " + str(length_of_name))
# print(round(3.14159, 3))
# num = int(input("enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("odd")
# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
#
# if bmi < 18.5:
#     print("underwieght")
# elif 18.5 <= bmi < 25:
#     print("normal")
# else:
#     print("Overwieght")

# print("Welcome to python pizza Deliveries!")
# size = input("what size pizza would you like? S,M,or L?")
# peporani = input("would you like peperoni on your pizza? Y or N")
# cheese = input("Would you like extra cheese? Y, or N")
# bill = 0
#
# if size == "S":
#     bill +=15
# elif size == "M":
#     bill +=20
# else:
#     bill +=25
# if peporani == "Y" and size == "S":
#     bill += 2
# else:
#     bill += 3
# if cheese == "Y":
#     bill+=1
# print(f"You final bill is: {bill}")

# import random
# poeple = ["angela", "Sara", "Mustafa", "khadija", "Shabnam"]
# random_number = random.randint(0,4)
# print(poeple[random_number])

# student_scores = [10,60,90,100,80,70,50]
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(max_score)

# sum = 0
# for number in range(1, 101):
#     sum +=


# def format_name(f_name, l_name):
#     """This function Take fist and last name to return the title case version of it"""
#     return f_name.title() +" " + l_name.title()
#
#
# output = format_name("shabnAm", "miRwais")
# print(output)

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap(2000))
