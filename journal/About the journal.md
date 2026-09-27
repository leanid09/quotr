---
type: overview
description: How to use the daily notes and the weekly and monthly reviews in this folder.
---
# About the journal

> [!abstract] What this folder is for
> Your working log: one note per day, a weekly review on Fridays and a monthly review in the first week of each month. The notes are created from templates, so they already have the right headings and live tables.

## Daily note (about 10 minutes)

- Click the **calendar** icon on the far left. Obsidian creates today's note in this folder, or opens it if it already exists.
- Or press **Ctrl+P** (Mac: **Cmd+P**) and choose **Daily notes: Open today's daily note**.

## Weekly review (Friday, about 20 minutes)

1. Create a new note in this folder and name it like `2026-W40 weekly review`.
2. Press **Ctrl+P** (Mac: **Cmd+P**), choose **Templates: Insert template**, then **Weekly review**.

## Monthly review (first week of the month)

The same steps with the **Monthly review** template. It holds the monthly checklist from [[Start here#How to keep it current: the monthly routine|Start here]].

> [!warning] This folder is yours
> Claude never creates or edits notes here. Its updates go into test-run notes, the [[Changelog]] and pull requests that you approve.

## Recent journal notes

```base
filters:
  and:
    - file.inFolder("journal")
    - '["daily-note", "weekly-review", "monthly-review"].contains(type)'
views:
  - type: table
    name: Recent journal notes
    order:
      - file.name
      - type
    sort:
      - property: file.name
        direction: DESC
    limit: 30
```
