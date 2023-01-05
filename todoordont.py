#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
def checkUserAnswer(userAnswers):
    if "important" not in userAnswers:
        return "set_important_key"
    if "urgent" not in userAnswers:
        return "set_urgent_key"
    if userAnswers.get("important") == False:
        if userAnswers.get("urgent") == False:
            print ("Trash it!")
            return {'important': False, 'urgent': False}
        if userAnswers.get("urgent") == True:
            print ("Delegate? Or add to backlog of less important TODO's")
            return {'important': False, 'urgent': True}
    if userAnswers.get("important") == True:
        if userAnswers.get("urgent") == False:
            if "actionable" not in userAnswers:
                return "set_actionable_key"
            if userAnswers.get("actionable") == False:
                print ("Delegate for incubation.")
                return {'important': True, 'urgent': False, 'actionable': False}
            if userAnswers.get("actionable") == True:
                print ("Add to backlog.")
                return {'important': True, 'urgent': False, 'actionable': True}
    if userAnswers.get("important") == True:
        if userAnswers.get("urgent") == True:
            if "actionable" not in userAnswers:
                return "set_actionable_key"
            if userAnswers.get("actionable") == True:
                if "singleStepTask" not in userAnswers:
                    return "set_singleStepTask_key"
                if userAnswers.get("singleStepTask") == False:
                    print ("Project. Break it down.")
                    return {'important': True, 'urgent': True, 'actionable': True, 'singleStepTask': False}
                if userAnswers.get("singleStepTask") == True:
                    if "doneIn2Mins" not in userAnswers:
                        return "set_doneIn2Mins_key"
                    if userAnswers.get("doneIn2Mins") == True:
                        print ("Do it now!")
                        return {'important': True, 'urgent': True, 'actionable': True, 'singleStepTask': True, 'doneIn2Mins': True}
                    if userAnswers.get("doneIn2Mins") == False:
                        print ("Add to TODO ASAP.")
                        return {'important': True, 'urgent': True, 'actionable': True, 'singleStepTask': True, 'doneIn2Mins': False}
            if userAnswers.get("actionable") == False:
                print("""Task needs to be defined and incubated.""")
                userAnswers['incubate'] = True
                if "forReference" not in userAnswers:
                    return "set_forReference_key"
                if userAnswers.get("forReference") == True:
                    print ("Put this where it can be referenced or produce the docs/blog post etc. Right now or add to TODO ASAP.")
                    return {'important': True, 'urgent': True, 'actionable': False, 'incubate': True, 'forReference': True}
                if userAnswers.get("forReference") == False:
                    if "delegate" not in userAnswers:
                        return "set_delegate_key"
                    if userAnswers.get("delegate") == True:
                        print ("Delegate for incubation.")
                        return {'important': True, 'urgent': True, 'actionable': False, 'incubate': True, 'forReference': False, 'delegate': True}
                    if userAnswers.get("delegate") == False:
                        print ("Incubate now or add to TODO for incubation.")
                        return {'important': True, 'urgent': True, 'actionable': False, 'incubate': True, 'forReference': False, 'delegate': False}
def cliLoop():
    """Run with user input from terminal"""
    userAnswers = {}
    while True:
        checkUserAnswer_status = checkUserAnswer(userAnswers)
        match checkUserAnswer_status:
            case None:
                break
            case "set_important_key":
                answer = input("""Is it important?""").upper()
                if answer == "Y":
                    userAnswers['important'] = True
                if answer == "N":
                    userAnswers['important'] = False
            case "set_urgent_key":
                answer = input("""Is it urgent?""").upper()
                if answer == "Y":
                    userAnswers['urgent'] = True
                if answer == "N":
                    userAnswers['urgent'] = False
            case "set_actionable_key":
                answer = input("""Is it actionable?""").upper()
                if answer == "N":
                    userAnswers['actionable'] = False
                if answer == "Y":
                    userAnswers['actionable'] = True
            case "set_singleStepTask_key":
                answer = input("""Is this a single step task?""").upper()
                if answer == "Y":
                    userAnswers['singleStepTask'] = True
                if answer == "N":
                    userAnswers['singleStepTask'] = False
            case "set_doneIn2Mins_key":
                answer = input("""Can you complete this in 2 mins?""").upper()
                if answer == "Y":
                    userAnswers['doneIn2Mins'] = True
                if answer == "N":
                    userAnswers['doneIn2Mins'] = False
            case "set_forReference_key":
                answer = input("""Is this for reference or a blog post or docs to be written? Perhaps some needed reading?""").upper()
                if answer == "Y":
                    userAnswers['forReference'] = True
                if answer == "N":
                    userAnswers['forReference'] = False
            case "set_delegate_key":
                answer = input("""Delegate this task?""").upper()
                if answer == "Y":
                    userAnswers['delegate'] = True
                if answer == "N":
                    userAnswers['delegate'] = False
            case {'important': False, 'urgent': False}:
                print ("Action for: Trash it!")
                break
            case {'important': False, 'urgent': True}:
                print ("Action for: Delegate or add to backlog of less important TODO's")
                print ("Like creating an issue with git-bug, for example")
                break
            case {'important': True, 'urgent': False, 'actionable': False}:
                print ("Action for: Delegate for incubation.")
                print ("Like creating an issue with git-bug, for example")
                break
            case {'important': True, 'urgent': False, 'actionable': True}:
                print ("Action for: Add to backlog.")
                print ("Like creating an issue with git-bug, for example")
                break
            case {'important': True, 'urgent': True, 'actionable': True, 'singleStepTask': True, 'doneIn2Mins': True}:
                print ("Action for: Do it now!")
                print ("Like creating an issue with git-bug, for example")
                break
            case {'important': True, 'urgent': True, 'actionable': True, 'singleStepTask': False}:
                print ("Action for: Project. Break it down.")
                print ("Like creating an issue with git-bug, for example")
                break
            case {'important': True, 'urgent': True, 'actionable': True, 'singleStepTask': True, 'doneIn2Mins': False}:
                print ("Action for: Add to TODO ASAP.")
                print ("Like creating an issue with git-bug, for example")
                break
            case {'important': True, 'urgent': True, 'actionable': False, 'incubate': True, 'forReference': True}:
                print ("Action for: Put this where it can be referenced or produce the docs/blog post etc. Right now or add to TODO ASAP.")
                print ("Like creating an issue with git-bug, for example")
                break
            case {'important': True, 'urgent': True, 'actionable': False, 'incubate': True, 'forReference': False, 'delegate': True}:
                print ("Action for: Delegate for incubation.")
                print ("Like creating an issue with git-bug, for example")
                break
            case {'important': True, 'urgent': True, 'actionable': False, 'incubate': True, 'forReference': False, 'delegate': False}:
                print ("Action for: Incubate now or add to TODO for incubation.")
                print ("Like creating an issue with git-bug, for example")
                break
def apiLoop():
    """Run with user input over web API"""
    pass
if __name__ == "__main__":
    cliLoop()