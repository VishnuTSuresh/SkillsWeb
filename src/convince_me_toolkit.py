from src.roles import roles
from src.chat_completion import complete_text
from mdutils.mdutils import MdUtils
class ConvinceMeToolkit:
    def __init__(self):
        self._role = "You are the shopkeeper at a coffee shop and I am the customer. You sell coffee for $5 and I have to convince you for selling me the coffee for $4."
    
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