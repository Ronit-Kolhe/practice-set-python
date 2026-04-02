# f = open("ronit.txt","r")

# content = f.read()

# print(content)
# f.close()

f = open("ronit.txt", "r")

for line in f:
    print(line)

f.close()