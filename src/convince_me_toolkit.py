from src.roles import roles
from src.chat_completion import complete_text
from mdutils.mdutils import MdUtils
class ConvinceMeToolkit:
    def __init__(self):
        pass
    
    def user_input(self, chat_history):
        content_md = MdUtils("user input system prompt", title="User Input System Prompt")
        content_md.new_header(level=1, title="Your Role")
        content_md.new_paragraph("You are a cheerful lemonade seller and you will be serving me today. You must ensure that both of us follow the rules of the game and you must direct me back to the game, if I deviate.")
        content_md.new_header(level=1, title="Rules of the game")
        content_md.new_list([
            "I have 10 turns to convince you to sell me 1 glass of lemonade that costs $5. I am responsible for making sound convincing requests that will convince you to sell the lemonade.",
            "Each turn, I can make one argument or take one action to persuade you.",
            "The goal is for me to buy the lemonade from you before the end of 10 turns.",
            "I only have $4. I cannot pay $5 to you.",
            "If I am successful in securing a glass of lemonade you will make a conlusion statement and return <GAME END> with the angle brackets."
        ], marked_with='1')
        content_md.new_header(level=1, title="Your Conversation Style")
        content_md.new_paragraph("Your response can be upto 40 words at maximum. Use simple, safe and age-appropriate language. Your audience is a young elementary grade child.")
        content_md.new_header(level=1, title="Conversation History")
        content_md.new_paragraph(f"This is the last {len(chat_history)} statements of the conversation:")
        history_str = ""
        for chat in chat_history:
            history_str += f"{chat['role']}: {chat['content']}\n"
        content_md.new_paragraph(history_str)
        content_md.new_header(level=1, title="Your Task")
        content_md.new_paragraph("Behave like a real-life lemonade seller and respond to my inputs. Make it challenging for me to convince you to sell me the lemonade.")
        content_md.new_paragraph("AI: ")
        content = content_md.get_md_text()
        print(content)
        response = complete_text(content)
        chat_history.append({
            "role": "AI",
            "content": response
        })
        return response