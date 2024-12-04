weight =50;

#Ground shipping 
if weight <=2:
  cost_ground = weight * 1.5 +20
elif weight >2 and weight <=6:
  cost_ground = weight * 3.0 + 20
elif weight >6 and weight <=10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20
  print("Ground Shipping",'$',cost_ground)
 
 
  #Cost Ground Premium
cost_ground_premium = 125
print("Ground Shipping Premium",'$',
cost_ground_premium)

#Drone shipping
weight = 5.6
#Price counting
if weight <=2:
  cost_drone= weight * 4.50
elif weight >2 and weight <=6:
  cost_drone = weight * 9.00
elif weight >6 and weight <=10:
  cost_drone = weight * 12.00
else:
    cost_drone =weight * 14.25
print("Drone Shipping",'$',cost_drone)





Ground Shipping $ 257.5
Ground Shipping Premium $ 125
Drone Shipping $ 50.4


