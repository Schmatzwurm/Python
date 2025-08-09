import time
import math

class ThrowingPath:

    def __init__(self, angle, start_pos, min_pos=(0,0), max_pos=(1000, 1000)):
        self.angle = angle
        self.start_pos = start_pos
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.start_time = None
        self.velocity = [0, 0]
        self.gravity = 9.81  # Gravity constant


    def start(self, velocity):
        self.start_time = time.time()
        self.velocity[0] = velocity * math.cos(self.angle)
        self.velocity[1] = velocity * math.sin(self.angle)


    def get_pos(self, elapsed_time):
        if self.velocity is None:
            return self.start_pos

        return (self.get_x_pos(elapsed_time), self.get_y_pos(elapsed_time))

    
    def get_x_pos(self, elapsed_time):
        pos = self.velocity[0] * elapsed_time + self.start_pos[0]

        return max(self.min_pos[0], min(self.max_pos[0], pos))


    def get_y_pos(self, elapsed_time):
        pos = -0.5 * self.gravity * math.pow(elapsed_time, 2) + self.velocity[1] * elapsed_time + self.start_pos[1]
    
        return max(self.min_pos[1], min(self.max_pos[1], pos))