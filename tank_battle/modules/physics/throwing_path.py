import time
import math

class ThrowingPath:

    def __init__(self, min_pos=(0,0), max_pos=(1000, 1000)):
        self.angle = 0
        self.start_time = None
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.start_pos = [0, 0]
        self.velocity = [0, 0]
        self.gravity = 9.81  # Gravity constant


    def throw(self, velocity, angle, start_pos):
        self.start_time = time.time()
        self.angle = angle
        self.start_pos = start_pos
        self.velocity[0] = velocity * math.cos(self.angle)
        self.velocity[1] = velocity * math.sin(self.angle)


    def update_and_get(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time()
        return self.get_pos(elapsed_time)
    

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