from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_completion():
    # Make a task and check its starting status
    task = Task("Feed Buddy", 10)

    assert task.completed is False

    # Mark the task as complete
    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    # Create a pet without any tasks
    pet = Pet("Buddy", "Dog")

    assert len(pet.tasks) == 0

    # Add a task
    task = Task("Morning Walk", 30)
    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_multiple_pets():
    # Make sure the scheduler includes both pets
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
