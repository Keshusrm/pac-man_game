# multiAgents.py
# Based on the UC Berkeley CS188 Pacman projects
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
"""
AI Lab 3 - Minimax agent for Pacman.
"""

from util import manhattanDistance
from game import Directions, Agent
import random
import util


def scoreEvaluationFunction(currentGameState):
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class ReflexAgent(Agent):
    """Simple reflex agent (kept so the file is a complete multiagent module)."""

    def getAction(self, gameState):
        legalMoves = gameState.getLegalActions()
        scores = [self.evaluationFunction(gameState, a) for a in legalMoves]
        best = max(scores)
        bestIndices = [i for i in range(len(scores)) if scores[i] == best]
        return legalMoves[random.choice(bestIndices)]

    def evaluationFunction(self, currentGameState, action):
        return currentGameState.generatePacmanSuccessor(action).getScore()


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Minimax agent. Agent 0 is Pacman (MAX); agents 1.. are ghosts (MIN).
    Depth increases after every agent has moved once.
    """

    def getAction(self, gameState):
        numAgents = gameState.getNumAgents()

        def value(state, depth, agent):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state)
            nxt = (agent + 1) % numAgents
            nd = depth + 1 if nxt == 0 else depth
            vals = [value(state.generateSuccessor(agent, a), nd, nxt)
                    for a in state.getLegalActions(agent)]
            return max(vals) if agent == 0 else min(vals)

        return max(gameState.getLegalActions(0),
                   key=lambda a: value(gameState.generateSuccessor(0, a), 0, 1))
