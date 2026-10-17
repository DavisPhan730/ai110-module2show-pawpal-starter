import streamlit as st
from datetime import date, time

from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PawPal+")
st.write("A simple way to manage your pets and their daily tasks.")


# Keep pets and tasks saved during the session
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Davis")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

owner = st.session_state.owner
scheduler = st.session_state.scheduler


# Owner information
st.header("Owner Information")

owner.name = st.text_input(
    "Owner name",
    value=owner.name
)

owner.available_minutes = int(st.number_input(
    "Available time today (minutes)",
    min_value=1,
    value=owner.available_minutes
))


# Add a new pet
st.header("Add a Pet")

with st.form("pet_form", clear_on_submit=True):
    pet_name = st.text_input("Pet name")
    species = st.selectbox(
        "Species",
        ["Dog", "Cat", "Other"]
    )

    if st.form_submit_button("Add Pet"):
        if pet_name.strip():
            owner.add_pet(Pet(pet_name.strip(), species))
            st.success(f"{pet_name} was added!")
        else:
            st.warning("Please enter a pet name.")


# Display saved pets
st.header("My Pets")

if owner.pets:
    for pet in owner.pets:
        st.write(f"🐾 {pet.name} ({pet.species})")
else:
    st.info("No pets added yet.")


# Add a task
st.header("Add a Care Task")

if owner.pets:
    with st.form("task_form", clear_on_submit=True):
        pet_index = st.selectbox(
            "Choose a pet",
            range(len(owner.pets)),
            format_func=lambda i: owner.pets[i].name
        )

        task_title = st.text_input("Task name")

        duration = st.number_input(
            "Duration (minutes)",
            min_value=1,
            value=20
        )

        priority = st.selectbox(
            "Priority",
            ["high", "medium", "low"]
        )

        preferred_time = st.time_input(
            "Preferred time",
            value=time(8, 0)
        )

        recurrence = st.selectbox(
            "Repeat",
            ["none", "daily", "weekly"]
        )

        if st.form_submit_button("Add Task"):
            if task_title.strip():
                task = Task(
                    title=task_title.strip(),
                    duration_minutes=int(duration),
                    priority=priority,
                    preferred_time=preferred_time.strftime("%H:%M"),
                    recurrence=recurrence
                )

                owner.pets[pet_index].add_task(task)
                st.success("Task added successfully!")
            else:
                st.warning("Please enter a task name.")
else:
    st.info("Add a pet before creating tasks.")


# Sort and filter tasks
st.header("View Tasks")

if owner.pets:
    pet_filter = st.selectbox(
        "Filter by pet",
        ["All Pets"] + [pet.name for pet in owner.pets]
    )

    status_filter = st.selectbox(
        "Filter by status",
        ["All", "Pending", "Completed"]
    )

    selected_pet = (
        None if pet_filter == "All Pets" else pet_filter
    )

    selected_status = None

    if status_filter == "Pending":
        selected_status = False
    elif status_filter == "Completed":
        selected_status = True

    filtered_tasks = scheduler.filter_tasks(
        owner,
        pet_name=selected_pet,
        completed=selected_status
    )

    sorted_tasks = scheduler.sort_by_time(filtered_tasks)

    rows = []

    for task in sorted_tasks:
        pet_for_task = "Unknown"

        for pet in owner.pets:
            if any(saved is task for saved in pet.tasks):
                pet_for_task = pet.name
                break

        rows.append({
            "Pet": pet_for_task,
            "Task": task.title,
            "Time": task.preferred_time or "Anytime",
            "Duration": task.duration_minutes,
            "Priority": task.priority,
            "Status": (
                "Done" if task.completed else "Pending"
            ),
            "Due Date": (
                str(task.due_date)
                if task.due_date else "Not set"
            )
        })

    if rows:
        st.table(rows)
    else:
        st.info("No tasks match your filters.")


# Mark tasks as complete
st.header("Complete a Task")

pending_options = []

for pet in owner.pets:
    for task in pet.tasks:
        if not task.completed:
            pending_options.append((pet, task))

if pending_options:
    selected_index = st.selectbox(
        "Choose a task to complete",
        range(len(pending_options)),
        format_func=lambda i: (
            f"{pending_options[i][0].name} - "
            f"{pending_options[i][1].title}"
        )
    )

    if st.button("Mark Task Complete"):
        pet, task = pending_options[selected_index]
        pet.complete_task(task)

        st.success(f"{task.title} marked as complete!")
        st.rerun()
else:
    st.info("No pending tasks.")


# Detect conflicts
st.header("Scheduling Conflicts")

todays_tasks = [
    task for task in owner.get_all_tasks()
    if not task.completed
    and (task.due_date is None or task.due_date <= date.today())
]

conflicts = scheduler.find_conflicts(todays_tasks)

if conflicts:
    for first, second in conflicts:
        st.warning(
            f"⚠️ {first.title} overlaps with {second.title}. "
            "Consider changing one of the times."
        )
else:
    st.success("No scheduling conflicts found!")


# Generate schedule
st.header("Today's Schedule")

if st.button("Generate Schedule"):
    plan = scheduler.generate_daily_plan(
        owner,
        day=date.today()
    )

    if plan:
        st.success("Your daily schedule is ready!")

        ordered_plan = scheduler.sort_by_time(plan)

        for task in ordered_plan:
            st.write(
                f"**{task.preferred_time or 'Anytime'} - "
                f"{task.title}** "
                f"({task.duration_minutes} min) "
                f"[Priority: {task.priority}]"
            )

        total_minutes = sum(
            task.duration_minutes for task in plan
        )

        st.write(f"**Total Time: {total_minutes} minutes**")
        st.caption(
            "Tasks are selected by priority and available time, "
            "then displayed in chronological order."
        )
    else:
        st.info("No tasks available to schedule today.")
