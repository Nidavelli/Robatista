print("Hello welcome to Nida's World")

name=input("What is your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil? (yes/no)\n")
    if evil_status == "yes":
        goodDeeds=int(input("How many good deeds have you done today? \n"))
        if goodDeeds > 4 :
            print(f"Welcome {name}! Thank you for coming in today")
        else:
            print(f"Sorry {name}, you are not welcome here \nSCRAAAAAMMMMMMMMMM!!!!!!")
            exit()

    else:
        print(f"Welcome {name}! You're a good one")
        print(f"Welcome {name}! Thank you for coming in today")
else:
    print(f"Welcome {name}! Thank you for coming in today")