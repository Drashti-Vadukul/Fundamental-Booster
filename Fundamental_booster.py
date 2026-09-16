print("Welcome to the interactive personal data Collector!")
print("")

name = input("Plese enter your name :")
age = int(input("Please Enter Your Age :"))
height = float(input("Please Enter Your Height In Meters :"))
num = int(input("Please Enter Your Favourite Number :"))


print("\nThank You ! Here is the Information We Collected :")
print("")

print("Name :" ,name ,"(Type :" ,type(name), " Memory Address :" ,id(name), ")")
print("Age :" ,age ,"(Type :" ,type(age), " Memory Address :" ,id(age), ")")
print("Height :" ,height ,"(Type :" ,type(height), " Memory Address :" ,id(height), ")")
print("Favourite Number :" ,num ,"(Type :" ,type(num), " Memory Address :" ,id(num), ")")

birth_year = 2026 - age
print(" \nYour Birth Year Is Approximately :" , birth_year ,"(Based on Your age of ", age, ")")

print("\n Thank You For Using The Interactive Personal Data Collector !")
print("")