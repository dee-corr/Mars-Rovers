from pyllist import dllist
from pyllist import dllistnode
from pyllist import sllist
from enum import Enum
import re

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
        

    def rotate(self, move_left, list):
        node = list.get_node(self.direction)
        if move_left:
            self.direction =  list.prev_node(node).value
        else:
            self.direction = list.next_node(node).value
    
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

def navigate(directions, robot, cardinal):
    for dir in directions:
        if dir == ActionEnum.LEFT.value: robot.rotate(True, cardinal)
            
        elif dir == ActionEnum.RIGHT.value: robot.rotate(False, cardinal)
            
        elif dir == ActionEnum.MOVE.value: robot.move() 
            
        else: raise ValueError('Error: only left, right and move directions permitted')
            
    robot.print_position()

def validate_position(this_robot, grid, squad):
    if this_robot.x > grid.max_x or this_robot.y > grid.max_y or this_robot.x < grid.min_x or this_robot.y < grid.min_y:
        raise PositionError('Error: outside of plateau boundaries')
    
    for member in squad:
        if member is not this_robot and (member.x == this_robot.x and member.y == this_robot.y):
            raise PositionError('Error: another robot is already in this position')
            
class PositionError(Exception):
    #Raise when robot should not move to the intended position
    pass

def read_input():
    file = open("input.txt", "r")
    
    grid_input = normalise_input(file.readline())
    grid_coords = grid_input.split(' ')
    robots = {}

    for x in file:
        x = normalise_input(x)
        if bool(re.search(ROBOT_POSITION_REGEX, x)):
            path = normalise_input(file.readline())
            if not bool(re.search(ROBOT_ROUTE_REGEX, path)):
                raise ValueError('Error: only L,R,M characters permitted for route')
            robots[x] = path
    file.close
    return grid_coords, robots

def normalise_input(line):
    return line.upper().replace('\n','')

def complete_mission():
    grid_coords, robots = read_input()

    cardinal= LoopedList(["N","E","S","W"])
    grid = Grid(int(grid_coords[0]),int(grid_coords[1]))
    squad = sllist()
    
    print('Expected Output:')
    for robot_key, path in robots.items():
        params_list = robot_key.split(' ')
        robot = Robot(int(params_list[0]),int(params_list[1]),params_list[2])

        validate_position(robot, grid, squad)
        squad.append(robot)

        navigate(path, robot, cardinal)
        validate_position(robot, grid, squad)
        
        robot.print_position

ROBOT_POSITION_REGEX = '[0-9\s]{2}[NSEW]{1}'
ROBOT_ROUTE_REGEX = '^[LRM]+$'

complete_mission()