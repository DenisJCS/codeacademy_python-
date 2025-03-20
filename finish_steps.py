# Sample data (replace with actual data)
sales = ["$5.50", "$8.00", "$4.75", "$7.25"]
thread_sold = ["red", "blue&yellow", "green", "blue&white", "white", "red"]

# Step 13: Define total_sales and initialize to 0
total_sales = 0

# Step 14: Process sales to remove '$' and convert to float
for sale in sales:
    total_sales += float(sale.strip("$"))

# Step 15: Print total sales
print("Total Sales: ${:.2f}".format(total_sales))

# Step 16-17: Prepare to process thread sales
thread_sold_split = []

# Step 18: Split multi-color threads and append single colors
total_sales = 0
for thread in thread_sold:
    if "&" in thread:
        thread_sold_split.extend(thread.split("&"))
    else:
        thread_sold_split.append(thread)

# Step 19: Define function to count occurrences of a color
def color_count(color):
    return thread_sold_split.count(color)

# Step 20: Test function
print("White threads sold:", color_count("white"))

# Step 21: Define list of available colors
colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

# Step 22: Print count of each color
for color in colors:
    print("We sold {} threads of {} today.".format(color_count(color), color))
