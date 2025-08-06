Call_queue=[]
print("*************Welcome To Call Centre Queue System***********************")
while True :
	print(""" 1.] Add a Call
		  2.] Exit""")

	choice = input("Enter Your Choice:")
	if choice =="1":
		CustomerID=input("Enter Customer ID:")
		CallTime=input("Enter Call Time (Minutes):")
		Call={"id":CustomerID,"Time":CallTime}
		Call_queue.append(Call)
		print("Call Added.")
	elif choice == "2":
		if Call_queue.pop(0)
			print("Answered Call:"Call["id"],"Time:",Call["Time"],"Minutes")
		else:
			print("No Calls to Answer.")
		print("Ans
		print("GoodBye!")
		break
	else:
		print("Invalid Choice.")
