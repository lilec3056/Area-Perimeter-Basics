
error = "Please enter a number more than zero\n"
while True:
    try:
        # ask the user for a width
        response = float(input("Width: "))

        # check the number is more than 0
        if response > 0:
            break
        else:
            print(error)

    except ValueError:
         print(error)