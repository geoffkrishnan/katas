"""
You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

Empty positions are marked ..
Walls are marked W.
Start and exit positions are empty in all test cases.

input:
    2D square array - maze
        n = len(maze)
        n by n grid

output:
    bool - true if can reach the bottom rightmost cell of grid ([n - 1, n - 1] coords)

walls - "W"
empty cells - "."

can move four directions up, down, left, right

obv can't move through walls, can only move through empty cells

ok did spiral matrix. solving problem similar to problem i've solved before is so much easier.
so can solve this similarly. actually not sure if this maps to dfs, did spiral matrix with bfs


grid review
2d array is a list of lists.
outer list len represents the number of rows
inner row len represents number of cols

so grid[row][col]
choosing which row list and then the index in that row list represents the column

num_rows = len(maze)
num_cols = len(maze[0])

model as finite state machine
- start state - maze[0][0]
- goal state - maze[n - 1][n - 1] where n = len(maze)
- transitions
    - when moving up, maze[row - 1][col] because you start at the top(0 index) and moving down you increment row index
    - when moving down, maze[row + 1][col]
    - when moving to the left maze[row][col - 1]
    - when moving to the right maze[row][col + 1]

    - represent these transitions as [[-1, 0] , [1, 0], [0, -1] , [0, 1]]
    - adding -1, 0 to current coord is same as going up, and same for rest
    - can use dict map direction name string to the corresponding deltas
    - transitions = {"up": [-1, 0], ...}

ok. now how do we actually find a path through the graph using recursion.

recursion so dfs probably




example:
 maze = [
      ['.', '.', '.', 'W'],
      ['W', 'W', '.', 'W'],
      ['.', '.', '.', '.'],
      ['.', 'W', 'W', '.']
  ]
right until hit wall.
down until hit wall.
right until hit wall.
down until hit wall.

but what if ur in a position where you HAVE to go left.

well. given start position 0,0, never need to start with up or left
so always try down or right first
what if either one hits dead end? need to like restart at 0,0 or go backwards i guess

actually. maybe start at n - 1, n - 1 and then try to see if path exists to 0, 0?

would that be easier or the same

idk.

like. do we just do visited set like we do for BFS? not sure if thats cheating.





"""

maze = [
    [".", ".", ".", "W"],
    ["W", "W", ".", "W"],
    [".", ".", ".", "."],
    [".", "W", "W", "."],
]
