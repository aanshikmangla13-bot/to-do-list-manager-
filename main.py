task_list=[]

def add_task() :
enter_task=input("enter the task ")
task_1st.append(enter_task)
def remove_task() :
rem_task=input("enter the task u want to remove=")
task_1st.remove(rem_task)

def view_task() :
print (view_list)
while true :
  print ("main menu")
  print ("1.add task")
  print("2.remove task")
  print("3.view task")
  print("4.exit")
ch=int(input("enter your choice = ") )
if ch == 1 :
   add_task()
elif ch == 2 :
   remove_task()
elif ch == 3 :
   view task ()
elif ch == 4 :
    break 
else :
  print ("invalid choice ,try again !")
  
