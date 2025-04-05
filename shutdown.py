import os
import time

print("Press S for shutdown R for restart")

def choice():
    user_input=input("")
    user_input= user_input.lower()
    if user_input=="r":
        print("Enter the time before your device restarts")

    elif user_input=="s":
        print("Enter the time before your device shutsdown")

    else: 
        print("Wrong output, please enter S for shutdown, R for restart")
        choice()

    hrs=int(input("Hours: "))
    min=int(input("Minutes: "))
    sec=int(input("Seconds: "))

    seconds=(hrs*60*60)+(min*60)+sec

    conf=input("Type Y to confirm, N to cancel \n")
    
    if conf.lower()=="y":
        if user_input == "r":
            os.system(f"shutdown /r /f /t {seconds}")
        elif user_input == "s":
            os.system(f"shutdown /s /f /t {seconds}")
        else:
            print("Invalid choice.")

    
    elif conf.lower()=="n":
        return 0
    
    else:
        print("Wrong input cancelling sutdown")
        return 0
        exit 
exit



choice()

time.sleep(5000)
