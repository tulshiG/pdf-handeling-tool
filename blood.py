import mysql.connector
from datetime import datetime

# Database Connection
conn = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="",
    database="blood_bank"
)
cursor = conn.cursor()

# Blood Compatibility Chart
BLOOD_COMPATIBILITY = {
    "O-": ["O-"],
    "O+": ["O-", "O+"],
    "A-": ["O-", "A-"],
    "A+": ["O-", "O+", "A-", "A+"],
    "B-": ["O-", "B-"],
    "B+": ["O-", "O+", "B-", "B+"],
    "AB-": ["O-", "A-", "B-", "AB-"],
    "AB+": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]
}

# Function to select blood group
def select_blood_group():
    blood_groups = ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]
    
    print("\nSelect a blood group:")
    for i, group in enumerate(blood_groups, 1):
        print(f"{i}. {group}")
    
    choice = int(input("Enter the number corresponding to the blood group: "))
    
    if 1 <= choice <= len(blood_groups):
        return blood_groups[choice - 1]
    else:
        print("Invalid selection. Please try again.")
        return select_blood_group()

# Function to add a donor
def add_donor():
    name = input("Enter donor name: ")
    age = int(input("Enter age: "))
    if age < 18:
        print("Donor must be at least 18 years old.")
        return
    
    blood_group = input("Enter blood group: ").upper()
    quantity = int(input("Enter quantity donated: "))
    branch_id = int(input("Enter branch ID: "))

    donation_date = datetime.today().strftime('%Y-%m-%d')
    
    # Insert donor record
    query = "INSERT INTO donors (name, age, blood_group, quantity_donated, donation_date, branch_id) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name, age, blood_group, quantity, donation_date, branch_id)
    cursor.execute(query, values)
    conn.commit()
    
    # Update blood inventory
    update_blood_quantity(branch_id, blood_group, quantity)

    print("Donor added successfully!")

    # Assign blood to waiting list if available
    process_waiting_list(branch_id, blood_group)

# Function to update blood inventory
def update_blood_quantity(branch_id, blood_group, quantity):
    query = "UPDATE blood_inventory SET quantity_available = quantity_available + %s WHERE branch_id = %s AND blood_group = %s"
    cursor.execute(query, (quantity, branch_id, blood_group))
    conn.commit()

# Function to check blood availability
# def check_blood_availability(branch_id, blood_group):
#     query = "SELECT quantity_available FROM blood_inventory WHERE branch_id = %s AND blood_group = %s"
#     cursor.execute(query, (branch_id, blood_group))
#     result = cursor.fetchone()
    
#     return result[0] if result else 0

def check_blood_availability(branch_id, blood_group):
    query = "SELECT quantity_available FROM blood_inventory WHERE branch_id = %s AND blood_group = %s"
    cursor.execute(query, (branch_id, blood_group))
    result = cursor.fetchone()
    
    return result[0] if result else 0


# Function to find compatible blood groups
def find_alternative_blood(branch_id, blood_group, quantity_required):
    for compatible_group in BLOOD_COMPATIBILITY[blood_group]:
        available = check_blood_availability(branch_id, compatible_group)
        if available >= quantity_required:
            return compatible_group
    return None

# Function to add a receiver
# def add_receiver():
#     name = input("Enter receiver name: ")
#     age = int(input("Enter age: "))
#     if age < 18:
#         print("Receiver must be at least 18 years old.")
#         return
    
#     blood_group = input("Enter blood group: ").upper()
#     quantity_required = int(input("Enter required quantity: "))
#     branch_id = int(input("Enter branch ID: "))

#     receive_date = datetime.today().strftime('%Y-%m-%d')

#     available = check_blood_availability(branch_id, blood_group)

#     if available >= quantity_required:
#         # Full requirement met
#         update_blood_quantity(branch_id, blood_group, -quantity_required)
#         status = 'Fulfilled'
#         print(f"Blood assigned from {blood_group}")
#     else:
#         # Check for compatible blood
#         alternative_group = find_alternative_blood(branch_id, blood_group, quantity_required)
#         if alternative_group:
#             update_blood_quantity(branch_id, alternative_group, -quantity_required)
#             status = 'Fulfilled'
#             print(f"Blood assigned from compatible group: {alternative_group}")
#         else:
#             # Partial fulfillment
#             if available > 0:
#                 update_blood_quantity(branch_id, blood_group, -available)
#                 quantity_required -= available
#                 print(f"Only {available} units assigned, remaining {quantity_required} added to waiting list.")

#             # Add remaining request to waiting list
#             add_to_waiting_list(name, age, blood_group, quantity_required, branch_id)
#             status = 'Pending'

#     # Insert receiver record
#     query = "INSERT INTO receivers (name, age, blood_group, quantity_required, receive_date, branch_id, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#     values = (name, age, blood_group, quantity_required, receive_date, branch_id, status)
#     cursor.execute(query, values)
#     conn.commit()

# Function to add a receiver
# def add_receiver():
#     name = input("Enter receiver's name: ")
#     age = int(input("Enter receiver's age: "))

#     if age < 18:
#         print("Receiver must be at least 18 years old.")
#         return

#     print("Select blood group:")
#     blood_group = select_blood_group()
    
