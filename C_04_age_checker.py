# Functions go here

# Checks user enters an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter a valid integer.")


# Main routine goes here
tickets_sold = 0

while True:

    name = input("Enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = num_check("Age: ")

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

print(f"You sold {tickets_sold} ticket/s")
