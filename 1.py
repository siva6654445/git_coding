def cx():
    for i in data:
        if i > 2000 and i is int:
            print("good")
        if i < 2000: 
            print("not godd")
        else:
            print("np")


data = [2000,888787,999999]


a = cx()
print(a)


data = "mylasivakumar9@gmail.com"
mask = data.split("@")
print((mask)[0])
print((mask)[-1])