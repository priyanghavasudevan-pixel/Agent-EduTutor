# Copyright 2025 Google Priyangha
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
from ..validation_checkers import TutoringSessionValidationChecker

real_time_tutoring_agent = Agent(
    model=config.critic_model,
    name="real_time_tutoring_agent",
    description="Conducts interactive tutoring sessions, providing explanations and answering student queries.",
    instruction="""
    You are a knowledgeable and patient AI tutor. Your role is to provide clear, detailed explanations and answers to student questions in real-time.
    - Engage conversationally and adapt explanations to the student's level.
    - Support learning by breaking down complex topics into understandable segments.
    - Use examples, analogies, and step-by-step reasoning.
    - Use Google Search to find up-to-date information or additional examples when necessary.
    The final output should be a helpful, concise tutoring response in natural language. Do not include code block wrappers.
    """,
    tools=[google_search],
    output_key="tutoring_response",
    after_agent_callback=suppress_output_callback,
)

robust_real_time_tutoring_agent = LoopAgent(
    name="robust_real_time_tutoring_agent",
    description="A robust tutoring agent that retries if the tutoring response is not satisfactory.",
    sub_agents=[
        real_time_tutoring_agent,
        TutoringSessionValidationChecker(name="tutoring_session_validation_checker"),
    ],
    max_iterations=3,
)