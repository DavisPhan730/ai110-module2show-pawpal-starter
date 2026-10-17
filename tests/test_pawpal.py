from datetime import date, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


# Test 1: Check that tasks can be marked complete
def test_task_completion():
    task = Task("Feed Buddy", 10)

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


# Test 2: Check that adding a task works
def test_task_addition():
    pet = Pet("Buddy", "Dog")

    assert len(pet.tasks) == 0

    task = Task("Morning Walk", 30)
    pet.add_task(task)

    assert len(pet.tasks) == 1


# Test 3: Check tasks from multiple pets
def test_multiple_pets():
    owner = Owner("Davis")

    dog = Pet("Buddy", "Dog")
    cat = Pet("Luna", "Cat")

    dog.add_task(Task("Walk Buddy", 30, "high"))
    cat.add_task(Task("Feed Luna", 10, "high"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler()
    plan = scheduler.generate_daily_plan(owner)

    assert len(plan) == 2
    assert "Walk Buddy" in [task.title for task in plan]
    assert "Feed Luna" in [task.title for task in plan]


# Test 4: Check sorting tasks by time
def test_sort_by_time():
    scheduler = Scheduler()

    tasks = [
        Task("Evening Walk", 30, preferred_time="18:00"),
        Task("Breakfast", 10, preferred_time="08:00"),
        Task("Playtime", 20, preferred_time="14:00")
    ]

    result = scheduler.sort_by_time(tasks)

    assert [task.title for task in result] == [
        "Breakfast",
        "Playtime",
        "Evening Walk"
    ]


# Test 5: Check filtering by pet and completion
def test_filter_by_pet_and_status():
    owner = Owner("Davis")

    dog = Pet("Buddy", "Dog")
    cat = Pet("Luna", "Cat")

    dog.add_task(Task("Walk", 30))
    cat.add_task(Task("Feed", 10, completed=True))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler()

    buddy_tasks = scheduler.filter_tasks(
        owner, pet_name="Buddy"
    )

    completed_tasks = scheduler.filter_tasks(
        owner, completed=True
    )

    assert len(buddy_tasks) == 1
    assert buddy_tasks[0].title == "Walk"

    assert len(completed_tasks) == 1
    assert completed_tasks[0].title == "Feed"


# Test 6: Check recurring tasks
def test_recurring_task():
    dog = Pet("Buddy", "Dog")

    today = date.today()

    task = Task(
        "Feed Buddy",
        10,
        recurrence="daily",
        due_date=today
    )

    dog.add_task(task)
    dog.complete_task(task)

    assert task.completed is True
    assert len(dog.tasks) == 2

    next_task = dog.tasks[1]

    assert next_task.completed is False
    assert next_task.due_date == today + timedelta(days=1)


# Test 7: Check scheduling conflicts
def test_conflict_detection():
    scheduler = Scheduler()

    tasks = [
        Task(
            "Walk Buddy",
            30,
            preferred_time="08:00"
        ),
        Task(
            "Feed Luna",
            15,
            preferred_time="08:10"
        )
    ]

    conflicts = scheduler.find_conflicts(tasks)

    assert len(conflicts) == 1
    assert conflicts[0][0].title == "Walk Buddy"
    assert conflicts[0][1].title == "Feed Luna"
