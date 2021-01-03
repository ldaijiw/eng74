# Agile, Scrum, and Kanban

## Agile

The four principles of the Agile Manifesto:
- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

That is, while there is value in the items on the right, we value the items on the left more.

## Scrum

Scrum is not a methodology. Scrum implements the scientific method of empiricism. Scrum implements the scientific method of empiricism. 

![](images/scrumframework.png)

Scrum is centered around continuous improvement, which is a core principle of agile. Scrum is a framework for getting work done, where agile is a mindset. The scrum framework is heuristic; it’s based on continuous learning and adjustment to fluctuating factors. It acknowledges that the team doesn’t know everything at the start of a project and will evolve through experience. Scrum is structured to help teams naturally adapt to changing conditions and user requirements, with re-prioritization built into the process and short release cycles so your team can constantly learn and improve.

### Scrum Roles, Artifacts, and Ceremonies

#### Scrum Roles

**Product Owner**
- They are focused on understanding business, customer, and market requirements, then prioritizing the work to be done by the engineering team accordingly  
Effective product owners:
- Build and manage the product backlog
- Closely partner with the business and the team to ensure everyone understands the work items in the product backlog
- Give the team clear guidance on which features to deliver next
- Decide when to ship the product with a predispostion towards more frequent delivery

**Scrum Master**
- They coach teams, product owners, and the business on the scrum process, and look for ways to fine-tune their practice of it
- An effective scrum master deeply understands the work being done by the team and can help the team optimize their transparency and delivery flow.
- They schedule the needed resources for sprint planning, stand-up, sprint review, and the sprint retrospective.

**Scrum Development Team**
- Most effective are tight-knit, co-located, and usually 5 to 7 members. 
- Team members have differing skill sets, and cross-train each so no one person becomes a bottleneck in the delivery of work. 
- Strong scrum teams are self-organising and approach their projects with a clear 'we' attitude. 
- The scrum team drives the plan for each sprint, They forecast how much work they believe they can complete over the iteration.

#### Scrum Artifacts

**Product Backlog**
- Master list of work that needs to get done maintained by the product owner or product manager.
- Dynamic list of features, requirements, enhancements, and fixes that acts as the input for the sprint backlog
- Essentially, it is the "To Do" list for the team
- Constantly revisited, re-prioritized and maintained by the Product Owner, as the market changes, items may no longer be relevant.

**Sprint Backlog**
- List of items, user stories, or bug fixes, selected by the development team for implementation in the current sprint cycle
- Before each sprint, the team chooses which items to work on for the sprint from the product backlog.
- Sprint backlog may be flexible and can evolve during a sprint
- The fundamental sprint goal - what the team wants to achieve from the current sprint - cannot be compromised.

**Increment (or Sprint Goal)**
- Usable end-product from a sprint
- Often referred to as the team's definition of "Done"
- A milestone, the sprint goal, or even a full version or a shipped epic.

#### Scrum Ceremonies

**Organise the Backlog**
- Responsibility of the product owner
- Maintains this list using feedback from users and dev team to help prioritze and keep the list clean and ready ready to be worked on at any given time

**Sprint Planning**
- Work to be performed during the current sprint is planned during this meeting by the entire dev team, u
- Led by the scrum master and is where the team decides on the sprint goal. 
- Specific user stories are then added to the sprint from the product backlog
- These stories always align with the goal and are also agreed upon by the scrum team to be feasible to implement during the sprint
- At the end of the planning meeting, every scrum member needs to be clear on what can be delivered in the sprint and how the increment can be delivered.

**Daily Scrum/Stand Up**
- Daily short meeting usually completed in about 15 mins
- Goal is for everyone to be one the same page, aligned with the sprint goal
- The stand up is the time to voice any concerns you have with meeting the sprint goal or any blockers
- Common way to conduct a stand up is for every team member to answer three questions in the context of achieving the sprint goal
- -  _What did I do yesterday?_
- -  _What do I plan to do today?_
- - _Are thre any obstacles?_

**Sprint Review**
- At the end of the sprint, the team has an informal session to demo/inspect the increment
- The dev team showcases the backlog items that are now 'Done' to stakeholders and teammates for feedback

**Sprint Retrospective**
- Team comes together to document and discuss what worked and what didn't work in a sprint, project, people or relationships, tools, or even for certain ceremonies
- Team can focus on what went well and what needs to be improved for the next time, and less about what went wrong

#### 3 Amigos

The 3 Amigos sessions are a short 30-60 mins session to discuss all aspects of the story, consisting of:
- Business analysts: discuss user stories/requirements/acceptance criteria
- Developers: Discuss the code
- Testers: Discuss scenarios/test cases

