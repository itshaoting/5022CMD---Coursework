# ------- Q2 Divide and Conquer Algorithm -------

# --- (ii) Create a Transaction entity class to represent a customer transaction in an online shopping system.
# You may include attributes such as:
# - transactionID
# - customerName
# - productName
# - amount
# - transactionDate
# You may choose appropriate data types for each attribute.

# Transaction class with 5 attributes. (self.xxx)
class Transaction:
    def __init__(self, transactionID, customerName, productName, amount, transactionDate):
        self.transactionID = transactionID
        self.customerName = customerName
        self.productName = productName
        self.amount = amount
        self.transactionDate = transactionDate

    # String Function that makes transactions readable.
    def __str__(self):
        return (f"ID: {self.transactionID} | "
                f"{self.customerName} | "
                f"{self.productName} | "
                f"RM{self.amount:.2f} | "
                f"{self.transactionDate}")



# --- (iii) Create a dataset of a minimum of TEN (10) transaction records and a maximum of THIRTY (30) records.
# Store them in a one-dimensional array or list. The dataset must initially be unsorted. ---

# One-dimensional list containing 15 predefined unsorted transaction records.
transactions = [
    Transaction(167, "Athif", "JBL Bluetooth Speaker", 39.99, "30-04-2026"),
    Transaction(210, "Herman", "Baseus Bass BP1 Pro Earbuds", 90.00, "20-05-2026"),
    Transaction(330, "Le Yee", "XBox Controller", 99.90, "25-06-2026"),
    Transaction(317, "Pei Wen", "LED Standing Mirror", 99.90, "14-06-2026"),
    Transaction(1, "Siew Pheng", "iPhone 12 Pro Clear Phone Case", 39.99, "28-11-2022"),
    Transaction(12, "Zephe", "Arknights Stickers", 9.99, "05-06-2023"),
    Transaction(137, "Callie", "JBL Bluetooth Speaker", 39.99, "30-04-2025"),
    Transaction(128, "Hao Ting", "Black Square Frame Glasses", 8.48, "03-03-2025"),
    Transaction(165, "Jansen", "RS PRO Pipe Wrench", 383.30, "15-04-2026"),
    Transaction(162, "Ken", "Presonus M7 Microphone", 209.00, "04-04-2026"),
    Transaction(117, "Hans", "Pokemon TCG Mega Evolution", 36.20, "30-12-2024"),
    Transaction(45, "Kinger", "Driving Gloves Suede", 92.70, "30-04-2024"),
    Transaction(146, "Justin", "Driving Gloves Suede", 39.99, "03-07-2025"),
    Transaction(289, "Lakshna", "JBL Bluetooth Speaker", 39.99, "01-06-2026"),
    Transaction(216, "Sean", "XBox Controller", 99.90, "21-05-2026"),
]



# --- (i) Implement a Divide and Conquer algorithm to solve the following problem.
# Develop a system that sorts and searches customer transaction data using:
# o Merge Sort (Divide and Conquer sorting algorithm)
# o Binary Search (Divide and Conquer searching algorithm)
# Your implementation must:
# o Clearly separate the divide, conquer, and combine steps
# o Show recursive implementation
# o Include comments explaining each stage ---

# Merge Sort (Divide and Conquer Sorting Algorithm)
# Sort transactions by transactionID
merge_sort_calls = 0
def merge_sort(arr):
    global merge_sort_calls
    merge_sort_calls += 1
    # This variable is part of (v).
    # Global counter is used to track number of recursive calls in Merge Sort.
    # This helps analyze the divide-and-conquer behavior of the algorithm.

    if len(arr) <= 1:
        return arr

    # Divide Step: Splits the list into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Conquer Step: Recursively sort left and right halves.
    # Combine Step: Merge sorted halves into final sorted array.
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].transactionID < right[j].transactionID:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Merge 2 sorted halves into one sorted list by comparing elements one by one.

    # Add remaining elements if there's any. These are already sorted.
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Binary Search (Divide and Conquer searching algorithm)
# Efficiently locate a transaction in the sorted dataset.
def binary_search(arr,target, low, high):
    if low > high:
        return None # if target is not found in the dataset

    mid = (low + high) // 2

    if arr[mid].transactionID == target:
        return arr[mid]
    elif arr[mid].transactionID > target:
        return binary_search(arr, target, low, mid-1)
    else:
        return binary_search(arr,target,mid+1,high)
    # Binary Search checks the middle.
    # If it's too big, they go left. If it's too small, they go right.



