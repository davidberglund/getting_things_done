#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
task = input("What's the task?")

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
                eisenhower = input("Is it actionable?").upper()
                match eisenhower:
                    case "YES":
                        eisenhower = input("Single step task?").upper()
                        match eisenhower:
                            case "YES":
                                eisenhower = input("Done in 2 mins?").upper()
                                match eisenhower:
                                    case "YES":
                                        print("Do it now!")
                                        exit()
                                    case "NO":
                                        eisenhower = input("Delegate to someone else?").upper()
                                        match eisenhower:
                                            case "YES":
                                                eisenhower = input("Delegate now?").upper()
                                                match eisenhower:
                                                    case "YES":
                                                        print("Delegate it now!")
                                                        exit()
                                                    case "NO":
                                                        print("Add to TODO: Delegate the following task...")
                                                        print(task)
                                                        exit()
                                            case "NO":
                                                eisenhower = input("Do it yourself?").upper()
                                                match eisenhower:
                                                    case "YES":
                                                        print("Add this to TODO (ASAP) _or_ schedule it:")
                                                        print(task)
                                                        exit()
                                                    case "NO":
                                                        print("Put this away somewhere and let someone else handle it whenever...")
                                                        print(task)
                                                        exit()
                            case "NO":
                                #Multi step task
                                eisenhower = input("Plan a project and specify goal(s) and each actionable task. Start planning now?").upper()
                                match eisenhower:
                                    case "YES":
                                        print("Ok, let's start planning this task as a project:")
                                        print(task)
                                        exit()
                                    case "NO":
                                        print("Add project planning of this task to TODO (schedule):")
                                        print(task)
                                        exit()
                    case "NO":
                        eisenhower = input("Trash it?").upper()
                        match eisenhower:
                            case "YES":
                                print("Awesome! Let's trash this task:")
                                print(task)
                                exit()
                            case "NO":
                                eisenhower = input("Incubate? I.e. develop idea further.").upper()
                                match eisenhower:
                                    case "YES":
                                        eisenhower = input("Start incubating/developing this idea further right now?").upper()
                                        match eisenhower:
                                            case "YES":
                                                print("Have fun developing this idea now! See ya.")
                                                print(task)
                                                exit()
                                            case "NO":
                                                print(task)
                                                exit()
                                    case "NO":
                                        eisenhower = input("Then you should instead document, blog or in some other way put this so that it can be referenced in the future. Here's the task again:").upper()
                                        print(task)
                                        exit()