#     quantity_required = int(input("Enter quantity required (in units): "))
#     branch_id = select_branch()
def add_receiver():
    receiver_name = input("Enter receiver name: ")
    quantity_required = int(input("Enter quantity required: "))
    branch_id = int(input("Enter branch ID: "))
    blood_group = select_blood_group()  # This function should be defined
    print(f"Receiver: {receiver_name}, Blood Group: {blood_group}, Quantity: {quantity_required}, Branch ID: {branch_id}")
    receive_date = datetime.today().strftime('%Y-%m-%d')

    # Default status
    status = 'Pending'

    # Check if the required blood is available
    # if check_blood_availability(branch_id, blood_group, quantity_required):
    if check_blood_availability(branch_id, blood_group, quantity_required):
        update_blood_quantity(branch_id, blood_group, -quantity_required)
        status = 'Fulfilled'
        print(f"Blood assigned from {blood_group}")
    else:
        alternative_group = find_alternative_blood(branch_id, blood_group, quantity_required)
        if alternative_group:
            update_blood_quantity(branch_id, alternative_group, -quantity_required)
            status = 'Fulfilled'
            print(f"Blood assigned from compatible group: {alternative_group}")
        else:
            add_to_waiting_list(name, age, blood_group, quantity_required, branch_id) # type: ignore
            print("No blood available. Added to waiting list.")

    # Debug statement to check status
    print(f"Receiver status: {status}")

    # Ensure status is inserted properly
    query = "INSERT INTO receivers (name, age, blood_group, quantity_required, receive_date, branch_id, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (name, age, blood_group, quantity_required, receive_date, branch_id, status) # type: ignore
    cursor.execute(query, values)
    conn.commit()
    print("Receiver added successfully!")


# Function to add receiver to waiting list
# def add_to_waiting_list(name, age, blood_group, quantity_required, branch_id):
#     query = "INSERT INTO waiting_list (receiver_name, blood_group, quantity_required, request_date, branch_id) VALUES (%s, %s, %s, %s, %s)"
#     values = (name, blood_group, quantity_required, datetime.today().strftime('%Y-%m-%d'), branch_id)
#     cursor.execute(query, values)
#     conn.commit()
#     print(f"{name} added to waiting list for {quantity_required} units of {blood_group}")

# Function to add receiver to waiting list
def add_to_waiting_list(name, age, blood_group, quantity_required, branch_id):
    # Step 1: Fetch the latest receiver_id with status 'Pending'
    # query = """
    # SELECT receiver_id 
    # FROM receivers 
    # WHERE name = %s AND blood_group = %s AND branch_id = %s AND status = 'Pending' 
    # ORDER BY receive_date DESC LIMIT 1
    # """
    query = """
    SELECT id, receiver_name, quantity_required
    FROM waiting_list
    WHERE branch_id = %s AND blood_group = %s
    ORDER BY request_date ASC
    """

    cursor.execute(query, (name, blood_group, branch_id))
    result = cursor.fetchone()

    if result:
        receiver_id = result[0]

        # Step 2: Insert into waiting_list table
        query = "INSERT INTO waiting_list (receiver_id, request_date, branch_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (receiver_id, datetime.today().strftime('%Y-%m-%d'), branch_id))
        conn.commit()
        print(f"Receiver with ID {receiver_id} added to waiting list successfully!")
        
    else:
        print("Error: No pending receiver found.")


# Function to process waiting list (FIFO logic)
def process_waiting_list(branch_id, blood_group):
    query = "SELECT id, receiver_name, quantity_required FROM waiting_list WHERE branch_id = %s AND blood_group = %s ORDER BY request_date ASC"
    cursor.execute(query, (branch_id, blood_group))
    waiting_list = cursor.fetchall()

    available = check_blood_availability(branch_id, blood_group)

    for entry in waiting_list:
        receiver_id, receiver_name, required_quantity = entry

        if available == 0:
            break

        if available >= required_quantity:
            # Full requirement met
            update_blood_quantity(branch_id, blood_group, -required_quantity)
            mark_request_fulfilled(receiver_name, blood_group, branch_id)
            delete_from_waiting_list(receiver_id)
            available -= required_quantity
            print(f"Waiting list request fulfilled for {receiver_name}")
        else:
            # Partial fulfillment
            update_blood_quantity(branch_id, blood_group, -available)
            update_waiting_list(receiver_id, required_quantity - available)
            print(f"Partially fulfilled {receiver_name}, remaining {required_quantity - available} units added back to waiting list.")
            available = 0

# Function to mark request as fulfilled
def mark_request_fulfilled(name, blood_group, branch_id):
    query = "UPDATE receivers SET status = 'Fulfilled' WHERE name = %s AND blood_group = %s AND branch_id = %s"
    cursor.execute(query, (name, blood_group, branch_id))
    conn.commit()

# Function to delete fulfilled request from waiting list
def delete_from_waiting_list(receiver_id):
    query = "DELETE FROM waiting_list WHERE id = %s"
    cursor.execute(query, (receiver_id,))
    conn.commit()

# Function to update remaining quantity in waiting list
def update_waiting_list(receiver_id, remaining_quantity):
    query = "UPDATE waiting_list SET quantity_required = %s WHERE id = %s"
    cursor.execute(query, (remaining_quantity, receiver_id))
    conn.commit()

# Function to display blood inventory
def display_blood_inventory():
    query = "SELECT b.branch_name, bi.blood_group, bi.quantity_available FROM blood_inventory bi JOIN branches b ON bi.branch_id = b.branch_id"
    cursor.execute(query)
    results = cursor.fetchall()
    
    print("\nBlood Inventory:")
    for row in results:
        print(f"Branch: {row[0]}, Blood Group: {row[1]}, Available: {row[2]} units")

# Menu for user input
while True:
    print("\n1. Add Donor\n2. Add Receiver\n3. Display Blood Inventory\n4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        add_donor()
    elif choice == 2:
        add_receiver()
    elif choice == 3:
        display_blood_inventory()
    elif choice == 4:
        break