
import PNR
trains = [
    {"train_no": "101", "train_name": "Express A", "source": "Delhi", "destination": "Mumbai", "seats": 55},
    {"train_no": "102", "train_name": "Superfast B", "source": "Kolkata", "destination": "Chennai", "seats": 34},
    {"train_no": "103", "train_name": "Mail C", "source": "Jaipur", "destination": "Pune", "seats": 43},
    {"train_no": "104", "train_name": "Shatabdi Express", "source": "NDLS", "destination": "BPL", "seats": 50, },
    {"train_no": "105", "train_name": "Rajdhani Express", "source": "BPL", "destination": "NDLS", "seats": 50,},
    {"train_no": "106", "train_name": "Intercity Express", "source": "JHS", "destination": "LKO", "seats": 100, },

]


# Function to view all trains
def view_trains():
    print("\n--- All Trains ---")
    for t in trains:
        print(f"Train No: {t['train_no']}, Name: {t['train_name']}, "
              f"From: {t['source']} To: {t['destination']}, "
              f"Available Seats: {t['seats']}")
    print()


# Function to search a train by number
def search_train():
    print("\n--- Search Train ---")
    num = input("Enter Train Number to search: ")

    for t in trains:
        if t["train_no"] == num:
            print("Train Found!")
            print(f"Train No: {t['train_no']}")
            print(f"Train Name: {t['train_name']}")
            print(f"Route: {t['source']} → {t['destination']}")
            print(f"Available Seats: {t['seats']}\n")
            return
    else:   
             print("Train not found.\n")


# Function to book seats
def book_seat():
    print("\n--- Book Seat ---")
    num = input("Enter Train Number: ")

    for t in trains:
        if t["train_no"] == num:
            if t["seats"] > 0:
                t["seats"] -= 1
                print("Seat booked successfully!")
                print(PNR.generate_pnr())
                print(f"Remaining Seats: {t['seats']}\n")
            else:
                print("No seats available.\n")
            return

    print("Train not found.\n")


# Main menu
def main():
    while True:
        print("===== Train Management System =====")
        print("1. View All Trains")
        print("2. Search Train")
        print("3. Book Seat")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_trains()
        elif choice == "2":
            search_train()
        elif choice == "3":
            book_seat()
        elif choice == "4":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Start the program
main()