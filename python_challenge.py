num1 = 6
num2 = 3

# Write your if statement here
if num1+num2 !=10:
  not_ten = True
else:
  not_ten = False

# Uncomment the below lines to show the result
# print("Does the sum of the numbers equal 10? " + str(not_ten))

# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total = food_bill + electricity_bill + internet_bill + rent
print(total)
# Check if the total is greater than the budget and store the result in over_budget
if total > budget :
  over_budget = True
else:
  over_budget = False

# Uncomment the below lines to see the results
print(over_budget)
print("\nTotal : " + str(total))


# Write your large_power function here:
def large_power (base , exponent):
  """Check weather if it over 5000"""
  if base ** exponent > 5000:
    return True
  else:
    return False

result = large_power(5000, 1)
print(result)

# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > num2*2:
    return True


  # Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  if (num % 10 == 0):
    return True
  else:
    return False
result = divisible_by_ten(10)
print(result)

# Uncomment these print() function calls to test your divisible_by_ten() function:

#print(divisible_by_ten(20))
# should print True
#print(divisible_by_ten(25))
# should print False
  else:
    return False
result = twice_as_large (100,25)
print(result)

# Write your same_name function here:
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
   return False
result = same_name("Colby", "Colby")
print(result)

result = same_name("Tina", "Amber")
print(result)

# Uncomment these function calls to test your same_name function:
#print(same_name("Colby", "Colby"))
# should print True
#print(same_name("Tina", "Amber"))
# should print False


# Write your max_num function here:
def max_num(num1, num2, num3):
  if num1>num2 and num1>num3:
   return num1
  elif num2>num1 and num2>num3:
    return num2
  elif num3>num1 and num3>num2:
    return num3
  else:
    return "It's a tie!"
# Uncomment these function calls to test your max_num function:
#print(max_num(-10, 0, 10))
print(max_num(-10, 0, 10))
# should print 10
#print(max_num(-10, 5, -30))
print(max_num(-10, 5, -30))
# should print 5
#print(max_num(-5, -10, -10))
print(max_num(-5, -10, -10))
# should print -5
#print(max_num(2, 3, 3))
print(max_num(2, 3, 3))
# should print "It's a tie!"


# Write your movie_review function here:
def movie_review(rating):
  if (rating <= 5):
    return "Avoid at all costs!"
  if (rating <9):
    return "This one was fun"
  return "Outstanding"



# Uncomment these function calls to test your movie_review function:
#print(movie_review(9))
print(movie_review(9))
# should print "Outstanding!"
#print(movie_review(4))
print(movie_review(4))
# should print "Avoid at all costs!"
#print(movie_review(6))
print(movie_review(6))
# should print "This one was fun."

#Write your function here
def append_size(my_list):
  my_list.append(len(my_list))
  return my_list



#Uncomment the line below when your function is done
append_size([23, 42, 108])

#print(append_size([23, 42, 108]))
print(append_size([23, 42 , 108]))

#Write your function here
def append_sum(my_list):
  my_list.append(my_list[-1]+ my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  return my_list

#Write your function here
def larger_list(my_list, my_list2):
  if len(my_list) >= len(my_list2):
    return my_list[-1]
  else:
    return my_list2[-1]



#Uncomment the line below when your function is done
#print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
#print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


#Write your function here
def every_three_nums(start):
  """Return every third number between start and 100 , above it empty list"""
  return list(range(start,101,3))


#Uncomment the line below when your function is done
# print(every_three_nums(91))
print(every_three_nums(91)

      #Write your function here
def remove_middle(my_list, start,end):
  return my_list[:start] + my_list[end+1:]
#Uncomment the line below when your function is done
# print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
print(remove_middle([4,8,15,16,23,42],1, 3))

#Uncomment the line below when your function is done
#print(append_sum([1, 1, 2]))
print(append_sum([1,1,2]))

#Write your function here
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) >= my_list.count(item2):
    return item1
  else:
    return item2
#Uncomment the line below when your function is done
#print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
output : 3

#Write your function here
def double_index(my_list, index):
  if index >= len(my_list):
    return my_list
  else:
    #Get the original list up to index
    my_new_list = my_list[0:index]
    #Adds double
  my_new_list.append(my_list[index]*2)
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list

#Uncomment the line below when your function is done
#print(double_index([3, 8, -10, 12], 2))
print(double_index([3, 8, -10, 12], 2))
