import random
import sys

sys.setrecursionlimit(1993)  # recursion limit set to 1993 for larger mazes


class Cell:  # class that will be used to link cells between each other
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.linked_cells = []


class Maze:
    def __init__(self, height, width):
        self.height = height  # Height of the maze
        self.width = width  # Width of the maze
        self.scalex = 0  # Scale of the x parameter
        self.scaley = 0  # Scale of the y parameter
        self.centrx = 0  # Scale of centerx
        self.centry = 0  # Scale of centery

        # Makes a 2D array filled with cell objects
        self.maze = [[Cell(x, y) for x in range(self.width)] for y in range(self.height)]  
        # gets random cordinate for x
        self.current_x = random.randint(0, self.width - 1)  
        # gets random cordinate for y
        self.current_y = random.randint(0, self.height - 1)
        # array that will be used for the backtracking of the algorithm
        self.backtracking = [[self.current_x, self.current_y]]
        # array that describes which coordinates have been visited
        self.visited_cells = [[self.current_x, self.current_y]]
        self.create_maze()

    # get_neighbor function gets all the neighbors of the current cell
    def get_neighbor(self):
        # make an array for all the neighbors
        self.all_neighbors_coords = []

        #check if coordinate is not out of the maze's boundaries
        if (self.current_x + 1 < self.width):
            # gets neighbor cordinate at the right
            neighbor_right_coords = [self.current_x + 1, self.current_y]  
            # appends right neighbor cordinates into list
            self.all_neighbors_coords.append(neighbor_right_coords)  
        
        #check if coordinate is not out of the maze's boundaries
        if (self.current_x - 1 >= 0):
            # gets neighbor cordinate at the left
            neighbor_left_coords = [self.current_x - 1, self.current_y]  
            # appends left neighbor cordinate into list
            self.all_neighbors_coords.append(neighbor_left_coords)  
        
        #check if coordinate is not out of the maze's boundaries
        if (self.current_y + 1 < self.height):
            # gets neighbor cordinate at the top
            neighbor_top_coords = [self.current_x, self.current_y + 1]  
            # appends top neighbor cordinate into list
            self.all_neighbors_coords.append(neighbor_top_coords)  
        
        #check if coordinate is not out of the maze's boundaries
        if (self.current_y - 1 >= 0):
            # gets neighbor cordinate at the bottom
            neighbor_bot_coords = [self.current_x, self.current_y - 1]  
            # appends bottom neighbor cordinates into list
            self.all_neighbors_coords.append(neighbor_bot_coords)  
        
        return self.all_neighbors_coords  # returns the list of all neighbors

    # create_maze function generates random maze
    def create_maze(self):
        while len(self.backtracking) != 0:
            # goes through list in reverse
            self.current_x, self.current_y = self.backtracking[-1]

            # asigns coords values of x and y
            coords = [self.current_x, self.current_y]  

            # gets all the neighbors of the coords
            self.all_neighbors_coords = (self.get_neighbor())  
            
            #use list comperhension to check for the 
            #neighbors that have not been visited
            unvisited_cells = ([self.all_neighbors_coords[i] for i,v in enumerate(self.all_neighbors_coords) if v not in self.visited_cells])

            # checks if the length of unvisited cells is 0
            if (len(unvisited_cells) == 0):
                self.backtracking.pop(len(self.backtracking) - 1)

            else:
                # pick a random unvisited neighbor from the unvisited_cells
                random_neighbor = random.choice(unvisited_cells)

                # link the initial cordinate with its neighbor
                self.maze[coords[1]][coords[0]].linked_cells.append(random_neighbor)  

                # link the neighbor with its initial cordinate
                self.maze[random_neighbor[1]][random_neighbor[0]].linked_cells.append(coords)

                # add the random neighbor to visited cells
                self.visited_cells.append(random_neighbor)

                # add the random neighbor to backtracking 
                self.backtracking.append(random_neighbor)
            self.create_maze()
        else:
            return
            

    def draw_square(self, canvas, x, y, color, outline=""):
        """
        This function is used to draw the start and end point as well as the
        path to the correct scale depending on the size of the window        
        """
        canvas.create_rectangle(
            x * self.scalex + self.centrx,
            y * self.scaley + self.centry,
            x * self.scalex + self.scalex + self.centrx,
            y * self.scaley + self.scaley + self.centry,
            outline=outline,
            fill=color,
        )

    def draw_walls(self, canvas):
        """
        This function checks where the walls should be placed and places them
        with the correct scale calculations
        """
        for y in range(self.height):
            for x in range(self.width):
                wall_position = []
                for i in self.maze[y][x].linked_cells:
                    wall_position.append([x - i[0], y - i[1]])

                if [0, 1] not in wall_position:  # Walls to the top
                    canvas.create_rectangle(
                        x * self.scalex + self.centrx,
                        y * self.scaley + self.centry,
                        x * self.scalex + self.scalex + self.centrx,
                        y * self.scaley + 10 + self.centry,
                        outline="#121212",
                        fill="#202528",
                    )

                if [0, -1] not in wall_position:  # Walls to the bottom
                    canvas.create_rectangle(
                        x * self.scalex + self.centrx,
                        y * self.scaley + self.scaley + self.centry,
                        x * self.scalex + self.scalex + self.centrx,
                        y * self.scaley - 10 + self.scaley + self.centry,
                        outline="#121212",
                        fill="#202528",
                    )

                if [1, 0] not in wall_position:  # Walls for the left
                    canvas.create_rectangle(
                        x * self.scalex + self.centrx,
                        y * self.scaley + self.centry,
                        x * self.scalex + 10 + self.centrx,
                        y * self.scaley + self.scaley + self.centry,
                        outline="#121212",
                        fill="#202528",
                    )

                if [-1, 0] not in wall_position:  # Walls for the right
                    canvas.create_rectangle(
                        x * self.scalex + self.scalex + self.centrx,
                        y * self.scaley + self.centry,
                        x * self.scalex - 10 + self.scalex + self.centrx,
                        y * self.scaley + self.scaley + self.centry,
                        fill="#202528",
                    )

    def update_scale(self, width, height):
        # Keeps size as a square so it resizes the maze to the min version of the canvases width and height
        keep_cube = min(width, height)
        # Changes the width depending on the new dimension
        self.scalex = (keep_cube / self.width)
        # Changes the height depending on the new dimension
        self.scaley = (keep_cube / self.height)
        # Changes CENTRY depending on scale
        self.centry = (height / 2 - (self.height * self.scaley) / 2)
        # Changes CENTERX depending on scale
        self.centrx = (width / 2 - (self.width * self.scalex) / 2)
