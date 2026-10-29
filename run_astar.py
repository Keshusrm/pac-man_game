import sys
import layout
import pacman
import searchAgents
from search import aStarSearch

layout_name = sys.argv[1] if len(sys.argv) > 1 else "mediumMaze"
lay = layout.getLayout(layout_name)
state = pacman.GameState()
state.initialize(lay, 0)
problem = searchAgents.PositionSearchProblem(state, warn=False, visualize=False)
path = aStarSearch(problem, searchAgents.manhattanHeuristic)
print("Layout:", layout_name)
print("Path:", path)
print("Path length:", len(path))
