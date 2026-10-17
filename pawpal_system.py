from dataclasses import dataclass, field, replace
from datetime import date, datetime, timedelta


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str = "medium"
    preferred_time: str | None = None
    recurrence: str = "none"
    completed: bool = False
    due_date: date | None = None

    def __post_init__(self):
        """Set a starting date for recurring tasks."""
        if self.due_date is None:
            if self.recurrence == "daily":
                self.due_date = date.today()
            elif self.recurrence == "weekly":
                today = date.today()
                days_until_monday = (7 - today.weekday()) % 7
                self.due_date = today + timedelta(
                    days=days_until_monday
                )

    def mark_complete(self):
        """Complete a task and create its next occurrence."""
        if self.completed:
            return None

        self.completed = True

        if self.recurrence not in ("daily", "weekly"):
            return None

        days = 1 if self.recurrence == "daily" else 7
        current_due = self.due_date or date.today()

        return replace(
            self,
            completed=False,
            due_date=current_due + timedelta(days=days)
        )


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a care task for this pet."""
        self.tasks.append(task)

    def complete_task(self, task: Task) -> None:
        """Finish a task and save its next occurrence."""
        if task not in self.tasks:
            raise ValueError("Task does not belong to this pet.")

        next_task = task.mark_complete()

        if next_task is not None:
            self.tasks.append(next_task)


@dataclass
class Owner:
    name: str
    available_minutes: int = 120
    preferences: list[str] = field(default_factory=list)
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's account."""
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        """Collect tasks from all pets."""
        all_tasks = []

        for pet in self.pets:
            all_tasks.extend(pet.tasks)

        return all_tasks


class Scheduler:

    def sort_tasks(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks by priority, then preferred time."""
        priority_order = {
            "high": 0,
            "medium": 1,
            "low": 2
        }

        return sorted(
            tasks,
            key=lambda task: (
                priority_order.get(task.priority.lower(), 3),
                task.preferred_time or "23:59"
            )
        )

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks from earliest to latest time."""
        return sorted(
            tasks,
            key=lambda task: task.preferred_time or "23:59"
        )

    def filter_tasks(
        self,
        owner: Owner,
        pet_name: str | None = None,
        completed: bool | None = None
    ) -> list[Task]:
        """Filter tasks by pet name or completion status."""
        results = []

        for pet in owner.pets:
            if pet_name is not None:
                if pet.name.lower() != pet_name.lower():
                    continue

            for task in pet.tasks:
                if completed is not None:
                    if task.completed != completed:
                        continue

                results.append(task)

        return results

    def find_conflicts(
        self, tasks: list[Task]
    ) -> list[tuple[Task, Task]]:
        """Find overlapping tasks and return the pairs."""
        conflicts = []

        timed_tasks = [
            task for task in tasks
            if task.preferred_time is not None
            and not task.completed
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

                if (
                    first_start < second_end
                    and second_start < first_end
                ):
                    conflicts.append((first, second))

        return conflicts

    def recurring_tasks_for_day(
        self, tasks: list[Task], day: date
    ) -> list[Task]:
        """Return recurring tasks due on a chosen day."""
        return [
            task for task in tasks
            if not task.completed
            and task.recurrence in ("daily", "weekly")
            and task.due_date is not None
            and task.due_date <= day
        ]

    def generate_daily_plan(
        self,
        owner: Owner,
        pet: Pet | None = None,
        day: date | None = None
    ) -> list[Task]:
        """Create a daily plan from all of the owner's pets."""
        if day is None:
            day = date.today()

        all_tasks = owner.get_all_tasks()

        todays_tasks = [
            task for task in all_tasks
            if not task.completed
            and (task.due_date is None or task.due_date <= day)
        ]

        sorted_tasks = self.sort_tasks(todays_tasks)

        daily_plan = []
        total_minutes = 0

        for task in sorted_tasks:
            if (
                total_minutes + task.duration_minutes
                <= owner.available_minutes
            ):
                daily_plan.append(task)
                total_minutes += task.duration_minutes

        return daily_plan