# --- (iv) Perform the following operations:
def performance_demo():
    import time
    global sorted_transactions

    # a) Sort the transactions based on transactionID using Merge Sort. You must:
    # • Display the array before sorting
    print("\n--- Before Sorting: ---")
    for t in transactions:
        print(t)

    # • Display the array after sorting

    start = time.perf_counter()
    sorted_transactions = merge_sort(transactions.copy())
    # Transactions.copy prevents original dataset mutation
    end = time.perf_counter()

    merge_sort_time = end - start

    print("\n--- After Sorting: ---")
    for t in sorted_transactions:
        print(t)


    # • Show recursive calls (optional but encouraged)---



    # b) Search for a specific transaction using Binary Search.
    # You must:
    # • Search for one existing transaction
    print("\n--- Binary Search: Existing Transaction ---")

    target = 167

    start = time.perf_counter()
    result = binary_search(sorted_transactions, target, 0, len(sorted_transactions)-1)
    end = time.perf_counter()

    binary_search_time_1 = end - start

    print(f"Searching for ID: {target}")

    if result is not None:
        print("Found Transaction:")
        print(result)
    else:
        print("Transaction NOT found")
    # • Display appropriate messages


    # • Search for one non-existing transaction
    target = 168

    start = time.perf_counter()
    result = binary_search(sorted_transactions, target, 0, len(sorted_transactions)-1)
    end = time.perf_counter()

    binary_search_time_2 = end - start

    print(f"\nSearching for ID: {target}")

    if result is not None:
        print("Found Transaction:")
        print(result)
    else:
        print("Transaction NOT found")
    # • Display appropriate messages



    # c) Compare both performance
    # Measure execution time and analyze the results for Merge Sort and Binary Search.
    print("\n=== Performance Comparison between Merge Sort and Binary Search ===")
    print(f"Merge Sort Time: {merge_sort_time:.7f} seconds")
    print(f"Binary Search Time (Existing Transaction): {binary_search_time_1:.7f} seconds")
    # Time measurement is used to compare algorithm efficiency between sorting and searching.
    # Merge Sort has O(n log n) complexity because it recursively divides the dataset and merges sorted halves.
    # Binary Search has O(log n) complexity because it eliminates half of the search space at each step after...
    # ...the dataset is sorted.
    # Therefore, Binary Search is faster for lookup operations, but it requires a pre-sorted dataset.



# 5. Design a menu-driven program that allows the user to:
# ❖ Mandatory Features (Compulsory):
# a) Display all of transactions
# b) Sort transactions using Merge Sort
# c) Search transaction using Binary Search
# d) Search transaction using Linear Search (for comparison).
# e) Count number of recursive calls made during Merge Sort. (Extra)

# (1) Display Function
def display_transactions(data):
    print("\n--- Transaction Records ---")
    for t in data:
        print(t)

# (4) Linear Search (For Comparison)
def linear_search(arr, target):
    for transaction in arr:
        if transaction.transactionID == target:
            return transaction
    return None
# Time Complexity is O(n)

sorted_transactions = merge_sort(transactions)
# Sorted once for Binary Search

def menu():
    while True:
        global merge_sort_calls
        global sorted_transactions
        print("\n=== Online Shopping Menu ===")
        print("1. Display Transactions")
        print("2. Sort using Merge Sort")
        print("3. Search using Binary Search")
        print("4. Search using Linear Search")
        print("5. Performance Demo")
        print("6. Count Number of Recursive Calls Made during Merge Sort")
        print("7. Exit")

        choice = input("Enter choice: ")

        # 1. Display
        if choice == "1":
            display_transactions(transactions)


        elif choice == "2":
            merge_sort_calls = 0  # reset before sorting

            print("\n--- Transactions After Merge Sort ---")

            sorted_transactions = merge_sort(transactions)

            display_transactions(sorted_transactions)


        elif choice == "3":
            target = int(input("Enter Transaction ID to search: "))

            result = binary_search(
                sorted_transactions,
                target,
                0,
                len(sorted_transactions) - 1)

            if result is not None:
                print("\nTransaction Found:")
                print(result)
            else:
                print("\nTransaction NOT Found.")


        elif choice == "4":
            target = int(input("Enter Transaction ID to search: "))

            result = linear_search(transactions, target)

            if result:
                print("\nTransaction Found:")
                print(result)
            else:
                print("\nTransaction NOT Found.")


        elif choice == "5":
            performance_demo()


        elif choice == "6":
            print(f"\nTotal Recursive Calls in Merge Sort: {merge_sort_calls}")


        elif choice == "7":
            print("\nExiting System...")
            break

        else:
            print("\nInvalid choice. Please try again.")


menu()
