# Education Agent Tests

This directory contains integration tests for the `education-agent` system.

## How to Run

You can run the test from the root of the project using the following command:

```bash
python -m tests.test_education_agent
```

## Test Scenario

The `test_education_agent.py` script is an integration test that runs the education agents (e.g., `feedback_agent`) through a predefined sequence of student queries. This test is designed to simulate a typical conversation with the agent(s) and ensure that they can handle the flow without errors.


The script will print the agent's responses to the console for each query in the sequence, allowing you to verify the feedback and interaction quality.
