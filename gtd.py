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
                                eisenhower = input("Break this task down into actionable steps. Do that now?").upper()
                                match eisenhower:
                                    case "YES":
                                        print("Ok, start breaking this task down now. Figure out if it's just a checklist of things to do or a bigger project that needs further planning:")
                                        print(task)
                                        exit()
                                    case "NO":
                                        print("Add a TODO to break this task down into actionable tasks (is it a project? Should it be scheduled?):")
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
                                                print("Go ahead and schedule time for developing this idea further:")
                                                print(task)
                                                exit()
                                    case "NO":
                                        eisenhower = input("Then this sounds like a documentation task or something that should be available for reference in the future. Perhaps a blog post or presentation? Here's the task again:").upper()
                                        print(task)
                                        exit()
            case "NO":
                eisenhower = input("Is it actionable?").upper()
                match eisenhower:
                    case "YES":
                        print("Put this task in the backlog. It's important but not urgent. Don't worry too much about the details right now (if it's a multi or single step task etc)")
                        print(task)
                        exit()
                    case "NO":
                        eisenhower = input("Is it really that important or can we please trash it right now?").upper()
                        match eisenhower:
                            case "YES":
                                print("Awesome! Let's trash this task:")
                                print(task)
                                exit()
                            case "NO":
                                print("This is apparently important. But it's not urgent and it's not actionable at the moment.")
                                print("Then this task is one of two things:")
                                print("1. A documentation task. Something that should be documented or shared in some form or just should be available for reference later. If that's the case, then add a docs/sharing/etc TODO in the backlog.")
                                print("2. Alternatively, this needs further incubation to be useful. If so, then add an incubation TODO in the backlog.")
                                print("3. There's no third option. Just trash this thing and focus on something important instead!")
                                print("")
                                print("The task at hand:")
                                print(task)