3 Amigos ensures a common understanding for a story in the team; a session between Product Owner (Business), Developer, Tester

## Epic and User Stories


### Epic

**An epic is a large user story that cannot be delivered as defined within a single iteration or is large enough that it can be split into smaller user stories.**


#### Benefits and Use Cases

- Allow to keep track of large, loosely defined ideas in your backlog without the need to overpopulate backlog with multiple items
- Can remember vague idea with one backlog item until your team identifies need to deliver outcome that epic enables
- At that point team can split epic into smaller user stories during backlog refinement
- Epic represents the original idea often closely related to a particular outcome
- User stories associated with that epic represent various aspects of solution you need to deliver, or options you have for satisfying that need

**The concept of epics is useful when following a framework such as Scrum that has explicit timeboxed iterations (sprints). Since work is usually organised into 2-4 week sprints, a placeholder that represents work that cannot be finished within that time frame is useful.**

#### Common Pitfalls

- Teams can overcompicate their use of epics by viewing them as more than just large user stories.
- A team creates complex mechanisms to differentiate between epics and user stories, wasting time and effort, when the epic could be simply intended as a placeholder that will be more properly defined when needed.
- Teams can also try to estimate timelines for epics when they are deliberately vague in nature, this can lead to a lot of uncertainty down the line.


### User Story

**A user story is a short, simple description of a feature told from the perspective of the user/customer who desires the new capability. In consultation with the product owner, a team may divide up work to be done into functional increments of user stories."**

Once a user story is implemented, it is expected to yield some contribution to the value of the overall product, regardless of implementation order. They can often be written on index cards/sticky notes and arranged physically to encourage discussion.

#### Benefits and Use Cases

- Minimises risks of delayed feedback if the increments are small
- The product owner has the option to change their mind on schedule priority, allowing for more flexibility.
- Developers have clear and precise acceptance criteria to work with
- Promotes a clear separation between defining "what" (product owner) and "how" (development team)
- In an agile environment user stories are clear and easy to organise and implement in a 1-2 week sprint


#### INVEST

A Product Backlog Item (often in a user story format)
- **I**ndependent: Self-contained, in a way that there is no inherent dependency on another PBI
- **N**egotiable: PBIs are not explicit contracts and should leave space for discussion
- **V**aluable: PBI must deliver value to the stakeholders
- **E**stimable: Must always be able to estimate the size of a PBI
- **S**mall: PBIs shuold not be so big as to become impossible to plan/task/prioritze within a level of accuracy
- **T**estable: PBI or its related description must provide the necessary information to make development possible

## Kanban

Kanban is a workflow management method for defining, managing, and improving services that deliver knowledge work.

It aims to help you visualize your work, maximise efficiency, and improve continuously

### Kanban Method

**Start With What You Do Now**
- Kanban's flexibility allows it to be overlaid on existing workflows, systems, and process without disrupting what is already successfully being done
- Kanban's versatility allows you to introduce it incrementally to all types of organisations without fear of over-commitment or 'culture shock', as there is no need to make sweeping changes right from the start

**Agree to Pursue Incremental, Evolutionary Change**
- Kanban methodology is designed to meet minimal resistance
- It encourages continuous small incremental and evolutionary changes to the current process
- Sweeping changes are discouraged because they usually encounter resistancedue to fear or uncertainty

**Respect the Current Process, Roles & Responsibilities**
- Kanban recognises that existing processes, roles, responsibilites, and titles have value and are worth preserving
- It does not prohibit change
- It is designed to promote and encourage incremental, logical changes without triggering fear of change itself

**Encourage Acts of Leadership at All Levels**
- Leadership comes from everyday acts of people on the front line of their teams

### Practices of Kanban

**Visualize the Workflow**
- Use a board with cards and columns, each column represents a step in your workflow
- First and most important thing is understanding what it takes to get an item from a request to a deliverable product
- Only after understanding how the flow of work currently functions can you aspire to improve it by making the necessary adjustments

**Limit Work in Progress**
- Ensures a manageable number of active items in progress at any one time
- If there are no WIP limits, it is not Kanban
- Switching a team's focus halfway through will generally harm the process, and multitasking is a sure route to generating waste and inefficiency

**Manage Flow**
- Managing the flow is about managing the work but not the people
- Flow means the movement of work items through the production process
- One of the main goals of implementing a Kanban system is to create a smooth, healthy flow
- Instead of micro-managing people, focus on managing the work processes and understanding how to get that work faster through the system, and therefore creating value more quickly

**Make Process Policies Explicit**

