for number in range(1, 101):
    count = 0

    for factor in range(1, number + 1):
        if number % factor == 0:
            count = count + 1

    if count == 3:
        print(number)