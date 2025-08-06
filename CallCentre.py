# Very Simple Call Center Queue using Dictionary

call_queue = []  # List to store calls (each call is a dictionary)

print("WELCOME TO CALL CENTER QUEUE SYSTEM")

while True:
    print("""
1. ADD A CALL
2. ANSWER NEXT CALL
3. VIEW PENDING CALLS
4. CHECK IF QUEUE IS EMPTY
5. EXIT
""")

    choice = input("ENTER YOUR CHOICE: ")

    if choice == "1":  # Add a call
        customerID = input("ENTER CUSTOMER ID: ")
        callTime = input("ENTER CALL TIME (MINUTES): ")
        call = {"id": customerID, "time": callTime}
        call_queue.append(call)
        print("CALL ADDED.")

    elif choice == "2":  # Answer call
        if call_queue:
            call = call_queue.pop(0)
            print("ANSWERED CALL:", call["id"], "TIME:", call["time"], "MINUTES")
        else:
            print("NO CALLS TO ANSWER.")

    elif choice == "3":  # View calls
        if call_queue:
            print("PENDING CALLS:")
            for c in call_queue:
                print("ID:", c["id"], "TIME:", c["time"], "MINUTES")
        else:
            print("NO PENDING CALLS.")

    elif choice == "4":  # Check empty
        if not call_queue:
            print("QUEUE IS EMPTY.")
        else:
            print("QUEUE IS NOT EMPTY.")

    elif choice == "5":  # Exit
        print("GOODBYE!")
        break

    else:
        print("INVALID CHOICE.")

