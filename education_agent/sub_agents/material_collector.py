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

from google.adk.agents import Agent

from ..config import config
from ..agent_utils import suppress_output_callback

study_material_editor = Agent(
    model=config.critic_model,
    name="study_material_editor",
    description="Edits personalized study material content based on student feedback.",
    instruction="""
    You are a professional educational content editor. You will be given study material and student feedback.
    Your task is to edit and improve the study material according to the feedback.
    The final output should be revised study material tailored to student learning needs.
    """,
    output_key="study_material",
    after_agent_callback=suppress_output_callback,
)