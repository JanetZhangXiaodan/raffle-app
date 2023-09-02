import random
import sys

# Global variables
pot = 100
tickets_sold = 0
participants = []
winning_ticket = []
draw_started = False

# Function to generate a random ticket
def generate_ticket():
    return random.sample(range(1, 16), 5)

# Function to start a new draw
def start_new_draw():
    global pot, draw_started
    pot = 100
    draw_started = True
    print("A new draw has been started with a pot of $100.")
    input("Press any key to return to the main menu.")

# Function to buy tickets
def buy_tickets():
    global tickets_sold
    try:
        user_input = input("Enter your name and the number of tickets to purchase (e.g., James,1): ")
        name, num_tickets = map(str.strip, user_input.split(','))
        num_tickets = int(num_tickets)
        if num_tickets < 1 or num_tickets > 5:
            print("Invalid number of tickets. You can purchase between 1 and 5 tickets.")
            return
    except ValueError as e:
        print(e)
        print("Invalid input. Please enter your name and the number of tickets to purchase.")
        return
    
    tickets = [generate_ticket() for _ in range(num_tickets)]
    participants.append({"name": name, "tickets": tickets})
    tickets_sold += num_tickets
    print(f"Hi {name}, you have purchased {num_tickets} ticket(s):")
    for i, ticket in enumerate(tickets):
        print(f"Ticket {i + 1}: {', '.join(map(str, ticket))}")
    input("Press any key to return to the main menu.")


def combine_nested_lists(input_list):
    combined_list = []
    for sublist in input_list:
        combined_list.extend(sublist)
    return combined_list

# Function to run the raffle
def run_raffle():
    global pot, participants, winning_ticket, tickets_sold, draw_started
    if not draw_started:
        print("Raffle draw has not been started yet.")
    elif tickets_sold == 0:
        print("No tickets have been purchased for this draw.")
    else:
        # Generate a winning ticket
        winning_ticket = generate_ticket()
        print("Running Raffle...")
        print("Winning Ticket is: {}".format(', '.join(map(str, winning_ticket))))

        winners = {"Group 2": [], "Group 3": [], "Group 4": [], "Group 5": []}

        # Check purchased tickets against the winning ticket
        for participant in participants:
            for ticket in participant["tickets"]:
                matching_numbers = len(set(ticket).intersection(winning_ticket))
                if matching_numbers == 2:
                    winners["Group 2"].append(participant["name"])
                elif matching_numbers == 3:
                    winners["Group 3"].append(participant["name"])
                elif matching_numbers == 4:
                    winners["Group 4"].append(participant["name"])
                elif matching_numbers == 5:
                    winners["Group 5"].append(participant["name"])

        # Calculate rewards
        total_reward = pot
        print("\nGroup 2 Winners:")
        for winner in winners["Group 2"]:
            reward = total_reward * 0.1 / len(winners["Group 2"])
            print("{} with {} winning ticket(s) - ${:.2f}".format(winner, participants[participants.index(participant)]["tickets"].count(ticket), reward))
            total_reward -= reward

        print("\nGroup 3 Winners:")
        for winner in winners["Group 3"]:
            reward = total_reward * 0.15 / len(winners["Group 3"])
            print("{} with {} winning ticket(s) - ${:.2f}".format(winner, participants[participants.index(participant)]["tickets"].count(ticket), reward))
            total_reward -= reward

        print("\nGroup 4 Winners:")
        for winner in winners["Group 4"]:
            reward = total_reward * 0.25 / len(winners["Group 4"])
            print("{} with {} winning ticket(s) - ${:.2f}".format(winner, participants[participants.index(participant)]["tickets"].count(ticket), reward))
            total_reward -= reward

        print("\nGroup 5 Winners (Jackpot):")
        for winner in winners["Group 5"]:
            reward = total_reward * 0.5 / len(winners["Group 5"])
            print("{} with {} winning ticket(s) - ${:.2f}".format(winner, participants[participants.index(participant)]["tickets"].count(ticket), reward))
            total_reward -= reward

        pot = total_reward
        participants = []
        tickets_sold = 0
        draw_started = False
        input("Press any key to return to the main menu.")

# Main menu loop
if __name__ == "__main__":
    while True:
        print("Welcome to My Raffle App")
        print(f"Status: {'Draw has not started' if not draw_started else 'Draw is in progress'}")
        print("[1] Start a New Draw")
        print("[2] Buy Tickets")
        print("[3] Run Raffle")
        print("[4] Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            start_new_draw()
        elif choice == '2':
            buy_tickets()
        elif choice == '3':
            run_raffle()
        elif choice == '4':
            sys.exit()  # Exit the program
        else:
            print("Invalid choice. Please enter a valid option.")
