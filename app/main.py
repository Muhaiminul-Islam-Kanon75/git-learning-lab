from app.quiz import start_quiz
from app.simulator import simulate_command


def menu():
    while True:
        print("\n=== Git Learning Lab ===")
        print("1. Start Quiz")
        print("2. Simulate Git Command")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            start_quiz()

        elif choice == "2":
            command = input("Enter git command: ")
            simulate_command(command)

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()