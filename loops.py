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
