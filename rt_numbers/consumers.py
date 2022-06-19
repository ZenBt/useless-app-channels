import json
import random
from time import sleep

from channels.generic.websocket import WebsocketConsumer

from .constants import DURATION

class NumbersConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
        for i in range(DURATION):
            num = random.randint(1, 100)
            self.send(json.dumps({'num': num}))
            sleep(1)