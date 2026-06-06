print("welcome to Tip Calculator!")
bill = float(input("How much was the bill?"))
tip = float(input("what percent tip would you like to give? 10,12,or 15?"))
num_people = int(input("How many poeple to split the bill? "))
calculate = round((bill * (tip / 100 + 1)) / num_people, 2)
print("The amount of money each person has to pay is: "+ str(calculate))

