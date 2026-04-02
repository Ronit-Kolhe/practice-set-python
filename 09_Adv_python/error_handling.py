# while True:
#     try:
a = int(input("Enter the A Number: "))
b = int(input("Enter The B Number: "))

if b == 0:
   raise ValueError("Please bhai")

print(f"The division is {a / b}")


    # except ValueError as e:
    #     print("Please don't perform typecaste",e)    

    # except ZeroDivisionError as e:
    #     print("Hey don't divide it by zero",e)    

    # except Exception as e:
    #     print(e)