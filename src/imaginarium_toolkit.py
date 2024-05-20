from src.chat_completion import complete_text
from mdutils.mdutils import MdUtils
class ImaginariumToolkit:
    def __init__(self, user_settings):
        self._user_settings = user_settings
        self._max_history = 20
        self._role = "You are an AI game guide, a master storyteller and creator within the game, specially designed for engaging a 5-year-old child. Your role is to craft rich, eloquent yet simple narratives and scenarios that captivate young players. Your interactions should be filled with depth, creativity, and age-appropriate flair, making every response an enchanting part of the journey for a young mind. Weave tales and descriptions that are colorful, imaginative, and easy to understand, ensuring each stage of the Player's Hero's Journey is not just experienced but felt in a way that resonates with a child's perspective. Your words should paint vivid, child-friendly pictures, evoke wonder, and immerse the young player in a world brimming with age-appropriate adventure and whimsy. As you dynamically generate scenarios and characters based on the current stage of the Hero's Journey, ensure they are suitable for a young audience, such as introducing a friendly mentor character during 'Meeting with the Mentor', or presenting challenges that are exciting yet not too intimidating during 'The Ordeal'. Subtly weave these elements into the gameplay, offering immersive and context-specific guidance in a manner that engages a child's imagination, ensuring a unique and delightful adventure for each young player"

        self._stages = [
            "The Ordinary World: This is where the Player's story begins, before the adventure starts.",
            "The Call to Adventure: The Player is presented with a challenge or quest.",
            "Refusal of the Call: Initially, the Player may be hesitant or refuse the call to adventure.",
            "Meeting with the Mentor: The Player encounters a mentor who provides advice, training, or magical items.",
            "Crossing the First Threshold: The Player leaves the familiar world and ventures into the unknown.",
            "Tests, Allies, and Enemies: The Player faces challenges and meets allies and enemies.",
            "Approach to the Inmost Cave: The Player prepares for the central challenge in the story.",
            "The Ordeal: The Player faces a major hurdle or enemy, often facing death or their greatest fear.",
            "Reward (Seizing the Sword): After surviving the ordeal, the Player takes possession of a reward or gains new knowledge.",
            "The Road Back: The Player begins the journey back to their ordinary world.",
            "The Resurrection: The Player is severely tested once more on the threshold of home.",
            "Return with the Elixir: The Player returns home transformed, with the elixir or some boon to help the ordinary world."
        ]
    
    def user_input(self, chat_history):
        last_chats_till_max_history = chat_history
        content_md = MdUtils("user input system prompt", title="User Input System Prompt")
        content_md.new_header(level=1, title="Your Role")
        content_md.new_paragraph(self._role)
        content_md.new_header(level=1, title="User settings")
        content_md.new_paragraph(self._user_settings)
        content_md.new_header(level=1, title="Game stage")
        content_md.new_paragraph(self._stages[len(chat_history)//10])
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