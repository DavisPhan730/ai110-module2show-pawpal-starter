# PawPal+ Project Reflection

## 1. System Design
The three main things I want users to be able to do are add their pets, make tasks for them, and see a daily schedule. For example, someone could add their dog, set up feeding and walking times, and see what they need to get done that day.

**a. Initial design**

When I first started PawPal+, I wanted users to be able to add pets, create care tasks, and generate a daily schedule. I decided to use four classes: Owner, Pet, Task, and Scheduler.

The Owner class keeps track of the owner's information and pets. The Pet class stores information about each pet and its tasks. The Task class handles things like feeding, walks, and medications. The Scheduler class is responsible for organizing everything into a daily plan. I also created a UML diagram to show how the different classes connect.

**b. Design changes**

As I worked on the project, I realized I needed more methods than I originally planned. I added a method to the Owner class to collect tasks from every pet because the scheduler needed to work with multiple pets.

I also added methods for filtering tasks, sorting them by time, and creating recurring tasks. These changes made the system more useful without having to completely change my original design.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler looks at task priority, available time, completion status, and due dates when creating a schedule. High-priority tasks are considered first because I wanted important activities like feeding and medication to be less likely to get skipped.

I also made sure the scheduler doesn't add more tasks than the owner's available time allows. Once the tasks are selected, they can be displayed in order by time.

**b. Tradeoffs**

One tradeoff I made was keeping conflict detection simple. The scheduler can tell when two tasks overlap, but it doesn't automatically change their times.

I decided this was reasonable because I wanted to focus on getting the main features working first. Automatically moving tasks around would make the code more complicated, and I would need to consider the owner's preferences more carefully.

---

## 3. AI Collaboration

**a. How you used AI**

I used ChatGPT to help me throughout the project. It helped me plan my classes, create the UML diagram, write Python methods, and come up with tests.

The most helpful part was being able to ask questions about specific problems while I worked in VS Code. I also used separate conversations for different phases, which made it easier to focus on one part of the project at a time.

I found that asking AI for specific code changes and explanations was more helpful than just asking it to build the entire application at once.

**b. Judgment and verification**

One design decision I focused on was keeping the scheduling logic separate from the pet and owner information. I didn't want everything to be handled by one large class because that would make the program harder to understand.

I also kept conflict detection as a warning instead of trying to automatically rearrange tasks. I thought that would be easier to test and more realistic for the amount of time I had.

I didn't just rely on the AI-generated code. I ran the program in the terminal, tested it in Streamlit, and used pytest to check whether the main features were working.

---

## 4. Testing and Verification

**a. What I tested**

I tested adding tasks, completing tasks, sorting by time, filtering by pet and status, and scheduling tasks for multiple pets.

I also tested edge cases, like pets with no tasks, tasks scheduled at the same time, and owners who don't have enough time to complete everything.

Another important thing I tested was recurrence. I made sure daily and weekly tasks created a new task with the correct next due date.

All 12 of my Phase 5 automated tests passed.

**b. Confidence**

I would rate my confidence in my program a 4 out of 5. I think the main features work well because I tested them using both the terminal and automated tests.

There are still things I could improve, especially how the scheduler handles overlapping tasks. If I had more time, I would test larger schedules with more pets and different types of recurring tasks.

---

## 5. Reflection

**a. What went well**

The part I'm most satisfied with is getting the Python classes and Streamlit app to work together. At first, I was mainly focused on understanding how the classes should connect, but by the end I had a working application that could manage pets and create schedules.

I also liked seeing the tests pass because it showed that the code was doing what I expected.

**b. What you would improve**

If I had more time, I would improve the way the app handles scheduling conflicts. Instead of only showing a warning, I would want it to suggest another available time.

I would also add permanent data storage so owners wouldn't lose their pets and tasks when their Streamlit session ends.

**c. Key takeaway**

The biggest thing I learned was that building an app is easier when I break it into smaller parts instead of trying to do everything at once.

Using AI helped me work faster, but I still had to make decisions about how the system should work, review the code, and test the results. I learned that being the lead architect means understanding the design and making sure everything works together instead of just accepting whatever code AI generates.
