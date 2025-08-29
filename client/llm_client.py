import json, os, asyncio
import google.generativeai as genai
from dotenv import load_dotenv
from fastmcp import Client

load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

MCP_SERVER_URL = "http://localhost:8080/mcp"

# -----------Step 1: MCP tool call wrapper -----------

async def call_mcp_tool(session, tool_name: str, args: dict):
    """
    """
    url = f"{MCP_SERVER_URL}/{tool_name}"
    try:
        async with session.post(url, json=args, timeout=30) as resp:
            data = await resp.json()
            return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ----------Step 2: Gemini Client ------------

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini_for_plan(test_case: str) -> list:
    plan_prompt = f"""
    You are a planner. Covert the following test case into a JSON array of steps.

    Rules:
    - Respond with only valid JSON.
    - Do not include extra text, commentary or markdown fences.
    - If a step does not contain any arguments then return None for that step.
    - Each step must be one of . ["launch_page", "enter_text", "click", "close_browser"]

    Example:
    [
        {{"action": "launch_page", "args": {{"url": "https://example.com", "browser": "edge"}}}},
        {{"action": "enter_text", "args": {{"locator_type": "name", "locator_value": "q", "text": "python mcp"}}}}
    ]

    Test case:
    {test_case}
    """

    response = model.generate_content(plan_prompt)

    # print raw output 
    print(f"Raw Gemini output: {response.text}")

    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        print(f"Gemini did not return valid JSON")
        return []
    
async def run_test_case(test_case: str):
    plan = ask_gemini_for_plan(test_case)
    print(f"Gemini Plan: \n {json.dumps(plan, indent=2)}")

    async with Client(MCP_SERVER_URL) as client:
        for step in plan:
            action = step["action"]
            args = step.get("args", {})

            print(f"\n Executing {action} {args}")
            result = await client.call_tool(action, args)
            print(f"Result: {result}")

if __name__ == "__main__":
    test_case = """
    Step 1: Launch https://www.google.com in chrome browser.
    Step 2: Enter `value` `python mcp test` in search box name='q'.
    Step 3: Click on Google Search button name='btnK'.
    Step 4: Close the browser.
    """
    asyncio.run(run_test_case(test_case))