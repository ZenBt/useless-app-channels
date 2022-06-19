import json
import random
from time import sleep

from channels.generic.websocket import WebsocketConsumer

from .constants import DURANTION

class NumbersConsmer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
        for i in range(DURANTION):
            num = random.randint(1, 100)
            self.send(json.dumps({'num': num}))
            sleep()