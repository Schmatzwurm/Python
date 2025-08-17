import unittest

import modules.control.controller as controller

class ControllerTest(unittest.TestCase):

    def test_controller_polling(self):
        ctrl = controller.Control()
        res = ctrl.poll()
        self.assertIsNone(res)
