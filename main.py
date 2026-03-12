import file_utils

def display_menu():
    print("\n--- 🏀 COURT VISION MENU ---")
    print("1. Add New Player")
    print("2. Record Game Stats")
    print("3. View All Players")
    print("4. Save and Exit")

def main():
    # Store players in a dictionary: {jersey_number: PlayerObject}
    players = file_utils.load_players()

    print("Discovered " + str(len(players)) + " players")#
    print(players)

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            # TODO: Get inputs, validate them, and add to the 'players' dictionary
            pass

        elif choice == "2":
            # TODO: Ask for a jersey number and update stats
            pass

        elif choice == "3":
            # TODO: Loop through 'players' and print details + Efficiency
            # TODO: HINT: for player in players.values():
            pass

        elif choice == "4":
            file_utils.save_players(players)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()