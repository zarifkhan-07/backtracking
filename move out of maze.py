def solve_maze(maze, x, y, end_x, end_y, visited):
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False
    if maze[x][y] == 1 or visited[x][y]:
        return False
    
    visited[x][y] = True
    
    if x == end_x and y == end_y:
        print(f"Reached at ({x}, {y})")
        return True
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        if solve_maze(maze, x + dx, y + dy, end_x, end_y, visited):
            print(f"Path through ({x}, {y})")
            return True
            
    visited[x][y] = False
    return False
