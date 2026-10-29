# search.py
# Based on the UC Berkeley CS188 Pacman projects
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
"""
AI Lab 3 - BFS and A* search for Pacman.
"""

import util


class SearchProblem:
    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def getSuccessors(self, state):
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    frontier = util.Stack()
    frontier.push((problem.getStartState(), []))
    visited = set()
    while not frontier.isEmpty():
        state, path = frontier.pop()
        if state in visited:
            continue
        visited.add(state)
        if problem.isGoalState(state):
            return path
        for succ, action, cost in problem.getSuccessors(state):
            if succ not in visited:
                frontier.push((succ, path + [action]))
    return []


def breadthFirstSearch(problem):
    frontier = util.Queue()
    frontier.push((problem.getStartState(), []))
    visited = set()
    while not frontier.isEmpty():
        state, path = frontier.pop()
        if state in visited:
            continue
        visited.add(state)
        if problem.isGoalState(state):
            return path
        for succ, action, cost in problem.getSuccessors(state):
            if succ not in visited:
                frontier.push((succ, path + [action]))
    return []


def uniformCostSearch(problem):
    return aStarSearch(problem)


def nullHeuristic(state, problem=None):
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    frontier = util.PriorityQueue()
    start = problem.getStartState()
    frontier.push((start, [], 0), heuristic(start, problem))
    best_g = {}
    while not frontier.isEmpty():
        state, path, g = frontier.pop()
        if state in best_g and best_g[state] <= g:
            continue
        best_g[state] = g
        if problem.isGoalState(state):
            return path
        for succ, action, cost in problem.getSuccessors(state):
            new_g = g + cost
            frontier.push((succ, path + [action], new_g),
                          new_g + heuristic(succ, problem))
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
