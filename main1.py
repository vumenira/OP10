garage = {}

while True:
    command = input("Your command (add, view, exit): ").split()
    if command[0].lower().strip() == "add" and len(command) == 4:
        garage[command[1]] = {"make":command[2], "year":command[3]}
    elif command[0].lower().strip() == "view" and len(command) == 2:
        print(f"Marka: {garage[command[1]]["make"]}, year: {garage[command[1]]["year"]}")
    elif command[0].lower().strip() == "exit":
        exit()
    else:
        print(f"Try again command: {command[0]} is not found. Or there are not enough arguments.")