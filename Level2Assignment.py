#Davis Passino

#Here are the needed inputs for the program:

print("ROAD TRIP PLANNER")
user_name = input("What is your name? ")
destination = input("Where do you want to go? ")       
one_way_distance = float(input("How far away is this destination? "))
miles_per_gallon = float(input("What is your vehicle's MPG? "))
gas_price = float(input("What is the cost of gas per gallon? "))
travelers_number = int(input("What is the total amount of travelers? "))

#Here are my calculations:

total_miles = (one_way_distance * 2)
gas_needed = (total_miles / miles_per_gallon)
gas_cost = (gas_needed * gas_price)
cost_per_person = (gas_cost / travelers_number)

#Here are my outputs for the trip summary:

print(f"TRIP SUMMARY FOR {user_name.upper()}'S TRIP TO {destination.upper()}")
print("The total cost of a round trip: $" + str(round (gas_cost, 2)))
print("The cost per traveler is: $" + str(round (cost_per_person, 2)))
print("Bon voyage!")

