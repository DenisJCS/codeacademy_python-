# Uncomment this when you reach the "Use the Force" section
# train_mass = 22680
# train_acceleration = 10
# train_distance = 100
# bomb_mass = 1

# Write your code below: 
def f_to_c(f_temp):
  """Turn up the Temperature"""
  c_temp = (f_temp - 32) * 5/9
  return c_temp
c_temp = f_to_c(0)
print(c_temp)


#Function from c to f
def c_to_f(c_temp):
  """Turn c to f  """
  f_temp = (c_temp * 9/5) + 32
  return f_temp
f_temp = c_to_f(0)
print(f_temp)

#Use the Force
def get_force(mass, acceleration):
  """Multiply mass and acceleration"""
  train_force = mass * acceleration
  return train_force
train_force = get_force(2268,9.8)
print(train_force)

#Checkpoint 7
print("The GE tran supplies 228600 Newton of force" )
def get_energy(mass, c = 3*10**8 ):
  bomb_energy = mass * c
  return bomb_energy
bomb_energy = get_energy(1, 3*10**8)
print(bomb_energy)

#Checkpoint 10
print("A 1kg bomb suppies 300000000 Joules ")
def get_force(mass, acceleration):
  """Multiply mass and acceleration"""
  force = mass * acceleration
  return force
def get_work(mass,acceleration, distance):
   force = get_force(mass, acceleration)
   work = force * distance
   return work
mass = 22680
acceleration = 10
distance = 100

#Calculating
work_done = get_work(mass,acceleration , distance)
print(work_done)

print("The GE train does 22680000 Joules of work over 100 meters")




-17.77777777777778
32.0
22226.4
The GE tran supplies 228600 Newton of force
300000000
A 1kg bomb suppies 300000000 Joules 
22680000
The GE train does 22680000 Joules of work over 100 meters
