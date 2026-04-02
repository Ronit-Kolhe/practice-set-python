try:
    a =  int(input("Enter the first No.: "))
    b =  int(input("Enter the second No.: "))

    print("what Kind of operation do you want  to perform:\n Press + for Addition\n Press - for Subtraction\n Press * for Multiplication\n Press / for Division")

    o = input("Enter the operation")
    match o:
        case "+":
            print(f"the result is {a+b}")
        case "-":
            print(f"the result is {a-b}")
        case "*":
            print(f"the result is {a*b}")
        case "/":
            print(f"the result is {a/b}")

        case default:
            print("Enter correct input")
except Exception as e:
    print("You are cooked man")    