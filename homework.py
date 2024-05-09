# Task 1: Restaurant Menu Update
# You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

# Problem Statement:
# Given the initial menu:

# Add a new category called "Beverages" with at least two items.
# Update the price of "Steak" to 17.99.
# Remove "Bruschetta" from "Starters".

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
#new beverage category w/ @least 2 items:
restaurant_menu["Beverages"] = {"Fountain Drink": 1.99, "Pink Lemonade": 2.99, "Milkshake": 2.99}
print(restaurant_menu)

#update price of steak
restaurant_menu["Steak"] = 17.99
print(restaurant_menu)

#Remove Bruschetta
#using a variable to print out the popped item
removed_item = restaurant_menu["Starters"].pop("Bruschetta", "that key doesnt exist")
print(removed_item)  #I dont know why this isnt printing*
print(restaurant_menu)

# class TicketTracker:
# Problem Statement: Develop a program that:
# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.

# Example ticket structure:


# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }


from collections import Counter

# Initialize service tickets dictionary
service_tickets =  {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket():
    global service_tickets
    # Generate ticket ID using "Ticket" & len(will give me the current # of tickets in dict.) +1 to add a # & .zfil I found online to help structure my Ticket ID by padding it with zeros, i put (3) for the character length
    ticket_id = "Ticket" + str(len(service_tickets) + 1).zfill(3)
    customer_name = input("Enter customer name: ")
    # Mapping of issue description numbers to actual problems
    issue_descriptions = {
        "1": "Login Problem",
        "2": "Payment Issue",
        "3": "Something else"
    }
    # Prompt user for ticket details and display the options for issue descriptions
    print("Choose the issue description:")
    for number, problem in issue_descriptions.items():
        print(f"{number}. {problem}")
    issue_description = input("Enter the number corresponding to the issue description: ")
    # Get the actual problem corresponding to the user's input
    actual_problem = issue_descriptions.get(issue_description)
    if actual_problem:
        service_tickets[ticket_id] = {"Customer": customer_name, "Issue": actual_problem, "Status": "open"}
        print("Ticket opened successfully.")
    else:
        print("Invalid issue description number. Ticket not opened.")


def update_ticket_status():
    global service_tickets
    ticket_id = input("Enter ticket ID to update status, (EX: Ticket007): ")
    new_status = input("Enter new status (open/closed): ")
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print("Ticket status updated successfully.")
    else:
        print("Ticket not found.")

def display_tickets(status=None): #set status=none because this function works for menu 3 & 4, you can view all tickets or just the open
    global service_tickets
    if status:
        filtered_tickets = [ticket for ticket, info in service_tickets.items() if info["Status"] == status]
        if filtered_tickets:
            for ticket in filtered_tickets:
                print(f"Ticket ID: {ticket}, Customer: {service_tickets[ticket]['Customer']}, Issue: {service_tickets[ticket]['Issue']}, Status: {service_tickets[ticket]['Status']}")
        else:
            print("No tickets with the specified status.")
    else:
        for ticket, info in service_tickets.items():
            print(f"Ticket ID: {ticket}, Customer: {info['Customer']}, Issue: {info['Issue']}, Status: {info['Status']}")


while True:
    print("\nMenu:")
    print("1. Add a new ticket")
    print("2. Update ticket status to closed")
    print("3. Display all tickets")
    print("4. Display open tickets")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        open_ticket()
    elif choice == "2":
        update_ticket_status()
    elif choice == "3":
        print("\nAll tickets:")
        display_tickets()
    elif choice == "4":
        print("\nOpen tickets:")
        display_tickets("open")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

















