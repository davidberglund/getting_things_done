````mermaid
flowchart LR
    Important[Important?]

    Important -->|No| ImportantNoUrgent[Urgent?]
    Important -->|Yes| ImportantYesUrgent[Urgent?]

    ImportantNoUrgent -->|No| ImportantNoUrgentNo[Trash it.]
    ImportantNoUrgent -->|Yes| ImportantNoUrgentYesActionable[Delegate.]

    ImportantYesUrgent -->|No| ImportantYesUrgentNoActionable[Actionable?]
    ImportantYesUrgent -->|Yes| ImportantYesUrgentYesActionable[Actionable?]

    ImportantYesUrgentNoActionable -->|Yes| ImportantYesUrgentNoActionableYes[Add to backlog but don't worry about the details.]
    ImportantYesUrgentNoActionable -->|No| ImportantYesUrgentNoActionableNoDelegate[Delegate and let someone else develop/incubate it?]

    ImportantYesUrgentNoActionableNoDelegate -->|No| ImportantYesUrgentNoActionableNoDelegateNo[Just keep for ref or docs, a blog post, reading etc? Add to backlog with proper label.]
    ImportantYesUrgentNoActionableNoDelegate -->|Yes| ImportantYesUrgentNoActionableNoDelegateYes[Delegate for someone else to inbubate/develop.]

    ImportantYesUrgentYesActionable -->|Yes| ImportantYesUrgentYesActionableYesSingleStepTask[Single step task?]
    ImportantYesUrgentYesActionable -->|No| ImportantYesUrgentYesActionableNoIncubate[Incubate?]
    
    ImportantYesUrgentYesActionableYesSingleStepTask -->|Yes| ImportantYesUrgentYesActionableYesSingleStepTaskYesDoneIn2Mins[Done in 2 min?]
    ImportantYesUrgentYesActionableYesSingleStepTask -->|No| ImportantYesUrgentYesActionableYesSingleStepTaskNoIncubateNow[Project? Break down into goal/s and actionable steps. Do that now?]

    ImportantYesUrgentYesActionableYesSingleStepTaskNoIncubateNow -->|Yes| ImportantYesUrgentYesActionableYesSingleStepTaskNoIncubateNowYes[Break this task down into actionable steps.]
    ImportantYesUrgentYesActionableYesSingleStepTaskNoIncubateNow -->|No| ImportantYesUrgentYesActionableYesSingleStepTaskNoIncubateNowNo[Add a TODO ASAP to break this task down into actionable steps.]

    ImportantYesUrgentYesActionableYesSingleStepTaskYesDoneIn2Mins -->|Yes| ImportantYesUrgentYesActionableYesSingleStepTaskYesDoneIn2MinsYes[Do it now!]
    ImportantYesUrgentYesActionableYesSingleStepTaskYesDoneIn2Mins -->|No| ImportantYesUrgentYesActionableYesSingleStepTaskYesDoneIn2MinsNo[Add to TODO ASAP.]

    ImportantYesUrgentYesActionableNoIncubate -->|Yes| ImportantYesUrgentYesActionableNoIncubateYes[Add TODO ASAP to incubate/develop this idea further.]
    ImportantYesUrgentYesActionableNoIncubate -->|No| ImportantYesUrgentYesActionableNoIncubateNoReference[Just keep for ref or docs, a blog post, reading etc?]

    ImportantYesUrgentYesActionableNoIncubateNoReference -->|Yes| ImportantYesUrgentYesActionableNoIncubateNoReferenceYes[Put this where it can be referenced or produce the docs/blog post etc. Right now or add to TODO ASAP.]
    ImportantYesUrgentYesActionableNoIncubateNoReference -->|No| ImportantYesUrgentYesActionableNoIncubateNoReferenceNoDelegate[Delegate?]

    ImportantYesUrgentYesActionableNoIncubateNoReferenceNoDelegate -->|Yes| ImportantYesUrgentYesActionableNoIncubateNoReferenceNoDelegateYes[Delegate for someone else to inbubate/develop/define.]
    ImportantYesUrgentYesActionableNoIncubateNoReferenceNoDelegate -->|No| ImportantYesUrgentYesActionableNoIncubateNoReferenceNoDelegateNo[Figure out what this is and make sure it doesn't amount to unnecessary clutter.]
```