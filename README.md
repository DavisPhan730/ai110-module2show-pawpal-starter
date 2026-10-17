# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Features

PawPal+ is a pet care app that helps owners manage tasks for
multiple pets and keep track of their daily routines.

Some of the main features include:

- Add multiple pets and their information.
- Create feeding, walking, medication, and other care tasks.
- Set a task's duration, priority, time, and recurrence.
- Sort tasks from earliest to latest.
- Filter tasks by pet or completion status.
- Mark tasks as complete.
- Automatically create the next daily or weekly task.
- Detect tasks that overlap and display a warning.
- Generate a daily schedule based on priority and available time.

The app uses four Python classes: Owner, Pet, Task, and Scheduler.
The Scheduler gets tasks from all of the owner's pets and
organizes them into a daily plan.

## Getting Started

### Setup

```bash
python -m venv .venv
```

Activate the virtual environment:

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:
```bash
pip install -r requirements.txt
pip install pytest
```

### Suggested Workflow

1. Read the scenario and figure out what the app needs.
2. Create a UML diagram showing the classes.
3. Turn the UML into Python classes.
4. Implement the scheduling logic.
5. Add tests to make sure everything works.
6. Connect the logic to the Streamlit UI.
7. Update the UML to match the finished code.

## Implementation Summary

For this part of the project, I worked on getting the main Python classes to actually work instead of just having empty methods.

I used four classes: Owner, Pet, Task, and Scheduler. The Owner class keeps track of the pets, and each Pet stores its own tasks. The Task class handles things like the task name, duration, priority, and completion status. The Scheduler takes all the tasks from the owner's pets and organizes them into a daily schedule.

I also made a `main.py` file so I could test everything in the terminal before connecting it to Streamlit. I used two pets with different tasks to make sure the scheduler could handle more than one pet.

## 🖥️ Sample Output

I ran my program using:

```bash
python main.py
```

Expected output from the demo:

```text
=== PawPal+ Today's Schedule ===
Owner: Davis
Number of Pets: 2

08:00 - Morning Walk (30 min) [Priority: high]
08:30 - Feed Luna (10 min) [Priority: high]
09:00 - Feed Buddy (10 min) [Priority: high]
17:00 - Play with Luna (20 min) [Priority: medium]

Total Tasks: 4
Total Time: 70 minutes
```

## 🧪 Testing PawPal+

For this phase, I used pytest to make sure my PawPal+ system
was working correctly. I tested the main features like adding
tasks, marking tasks as complete, sorting tasks by time,
and creating schedules for multiple pets.

I also added some extra tests to see how the program handles
different situations. For example, I tested what happens when
a pet has no tasks, when two tasks are scheduled at the same
time, and when the owner doesn't have enough time to finish
everything.

I also checked that daily and weekly recurring tasks create
a new task with the correct due date after being completed.


To run the tests:

```bash
python -m pytest -v
```

Expected results:

```text
tests/test_pawpal.py::test_task_completion PASSED            [  8%]
tests/test_pawpal.py::test_task_addition PASSED              [ 16%]
tests/test_pawpal.py::test_multiple_pets PASSED              [ 25%]
tests/test_pawpal.py::test_sort_by_time PASSED               [ 33%]
tests/test_pawpal.py::test_filter_by_pet_and_status PASSED   [ 41%]
tests/test_pawpal.py::test_recurring_task PASSED             [ 50%]
tests/test_pawpal.py::test_conflict_detection PASSED         [ 58%]
tests/test_pawpal.py::test_empty_pet_schedule PASSED         [ 66%]
tests/test_pawpal.py::test_duplicate_task_times PASSED       [ 75%]
tests/test_pawpal.py::test_available_time_limit PASSED       [ 83%]
tests/test_pawpal.py::test_completed_tasks_not_scheduled PASSED [ 91%]
tests/test_pawpal.py::test_weekly_recurrence PASSED          [100%]

======================= 12 passed in 0.03s ========================
```
### What I Tested

- Adding tasks to a pet
- Marking tasks as completed
- Scheduling tasks from multiple pets
- Sorting tasks by time
- Filtering tasks by pet and completion status
- Creating daily recurring tasks
- Detecting overlapping tasks
- Handling pets with no tasks
- Detecting tasks scheduled at the exact same time
- Staying within the owner's available time
- Excluding completed tasks from the schedule
- Creating weekly recurring tasks

### Confidence Level

★★★★☆ (4/5 stars)

I would rate my confidence in the system a 4 out of 5
if all 12 tests pass. I think the program works well
for the main features, and the tests helped me check
that everything was behaving the way I expected.

There are still a few things I could improve. For
example, the scheduler detects overlapping tasks,
but it doesn't automatically change their times.
I would also want to test more complicated schedules
before saying the system is completely reliable.


## 📐 Smarter Scheduling

For this phase, I added some new features to make the scheduling
system more useful. The app can now sort tasks by time, filter
tasks, handle repeating tasks, and find scheduling conflicts.

| Feature | Method(s) | What it does |
|---|---|---|
| Sorting | sort_by_time() | Organizes tasks from earliest to latest |
| Filtering | filter_tasks() | Filters by pet name or completion status |
| Recurring tasks | mark_complete(), complete_task() | Creates the next daily or weekly task |
| Conflict detection | find_conflicts() | Checks if task times overlap |
| Daily planning | generate_daily_plan() | Creates a plan based on priority and available time |

I tested the features in main.py using two pets, Buddy and Luna.
I added tasks out of order to check sorting and scheduled two
tasks at overlapping times to check conflict detection.

I also tested recurring tasks by completing a daily feeding
task and checking that a new task was created for the next day.

## 📸 Demo Walkthrough

For this project, I created a Streamlit app that lets pet owners
add pets, schedule care tasks, and organize their daily routines.

### How to Use the App

1. Run the app using `python -m streamlit run app.py`.
2. Enter the owner's name and available time for the day.
3. Add a pet by entering its name and species.
4. Add tasks for the pet, including the task name, duration,
   priority, preferred time, and recurrence.
5. Use the filters to view tasks for a specific pet or status.
6. Mark a task as complete when it is finished.
7. Check the Scheduling Conflicts section for overlapping tasks.
8. Click Generate Schedule to see the daily plan.

### Example Workflow

For my example, I created two pets named Buddy and Luna.
I added walking and feeding tasks and gave them different
priorities and times.

The Scheduler organizes tasks by priority while staying within
the owner's available time. The app can then display the selected
tasks in chronological order.

If two tasks overlap, the app shows a warning so the owner knows
there might be a scheduling problem.

I also tested recurring tasks. When I complete a daily task,
the system creates another task for the next day.

### Sample CLI Output

```text
=== PawPal+ Smart Scheduling Demo ===
Owner: Davis
Pets: 2

--- Tasks Sorted by Time ---
08:00 - Feed Luna
08:00 - Feed Buddy
14:00 - Play with Luna
18:00 - Evening Walk

--- Buddy's Tasks ---
Evening Walk
Feed Buddy

--- Scheduling Conflicts ---
WARNING: Feed Luna overlaps with Feed Buddy!

--- Recurring Task Test ---
Original due date: 2026-10-17
Completed: True
Next due date: 2026-10-18

--- Today's Schedule ---
08:00 - Feed Luna (10 min)
14:00 - Play with Luna (20 min)
18:00 - Evening Walk (30 min)

Total Tasks: 3
Total Time: 60 minutes
```

### Testing

I used pytest to check the most important parts of my system.
My tests cover sorting, task completion, filtering, multiple
pets, recurring tasks, time limits, and conflicts.

The tests help me make sure changes to the program don't
break features that were already working.