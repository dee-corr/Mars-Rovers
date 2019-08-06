import unittest
import robotsmars
from pyllist import sllist
from pyllist import dllist
from pyllist import dllistnode

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNavigation))
    suite.addTest(unittest.makeSuite(TestPosition))
    return suite

class TestNavigation(unittest.TestCase):

    def setUp(self):
        self.cardinal = robotsmars.LoopedList(["N","E","S","W"])
        self.grid = robotsmars.Grid(5,5)
        self.squad = dllist()
        
    def tearDown(self):
        super(TestNavigation, self).tearDown()
        self.squad is None

    def test_navigate_loop_right(self):
        self.robot = robotsmars.Robot(1,2,"W")
        self.nav("R")
        self.assertEqual(self.robot.direction, "N")

    def test_navigate_loop_left(self):
        self.robot = robotsmars.Robot(1,1,"N")
        self.nav("L")
        self.assertEqual(self.robot.direction, "W")

    def test_navigate_move(self):
        self.robot = robotsmars.Robot(4,4,"S")
        self.squad.append(self.robot)
        self.nav("M")
        self.assertEqual(self.robot.x, 4)
        self.assertEqual(self.robot.y, 3)
                
        self.robot.direction = "W"
        self.squad.append(self.robot)
        self.nav("M")
        self.assertEqual(self.robot.x, 3)
        self.assertEqual(self.robot.y, 3)

        self.robot.direction = "N"
        self.squad.append(self.robot)
        self.nav("M")
        self.assertEqual(self.robot.x, 3)
        self.assertEqual(self.robot.y, 4)

        self.robot.direction = "E"
        self.squad.append(self.robot)
        self.nav("M")
        self.assertEqual(self.robot.x, 4)
        self.assertEqual(self.robot.y, 4)

    def nav(self, action):
        robotsmars.navigate(action, self.robot, self.cardinal)

class TestPosition(unittest.TestCase):

    def setUp(self):
        self.cardinal = robotsmars.LoopedList(["N","E","S","W"])
        self.grid = robotsmars.Grid(5,5)
        self.squad = dllist()
        
    def tearDown(self):
        super(TestPosition, self).tearDown()
        self.squad is None
    
    def test_validate_initial_position_out_of_boundary_x(self):
        self.robot = robotsmars.Robot(6,5,"W")
        self.assertRaises(robotsmars.PositionError, robotsmars.validate_position, self.robot, self.grid, self.squad)

    def test_validate_initial_position_out_of_boundary_y(self):
        self.robot = robotsmars.Robot(5,6,"W")
        self.assertRaises(robotsmars.PositionError, robotsmars.validate_position, self.robot, self.grid, self.squad)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())