# --- (ii) Write a function that performs the calculation of a Factorial based on a given number.
# Derive the Big-O of this function by calculating the number of primitive operations
# and explain its time complexity. ---

import threading
import time

# Factorial Function
def factorial(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result
# This function stores the multiplication result, then multiply the result by each integer from 1 to n.
# It's O(n) time complexity



# --- (iii) Using multithreading:
# ▪ Write a program to calculates the factorials: 50!, 100! and 200!.
# Use multithreading and create a separate thread to handle each set of the operation
# (i.e. you must create 3 separate threads to handle the 3 sets, 1 thread for each set).

# This function runs factorial calculations using multithreading (3 parallel threads)
def multithreading_test():
    times = []

    for round_no in range(1,11):
        start_time = time.time_ns()

        # Create 3 threads
        t1 = threading.Thread(target=factorial, args=(50,))
        t2 = threading.Thread(target=factorial, args=(100,))
        t3 = threading.Thread(target=factorial, args=(200,))

        threads = [t1, t2, t3]

        # Start threads
        for t in threads:
            t.start()

        # Wait for all threads to complete
        for t in threads:
            t.join()

        # Timer is stopped
        end_time = time.time_ns()

        # Duration is calculated
        total_time = end_time - start_time
        times.append(total_time)

        print(f"Round {round_no}: {total_time} ns")

    avg_time = sum(times) / len(times)
    print(f"\nAverage Time (Multithreading): {avg_time:.2f} ns")



# --- (iv) 4. Perform the same operations as #3 (i.e. generate the factorial for 50!, 100!, and 200!),
# this time without multithreading. Calculate the total time taken for each round
# and the average time taken and display the results in your program output. ---

# This function creates and runs 3 threads at the same time to measure their execution time.
def single_thread_test():
    times = []

    for round_no in range(1,11):
        start_time = time.time_ns()

        # Sequential execution
        factorial(50)
        factorial(100)
        factorial(200)

        end_time = time.time_ns()

        total_time = end_time - start_time
        times.append(total_time)

        print(f"Round {round_no}: {total_time} ns")

    avg_time = sum(times) / len(times)
    print(f"\nAverage Time (Single Thread): {avg_time:.2f} ns")



def main():
    print("=== MULTITHREADING TEST ===")
    multithreading_test()

    print("\n=== NON-MULTITHREADING TEST ===")
    single_thread_test()

if __name__ == "__main__":
    main()
# Some execution rounds returned 0 nanoseconds, especially in the single-thread test.
# It's because the factorial calculations complete extremely quick,
# ...and the system couldn't capture such short execution duration.
# Larger input values or repeated computations would be required to generate more significant execution times.
