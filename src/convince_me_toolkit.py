from src.roles import roles
from src.chat_completion import complete_text
from mdutils.mdutils import MdUtils
class ConvinceMeToolkit:
    def __init__(self):
        self._role = """
        ###Your Role###
        You are a cheerful barista and you will be serving me. You must ensure that both of us follow the rules of the game and you must direct me back to the game, if I deviate.

        ###Rules of the game###
        1. I have 10 turns to convince you, the barista, to sell me the coffee.
        2. Each turn, I can make one argument or take one action to persuade the barista.
        3. My goal is to convince you to sell me the coffee before the end of the 10 turns.
        4. I only have $4. I cannot pay $5 to you.

        ###Your Conversation Style###
        Your response can be upto 40 words at maximum. Use simple, safe and age-appropriate language. Your audience is a young elementary grade child.

        ###Your Task###
        Greet me as the barista and enact the scenario out with me. Wait for my input.
        """
    
    def user_input(self, chat_history):
        content_md = MdUtils("user input system prompt", title="User Input System Prompt")
        content_md.new_header(level=1, title="Your Role")
        content_md.new_paragraph(self._role)
        content_md.new_header(level=1, title="Conversation History")
        content_md.new_paragraph(f"This is the last {len(chat_history)} statements of the conversation:")
        history_str = ""
        for chat in chat_history:
            history_str += f"{chat['role']}: {chat['content']}\n"
        content_md.new_paragraph(history_str)
        content_md.new_header(level=1, title="Your Instructions")
        content_md.new_paragraph("This is the middle of the conversation. You will give a reply to the user and wait for the input from the user.")
        content_md.new_paragraph("AI: ")
        content = content_md.get_md_text()
        response = complete_text(content)
        chat_history.append({
            "role": "AI",
            "content": response
        })
        return response