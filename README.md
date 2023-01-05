````mermaid
graph TD
    Important[Important?]

    Important -->|No| ImportantNoUrgent[Urgent?]
    Important -->|Yes| ImportantYesUrgent[Urgent?]

    ImportantNoUrgent -->|No| ImportantNoUrgentNo[Trash it!]
    ImportantNoUrgent -->|Yes| ImportantNoUrgentYesActionable[Delegate!]

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
    ImportantYesUrgentYesActionableNoIncubate -->|No| ImportantYesUrgentYesActionableNoIncubateNoDelegate[Delegate?]

    ImportantYesUrgentYesActionableNoIncubateNoDelegate -->|Yes| ImportantYesUrgentYesActionableNoIncubateNoDelegateYes[Delegate for someone else to inbubate/develop/define.] 
    ImportantYesUrgentYesActionableNoIncubateNoDelegate -->|No| ImportantYesUrgentYesActionableNoIncubateNoDelegateNo[Just keep for ref or docs, a blog post, reading etc? Define and add to TODO ASAP.]
```