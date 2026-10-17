from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create the owner
    owner = Owner("Davis", available_minutes=120)

    # Create two pets
    dog = Pet("Buddy", "Dog")
    cat = Pet("Luna", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    # Add care tasks
    dog.add_task(Task(
        "Morning Walk", 30, "high", "08:00", "daily"
    ))

    dog.add_task(Task(
        "Feed Buddy", 10, "high", "09:00", "daily"
    ))

    cat.add_task(Task(
        "Feed Luna", 10, "high", "08:30", "daily"
    ))

    cat.add_task(Task(
        "Play with Luna", 20, "medium", "17:00", "daily"
    ))

    # Generate the schedule
    scheduler = Scheduler()
    schedule = scheduler.generate_daily_plan(
        owner, day=date.today()
    )

    print("=== PawPal+ Today's Schedule ===")
    print(f"Owner: {owner.name}")
    print(f"Number of Pets: {len(owner.pets)}")
    print()

    for task in schedule:
        time = task.preferred_time or "Anytime"
        print(
            f"{time} - {task.title} "
            f"({task.duration_minutes} min) "
            f"[Priority: {task.priority}]"
        )

    print()
    print(f"Total Tasks: {len(schedule)}")
    print(
        "Total Time:",
        sum(task.duration_minutes for task in schedule),
        "minutes"
    )


if __name__ == "__main__":
    main()
