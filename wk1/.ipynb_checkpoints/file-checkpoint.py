with open("data.txt") as f:
    num = 0
    for line in f:
        number = int(line)  # Here we do the type conversion
        new_number = number * 10  # Here is where we do our "data analysis"
        print(new_number)
        
        num = new_number + num
        print(num)
