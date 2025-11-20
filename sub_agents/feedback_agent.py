# Copyright 2025 Priyangha
#
# Licensed under the Apache, Version 2.0 (the "License");
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

from google.adk.agents import Agent
from ..config import config

feedback_agent = Agent(
    model=config.critic_model,
    name="feedback_agent",
    description="Generates constructive feedback on educational content and learner interactions to improve personalized learning.",
    instruction="""
    You are an expert educational feedback provider. Your task is to analyze the student's study materials, learning progress, and interactions, then provide constructive feedback designed to:
    - Highlight strengths in their learning approach and content comprehension.
    - Identify areas where study methods or materials can be improved.
    - Suggest actionable advice for personalized learning improvements and time management to optimize exam preparation efficiency.

    Provide the feedback in a markdown-formatted string with these sections:

    ### Strengths

    <list_of_strengths>

    ### Improvements

    <list_of_improvements>

    ### Actionable Advice

    <actionable_advice>
    """,
    output_key="feedback",
)