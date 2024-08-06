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


#Write your function here
def odd_indices(my_list):
  new_list = []
  for index in range(1, len(my_list), 2):
    new_list.append(my_list[index])
  return new_list

#Uncomment the line below when your function is done
#print(odd_indices([4, 3, 7, 10, 11, -2]))
print(odd_indices([4, 3, 7, 10, 11, -2]))




#Write your function here
def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers:
      new_list.append(base ** power)
  return new_list

#Uncomment the line below when your function is done
#print(exponents([2, 3, 4], [1, 2, 3]))
print(exponents([2, 3, 4], [1, 2, 3]))
