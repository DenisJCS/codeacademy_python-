# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1, 100) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)


import codecademylib3_seaborn

# Add your code below:
from matplotlib import pyplot as plt
import random 

numbers_a = range(1, 13)

numbers_b = random.sample(range(1000), 12)
print(numbers_b)

plt.plot(numbers_a, numbers_b)
plt.show()


# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)
