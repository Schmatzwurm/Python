import unittest

from tank_battle.physics import throwing_path

class ThrowingPathTest(unittest.TestCase):

    def test_x_pos_angle0(self):
        tp1 = throwing_path.ThrowingPath()
        tp1.throw(20, 0, (10, 0))
        pos = tp1.get_pos(0.1)
        self.assertAlmostEqual(12, pos[0], 2)


    def test_y_pos_angle0(self):
        tp1 = throwing_path.ThrowingPath()
        tp1.throw(1, 0, (0, 10))
        pos = tp1.get_pos(1)
        self.assertAlmostEqual(5.1, pos[1], 1)


    def test_x_pos_angle45(self):
        tp1 = throwing_path.ThrowingPath()
        tp1.throw(2, 45, (0, 0))
        pos = tp1.get_pos(0.2)
        self.assertAlmostEqual(0.21, pos[0], 2)

    def test_y_pos_angle45(self):
        tp1 = throwing_path.ThrowingPath()
        tp1.throw(2, 45, (0, 10))
        pos = tp1.get_pos(1)
        self.assertAlmostEqual(6.8, pos[1], 2)

