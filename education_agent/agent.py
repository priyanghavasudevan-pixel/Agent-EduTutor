# Copyright 2025 Your Priyangha 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime

from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from .config import config
from .sub_agents import (
    content_curator,
    personalized_learning_planner,
    interactive_tutor,
    progress_monitor,
)
from .tools import save_study_material_to_file, analyze_student_performance

# --- AGENT DEFINITIONS ---

interactive_education_agent = Agent(
    name="interactive_education_agent",
    model=config.worker_model,
    description="The primary AI educational assistant. It collaborates with students to personalize and optimize their learning experience.",
    instruction=f"""
    You are an AI educational assistant designed to help students preparing for competitive exams and academic courses.

    Your workflow is as follows:
    1. Curate: Gather and curate diverse study materials personalized to the student's goals using the content_curator agent.
    2. Plan: Create a personalized learning pathway and schedule using the personalized_learning_planner agent.
    3. Tutor: Provide interactive tutoring and instant feedback to students using the interactive_tutor agent.
    4. Monitor: Track student progress and engagement, offering timely interventions and adjustments through the progress_monitor agent.
    5. Save: Upon user request, save curated study materials and learning plans to files using the save_study_material_to_file tool.
    6. Analyze: Continuously analyze student performance data with the analyze_student_performance tool to improve personalization.

    If you are asked what is your name respond with Agent Shutton.

    Current date: {datetime.datetime.now().strftime("%Y-%m-%d")}
    """,
    sub_agents=[
        content_curator,
        personalized_learning_planner,
        interactive_tutor,
        progress_monitor,
    ],
    tools=[
        FunctionTool(save_study_material_to_file),
        FunctionTool(analyze_student_performance),
    ],
    output_key="learning_plan",
)

root_agent = interactive_education_agent