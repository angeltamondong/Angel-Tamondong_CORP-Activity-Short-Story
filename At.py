import random

# Basic setup
astronaut = input("What's your astronaut name? ")
print(f"Welcome, {astronaut}!")

# Fixed location & simple ship selection
space_station = "Moon Base One"
ships = ["Star Scout", "Moon Rover", "Sky Pilot"]

print("\nAvailable ships:", ", ".join(ships))
while True:
    ship = input("Pick your ship: ")
    if ship in ships:
        print(f"Ship {ship} ready for mission!")
        break
    print("Not a valid ship - try again!")

# Simple alien interaction
print(f"\nAt {space_station}, you spot an alien signal!")
contact_choice = input("Contact alien? (yes/no): ").lower()

if contact_choice == "yes":
    success = random.choice([True, False])
    if success:
        print("Alien responds - friendly contact made! Mission SUCCESS.")
    else:
        print("No response - alien moves away. Mission FAILED.")
else:
    print("You decide not to contact - mission ended early.")

