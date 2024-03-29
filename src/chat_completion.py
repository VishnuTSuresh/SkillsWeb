import os
from src.roles import roles
from openai import OpenAI
import json

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def rate_consolation(character, chat_history):
    # Step 1: send the conversation and available functions to the model

    chat_history_str = ""
    for chat in chat_history:
        chat_history_str += f"{chat['role']}: {chat['content']}\n"
    messages = [{"role": "system", "content": f"""
    You are the AI. you represent:
    {roles[int(character)-1]}.
                 
    The User is trying to console you. You will give a rating from 1 to 10 as to how well the User is doing in consoling you. The rating should be based on the whole conversation.
    
    This is the conversation history so far:
    {chat_history_str}
    """}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_consolation_rating",
                "description": "Rate how well the user is consoling you",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rating": {
                            "type": "string",
                            "description": "The rating from 1 to 10",
                        }
                    },
                    "required": ["rating"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        tools=tools,
        temperature=0,
        tool_choice={"type": "function", "function": {"name": "get_consolation_rating"}},
    )
    rating = int(json.loads(response.choices[0].message.tool_calls[0].function.arguments)["rating"])
    return rating

def complete_text(input_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": input_text
            }
        ]
    )
    response_content = response.choices[0].message.content
    return response_content

def rate_convincing(chat_history):
    # Step 1: send the conversation and available functions to the model

    chat_history_str = ""
    for chat in chat_history:
        chat_history_str += f"{chat['role']}: {chat['content']}\n"
    messages = [{"role": "system", "content": f"""
    You are the shopkeeper at a coffee shop and I am the customer. You sell coffee for $5 and I have to convince you for selling me the coffee for $4. Within 10 turns, I have to convince you to sell the coffee to me. 
    
    This is the conversation history so far:
    {chat_history_str}
    """}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_convincing_rating",
                "description": "Rate how well the user is convincing you",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rating": {
                            "type": "string",
                            "description": "The rating from 1 to 10",
                        },
                        "convinced": {
                            "type": "boolean",
                            "description": "Whether you are convinced or not",
                        }
                    },
                    "required": ["rating", "convinced"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        tools=tools,
        temperature=0,
        tool_choice={"type": "function", "function": {"name": "get_convincing_rating"}},
    )
    arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)
    rating = int(arguments["rating"])
    convinced = bool(arguments["convinced"])
    return rating, convinced