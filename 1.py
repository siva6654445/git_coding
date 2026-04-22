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

class swedbank:

    def __init__(self,tech,domain):
        self.tech = tech
        self.domain = domain
    

    def fx1(self):
        print(f"odi is still used instead of '{tech}'")
    

o1 = swedbank('snowflake','ai')
q=o1.fx1()
print(q)
print('feature_1')