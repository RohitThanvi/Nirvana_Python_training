# Write a program in Python to perform the following operation:

"""If a number is divisible by 3 it should print “SKILLBREW” as a string
If a number is divisible by 5 it should print “BRUDITE” as a string
If a number is divisible by both 3 and 5 it should print “BRUDITE - NIRVANA” as a string.If a number is divisible by 3 it should print “SKILLBREW” as a string
If a number is divisible by 5 it should print “BRUDITE” as a string
If a number is divisible by both 3 and 5 it should print “BRUDITE - NIRVANA” as a string.
"""

a = int(input("Enter a numner"))

print(a, "here is the input number")   # print functions
print(f"here is the input number {a}")   # formated string pint



if a % 5 == 0 and a % 3 == 0:
    print("BRUDITE - NIRVANA")
elif a % 3 == 0:
    print("SKILLBREW")
elif a % 5 == 0:
    print("BRUDITE")



"""2. Write a program that accepts a string as input from the user and calculates the number of digits and letters.
     Input: Hello123 
     Output: Alphabets: 5 & Number : 3
"""


alpha = 0
num = 0

for i in list("Brudite 1234hil"):
    if i.isalpha():
        alpha += 1
    elif i.isnumeric():
        num += 1

print(f"total alphabets: {alpha}")
print(f"total nums: {num}")


"""5. Write a Python program to find the factorial of a number using a for loop.
"""

a = 10
fact = 1

while a>0:
    fact = fact * a
    a -= 1


print(fact)