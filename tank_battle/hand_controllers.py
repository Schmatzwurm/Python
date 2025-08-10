import pygame

class HandControllers:
    def __init__(self):
        pygame.joystick.init()
        self._controllers = {}
        self._callbacks = {}
        for index in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(index)
            self._controllers[index] = joystick


    def register_callback(self, controller, event, callback):
        key = (controller, event)
        self._callbacks[key] = callback


    def get_count(self):
        return len(self._controllers)


    def poll(self):
        for (index, controller) in self._controllers:
            if controller.get_button(0):
                callback = self._callbacks.get((index, 'A'))
                if callback is not None:
                    callback(index, 'A')


if __name__ == "__main__":
    hc = HandControllers()
    print("Detected {} controllers".format(hc.get_count()))

