MAX = 15
stack = []

while True:
    print("\n1.Call Function")
    print("2.Return from Function")
    print("3.Current Function")
    print("4.Display Call Stack")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter Function Name: ")

        if len(stack) == MAX:
            print("Call Stack Full")

        elif not name or not name[0].isalpha():
            print("Invalid Function Name")

        elif stack.count(name) >= 3:
            print("Recursive calls allowed only up to 3 levels")

        else:
            stack.append(name)

    elif ch == 2:
        if stack:
            print("Returned:", stack.pop())
        else:
            print("No Function Calls")

    elif ch == 3:
        if stack:
            print("Current Function:", stack[-1])
        else:
            print("No Function Calls")

    elif ch == 4:
        print(stack)

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
