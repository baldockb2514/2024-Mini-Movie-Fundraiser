import pandas
import random

# Functions go here...


# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if response is blank, outputs error
        if response == "":
            print("Sorry this can't be blank. Please try again.")
        else:
            return response


# Checks user enters an integer to a given question
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter a valid integer.")


# Calculate the ticket price depending on the age
def price_calc(var_age):
    # price is 7.50 for those aged 15 and under
    if var_age <= 15:
        var_price = 7.50

    # price is 10.50 for those aged between 16 and 64
    elif var_age <= 64:
        var_price = 10.5

    # price is 6.50 for those aged 65 and over
    else:
        var_price = 6.5

    return var_price


# checks user response is a valid response based on a list of options
def string_check(question, answer_list, num_letters, error):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

        while True:
            for item in answer_list:
                if response == item[:num_letters] or response == item:
                    return item

            # If not, print error
            else:
                print(error)
                break


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# main routine starts here

# set max amount of tickets below
MAX_TICKETS = 5
tickets_sold = 0

# Lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# dictionary used to create data frame ie: column:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# string checker lists
yn_list = ["yes", "no"]
pay_list = ["cash", "credit"]

# Ask use if they want to see instructions
want_instructions = string_check("Do you want to read the instructions?: ", yn_list, 1, "Please answer yes / no")

if want_instructions == "yes":
    print("Instructions go here")

# loop to sell all tickets
while tickets_sold < MAX_TICKETS:
    print()
    name = not_blank("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    age = num_check("Please enter your age: ")

    # If age is between 12 and 120, continue
    if 12 <= age <= 120:
        pass

    # else, output error
    elif age < 12:
        print("Sorry you are too young to see this movie")
        continue

    else:
        print("?? That looks like a typo, please try again.")
        continue

    # calc ticket price
    ticket_price = price_calc(age)

    # get payment method
    pay_method = string_check("Choose a payment method (cash/credit): ", pay_list, 2, "Please answer cash/card.")

    # if paying with credit, surcharge is 5%
    if pay_method == "credit":
        surcharge = ticket_price * 0.05

    else:
        surcharge = 0

    print(f"Pay Method: {pay_method} "
          f"\nTicket Price: ${ticket_price + surcharge:.2f}")

    tickets_sold += 1

    # add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharge.append(surcharge)

# create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# calc the total ticket price (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calc the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calc the ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# currency formatting
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# choose a winner from our name list
winner_name = random.choice(all_names)

# get position of winner name in list
win_index = all_names.index(winner_name)

# look up total amount won (ie: ticket price + surcharge)
total_won = mini_movie_frame.at[win_index, 'Total']

print("---- Ticket Data ----")
print()

# output table with ticket data
print(mini_movie_frame)

print()
print("----- Ticket Cost / Profit")

# output total sales and profit
print(f"Total Ticket sales: ${total:.2f} \nTotal Profit: ${profit:.2f}")
print()

print()
print("---- Raffle winner ----")
print(f"Congratulations {winner_name}! You have won {total_won} ie: your ticket is free!")
print()

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the tickets!")

else:
    print(f"You have sold {tickets_sold} ticket/s. "
          f"There is {MAX_TICKETS - tickets_sold} ticket/s remaining.")
