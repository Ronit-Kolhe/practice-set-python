#1 if-else statement

#Q1
# num = int(input("Enter the number: "))
# print(num)

# if num > 0:
#     print("Number is positive")

# elif num < 0:
#     print("Number is Negative")

# else:
#     print("the number is zero")    

#Q2
# age  = int(input("enter you age: "))
# print(age)

# if (age >= 18):
#     print("the person is eligible for voting")

# else:
#     print("The person isn't eligible for voting")

#Q3
# num = int(input("Enter the number: "))
# if num%2==0:
#     print("number is even")

# else:
#     print("number is odd ")

#2 Match case statements

#Q1
# num = int(input("enter a number between 1-7\n"))

# match num:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")

#Q2
a = int(input("enter a number: "))
b = int(input("enter a number: "))

operation = input(("Choose an Operation: "))

match operation:
    case "+":
        print(a+b)
    case "-":
        print("a-b")
    case "*":
        print(a*b)
    case "/":
        print(a/b)