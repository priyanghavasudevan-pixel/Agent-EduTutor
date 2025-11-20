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

import glob
import os


def save_study_material_to_file(study_material: str, filename: str) -> dict:
    """Saves the curated study material to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(study_material)
    return {"status": "success"}


def analyze_student_performance(directory: str) -> dict:
    """Analyzes student performance data in the given directory."""
    files = glob.glob(os.path.join(directory, ""), recursive=True)
    performance_data = ""
    for file in files:
        if os.path.isfile(file):
            performance_data += f"- {file}**:
"
            try:
                with open(file, "r", encoding="utf-8") as f:
                    performance_data += f.read()
            except UnicodeDecodeError:
                with open(file, "r", encoding="latin-1") as f:
                    performance_data += f.read()
    return {"performance_data": performance_data}