#                           < === ---: To-Do list:--- === >



to_do_list = []

while True:
	
    print("\n1. Add Tasks\n2. View Tasks\n3.Remove Tasks\n4.Exit")
	
    add_task = input("enter your choice:\t")
	
    if add_task == "1":
			
        enter_task = input("enter the new task:\t")
			
        to_do_list.append(enter_task)
			
        print("Task added!")
			
    elif add_task =="2":
			
        print("Your Tasks:")
			
        for idx, task in enumerate(to_do_list, 1):
					
            print(f"{idx}. {task}")
					
    elif add_task == "3":
			
        print("Your tasks:")
			
        for idx,task in enumerate(to_do_list,1):
					
            print(f"{idx}. {task}")
					
            remove_task = int(input("Enter the task number to remove:\t"))
					
            if 0 < remove_task <= len(to_do_list):
							
                removed = to_do_list.pop(remove_task - 1)
							
                print(f"Removed: {removed}")
							
            elif remove_task == "exit":
							
                break
            else:
							
                print("Invalid task number.")
							
    elif add_task == "4":
			
                break
    else:
                print("You are enter the wrong number of item!!!")
                
                
                
            
                
        
