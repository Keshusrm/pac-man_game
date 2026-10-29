AI LAB 3 - BFS, A* and Minimax on the Pacman (UC Berkeley CS188) interface
==========================================================================

This folder is a complete, ready-to-run Pacman project. Nothing else to copy.
Needs Python 3 (graphics window needs tkinter, included with normal Python
on Windows/macOS; on Linux: sudo apt install python3-tk).

OPEN A TERMINAL INSIDE THIS FOLDER, then run:

BFS  (code: breadthFirstSearch in search.py)
  python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
  python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

A*   (code: aStarSearch in search.py)
  python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
  python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic -z .5

MINIMAX (code: MinimaxAgent in multiAgents.py)
  python pacman.py -p MinimaxAgent -a depth=3 -l minimaxClassic -k 2
  python pacman.py -p MinimaxAgent -a depth=2 -l smallClassic -k 2

Print only the path (no game window):
  python run_bfs.py mediumMaze
  python run_astar.py bigMaze

HOW TO GIVE INPUT VALUES
Values are command-line flags (not typed while running):
  -l  layout / maze name        -p  agent name
  -a  agent arguments           -k  number of ghosts
  -q  quiet, no graphics        -z  zoom (e.g. -z .5 for a smaller window)
  -n  number of games           --frameTime 0  run as fast as possible
Layouts are in the "layouts" folder (tinyMaze, mediumMaze, bigMaze, ...).
In VS Code / PyCharm put the same flags in the run arguments / Parameters box.

FILES YOU WROTE / CHANGED
  search.py        BFS + A*
  multiAgents.py   Minimax
Everything else is the standard Pacman interface.
