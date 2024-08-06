#Write your function here
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 ==0:
      count +=1
  return count


#Uncomment the line below when your function is done
#print(divisible_by_ten([20, 25, 30, 35, 40]))
print(divisible_by_ten([20, 25, 30, 35, 40]))

#Write your function here
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list

#Uncomment the line below when your function is done
#print(add_greetings(["Owen", "Max", "Sophie"]))
print(add_greetings(["Owen", "Max", "Sophie"]))


#Write your function here
def delete_starting_evens(my_list):
  while (len(my_list)> 0 and my_list[0] % 2 ==0):
    my_list = my_list[1:]
  return my_list

#Uncomment the lines below when your function is done
#print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
