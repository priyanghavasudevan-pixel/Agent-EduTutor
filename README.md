\## Project Overview - Agent EduTutor

This project contains the core logic for Agent EduTutor, a multi-agent
system designed to assist students preparing for competitive exams and
academic courses. The agent is built using Google Agent Development Kit
(ADK) and follows a modular architecture. Agent EduTutor is not a
monolithic application but an ecosystem of specialized agents, each
responsible for a different aspect of the learning process. These
sub-agents automate the most time-consuming and critical components of
modern learning: collecting study materials, building personalized
pathways, delivering real-time tutoring, and providing actionable
performance feedback.

![](media/image1.jpeg){width="5.451340769903762in"
height="7.384241032370953in"}

\### Problem Statement

Students preparing for competitive exams and academic courses face
challenges such as fragmented access to study materials, lack of
personalized learning pathways, and limited real-time support. These
issues result in inefficiencies that reduce learning outcomes and
increase frustration and dropout risks. Manual searching and organizing
of educational resources is exhausting and difficult to scale with
growing content demands.

\### Solution Statement

Agent EduTutor leverages autonomous agents to gather, curate, and
personalize diverse educational content dynamically, adapting to each
student\'s pace, preferences, and performance. It offers real-time
interactive tutoring and instant feedback, reducing repetitive tasks for
educators and enabling timely student interventions. This multi-agent
system facilitates hyper-personalized and engaging learning experiences,
transforming education into an efficient, accessible, and
student-centered process.

\### Architecture

At the core is the \`education-agent\`, a multi-agent system designed
with modular components to manage different stages of the learning and
tutoring workflow. Developed using Google Agent Development Kit (ADK),
this architecture supports scalability and robustness through
specialized sub-agents.

![](media/image2.png){width="6.414583333333334in" height="4.1875in"}

The central orchestrator is the main education-agent, which coordinates
the following sub-agents:

\- \`material_collector.py\`: Aggregates and updates study materials
relevant to student needs.

\- \`pathway_builder.py\`: Constructs personalized study pathways and
plans.

\- \`tutoring_agent.py\`: Facilitates interactive tutoring sessions with
real-time feedback.

\- \`feedback_agent.py\`: Captures and integrates user feedback to
refine learning pathways.

Supporting files include \`\_\_init\_\_.py\` for package initialization
and auxiliary modules for tools and configuration.

\### Value Statement

Agent EduTutor reduces student time spent searching for materials by
centralizing and customizing resources. It improves learning
effectiveness via adaptive tutoring and continuous feedback, fostering
deeper comprehension and retention. By automating routine educational
functions and supporting educators, it creates a manageable, engaging
learning journey geared toward higher exam readiness and academic
success.

\### Installation

The project is compatible with Python 3.11.3.

It is recommended to create a virtual environment (e.g., with \`venv\`).

Install dependencies via:

\`\`\`

pip install -r requirements.txt

\`\`\`

\### Running the Agent in ADK Web Mode

From the project root directory, run:

\`\`\`

adk web

\`\`\`

To execute integration tests, run:

\`\`\`

python -m tests.test_agent

\`\`\`

\### Project Structure

\- \`education_agent/\`: Main package for the agent.

\- \`agent.py\`: Defines the main education-agent and orchestrates
sub-agents.

\- \`sub_agents/\`: Contains sub-agent modules:

\- \`\_\_init\_\_.py\`: Initializes the sub-agents package.

\- \`material_collector.py\`: Gathers and updates educational content.

\- \`pathway_builder.py\`: Builds personalized study plans.

\- \`tutoring_agent.py\`: Delivers interactive tutoring sessions.

\- \`feedback_agent.py\`: Manages user feedback to improve plans.

\- \`study_planner.py\`: Generates personalized study outlines.

\- \`study_tutor.py\`: Executes tutoring interactions.

\- \`tools.py\`: Defines custom tools utilized by agents.

\- \`config.py\`: Houses agent configuration including model settings.

\- \`eval/\`: Contains evaluation framework components.

\- \`tests/\`: Holds integration tests for the agent system.

\### Workflow

The \`education-agent\` operates in the following sequence:

\- Analyze Student Profile (Optional): Evaluate student strengths,
weaknesses, and preferences.

\- Plan: Delegate study plan creation to \`pathway_builder\`.

\- Refine: Incorporate user feedback via \`feedback_agent\` to adjust
plans.

\- Curate Content: Collect targeted materials using
\`material_collector\`.

\- Tutor: Conduct tutoring sessions with \`tutoring_agent\`, providing
real-time feedback.

\- Monitor: Track student progress and recommend plan updates.

\- Export: Summarize learning achievements with downloadable reports and
materials.
