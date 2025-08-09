import unittest

from tank_battle import throwing_path as tp

class ThrowingPathTest(unittest.TestCase):

    def test_x_pos_no_start(self):
        tp1 = tp.ThrowingPath(0, (2,0))
        pos = tp1.get_pos(0.001)
        self.assertAlmostEqual(2, pos[0], 2)


    def test_y_pos_no_start(self):
        tp1 = tp.ThrowingPath(0, (0,2))
        pos = tp1.get_pos(0.001)
        self.assertAlmostEqual(2, pos[1], 2)


    def test_x_pos_with_start(self):
        tp1 = tp.ThrowingPath(0, (0,2))
        tp1.start(20)
        pos = tp1.get_pos(0.02)
        self.assertAlmostEqual(0.4, pos[0], 2)

    def test_y_pos_with_start(self):
        tp1 = tp.ThrowingPath(0, (0,10))
        tp1.start(20)
        pos = tp1.get_pos(0.6)
        self.assertAlmostEqual(8.23, pos[1], 2)

