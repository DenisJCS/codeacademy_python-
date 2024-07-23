# Write your code below:

def trip_planner(first_destination, second_destination,final_destination="Codecademy HQ"):
 print("Here is what your trip will look like!")
 print("First, we will stop in " + first_destination + " , then " + second_destination + ", and lastly " + final_destination )
 
trip_planner("London", "India", "New Zeland")
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France","Germany")
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")
trip_planner("Brooklyn", "Queens")

Here is what your trip will look like!
First, we will stop in London , then India, and lastly New Zeland

Here is what your trip will look like!
First, we will stop in France , then Germany, and lastly Denmark

Here is what your trip will look like!
First, we will stop in Denmark , then France, and lastly Germany

Here is what your trip will look like!
First, we will stop in Iceland , then India, and lastly Germany

Here is what your trip will look like!
First, we will stop in Brooklyn , then Queens, and lastly Codecademy HQ





















#TripPlanner V1.0
def trip_planner_welcome(name):
   print("Welcome to tripplanner v1.0 :"+ name)
trip_planner_welcome("<Your Name Here>")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.43)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
 print("Your trip start off in " + origin)
 print("And you are traveling to " + destination)
 print("You will be traveling by " + mode_of_transport)
 print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Frace","London",estimate)


  






