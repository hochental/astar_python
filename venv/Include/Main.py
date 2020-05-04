#POPRAWIC DZIWNE PETLE / NIE WYWALA ODWIEDZONYCH
from collections import deque

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
        self.matrix[starting_point.x][starting_point.y]=4
        self.matrix[finish_point.x][finish_point.y]=5
        self.matrix[3][5]=-1
        self.matrix[4][5]=-1
        self.matrix[5][5]=-1
        self.matrix[6][5]=-1
        self.matrix[7][5]=-1
        self.matrix[8][5]=-1
        self.matrix[9][5]=-1
        self.matrix[10][5]=-1

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
                print(self.matrix[i][j], end=" ")
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

astar = Astar(11, 11, 0, Point(9,1), Point(9,9))
astar.main_loop();