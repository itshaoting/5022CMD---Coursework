# ------- Q1 Hashing (i), (ii), (iii) -------

# --- (i) Implement a Hash Table that uses Linear Probing
# (Open Addressing) as its collision-resolution technique. ---

# Hash Table implementing Linear Probing
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
# A fixed-size array is used as underlying storage for hash table.

    # Hash function
    def hash_function(self, key):
        return key % self.size
    # It converts a key into valid index within table range.

    # Insert Function
    def insert(self, key, value):
        index = self.hash_function(key)

        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = (key, value)
    # Linear Probing resolves collision by checking next available slot.
    # Key-value pair is then stored in next available position.

    # Display Function *part of (ii)*
    def display(self):
        for i in range(self.size):
            item = self.table[i]

            if item is None:
                print(i, ": Empty")
            else:
                key, medicine = item
                print(i, ":", key, "-", medicine)
    # This function displays internal structure of hash table for verification.

    # Search Function *part of (iii)*
    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            stored_key, value = self.table[index]

            if stored_key == key:
                return value

            index = (index + 1) % self.size

            if index == start_index:
                break

        return None
    # Prevents infinite loop if table is fully traversed.
    # Otherwise, return None if key isn't found.



# --- (ii) Develop a simple Local Management System for a Pharmacy Store
# based on the data structure created in #1.
#   • You must create at least ONE (1) entity class to
# represent pharmacy products (e.g., Medicine).
#   • The system must be able to store at least
# ONE (1) type of item (e.g., tablets, syrup, supplements).
#   • Insert several predefined sample records into the hash table.
#   • You may determine:
#     o The size of the hash table
#     o The number of records to insert ---

# Medicine class
class Medicine:
    def __init__(self, med_id, med_name, med_type,
                 med_no, med_price):
        self.med_id = med_id
        self.med_name = med_name
        self.med_type = med_type
        self.med_no = med_no
        self.med_price = med_price
# This class represents a structured entity for pharmacy inventory system.

    def __str__(self):
        return (f"{self.med_name} ({self.med_type}) "
                f"- Number: {self.med_no} - RM{self.med_price}")
    # String representation is returned for display output.

# Predefined dataset for testing and demonstration purpose.
ht = HashTable(7)
m1 = Medicine(101, "Parcetamol", "Tablet",
              33, 13.75)
m2 = Medicine(102, "Ibuprofen", "Tablet",
              41, 23.95)
m3 = Medicine(103, "Vitamin C", "Supplement",
              67, 12.80)
m4 = Medicine(104, "Cough Syrup", "Syrup",
              21, 14.50)
m5 = Medicine(105, "Painkiller", "Tablet",
              49, 7.20)
# These codes insert key-value data pairs (sample medicine records) into hash table
# with linear probing.

ht.insert(m1.med_id, m1)
ht.insert(m2.med_id, m2)
ht.insert(m3.med_id, m3)
ht.insert(m4.med_id, m4)
ht.insert(m5.med_id, m5)
# Full object is stored as value, while Medicine ID is used as a key.

ht.display()
# This function displays the full pharmacy inventory, which helps verify insertion and collisions.



# --- (iii) Create a Command-Line Pharmacy Inventory System for the local storage system done in #2.
# Your Inventory System must display, have insert function and a search function,
# while the edit and delete function are optional. ---

def menu():
    while True:
        print("\n======= Pharmacy Inventory System =======")
        print("1. Display Medicines")
        print("2. Insert Medicine")
        print("3. Search Medicine")
        print("4. Exit")

        choice = input("Enter choice: ")
    # Accepts user input to perform different operations.

        # 1. Display
        if choice == "1":
            ht.display()
        # This function displays the full pharmacy inventory, which helps verify insertion and collisions.

        # 2. Insert Function
        elif choice == "2":
            med_id = int(input("Enter Medicine ID: "))
            med_name = input("Enter Medicine Name: ")
            med_type = input("Enter Medicine Type: ")
            med_no = int(input("Enter Medicine Quantity: "))
            med_price = float(input("Enter Price: "))

            medicine = Medicine(med_id, med_name, med_type,
                                med_no, med_price)
            ht.insert(med_id, medicine)
            print("Medicine inserted successfully.")
        # This function creates new Medicine object and stores it in hash table.

        # 3. Search Function
        elif choice == "3":
            med_id = int(input("Enter Medicine ID to search: "))
            result = ht.search(med_id)

            if result:
                print("Found: ", result)
            else:
                print("Medicine not found.")
        # This function searches hash table using key and return matching record if exists.


        # 4. Exit Function
        elif choice == "4":
            print("Exiting System...")
            break

        else:
            print("Invalid choice. Try again.")
        # This function terminates the program loop. Else function handles invalid menu input.

menu()
