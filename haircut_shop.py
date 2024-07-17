hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#Total price 
total_price = 0

for price in prices:
  total_price += price
print("Total prices",total_price)
#Average price
average_price = total_price/len(prices)
print("Average Haircut Price",average_price)
#New price
new_prices = [ price - 5 for price in prices]
print("New prices",new_prices)
#Revenue
total_revenue = 0
for i in range(len(hairstyles)):
  #Calculate revenur for each hairstyle
  revenue = prices[i] * last_week[i]
  total_revenue += revenue
  print(total_revenue)
#Revenue for each type of haircut
revenue_per_haircut = []
for i in range(len(hairstyles)):
  revenue = prices[i] * last_week[i]
  revenue_per_haircut.append(revenue)
for i in range(len(hairstyles)):
    print(f"Revenue for {hairstyles[i]}: ${revenue_per_haircut[i]}")
print("Total Revenue", total_revenue)
#Finding average revenue
average_daily_revenue = [total_revenue / 7]
print("Average daily revenue",average_daily_revenue)

#Cuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Cuts under 30", cuts_under_30)

Output :
Total prices 255
Average Haircut Price 31.875
New prices [25, 20, 35, 15, 15, 30, 45, 30]
60
135
335
495
575
715
1015
1085
Revenue for bouffant: $60
Revenue for pixie: $75
Revenue for dreadlocks: $200
Revenue for crew: $160
Revenue for bowl: $80
Revenue for bob: $140
Revenue for mohawk: $300
Revenue for flattop: $70
Total Revenue 1085
Average daily revenue [155.0]
Cuts under 30 ['bouffant', 'pixie', 'crew', 'bowl']




  




