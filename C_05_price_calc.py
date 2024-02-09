# Functions go here

# Calculate the ticket price depending on the age
def price_calc(var_age):

    # price is 7.50 for those aged 15 and under
    if var_age <= 15:
        price = 7.50

    # price is 10.50 for those aged between 16 and 64
    elif var_age <= 64:
        price = 10.5

    # price is 6.50 for those aged 65 and over
    else:
        price = 6.5

    return price


# loop for testing
while True:

    # Get age
    age = int(input("Age: "))

    # calc ticket price
    ticket_price = price_calc(age)
    print(f"Age: {age}, Ticket Price: ${ticket_price:.2f}")

