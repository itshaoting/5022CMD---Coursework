# --- (iv) Compare the performance of searching for records in the Hash Table (Linear Probing)
# with a one-dimensional array. For this comparison to work, you must insert the same data
# into the array and measure the execution time for the searching, perform multiple searches
# (existing and non-existing keys). Analyze the results and provide the explanations of why
# one is more superior in performance compared with the other. ---

import time
import random

# Medicine Class
class Medicine:
    def __init__(self, med_id, name, med_type, quantity, price):
        self.med_id = med_id
        self.name = name
        self.med_type = med_type
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.med_type}) - RM{self.price}"



# Hash Table (Linear Probing)
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = (key, value)

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



# Array Search (Linear Search)
def array_search(arr, key):
    for item in arr:
        if item.med_id == key:
            return item
    return None
# Array uses Linear Search with O(n) time complexity to inspects elements one by one
# from index 0 (beginning) until target is found or end of array is reached.
# Hash Table uses a hash function to calculate starting index,
# getting direct access to the appropriate bucket.



# Create Data Set
ht = HashTable(2000)
array = []
# Hash Table has 2000 buckets (slots).
# Using more buckets reduces collisions for fast searching. O(1)
# This allows searches to remain close to O(1) on average.
# This provides a fair comparison with the array search.

# Sample Data
for i in range(200):
    med = Medicine(
        i,
        f"Med{i}",
        "Tablet",
        random.randint(1, 100),
        round(random.uniform(5, 100), 2)
    )

    ht.insert(med.med_id, med)
    array.append(med)
# This function runs 200 times, creating one Medicine object each time.
# Hash Table contains 2000 Buckets but only 200 records,
# It means only about 10% of the table is occupied.
# Collisions are less likely to occur in result.

# Search Test Keys
test_keys = []

# Existing Keys
for i in range(500):
    test_keys.append(random.randint(0, 200- 1))

# Non-existing Keys
for i in range(500):
    test_keys.append(random.randint(2000, 2000 * 2))
# Empty list stores all keys that will be searched later.
# 500 existing and non-existing keys are both generated.
# This allows experiment to evaluate both successful and...
# ...unsuccessful search operations for an average-case performance.


# Hash Table Timing Test
start = time.perf_counter()

for key in test_keys:
    ht.search(key)

end = time.perf_counter()

hash_time = end - start



# Array Timing Test
start = time.perf_counter()

for key in test_keys:
    array_search(array, key)

end = time.perf_counter()

array_time = end - start
# Both timing tests measure total execution time.
# They're required to search all test keys.
# The first test uses Hash Table,
# while the second uses one-dimensional array.



# Results
print("\n=== Performance Comparison between Hash Table and Array ===")
print(f"Hash Table Search Time: {hash_time:.7f} seconds")
print(f"Array Search Time     : {array_time:.7f} seconds")
# This section displays the execution times for both search methods.
# Hash Tables generally perform faster than arrays...
# ...on average because they have O(1) average search complexity,
# whereas array searches require O(n) time.
