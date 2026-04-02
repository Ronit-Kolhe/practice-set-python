a = int(input("Enter the lucky numbe between 1 to 10: "))

match a:
    case 6:
        print("you won a car")

    case 3:
        print("you won a bangkok trip")
    
    case 1:
        print("you won lifetime fortune")

    case _:
        print ("you won a dick")