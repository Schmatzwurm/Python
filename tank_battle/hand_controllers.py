import pygame
import time

pygame.init()

class HandControllers:
    def __init__(self):
        pygame.joystick.init()
        self._controllers = dict()
        self._callback = None
        self._clock = pygame.Clock()

    def register_callback(self, callback):
        self._callback = callback


    def get_count(self):
        return len(self._controllers)
    
    def vibrate(self, id):
        vibrated = False
        ctlr = self._controllers[id]
        if ctlr is not None:
            if ctlr.rumble(0, 0.7, 500):
                return True
            
    def poll(self):
        done = False
        for event in pygame.event.get():
            if event.type == pygame.JOYDEVICEADDED:
                ctlr = pygame.joystick.Joystick(event.device_index)
                self._controllers[ctlr.get_instance_id()] = ctlr
                print(f"Joystick {ctlr.get_instance_id()} connencted")
            if event.type == pygame.JOYDEVICEREMOVED:
                del self._controllers[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    self._callback(event.instance_id, 'A')
                elif event.button == 1:
                    self._callback(event.instance_id, 'B')
                elif event.button == 3:
                    self._callback(event.instance_id, 'X')
                elif event.button == 4:
                    self._callback(event.instance_id, 'Y')
                elif event.button == 6:
                    self._callback(event.instance_id, 'LB')
                elif event.button == 7:
                    self._callback(event.instance_id, 'RB')
                else:
                    self._callback(event.instance_id, '?')
            elif event.type == pygame.JOYAXISMOTION:
                delta_time = self._clock.get_time()
                if delta_time > 200:
                    if event.axis == 5:
                        self._callback(event.instance_id, 'LT')
                    elif event.axis == 4:
                        self._callback(event.instance_id, 'RT')
            if event.type == pygame.QUIT:
                done = True
            
            self._clock.tick()
        return done


if __name__ == "__main__":
    import time

    hc = HandControllers()

    def test_handler(index, event):
        print("Event {} from controller {} received".format(event, index))
        hc.vibrate(index)

    hc.register_callback(test_handler)

    while True:
        if hc.poll():
            pass
        time.sleep(0.1)
     

