# Strings are immutable

a = "Rocky"
print(len(a))
print(a.upper())
print(a.lower())
print(a.replace("Rocky", "Mr. Rocky"))
print(a.count(a))

b = "!!!Rokcy!!! !!!       Haque!!"
print(b.rstrip("!"))
print(b.split(" "))

str1 = "He's name is Don. He is an honest man."
print(str1.find("is"))
print(str1.index("is"))

str2 = "WelcomeToTheConsole"
print(str2.isalnum())