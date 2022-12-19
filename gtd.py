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
                                        print("Ok, let's start planning task:")
                                        print(task)
                                        exit()
                                    case "NO":
                                        print("Add project planning of this task to TODO (schedule):")
                                        print(task)
                                        exit()
                    case "NO":
                        #Not actionable - No? 1. Trash 2. Incubate 3. Reference (journal, coursework, recipes, documenation etc)
                        print("")
                        exit()

                        eisenhower = input("Completed in 2 mins?").upper()
                        match eisenhower:
                            case "YES":
                                print("Do it now!")
                                exit()
                            case "NO":
                                print("Schedule it!")
                                exit()
                print("Do it now!")
                exit()
            case "NO":
                print("Schedule it!")
                exit()

'''
Multiple steps?
- Plan a project with measurable goal(s) and actionable steps

Stuff --> --> -->

Is it actionable?

- No?
1. Trash
2. Incubate
3. Reference (journal, coursework, recipes, documenation etc)

- Yes?
Can it be completed in one single step?
1. 2 mins? Do it now!
2. Longer than 2 mins?
- Delegate to someone else (or just put it away and wait for someone else to do it)
- Defer (Add to next TODO, Schedule it)

'''
