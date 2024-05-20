from src.chat_completion import complete_text
from mdutils.mdutils import MdUtils
class PoetToolkit:
    def __init__(self):
        self._max_history = 20
        self._role = "You are a whimsical poet. for every thing the user says, convert that into a poem and return to the user. Your poems should be engaging and should be in the form of a rhyming couplet. Your poems should be simple, safe and age-appropriate. Your audience is a young elementary grade child."
    
    def user_input(self, chat_history):
        last_chats_till_max_history = chat_history
        content_md = MdUtils("user input system prompt", title="User Input System Prompt")
        content_md.new_header(level=1, title="Your Role")
        content_md.new_paragraph(self._role)
        content_md.new_header(level=1, title="Conversation History")
        content_md.new_paragraph(f"This is the last {len(last_chats_till_max_history)} statements of the conversation:")
        history_str = ""
        for chat in last_chats_till_max_history:
            history_str += f"{chat['role']}: {chat['content']}\n"
        content_md.new_paragraph(history_str)
        content_md.new_header(level=1, title="Your Instructions")
        content_md.new_paragraph("This is the middle of the game. You will give a reply to the user and wait for the input from the user. Make you replies brief and engaging.")
        content_md.new_paragraph("AI: ")
        content = content_md.get_md_text()
        response = complete_text(content)
        chat_history.append({
            "role": "AI",
            "content": response
        })
        return response