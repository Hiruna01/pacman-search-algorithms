# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # Initialize the frontier with the start state and an empty list of actions.
    frontier = util.Stack()
    frontier.push((problem.getStartState(), []))
    # Initialize the explored set to keep track of visited states.
    explored = set()


    # Loop until the frontier is empty.
    while not frontier.isEmpty():

        state, actions = frontier.pop()

        # Return this route's moves when the goal is reached.
        if problem.isGoalState(state):
            return actions

        # Skip states whose successors were already explored.
        if state in explored:
            continue

        
        explored.add(state)

        # Add the successors of the current state to the frontier.
        for next_state, action, step_cost in problem.getSuccessors(state):
            if next_state not in explored:
                # Create a separate move list for this new route.
                new_actions = actions + [action]
                frontier.push((next_state, new_actions))



    return []



    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()

    frontier.push((problem.getStartState(), []))
    explored = set()

    while not frontier.isEmpty():

        state, actions = frontier.pop()

        if problem.isGoalState(state):
            return actions

        # Skip states whose successors were already explored.
        if state in explored:
            continue

        explored.add(state)

        # Add each legal next state to the back of the queue.
        for next_state, action, step_cost in problem.getSuccessors(state):
            if next_state not in explored:
                # Give the new route its own move list.
                new_actions = actions + [action]
                frontier.push((next_state, new_actions))

    # No route to the goal was found.
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """Search the node of least total cost first."""
    fringe = util.PriorityQueue()
    expanded =set()
    start = problem.getStartState()

    # Fringe entry: (state, actions so far, total cost so far); priority = total cost g
    fringe.push((start, [], 0), 0)
 
    while not fringe.isEmpty():

        state, actions, cost = fringe.pop()
 
        # Goal test happens when the node is POPPED, not when it is generated.
        if problem.isGoalState(state):
            return actions
 
        # Skip states that were already expanded (graph search).
        if state in expanded:
            continue
        expanded.add(state)
 
        for successor , action, stepCost in problem.getSuccessors(state):

            if successor not in expanded:
                newCost = cost+ stepCost
                fringe.push((successor, actions + [action], newCost), newCost)
 
    return []  

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    


    fringe = util.PriorityQueue()
    expanded =set()
    start =  problem.getStartState()

    # Fringe entry stores g (cost so far); priority is f = g + h
    fringe.push((start, [], 0) , heuristic(start, problem))
 
    while not fringe.isEmpty():

        state, actions, cost = fringe.pop()
 
        if problem.isGoalState(state):
            return actions
 
        if state in expanded:
            continue
        expanded.add(state)
 
        for successor, action, stepCost in problem.getSuccessors(state):
                
                newCost =cost + stepCost
                priority = newCost + heuristic(successor, problem)
                fringe.push((successor, actions + [action], newCost), priority)
 
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
