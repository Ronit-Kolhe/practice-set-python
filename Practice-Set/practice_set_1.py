#Q1
print ("helle, world! welcome to python")

#Q2
print("Twinkle, Twinkle , little star \nhow i wonder what you are")

#Q3
name = str(input("Enter Your Name:"))
age = int(input("Enter Your Age: "))
height  = float(input("Enter your Height in CM: "))
is_student = True
print(f"The Name of Student is: {name},", f"The age of Student is: {age},", f"The Height of Student is: {height},", is_student)

#Q4
num = "45"
int = int(num)
print(int + 10, type(int))

#Q5
food = input("Enter your favorite food: ")
print(f"Wow! I also like {food}.")

#Q6
a = int(input("Enter Num 1: "))
b = int(input("Enter Num 2: "))

print(f"sum = {a + b}\n",f"difference =  {a - b}\n", f"product =  {a * b}\n", f"quotient =  {a / b}\n")


#Q8
integer = int(input("enter the number: "))
sq = integer*integer
cube = integer*integer*integer
print(f"the square of {integer} = {sq}")
print(f"the cube of {integer} = {cube}")