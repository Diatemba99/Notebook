"""
def my_function():
    print("Hello from a function")
my_function()

print("Function part 2")

def addition():
    a=int(input("give your age :"))
    b=int(input("give your second age :"))
    print("Sum is:", a+b)
#addition()    


#With this function i shall use parameters for having numbers at the end
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Function part 3 calling function with parameter")
def mixedNumber(age):
    print("hello boy number" +age)

mixedNumber(" 5")
mixedNumber(" 54")


#With this function i shall use parameters for having numbers at the end
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Function part 4 calling function with parameters")
def mixedNumbers(ages,nom):
    print("hello boy number" + ages)
    print("hello boy number" + nom)

#mixedNumbers(" 5","claudia")
#mixedNumbers(" 54", "brown")



#With this function i shall use parameters for having numbers at the end
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Function part 5 calling function with initialed parameters")
def initial(zone="essill"):
    print("hello boy number " + zone)
    print("hello boy number " + zone + " guelwar")

#initial(" bandial")
#initial(" brin")



#With this function i used with returned statement
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Function part 6 calling function returned statement")
def produit(x):
    return 5*x



print(produit(15))    
print(produit(90))    
print(produit(25))    

#With this function i used with returned statement
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Function part 7 using lamba function")

sum = lambda a,b,c,d: a+b+c+d
print(sum(41,65,85,47))



sum = lambda a,b,c : a*b*c
print(sum(2,6,3))


print("MATRICULE")
matricule = lambda mat: mat[:5]
mat ="SIDK85475F"

print(matricule(mat))
"""


Tu1 = (1,2,3)
Tu2 = (4,5,6)

rs= list(map(lambda x,y: x*y, Tu1,Tu2 ))
print(rs)
print("Part 2 of using map function")
print("*"*15)

def multiplication(a,b):
    return a * b

rs2 = list(map(multiplication,(1,2,3),(4,5,6)))

print(rs2)