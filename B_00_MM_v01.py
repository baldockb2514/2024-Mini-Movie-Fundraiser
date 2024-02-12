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
                print()
                break


# main routine starts here

# set max amount of tickets below
MAX_TICKETS = 3
tickets_sold = 0

yn_list = ["yes", "no"]
pay_list = ["cash", "credit"]

# Ask use if they want to see instructions
want_instructions = string_check("Do you want to read the instructions?: ", yn_list, 1, "Please answer yes / no")

if want_instructions == "Yes":
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
        price = price_calc(age)
        buy_ticket = string_check(f"Your ticket is ${price:.2f}. "
                                  f"Would you like to buy?", yn_list, 1, "Please answer yes / no")
        if buy_ticket == "Yes":
            pass

        else:
            continue

    # else, output error
    elif age < 12:
        print("Sorry you are too young to see this movie")
        continue

    else:
        print("?? That looks like a typo, please try again.")
        continue

    tickets_sold += 1
    # calc ticket price
    ticket_price = price_calc(age)

    # get payment method
    pay_method = string_check("Choose a payment method (cash/credit): ", pay_list, 2, "Please answer cash/card.")

# Output number of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the tickets!")

else:
    print(f"You have sold {tickets_sold} ticket/s. "
          f"There is {MAX_TICKETS - tickets_sold} ticket/s remaining.")
