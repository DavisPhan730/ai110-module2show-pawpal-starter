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

I added three tests to check the main features of my program.

The first test checks that marking a task as complete changes its status. The second test checks that adding a task to a pet increases its task count. The third test checks that the scheduler can get tasks from multiple pets.

To run the tests:

```bash
python -m pytest -v
```

Expected results:

```text
tests/test_pawpal.py::test_task_completion PASSED
tests/test_pawpal.py::test_task_addition PASSED
tests/test_pawpal.py::test_multiple_pets PASSED

3 passed
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | sort_tasks() | Sorts tasks by priority and preferred time |
| Filtering | generate_daily_plan() | Skips completed tasks and tasks that exceed the available time |
| Conflict handling | find_conflicts() | Finds tasks that have overlapping times |
| Recurring tasks | recurring_tasks_for_day() | Handles daily tasks and weekly tasks scheduled for Monday |

The scheduler uses the Owner class to collect tasks from all pets. It then organizes the tasks based on priority and available time.

Right now, the scheduling system is pretty basic, but it works for organizing multiple pets' tasks. Some improvements I could make later are handling different days for weekly tasks and automatically adjusting tasks that overlap.

## 📸 Demo Walkthrough

1. Run `python main.py` in the terminal.
2. The program creates an owner named Davis and two pets named Buddy and Luna.
3. Each pet gets its own care tasks, including walks, feeding, and playtime.
4. The Scheduler collects all the tasks and organizes them into a daily schedule.
5. The program prints the schedule, showing the task times, priorities, and total time needed.

**Screenshot or video** *(optional)*:
