courses=["MIT","Python","Android"]
print(courses)
#accessing an element

print(courses[0])
#looping through an array

for x in courses:
  print(x)

#Adding a new element
courses.append("Java")
print(courses)

#Removing an element
courses.remove("Android")
print(courses)
