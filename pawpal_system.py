from dataclasses import dataclass, field
from datetime import date


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str = "medium"
    preferred_time: str | None = None
    recurrence: str = "none"
    completed: bool = False

    def mark_complete(self) -> None:
        raise NotImplementedError


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        raise NotImplementedError


@dataclass
class Owner:
    name: str
    available_minutes: int = 120
    preferences: list[str] = field(default_factory=list)
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        raise NotImplementedError


class Scheduler:

    def sort_tasks(self, tasks: list[Task]) -> list[Task]:
        raise NotImplementedError

    def find_conflicts(
        self, tasks: list[Task]
    ) -> list[tuple[Task, Task]]:
        raise NotImplementedError

    def recurring_tasks_for_day(
        self, tasks: list[Task], day: date
    ) -> list[Task]:
        raise NotImplementedError

    def generate_daily_plan(
        self, owner: Owner, pet: Pet, day: date
    ) -> list[Task]:
        raise NotImplementedError
