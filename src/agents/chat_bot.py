from core.agent import Agent
from core.events.chat_event_adapter import ChatEventAdapter
from core.events.default_event_handler import DefaultEventHandler
from hugchat.login import Login
from hugchat import hugchat

sign = Login("gamec11123@chosenx.com", "n;>;V6?*fq]VWx9")
cookies = sign.login(cookie_dir_path="./cookies/", save_cookies=True)
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

def ask(question):
    message_result = chatbot.chat(question)
    return message_result.wait_until_done()[:150].encode('cp437', errors='replace').decode('cp437', errors='replace')

class CustomEventHandler(DefaultEventHandler):
    def handle_chat_event(self, event: ChatEventAdapter, agent: Agent):
        agent.message(ask(event.get_data()))

def create_agent():
    return Agent("ChatBot", None, CustomEventHandler())
