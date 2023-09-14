print("Menu:")
print("1. Draw a Triangle")
print("2. Draw a Rectangle")
print("3. Draw a Pyramid")
print("4. Quit")
print()

while True:
    selector = input("Enter your choice (1/2/3/4): ")
    if selector == "4":
        print("Goodbye!")
        break

    elif selector == "1":
        rows = int(input("Enter the number of rows for the triangle: "))
        direction = input("Enter 'u' for upward or 'd' for downward: ")
        if direction == "u":
            for u in range(1, rows + 1):
                print(u * "*")
            continue
        if direction == "d":
            for d in range(rows, 0, -1):
                print(d * "*")
                continue
    elif selector == "2":
        rows = int(input("Enter the number of rows for the rectangle: "))
        columns = int(input("Enter the number of columns for the rectangle: "))
        for row in range(rows):
            print(columns * "*")
        continue
    elif selector == "3":
        rows = int(input("Enter the number of rows for the pyramid: "))
        spacer = rows - 1
        star = 1
        for i in range(rows):
            print(spacer * " " + star * "*")
            star += 2
            spacer -= 1
        continue
    elif selector != "1" or selector != "2" or selector != "3":
        continue
