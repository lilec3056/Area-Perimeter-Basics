def num_check(question):
    error = "Please enter a number more than zero\n"
    while True:
        try:
            # ask the user for a width/height
            response = float(input(question))

            # check the number is more than 0
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here

keep_going = ""
while keep_going == "":
    # get width and height
    width = num_check("Width: ")
    print(width)

    print()

    height = num_check("Height: ")
    print(height)

    # calculate area and perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # display output
    print()
    print(f"Area: {area} square units")
    print(f"Perimeter: {perimeter} units")

    # ask user if they want to keep going
    keep_going = input("Press enter to continue other wise press any other key to quit ")
    print()

print("Thanks for using this area/perimeter calculator")