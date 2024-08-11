#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
   sum1 += number
  for number in lst2:
   sum2 += number
  if sum1 >= sum2:
    return lst1
  else:
    return lst2


#Uncomment the line below when your function is done
#print(larger_sum([1, 9, 5], [2, 3, 7]))
print(larger_sum([1, 9, 5], [2, 3, 7]))


#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum
#Uncomment the line below when your function is done
#print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([8000, 900, 120, 5000]))
