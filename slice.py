# Your code below:
toppings = ["pepperoni", "pineapple", "chese", "sausage", "olives", "anchovies", "mashrooms"]
#price
prices = [2, 6, 1, 3, 2, 7, 2]

#Checkpoint 1
num_two_dollar_slice = prices.count(2)
print(num_two_dollar_slice)
#Checkpoint 2
num_pizzas = len(toppings)
print(num_pizzas)
#Checkpoint 3
print("We sell", "" + str(num_pizzas) + "" "different kinds of pizzas")
#Checkpoint 4
pizza_and_prices = [[2,"pepperoni"], [6,"pineapple"], [1,"cheese"], [3,"sausage"], [2,"olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
#Checkpoint 5
pizza_and_prices.sort()
print(pizza_and_prices)
#Checkpoint
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
#Checkpoint 6
priciest_pizza = pizza_and_prices[6]
print(priciest_pizza)
#Checkpont 7
pizza_and_prices.pop()
print(pizza_and_prices)
#Checkpoint 8
pizza_and_prices.insert(4,["2.5, peppers"])
print(pizza_and_prices)
#Checkpoint 9
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

print("Great Job!")



