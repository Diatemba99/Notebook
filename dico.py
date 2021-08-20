weeks= {"nom": "diop", "prenom": "Jonas", "age": 19, "lieu": "Thiaroye"}


print(weeks)
print(len(weeks))

var1 = weeks["prenom"]
print(var1)

var2 = weeks.get("prenom")
print(var2)

weeks["age"]=25
weeks["nom"]="Lilly_POP"
print(weeks)

print("----------------------OTHERS DICTIONARIES OPERATIONS--------------------")

print("Priting keys only")
print(weeks.keys())

print("Priting values only")
print(weeks.values())

print("Priting items only")
print(weeks.items())

print("Adding values into dictionary")
weeks["sexe"]="masculin"
print(weeks)