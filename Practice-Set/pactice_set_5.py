# fruits = ["apple", "Banana", "guava"]
# fruits[2] = "orange"
# print(len(fruits))
# print(fruits)

# num_list = [i for i in range (1,11)]
# print(num_list)
# print(num_list[0:3])

# random_num = [5,2,4,6,8,9]
# random_num.sort()
# random_num.append(15)
# print(random_num)

# names = ["alice", "arjun", "akshada"]
# names.insert(1, "ronit")
# print(names)

# coords = (10 ,50)
# corlist = list(coords)
# corlist [1] = 20
# coords = tuple (corlist)
# print(coords)

# pra_list = [1,2,2,4,5,5,6,7,8,9]
# r_set = set(pra_list)
# print(r_set)

mydict = {
    "medicine" : 100,
    "chocolate" : 200,
    "bicuit": 250
}

print(max(mydict, key=mydict.get))