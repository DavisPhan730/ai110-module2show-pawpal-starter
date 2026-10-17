from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner("Davis", available_minutes=120)

    dog = Pet("Buddy", "Dog")
    cat = Pet("Luna", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    # Add tasks out of time order
    dog.add_task(Task(
        "Evening Walk", 30, "medium", "18:00", "daily"
    ))

    cat.add_task(Task(
        "Feed Luna", 10, "high", "08:00", "daily"
    ))

    dog.add_task(Task(
        "Feed Buddy", 15, "high", "08:00", "daily"
    ))

    cat.add_task(Task(
        "Play with Luna", 20, "low", "14:00", "none"
    ))

    scheduler = Scheduler()

    print("=== PawPal+ Smart Scheduling Demo ===")
    print(f"Owner: {owner.name}")
    print(f"Pets: {len(owner.pets)}")

    # Test sorting
    print("\n--- Tasks Sorted by Time ---")

    sorted_tasks = scheduler.sort_by_time(
        owner.get_all_tasks()
    )

    for task in sorted_tasks:
        print(f"{task.preferred_time} - {task.title}")

    # Test filtering
    print("\n--- Buddy's Tasks ---")

    buddy_tasks = scheduler.filter_tasks(
        owner, pet_name="Buddy"
    )

    for task in buddy_tasks:
        print(task.title)

    # Test conflict detection
    print("\n--- Scheduling Conflicts ---")

    conflicts = scheduler.find_conflicts(
        owner.get_all_tasks()
    )

    if conflicts:
        for first, second in conflicts:
            print(
                f"WARNING: {first.title} overlaps "
                f"with {second.title}!"
            )
    else:
        print("No conflicts found.")

    # Test recurring tasks
    print("\n--- Recurring Task Test ---")

    feeding = dog.tasks[1]
    print(f"Original due date: {feeding.due_date}")

    dog.complete_task(feeding)

    next_feeding = dog.tasks[-1]
    print(f"Completed: {feeding.completed}")
    print(f"Next due date: {next_feeding.due_date}")

    # Generate the daily plan
    print("\n--- Today's Schedule ---")

    plan = scheduler.generate_daily_plan(
        owner, day=date.today()
    )

    for task in scheduler.sort_by_time(plan):
        print(
            f"{task.preferred_time or 'Anytime'} - "
            f"{task.title} "
            f"({task.duration_minutes} min)"
        )

    print(f"\nTotal Tasks: {len(plan)}")
    print(
        "Total Time:",
        sum(task.duration_minutes for task in plan),
        "minutes"
    )


if __name__ == "__main__":
    main()
