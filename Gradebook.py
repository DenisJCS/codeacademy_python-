last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]

grades = [98 , 97 , 85, 88]

#combined list
gradebook = [["physics", 98], ["calculum", 97], ["poetry", 85], ["history", 88]]
print(gradebook)
#adding new subject
gradebook.append(["computer science", 100])
print(gradebook)
#one more
gradebook.append(["visual arts", 93])
print(gradebook)
#adding points
gradebook[-1][-1]=98
print(gradebook)
#remove 
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)
#final one
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)








