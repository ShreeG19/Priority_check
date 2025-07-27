'''
# simple priority queue pgm
import queue

pq = queue.PriorityQueue()

pq.put((1, "High Priority")) 
pq.put((2, "Medium Priority"))
pq.put((3, "Low Priority"))

while not pq.empty():
    priority, task = pq.get()
    print(f"Priority: {priority}, Task: {task}")

'''
# dynamic task priority system 

import queue
import threading
import time

# Create a priority queue
pq = queue.PriorityQueue()

# Lock to handle task updates safely
lock = threading.Lock()

# Function to process tasks
def process_tasks():
    while True:
        lock.acquire()
        if not pq.empty():
            priority, task = pq.get()
            lock.release()
            print(f"\nProcessing: {task} (Priority {priority})")
            time.sleep(2)  # Simulate task execution time
        else:
            lock.release()
            time.sleep(1)  # Wait if no tasks are available

# Start task processing in a separate thread
threading.Thread(target=process_tasks, daemon=True).start()

# User input loop
while True:
    print("\nOptions:")
    print("1. Add a new task")
    print("2. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        task_name = input("Enter task name: ").strip()
        priority = input("Enter priority (1 = High, 2 = Medium, 3 = Low): ").strip()
        
        if not priority.isdigit():
            print("Invalid priority! Please enter a number.")
            continue
        
        priority = int(priority)
        
        lock.acquire()
        pq.put((priority, task_name))
        lock.release()

        print(f"Task '{task_name}' added with priority {priority}.")

    elif choice == "2":
        print("Exiting...")
        break

    else:
        print("Invalid option! Try again.")
    