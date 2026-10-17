from dataclasses import dataclass, field
from datetime import date, datetime, timedelta


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str = "medium"
    preferred_time: str | None = None
    recurrence: str = "none"
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark a task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)


@dataclass
class Owner:
    name: str
    available_minutes: int = 120
    preferences: list[str] = field(default_factory=list)
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        """Get tasks from all of the owner's pets."""
        all_tasks = []

        for pet in self.pets:
            all_tasks.extend(pet.tasks)

        return all_tasks


class Scheduler:
    def sort_tasks(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks by priority and preferred time."""
        priority_order = {"high": 0, "medium": 1, "low": 2}

        return sorted(
            tasks,
            key=lambda task: (
                priority_order.get(task.priority.lower(), 3),
                task.preferred_time or "23:59"
            )
        )

    def find_conflicts(
        self, tasks: list[Task]
    ) -> list[tuple[Task, Task]]:
        """Find tasks with overlapping scheduled times."""
        conflicts = []

        timed_tasks = [
            task for task in tasks
            if task.preferred_time is not None
        ]

        for i in range(len(timed_tasks)):
            first = timed_tasks[i]
            first_start = datetime.strptime(
                first.preferred_time, "%H:%M"
            )
            first_end = first_start + timedelta(
                minutes=first.duration_minutes
            )

            for second in timed_tasks[i + 1:]:
                second_start = datetime.strptime(
                    second.preferred_time, "%H:%M"
                )
                second_end = second_start + timedelta(
                    minutes=second.duration_minutes
                )

                if first_start < second_end and second_start < first_end:
                    conflicts.append((first, second))

        return conflicts

    def recurring_tasks_for_day(
        self, tasks: list[Task], day: date
    ) -> list[Task]:
        """Get tasks that repeat on the chosen day."""
        repeating = []

        for task in tasks:
            frequency = task.recurrence.lower()

            if frequency == "daily":
                repeating.append(task)
            elif frequency == "weekly" and day.weekday() == 0:
                repeating.append(task)

        return repeating

    def generate_daily_plan(
        self, owner: Owner, pet: Pet | None = None,
        day: date | None = None
    ) -> list[Task]:
        """Make a daily schedule using all of the owner's pets."""
        if day is None:
            day = date.today()

        # Retrieve tasks from every pet, not just one.
        all_tasks = owner.get_all_tasks()

        todays_tasks = [
            task for task in all_tasks
            if not task.completed
            and task.recurrence.lower() in ("none", "daily")
        ]

        todays_tasks.extend(
            task for task in all_tasks
            if not task.completed
            and task.recurrence.lower() == "weekly"
            and day.weekday() == 0
        )

        sorted_tasks = self.sort_tasks(todays_tasks)

        daily_plan = []
        total_minutes = 0

        for task in sorted_tasks:
            if total_minutes + task.duration_minutes <= owner.available_minutes:
                daily_plan.append(task)
                total_minutes += task.duration_minutes

        return daily_plan
