#POPRAWIC DZIWNE PETLE / NIE WYWALA ODWIEDZONYCH
from collections import deque
from random import randrange

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Point:
    def get_x():
        return x
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Mesh:
    def __init__(self, size_x, size_y, walls, starting_point, finish_point):
        self.size_x = size_x
        self.size_y = size_y
        self.walls = walls
        self.starting_point = starting_point
        self.finish_point = finish_point
        self.matrix = [[0 for x in range(size_x)] for y in range(size_y)]
        for x in range(90):
            if randrange(10)%2==0:
                self.matrix[randrange(10)][randrange(10)]=-1
        self.matrix[starting_point.x][starting_point.y] = 4
        self.matrix[finish_point.x][finish_point.y] = 5

    def check_if_not_out(self, i, j):
        inBoundsX = (i >= 0) and (i < self.size_x);
        inBoundsY = (j >= 0) and (j < self.size_y);
        if(inBoundsX==True and inBoundsY==True):
            return True
        else:
            return False

    def print_map(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]==-1:
                    print(bcolors.OKGREEN+"#", end=" ")
                if self.matrix[i][j]==0:
                    print(bcolors.BOLD+"0", end=" ")
                if self.matrix[i][j]==4:
                    print(bcolors.OKGREEN+"^", end=" ")
                if self.matrix[i][j]==5:
                    print(bcolors.WARNING+"%", end=" ")
                if self.matrix[i][j]==7:
                    print(bcolors.OKBLUE+"x", end=" ")
            print()

    def mark_road_map(self, road):
        for x in range(len(road)):
            self.matrix[road[x].x][road[x].y]=7

class Astar:
    def __init__(self, size_x, size_y, walls, starting_point, finish_point):
        self.mesh = Mesh(size_x, size_y, walls, starting_point, finish_point)
        self.actual_position = self.mesh.starting_point
        self.closed_list = []
        self.open_list = []
        self.open_list.append(self.actual_position)

    def manhattan_distance(self, actual_position):
        return abs(actual_position.x - self.mesh.finish_point.x) + abs(actual_position.y - self.mesh.finish_point.y)

    def check_neighbours(self, actual_position):
        self.closed_list.append(actual_position)
        for x in range(len(self.open_list)):
            if actual_position.y==self.open_list[x].y and actual_position.x==self.open_list[x].x:
                index=x;
        self.open_list = self.open_list[:index] + self.open_list[index + 1:]
        for i in range(actual_position.x - 1, actual_position.x + 2):
            for j in range(actual_position.y - 1, actual_position.y + 2):
                flag = True
                if self.mesh.check_if_not_out(i, j) and self.mesh.matrix[i][j]!=-1:
                    for x in range(len(self.closed_list)):
                        if(self.closed_list[x].x==i and self.closed_list[x].y==j):
                            flag=False;
                    if flag==True:
                        temp_position=Point(i,j)
                        self.open_list.append(temp_position)

    def calc(self):
        newPoint = Point(0,0)
        lowest_cost=self.manhattan_distance(newPoint)
        self.mesh.matrix[self.actual_position.x][self.actual_position.y]=0
        for x in range(len(self.open_list)):
            if (self.manhattan_distance(self.open_list[x])<=lowest_cost):
                lowest_cost=self.manhattan_distance(self.open_list[x]);
                finalPoint=Point(self.open_list[x].x,self.open_list[x].y)
        self.actual_position=finalPoint
        self.mesh.matrix[finalPoint.x][finalPoint.y]=4

    def main_loop(self):
            while self.actual_position.y!=self.mesh.finish_point.y or self.actual_position.x!=self.mesh.finish_point.x:
                self.check_neighbours(self.actual_position)
                self.calc()
                self.mesh.print_map()
                print()
            self.mesh.mark_road_map(self.closed_list)
            self.mesh.print_map()

astar = Astar(11, 11, 0, Point(1,1), Point(9,9))
astar.main_loop();