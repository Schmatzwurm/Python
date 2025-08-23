from .base_object import BaseObject

class Grenade(BaseObject):
    def __init__(self, screen):
        super().__init__(screen, 'cannon_ball.png')