import unittest
from src.robotsmars import *
from pyllist import sllist
from pyllist import dllist
from pyllist import dllistnode

cardinal = robotsmars.LoopedList(["N","E","S","W"])
grid = robotsmars.Grid(5,5)
squad = sllist()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNavigation))
    suite.addTest(unittest.makeSuite(TestPosition))
    return suite

class TestNavigation(unittest.TestCase):

    def tearDown(self):
        super(TestNavigation, self).tearDown()
        robotsmars.squad is None

    def test_navigate_loop_right(self):
        robot = robotsmars.AddRobot(1,2,"W")
        robotsmars.navigate("R", robot)
        self.assertEqual(robot.direction, "N")

    def test_navigate_loop_left(self):
        robot = robotsmars.AddRobot(1,1,"N")
        robotsmars.navigate("L", robot)
        self.assertEqual(robot.direction, "W")

    def test_navigate_move(self):
        robot = robotsmars.AddRobot(4,4,"S")
        robotsmars.navigate("M", robot)
        self.assertEqual(robot.x, 4)
        self.assertEqual(robot.y, 3)
        
        robot.direction = "W"
        robotsmars.navigate("M", robot)
        self.assertEqual(robot.x, 3)
        self.assertEqual(robot.y, 3)

        robot.direction = "N"
        robotsmars.navigate("M", robot)
        self.assertEqual(robot.x, 3)
        self.assertEqual(robot.y, 4)

        robot.direction = "E"
        robotsmars.navigate("M", robot)
        self.assertEqual(robot.x, 4)
        self.assertEqual(robot.y, 4)

class TestPosition(unittest.TestCase):

    def tearDown(self):
        #super(TestPosition, self).tearDown()
        #robot is None
        squad is None
    
    def test_validate_initial_position_out_of_boundary_x(self):
        self.assertRaises(robotsmars.PositionError, robotsmars.AddRobot,6,5,"W")

    def test_validate_initial_position_out_of_boundary_y(self):
        self.assertRaises(robotsmars.PositionError, robotsmars.AddRobot,5,6,"W")

    def test_validate_position_after_move_max_x(self):
        robot = robotsmars.AddRobot(5,5,"E")
        self.assertRaises(robotsmars.PositionError, robotsmars.navigate,"M", robot)
    
    def test_validate_position_after_move_max_y(self):
        robot = robotsmars.AddRobot(5,5,"N")
        self.assertRaises(robotsmars.PositionError, robotsmars.navigate,"M", robot)

    def test_validate_position_after_move_min_x(self):
        robot = robotsmars.AddRobot(0,0,"S")
        self.assertRaises(robotsmars.PositionError, robotsmars.navigate,"M", robot)
    
    def test_validate_position_after_move_min_y(self):
        robot = robotsmars.AddRobot(0,0,"W")
        self.assertRaises(robotsmars.PositionError, robotsmars.navigate,"M", robot)


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())