#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
task = input("""What's the task?
""")
print("")
print("Answer yes or no to the following questions.")
print("")
answer = input("""Is it important?
""").upper()
match answer:
    case "NO":
        answer = input("""Is it urgent?
""").upper()
        match answer:
            case "YES":
                answer = input("""Do you have time to delegate it now?
""").upper()
                match answer:
                    case "YES":
                        print("Delegate it now! Or attempt to delegate and then put the issue on hold/awaiting response.")
                        exit()
                    case "NO":
                        print("Create a TODO (ASAP) to delegate this immediately.")
                        print(task)
                        exit()
            case "NO":
                print("Trash it now!")
                exit()
            case _:
                print("Yes or No, please.")
                exit()
    case "YES":
        answer = input("""Is it urgent?
""").upper()
        match answer:
            case "YES":
                answer = input("""Is it actionable?
""").upper()
                match answer:
                    case "YES":
                        answer = input("""Single step task?
""").upper()
                        match answer:
                            case "YES":
                                answer = input("""Done in 2 mins?
""").upper()
                                match answer:
                                    case "YES":
                                        print("Do it now!")
                                        exit()
                                    case "NO":
                                        answer = input("""Delegate to someone else?
""").upper()
                                        match answer:
                                            case "YES":
                                                answer = input("""Delegate now?
""").upper()
                                                match answer:
                                                    case "YES":
                                                        print("Delegate it now!")
                                                        exit()
                                                    case "NO":
                                                        print("Add to TODO: Delegate the following task...")
                                                        print(task)
                                                        exit()
                                            case "NO":
                                                answer = input("""Do it yourself?
""").upper()
                                                match answer:
                                                    case "YES":
                                                        answer = input("""Do you have time for it now?
""").upper()
                                                        match answer:
                                                            case "YES":
                                                                print("Do it now!")
                                                                exit()
                                                            case "NO":
                                                                print("Add this to TODO (ASAP) _or_ schedule it:")
                                                                print(task)
                                                                exit()
                                                    case "NO":
                                                        print("Put this away somewhere and let someone else handle it whenever...")
                                                        print(task)
                                                        exit()
                            case "NO":
                                #Multi step task
                                answer = input("""Break this task down into actionable steps. Do that now?
""").upper()
                                match answer:
                                    case "YES":
                                        print("Ok, start breaking this task down now. Figure out if it's just a checklist of things to do or a bigger project that needs further planning:")
                                        print(task)
                                        exit()
                                    case "NO":
                                        print("Add a TODO to break this task down into actionable tasks (is it a project? Should it be scheduled?):")
                                        print(task)
                                        exit()
                    case "NO":
                        answer = input("""Incubate? I.e. develop idea further.
""").upper()
                        match answer:
                            case "YES":
                                answer = input("""Start incubating/developing this idea further right now?
""").upper()
                                match answer:
                                    case "YES":
                                        print("Have fun developing this idea now! See ya.")
                                        print(task)
                                        exit()
                                    case "NO":
                                        print("Go ahead and schedule time for developing this idea further:")
                                        print(task)
                                        exit()
                            case "NO":
                                answer = input("""Is this a documentation task or something that should be available for reference in the future? Perhaps a blog post or presentation?")
""").upper()
                                match answer:
                                    case "YES":
                                        answer = input("""Do you have time to do this work right now?
""").upper()
                                        match answer:
                                            case "YES":
                                                print("Awesome! Have fun.")
                                                print(task)
                                                exit()
                                            case "NO":
                                                print("Add a TODO (ASAP): schedule time to work on this task.")
                                                print(task)
                                                exit()
                                    case "NO":
                                        answer = input("""Are you sure this is worth your time? Trash it?
""").upper()
                                        match answer:
                                            case "YES":
                                                print("Awesome! Let's trash this task:")
                                                print(task)
                                                exit()
                                            case "NO":
                                                print("Ok, maybe this should be delegated or maybe time will tell what to do with this (if anything). Put it away somewhere where it doesn't bother you for now.")
                                                exit()
            case "NO":
                answer = input("""Is it actionable?
""").upper()
                match answer:
                    case "NO":
                        answer = input("""Can you delegate this task and let someone else develop/incubate it?
""").upper()
                        match answer:
                            case "YES":
                                print("Great! Put this task in the backlog and label it delegate and that it needs incubating (or something more descriptive if you can). It's important (apparently), so don't trash it, but it's not urgent. Let someone else worry about the details.")
                                print(task)
                                exit()
                            case "NO":
                                print("Do yourself a favour and ask yourself if this really is worth cluttering your backlog (since it's not actionable at the moment and not urgent). If the answer is yes, then put this task in the backlog and describe it as incubating or something more descriptive if you can. Don't worry too much about the details right now (if it's a multi or single step task etc).")
                                print("Perhaps this is a documentation task? Something to keep for reference? Then put it somewhere where whoever needs the information can access it and stop it from cluttering your backlog.")
                                print(task)
                                exit()
                    case "YES":
                        print("Put this task in the backlog and describe the task at hand in broad terms. It's important (so don't trash it) but it's not urgent. Don't worry too much about the details right now (if it's a multi or single step task etc)")
                        print(task)
                        exit()