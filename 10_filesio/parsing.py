import argparse
parser = argparse.ArgumentParser(description = "A simple calculator")
parser.add_argument("num1", type = float, help = "First number")
parser.add_argument("num2", type = float, help = "second number")
parser.add_argument("operation", choices =  ["add", "subtract", "multiply", "divide"], help = "Operation to perform")

args = parser.parse_args()

print (args)

if(args.operation == "add"):
    print (args.num1 + args.num2)

elif(args.operation == "subtract"):
    print (args.num1 - args.num2)
    
elif(args.operation == "miltiply"):
    print (args.num1 * args.num2)
    
elif(args.operation == "divide"):
    print (args.num1 / args.num2)

else:
    print ("Invalid operation")    



