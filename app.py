import streamlit as st
from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PawPal+")
st.write("Keep track of your pets and their daily care tasks.")


# Keep the owner saved when Streamlit reruns
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

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

owner.available_minutes = st.number_input(
    "Available time today (minutes)",
    min_value=1,
    value=owner.available_minutes
)


# Add a pet
st.header("Add a Pet")

with st.form("pet_form", clear_on_submit=True):
    pet_name = st.text_input("Pet name")
    species = st.selectbox(
        "Species",
        ["Dog", "Cat", "Other"]
    )

    add_pet = st.form_submit_button("Add Pet")

    if add_pet:
        if pet_name.strip():
            new_pet = Pet(pet_name.strip(), species)
            owner.add_pet(new_pet)
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
        selected_pet = st.selectbox(
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
            ["low", "medium", "high"]
        )

        preferred_time = st.time_input(
            "Preferred time",
            value="08:00"
        )

        recurrence = st.selectbox(
            "Repeat",
            ["none", "daily", "weekly"]
        )

        add_task = st.form_submit_button("Add Task")

        if add_task:
            if task_title.strip():
                new_task = Task(
                    title=task_title.strip(),
                    duration_minutes=int(duration),
                    priority=priority,
                    preferred_time=preferred_time.strftime("%H:%M"),
                    recurrence=recurrence
                )

                owner.pets[selected_pet].add_task(new_task)
                st.success("Task added successfully!")
            else:
                st.warning("Please enter a task name.")
else:
    st.info("Add a pet before creating tasks.")


# Show current tasks
st.header("Current Tasks")

task_rows = []

for pet in owner.pets:
    for task in pet.tasks:
        task_rows.append({
            "Pet": pet.name,
            "Task": task.title,
            "Duration": task.duration_minutes,
            "Priority": task.priority,
            "Time": task.preferred_time,
            "Completed": task.completed
        })

if task_rows:
    st.dataframe(task_rows, use_container_width=True)
else:
    st.info("No tasks added yet.")


# Generate a schedule
st.header("Today's Schedule")

if st.button("Generate Schedule"):
    plan = scheduler.generate_daily_plan(
        owner,
        day=date.today()
    )

    if plan:
        st.success("Your daily schedule is ready!")

        for task in plan:
            time = task.preferred_time or "Anytime"

            st.write(
                f"**{time} - {task.title}** "
                f"({task.duration_minutes} min) "
                f"[Priority: {task.priority}]"
            )

        total = sum(
            task.duration_minutes for task in plan
        )

        st.write(f"**Total Time:** {total} minutes")

    else:
        st.info("No tasks available to schedule.")
