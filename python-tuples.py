"""
1. Tuple Mastery in Python

Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"
"""

def format_itineraries(itineraries):
    formatted_itineraries = []
   
    for index, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        itinerary = f"Itinerary {index}: {traveler_name} - From {origin} to {destination}"
        formatted_itineraries.append(itinerary)
    return "\n".join(formatted_itineraries)


def get_user_itineraries():
    itineraries = []
    
    while True:
        traveler_name = input("Enter the traveler's name (or type 'done' to finish): ")
        if traveler_name.lower() == 'done':
            break
        
        origin = input("Enter the origin: ")
        
        destination = input("Enter the destination: ")
        
        itinerary_tuple = (traveler_name, origin, destination)
        
        itineraries.append(itinerary_tuple)
        
        print(f"Itinerary for {traveler_name} added.")
    
    return itineraries

user_itineraries = get_user_itineraries()

print("\nList of itineraries:")
print(user_itineraries)


print("\nIndividual itineraries:")
for index, itinerary in enumerate(user_itineraries, start=1):
    print(f"Itinerary {index}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}")


"""
2. Python Data Structure Challenges in Real-World Scenarios
Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.
"""


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):
   
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")

    if (title, author) in library:
        print(f"'{title}' by {author} is already in the library.")
    else:
        library.append((title, author))
        print(f"'{title}' by {author} has been added to the library.")

def display_library(library):
  
    print("\nLibrary:")
    print(library) 

    print("\nBooks in the Library:")
    for title, author in library:
        print(f"- '{title}' by {author}")

display_library(library)

while True:
    add_book(library)
    display_library(library)
    
    another = input("Do you want to add another book? (yes/no): ").strip().lower()
    if another != 'yes':
        break

print("\nFinal Library:")
display_library(library)


"""
3. Mastering Tuple Packing and Unpacking in Python
Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python.

Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]
- Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.
"""


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Josh", "Smartphone", 3),
    ("Marina", "Tablet", 1)
]

def display_orders(orders):
   
    print("Customer Orders:")
    for customer_name, product, quantity in orders:
        print(f"{customer_name} ordered {quantity} {product}(s).")


display_orders(orders)