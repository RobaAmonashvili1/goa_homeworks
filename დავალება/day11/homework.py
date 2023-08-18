for number in range(1, 101):
    if number % 15 == 0:
        print("GOA15")
    elif number % 5 == 0:
        print("GOA11")
    elif number % 3 == 0:
        print("GOA")
    else:
        print(number)