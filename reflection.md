# PawPal+ Project Reflection

## 1. System Design
The three main things I want users to be able to do are add their pets, make tasks for them, and see a daily schedule. For example, someone could add their dog, set up feeding and walking times, and see what they need to get done that day.

**a. Initial design**

For my UML diagram, I connected the classes based on how they would work in the app. One owner can have multiple pets, and each pet can have different tasks. I made the Scheduler its own class because I thought it would be easier to manage the scheduling part separately instead of putting everything into one class.

**b. Design changes**

After looking over my design, I realized it made more sense to have each pet keep track of its own tasks instead of having the Owner class handle everything. This way, if someone has more than one pet, their tasks won't all be mixed together.

I also decided to keep the Scheduler separate because it will have to handle things like sorting tasks and checking for scheduling conflicts. I think this will make the code easier to work with when I start adding more features later.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

For this phase, I worked on making the scheduling system smarter by adding sorting, filtering, recurring tasks, and conflict detection. I used AI to help figure out how to organize the methods and how to use Python's sorted function with lambda.

One tradeoff I made was keeping the conflict detection pretty simple. The program checks whether task times overlap and gives a warning, but it doesn't automatically move the tasks around to fix the conflict. I decided to keep it this way because I wanted the code to be easier to understand and test. A more advanced scheduler could automatically reschedule tasks, but that would add more complexity.

I also kept the sorting method simple by sorting the time strings in HH format. This works because the times are stored consistently in 24-hour format. I think this was a good choice for now since it gets the job done without adding unnecessary code.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
