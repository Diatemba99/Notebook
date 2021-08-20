week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saterday", "Sunday"]


print(week[3])


week[1]="Lundi"

print(len(week))
print((week))

print("----------------------------------")
mylist=[1, 56, "hello", [7, 20], True] 
print(len(mylist[3]))

mylist.append("Toyota")

print(mylist)

mylist.insert(2, "Ziar")

print(mylist)

#Delete operation with list
print("***********************************")

mylist.remove("hello")
print(mylist)

print("***********************************")

del mylist[3]

print(mylist)
print("++++++++++++++++++++++++++++++++++++++")

mylist2=[1, 56, "hello", [7, 20], True]
del mylist2[3][1]
print(mylist2)