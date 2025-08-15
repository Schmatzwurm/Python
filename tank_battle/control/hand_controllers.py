import pygame
import time

pygame.init()

class HandControllers:

    MAPPINGS = {
        "Xbox 360 Controller":
        {
            'buttons': {
                0: 'A',
                1: 'B',
                2: 'X',
                3: 'Y',
                4: 'LB',
                5: 'RB',
                6: 'BACK',
                7: 'START',
                8: 'M',
                9: 'S2',
                10: 'S1',
            },
            'axes': {
                0: 'LSX',
                1: 'LSY',
                2: 'LT',
                3: 'RSX',
                4: 'RSY',
                5: 'RT',
                6: '6',
                7: '7'
            }
        }
    }

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
            if ctlr.rumble(10, 10, 100):
                vibrated = True
        return vibrated


    def poll(self):
        done = False
        for event in pygame.event.get():
            if event.type == pygame.JOYDEVICEADDED:
                ctlr = pygame.joystick.Joystick(event.device_index)
                instance_id = ctlr.get_instance_id()
                name = ctlr.get_name()
                self._controllers[instance_id] = ctlr
            if event.type == pygame.JOYDEVICEREMOVED:
                del self._controllers[event.instance_id]
            elif event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYAXISMOTION:
                ctlr = self._controllers[event.instance_id]
                dev_name = ctlr.get_name()
                mapping = self.MAPPINGS[dev_name]
                event_name = None
                if event.type == pygame.JOYBUTTONDOWN:
                    event_name = mapping['buttons'][event.button]
                elif event.type == pygame.JOYAXISMOTION:
                    elapsed_time = self._clock.get_time()
                    if elapsed_time > 200:
                        event_name = mapping['axes'][event.axis]
                if event_name is not None:
                    self._callback(event.instance_id, event_name)
            elif event.type == pygame.QUIT:
                done = True
            self._clock.tick()
        return done


if __name__ == "__main__":
    import time

    hc = HandControllers()

    def test_handler(index, event):
        print("Event {} from controller {} received".format(event, index))
        #hc.vibrate(index)

    hc.register_callback(test_handler)

    try:
        while True:
            if hc.poll():
                pass
            time.sleep(0.1)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")

    pygame.joystick.quit()
     

