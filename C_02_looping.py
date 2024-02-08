# main routine starts here

# set max amount of tickets below
MAX_TICKETS = 3

# loop to sell all tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    tickets_sold += 1


# Output numer of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the tickets!")

else:
    print(f"You have sold {tickets_sold} ticket/s. "
          f"There is {MAX_TICKETS - tickets_sold} ticket/s remaining.")
