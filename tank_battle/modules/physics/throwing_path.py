import time
import math

class ThrowingPath:

    def __init__(self, min_pos=(0,0), max_pos=(100, 100), invert_x=False, invert_y=False):
        self._invert_x = invert_x
        self._invert_y = invert_y
        self._angle = 0
        self._start_time = None
        self._min_pos = min_pos
        self._max_pos = max_pos
        self._start_pos = [0, 0]
        self._velocity = [0, 0]
        self._velocity_factor = 2
        self._gravity = 9.81  # Gravity constant


    def reset(self):
        self._start_time = None
        self._start_pos = [0, 0]
        self._velocity = [0, 0]


    def throw(self, velocity, angle, start_pos):
        self._start_time = time.time()
        self._angle = angle
        self._start_pos = start_pos
        self._velocity[0] = velocity * self._velocity_factor * math.cos(self._angle)
        self._velocity[1] = velocity * self._velocity_factor * math.sin(self._angle)


    def update_and_get(self):
        if self._start_time is None:
            return self._start_pos
        current_time = time.time()
        elapsed_time = current_time - self._start_time
        return self.get_pos(elapsed_time)
    

    def get_pos(self, elapsed_time):
        if self._velocity is None:
            return self._start_pos

        x_pos = self.get_x_pos(elapsed_time)
        y_pos = self.get_y_pos(elapsed_time)

        if (x_pos == self._min_pos[0] or x_pos == self._max_pos[0] or
            y_pos == self._min_pos[1] or y_pos == self._max_pos[1]):
            return None

        return (x_pos, y_pos)

    
    def get_x_pos(self, elapsed_time):
        factor = -1 if self._invert_x else 1
        pos = (factor * self._velocity[0] * elapsed_time) + self._start_pos[0]

        return max(self._min_pos[0], min(self._max_pos[0], pos))


    def get_y_pos(self, elapsed_time):
        factor = -1 if self._invert_y else 1
        pos = (factor * (-0.5 * self._gravity * math.pow(elapsed_time, 2) + self._velocity[1] * elapsed_time)) + self._start_pos[1]
    
        return max(self._min_pos[1], min(self._max_pos[1], pos))