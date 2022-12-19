#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
#Urgent? Important?
#Do it now!
#
#Urgent? Not important?
#Delegate!
#
#Not urgent? Important?
#Schedule it!
#
#Not urgent? Not important?
#Eliminate!

eisenhower = input("Is it important?").upper()
match eisenhower:
    case "NO":
        eisenhower = input("Is it urgent?").upper()
        match eisenhower:
            case "YES":
                print("Delegate it!")
                exit()
            case "NO":
                print("Trash it now!")
                exit()
    case "YES":
        eisenhower = input("Is it urgent?").upper()
        match eisenhower:
            case "YES":
                print("Do it now!")
                exit()
            case "NO":
                print("Schedule it!")
                exit()
