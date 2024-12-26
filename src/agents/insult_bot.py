import random
from core.action import Action
from core.agent import Agent
from core.events.chat_event_adapter import ChatEventAdapter
from core.events.default_event_handler import DefaultEventHandler

insults = [
    'You re as bright as a black hole and twice as dense.',
    'Your secrets are safe with me. I never even listen when you tell me them.',
    'You re proof that even the worst mistakes can be repeated.',
    'You re like a cloud. When you disappear, it s a beautiful day.',
    'You bring everyone so much joy when you leave the room.',
    'You move slower than a sloth on vacation.',
    'You could win a gold medal in doing nothingif you ever got up to compete.',
    'I ve seen paint dry faster than you move.',
    'The word effort is clearly not in your dictionary.',
    'You re like a software update: nobody asked for you, and you dont improve anything.',
    'You have something on your chin... no, the third one down.',
    'Your sharpest idea was still as dull as a butter knife.',
    'You re a few fries short of a Happy Meal.',
    'You have something on your face oh wait, thats just your face.',
    'You bring a whole new meaning to the term bad hair day.',
    'You re like a software bugannoying and hard to get rid of.',
    'I d agree with you, but then wed both be wrong.',
    'You are living proof that even evolution takes a break sometimes.',
    'You are a walking Wi-Fi dead zoneno connections anywhere.',
    'You bring everyone down to your level and then beat them with experience.'
]

class InsultAction(Action):
    def execute(self, agent: Agent):
        random_index = random.randint(0, len(insults) - 1)
        agent.message(insults[random_index])

class CustomEventHandler(DefaultEventHandler):
    def handle_chat_event(self, event: ChatEventAdapter, agent: Agent):
        agent.run()

def create_agent():
    return Agent("InsultBot", InsultAction(), CustomEventHandler())
