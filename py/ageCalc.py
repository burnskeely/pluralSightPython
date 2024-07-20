hello = "Hello"
age = int(input("How old are you?\n"))

ageCalc = age // 10
decade = int(ageCalc)

years = age % 10

response = "You are " + str(decade) + " decades and " + str(years) + " year(s) old"
print(response)