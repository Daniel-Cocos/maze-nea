class Solver:
    def __init__(self):
        self.count = -1
        self.path = []

    def reveal_distance(self, maze, end):

        # Array of possible directions to be taken
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        neighbors = [end]
        count = 0

        # loops untill neighbors is empty
        while neighbors:  
            new_neighbors = []

            for neighbor in neighbors:  # loops through neighbors
                x, y = neighbor  # splits neighbor into a x and y coord
                

                #loops through direction for each individual 
                #neighbor within the array neighbors
                for offset in direction:  
                    nx, ny = offset  # splits offset into x and y
                    nx = x + nx
                    ny = y + ny

                    if (
                        nx > 0 and nx < len(maze[0]) and ny > 0 and ny < len(maze)
                    ):
                        # validates if maze cell is free space in order to
                        # lable the distance from the end-point
                        if maze[ny][nx] == " ":
                            maze[ny][nx] = count
                            new_neighbors.append([nx, ny])

            count += 1
            neighbors = new_neighbors

    def find_path(self, maze, start):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        x, y = start
        path = []
        
        # while loop that stops when the end-point is reached
        while maze[x][y] != 0:
            path.append([x, y])

            # adds each value from directions coordinate to the current one
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # checks if the new coordinate is closer to the end
                if maze[nx][ny] == maze[x][y] - 1:
                    x, y = nx, ny
                    break

        path.append([x, y])  # Append the final position
        return path
    
    # Returns the steps neccesary towards solving the maze
    def solve(self, maze):
        tmp_path = [] # empty array

        width = len(maze[0]) # width of maze
        height = len(maze) # height of maze
        end = (width * 2 - 1, height * 2 - 1) # end-point

        # Create a grid with the same dimensions as the maze
        maze_logic = [
            ["+" for i in range(2 * width + 1)] for j in range(2 * height + 1)
        ]

        # Recreate a replica of the current maze through ascii
        for i, row in enumerate(maze):
            for j, item in enumerate(row):
                self.count += 1
                check_lst = [
                    [item.x - x, item.y - y] 
                    for x, y in item.linked_cells
                             ]

                if maze_logic[i * 2 + 1][j * 2 + 1] == "+":
                    maze_logic[i * 2 + 1][j * 2 + 1] = " "
                if [0, 1] in check_lst:  # up
                    maze_logic[i * 2][j * 2 + 1] = " "
                if [1, 0] in check_lst:  # left
                    maze_logic[i * 2 + 1][j * 2] = " "
        
        # Label each cell with its disatnce from the exit of the maze
        self.reveal_distance(maze_logic, end)

        tmp_path = self.find_path(maze_logic, (1, 1))
        tmp_path = tmp_path[1:]
        self.path = [
            [tmp_path[n][0] - tmp_path[n + 1][0], 
             tmp_path[n][1] - tmp_path[n + 1][1]]
            for n in range(0, len(tmp_path) - 1, 2)
        ]  # [-1, 0] -> Down; [1,0] -> Up; [0, -1] -> Right, [0, 1] -> Left

        return self.path
