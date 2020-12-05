phoneBook = {}

n = int(input());
for _ in range(n):
    name, phone = input().split(" ")
    phoneBook.update({name : phone})


try:
    while True:
        q = input()
        if q in phoneBook.keys():
            print("{}={}".format(q, phoneBook.get(q)))
        else:
            print("Not found")
except:
    pass        
