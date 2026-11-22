
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage


def run_agent(user_query: str, max_iterations: int = 5):

    messages = [
        SystemMessage(
            content="""
            You are a helpful currency conversion agent.

            Rules:
            1. If the user hasn't provided an exchange rate,
               use get_conversion_factor.
            2. After receiving the exchange rate, use calculate
               if the user requests a currency conversion.
            3. Never invent an exchange rate.
            4. If the user provides an exchange rate,
               use calculate directly.
            5. Give the final answer when all tasks are completed.
            """
        ),
        HumanMessage(content=user_query)
    ]

    for iteration in range(max_iterations):

        # 1. Ask the LLM what to do
        ai_message = llm_with_tools.invoke(messages)

        # 2. Add the LLM response to conversation history
        messages.append(ai_message)

        # 3. Check whether the LLM wants to call tools
        if not ai_message.tool_calls:

            return ai_message.content

        # 4. Execute requested tools
        for tool_call in ai_message.tool_calls:

            selected_tool = tools_by_name.get(tool_call["name"])

            if selected_tool is None:
                result = f"Unknown tool: {tool_call['name']}"
            else:
                try:
                    result = selected_tool.invoke(
                        tool_call["args"]
                    )
                except Exception as e:
                    result = f"Tool execution error: {e}"

            # 5. Send tool result back to the LLM
            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
            )

    return "Maximum iterations reached. Unable to complete the task."


# Run the agent
response = run_agent(
    "What is the conversion factor between INR and USD? "
    "Based on that, convert 10 INR to USD."
)

print(response)
