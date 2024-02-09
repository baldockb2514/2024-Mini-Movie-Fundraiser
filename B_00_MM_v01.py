# Functions go here...

# checks that user response is yes/no
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # Return user response if it's yes/no
        if response == "yes" or response == "y":
            response = "Yes"
            return response


        elif response == "no" or response == "n":
            response = "No"
            return response

        # else, output error
        else:
            print("Please answer yes / no")


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


# main routine starts here

# set max amount of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# Ask use if they want to see instructions
want_instructions = yes_no("Do you want to read the instructions?: ")

if want_instructions == "Yes":
    print()
    print("Instructions go here")


# loop to sell all tickets
while tickets_sold < MAX_TICKETS:
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

    tickets_sold += 1


# Output number of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the tickets!")

else:
    print(f"You have sold {tickets_sold} ticket/s. "
          f"There is {MAX_TICKETS - tickets_sold} ticket/s remaining.")

