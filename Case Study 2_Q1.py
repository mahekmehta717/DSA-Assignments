MAX = 50
queue = []

while True:
    print("\n1.Add Passenger")
    print("2.Serve Passenger")
    print("3.View First Passenger")
    print("4.Display Passenger Queue")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        ticket = input("Enter Ticket ID: ")
        status = input("Enter Status: ")

        if len(queue) == MAX:
            print("Queue Full")

        elif status != "Confirmed":
            print("Only Confirmed passengers can join the queue")

        elif any(p[0] == ticket for p in queue):
            print("Ticket ID must be unique")

        else:
            queue.append((ticket, status))

    elif ch == 2:
        if queue:
            print("Served:", queue.pop(0))
        else:
            print("No Passengers")

    elif ch == 3:
        if queue:
            print("First Passenger:", queue[0])
        else:
            print("No Passengers")

    elif ch == 4:
        print(queue)

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
