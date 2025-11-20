import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from agents.feedback_agent import feedback_agent
from google.genai import types as genai_types


async def main():
    """Runs the feedback agent with a sample sequence of student queries."""
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name="education_app", user_id="test_user", session_id="test_session"
    )
    runner = Runner(
        agent=feedback_agent, app_name="education_app", session_service=session_service
    )

    queries = [
        "I am struggling with time management in my UPSC preparation. How can I improve?",
        "My understanding of Indian Polity is good but I often forget key facts. Suggestions?",
        "I need advice on mastering current affairs for IB ACIO exams.",
        "How can I retain environment science concepts better?",
        "Do you have tips for improving concentration during study sessions?"
    ]

    for query in queries:
        print(f">>> {query}")
        async for event in runner.run_async(
            user_id="test_user",
            session_id="test_session",
            new_message=genai_types.Content(
                role="user",
                parts=[genai_types.Part.from_text(text=query)]
            ),
        ):
            if event.is_final_response() and event.content and event.content.parts:
                print(event.content.parts[0].text)


if name == "main":
    asyncio.run(main())