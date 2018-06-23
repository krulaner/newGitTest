name = input("What is your name? ")
meal = input("Did you have breakfast, lunch, or dinner? ")


amount = (input(f"Hello {name} please put down how much you will pay in dollars: ")) # user gives amount in dollars
pay = float(amount.replace("$", "")) #strips the dollar sign from the amount and turns the string into a float

# our tip options for the user
first_option = pay * .15
second_option = pay * .18
third_option = pay * .20

# displays all options to user
print(f"15% tip: ${first_option:.2f}")
print(f"18% tip: ${second_option:.2f}")	
print(f"20% tip: ${third_option:.2f}")

# enter in amount to be added to the final
pick_option = input(f"Please choose between ${first_option:.2f}, ${second_option:.2f}, or ${third_option:.2f} to tip for your final amount: ")
final_amount = pay + float(pick_option.replace("$", ""))#strips the dollar sign from the amount, turns the string into a float, and adds for the total

# total amount with tip due at time of checkout
print(f"The total amount due for your {meal} with tip was: ${final_amount:.2f}")

