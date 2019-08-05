from pyllist import dllist
from pyllist import dllistnode
from pyllist import sllist
from enum import Enum

class CardinalEnum(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"
        
class ActionEnum(Enum):
    LEFT = "L"
    RIGHT = "R"
    MOVE = "M"

class LoopedList(dllist):
    def __init__(self, list):
        dllist.__init__(self, list)
        
    def next_node(self, node):
        return self.first if node.next is None else node.next
        
    def prev_node(self, node):
        return self.last if node.prev is None else node.prev
    
    def get_node(self, node_value):
        for i in super().iternodes():
            if i.value == node_value: return i
        raise ValueError('Error: node doesnt exist')

class Robot():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        
    def print_position(self):
        print(("{} {} "+ self.direction).format(self.x, self.y))
        

    def rotate(self, move_left):
        node = cardinal.get_node(self.direction)
        if move_left:
            self.direction =  cardinal.prev_node(node).value
        else:
            self.direction = cardinal.next_node(node).value
    
    def move(self):
        if self.direction == CardinalEnum.NORTH.value: self.y += 1
            
        elif self.direction == CardinalEnum.SOUTH.value: self.y -= 1
            
        elif self.direction == CardinalEnum.EAST.value: self.x += 1
            
        elif self.direction == CardinalEnum.WEST.value: self.x -= 1
            
        else: raise ValueError('Error: direction is not a cardinal value')

class Grid():
    def __init__(self, max_x, max_y):
        self.min_x = 0
        self.min_y = 0
        self.max_x = max_x
        self.max_y = max_y

def navigate(directions, robot):
    for dir in directions:
        if dir == ActionEnum.LEFT.value: robot.rotate(True)
            
        elif dir == ActionEnum.RIGHT.value: robot.rotate(False)
            
        elif dir == ActionEnum.MOVE.value:
            validate_position(robot)
            robot.move()
            
        else: raise ValueError('Error: only left, right and move directions permitted')
            
    robot.print_position()

def validate_position(this_robot):
    if this_robot.x > grid.max_x or this_robot.y > grid.max_y or this_robot.x < grid.min_x or this_robot.y < grid.min_y:
        raise PositionError('Error: outside of plateau boundaries')
    
    for member in squad:
        if member is not this_robot and (member.x == this_robot.x and member.y == this_robot.y):
            raise PositionError('Error: another robot is already in this position')
            
class PositionError(Exception):
    #Raise when robot should not move to the intended position
    pass

def AddRobot(x, y, direction):
    robot = Robot(x, y, direction)
    validate_position(robot)
    squad.append(robot)
    robot.print_position()
    return robot

def begin_mission():
    robot1 = AddRobot(1,2,"N")
    robot2 = AddRobot(3,3,"E")
    
    navigate('LMLMLMLMM',robot1)   
    navigate('MMRMMRMRRM',robot2)

cardinal = LoopedList(["N","E","S","W"])
grid = Grid(5,5)
squad = sllist()

#begin_mission()