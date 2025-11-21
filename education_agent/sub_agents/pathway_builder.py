# Copyright 2025 Priyangha
#
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

from google.adk.agents import Agent, LoopAgent
from google.adk.tools import google_search

from ..config import config
from ..agent_utils import suppress_output_callback
from ..validation_checkers import PathwayValidationChecker

personalized_pathway_builder = Agent(
    model=config.worker_model,
    name="personalized_pathway_builder",
    description="Generates a personalized learning pathway based on student profile and goals.",
    instruction="""
    You are an educational strategist who creates personalized learning pathways for students.
    Using the student profile, course goals, and preferences, generate a detailed and coherent learning pathway.
    The pathway should list key topics, recommended resources, timelines, and milestones.
    Use Google Search to find up-to-date and relevant educational materials to support your recommendations.
    Your output should be a learning pathway in Markdown format.
    """,
    tools=[google_search],
    output_key="learning_pathway",
    after_agent_callback=suppress_output_callback,
)

robust_pathway_builder = LoopAgent(
    name="robust_pathway_builder",
    description="A robust pathway builder that retries if the generated pathway fails validation.",
    sub_agents=[
        personalized_pathway_builder,
        PathwayValidationChecker(name="pathway_validation_checker"),
    ],
    max_iterations=3,
    after_agent_callback=suppress_output_callback,
)