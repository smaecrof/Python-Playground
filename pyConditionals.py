# Author: Spencer Mae-Croft
# Date: 08/31/2020

str1 = "Hello"
str2 = "Hello"
print("Str1 == Str2: " + str(str1 == str2))


users = ["Spencer", "Jake", "Admin", "Elise", "Nick", "Julia", "Hendrick", "Dean"] 

if users:
    for user in users:
        if user.lower() == 'admin':
            print("Hello Admin, would you like a status update?:")
        else:
            print("Hello " + str(user) + ", welcome back to the system")
else:
    print("We need to find some users")




currentUsers = ["Jake", "Doug", "Steven", "Dean", "Mark"]
newUsers = ["Dan", "Jake", "Steve", "Marcus", "Dean"] 

for user in newUsers:
    if user in currentUsers:
        print(user + " already taken. Please choose a new username")
    else:
        print(user + " is available")























