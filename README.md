````mermaid
graph TD
    Important[Important?]
    Important -->|No| ImportantNo[Not important. Urgent?]
    Important -->|Yes| ImportantYes[Yes. Urgent?]
    ImportantNo -->|No| ImportantNoUrgentNo[Not important nor urgent. Trash it!]
    ImportantNo -->|Yes| ImportantNoUrgentYes[Important: no. Urgent? Yes. Delegate!]
    ImportantYes -->|No| ImportantYesUrgentNo[Not urgent. But important. Actionable?]

    ImportantYesUrgentNo -->|Yes| ImportantYesUrgentNoActionableYes[Yes. Add to backlog. Don't trash it but don't worry about the details - i.e. multi or single step task etc.]
    ImportantYesUrgentNo -->|No| ImportantYesUrgentNoActionableNo[No. Can you delegate this task and let someone else develop/incubate it?]
    ImportantYesUrgentNoActionableNo -->|No| ImportantYesUrgentNoActionableNoDelegateNo[No. Is this really worth cluttering your backlog? If it as incubating/etc in backlog. Don't worry about the details. Is it a docs task? Something to keep for reference? Then put it somewhere where whoever needs the information can access it and stop it from cluttering your backlog.]

    ImportantYes -->|Yes| ImportantYesUrgentYes[Yes, it's urgent. Actionable?]
    ImportantYesUrgentYes -->|Yes| ImportantYesUrgentYesActionableYes[Yes. Single step task?]
    ImportantYesUrgentYes -->|No| ImportantYesUrgentYesActionableNo[No. Delegate?]
    ImportantYesUrgentYesActionableYes -->|Yes| ImportantYesUrgentYesActionableYesSingleStepTaskYes[Yes. Done in 2 min?]
    ImportantYesUrgentYesActionableYes -->|No| ImportantYesUrgentYesActionableYesSingleStepTaskNo[No. Break this task down into actionable steps. Do that now?]
    ImportantYesUrgentYesActionableYesSingleStepTaskYes -->|Yes| ImportantYesUrgentYesActionableYesSingleStepTaskYesDoneIn2Mins[Yes. Do it now]
    ImportantYesUrgentYesActionableYesSingleStepTaskYes -->|No| ImportantYesUrgentYesActionableYesSingleStepTaskYesNotDoneIn2Mins[No. Delegate to someone else?]
    ImportantYesUrgentYesActionableYesSingleStepTaskYesNotDoneIn2Mins -->|No| ImportantYesUrgentYesActionableYesSingleStepTaskYesNotDoneIn2MinsDelegateNo[No. Do it yourself?]
    ImportantYesUrgentYesActionableYesSingleStepTaskYesNotDoneIn2MinsDelegateNo -->|No| ImportantYesUrgentYesActionableYesSingleStepTaskYesNotDoneIn2MinsDelegateNoDoItYourselfNo[No. Put this away somewhere.]
    ImportantYesUrgentYesActionableYesSingleStepTaskYesNotDoneIn2MinsDelegateNo -->|Yes| ImportantYesUrgentYesActionableYesSingleStepTaskYesNotDoneIn2MinsDelegateNoDoItYourselfYes[Yes. Do you have time for it now?]
    ImportantYesUrgentYesActionableYesSingleStepTaskYesNotDoneIn2MinsDelegateNoDoItYourselfYes -->|Yes| ImportantYesUrgentYesActionableYesSingleStepTaskYesNotDoneIn2MinsDelegateNoDoItYourselfYesTimeForItNowYes[Yes. Do it now!]
    ImportantYesUrgentYesActionableYesSingleStepTaskYesNotDoneIn2MinsDelegateNoDoItYourselfYes -->|No| ImportantYesUrgentYesActionableYesSingleStepTaskYesNotDoneIn2MinsDelegateNoDoItYourselfYesTimeForItNowNo[No. Add this to TODO ASAP _or_ schedule it]

    ImportantYesUrgentYesActionableNo -->|Yes| ImportantYesUrgentYesActionableNoDelegateYes[Yes. Delegate for someone else to inbubate/develop]
    ImportantYesUrgentYesActionableNo -->|No| ImportantYesUrgentYesActionableNoDelegateNo[No. Incubate? I.e. develop idea further.]
    ImportantYesUrgentYesActionableNoDelegateNo -->|Yes| ImportantYesUrgentYesActionableNoDelegateNoIncubateYes[Yes. Incubate right now?]
    ImportantYesUrgentYesActionableNoDelegateNoIncubateYes -->|Yes| ImportantYesUrgentYesActionableNoDelegateNoIncubateYesRightNowYes[Yes. Have fun developing this idea now!]
    ImportantYesUrgentYesActionableNoDelegateNoIncubateYes -->|No| ImportantYesUrgentYesActionableNoDelegateNoIncubateYesRightNowNo[No. Schedule time for developing this idea further.]

    ImportantYesUrgentYesActionableNoDelegateNo -->|No| ImportantYesUrgentYesActionableNoDelegateNoIncubateNo[No. Is this a documentation task or something that should be available for reference in the future? Perhaps a blog post or presentation?]
    ImportantYesUrgentYesActionableNoDelegateNoIncubateNo -->|No| ImportantYesUrgentYesActionableNoDelegateNoIncubateNoForReferenceNo[No. Probably not worth your time? Or delegate or put somewhere to be handled at a later date.]
    ImportantYesUrgentYesActionableNoDelegateNoIncubateNo -->|No| ImportantYesUrgentYesActionableNoDelegateNoIncubateNoForReferenceYes[Yes. Start documenting, blogging or put wherever this needs to be for future reference.]

    ImportantYesUrgentYesActionableYesSingleStepTaskNo -->|Yes| ImportantYesUrgentYesActionableYesSingleStepTaskNoIncubateNowYes[Yes. Have fun breaking this task down into actionable steps!]
    ImportantYesUrgentYesActionableYesSingleStepTaskNo -->|No| ImportantYesUrgentYesActionableYesSingleStepTaskNoIncubateNowNo[No. Add a TODO ASAP to break this task down into actionable steps.]
```
