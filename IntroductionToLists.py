food = ["banana","kiwi","orange","apple","mango","passionfruit"]
print (food)
food [4] = "blueberry"
food.append ("dragonfruit")
food.remove("orange")
print (food)

#Iterate in a sequence - JetLearn Class 25.03.2026

for item in food:
    print (item)

#Iterating over a range - JetLearn Class 25.03.2026

for i in range (len(food)):
    print (i,food[i])

#Get 20 random marks for 20 students (between 0 to 100). Create 3 separate lists . The first list should contain the marks <=30. The second list between 31 to 69. The third list >= 70.
#Display the output lists