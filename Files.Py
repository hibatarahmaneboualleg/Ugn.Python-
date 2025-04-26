print("=== User Registration ===\n")

with open("users.txt", "a") as file:
    continue_adding = True

    while continue_adding:
        print("--- Add New User ---")
        name = input("Enter your name: ").strip()
        age = input("Enter your age: ").strip()
        phone = input("Enter your phone number: ").strip()

        file.write(f"{name}, {age}, {phone}\n")
        
        answer = input("\nDo you want to add another user? (yes/no): ").strip().lower()
        continue_adding = (answer == "yes")

print("\n=== All Registered Users ===\n")

with open("users.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\n=== End of Users List ===")
