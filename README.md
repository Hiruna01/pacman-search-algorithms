# Search Algorithms in Pac-Man

**IT3012 Intelligent Systems — Group Assignment (Group AI49)**  
Faculty of Computing, SLIIT · Year 3 · 2026

## Overview

This project applies classical artificial intelligence search techniques to the Pac-Man game environment. Based on the UC Berkeley CS188 Pac-Man AI project, it focuses on planning routes through maze-like environments using graph search and informed search strategies.

The implementation includes:

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search with heuristics
- Corner-search problem solving
- Food-collection optimization using heuristic evaluation

These algorithms are implemented in the project’s core search files and are validated with the included autograder and test cases.

## Project Structure

- `search.py` — generic search algorithms and heuristics
- `searchAgents.py` — Pac-Man problem definitions and agent behavior
- `pacman.py` — game engine and simulation loop
- `autograder.py` — official project grading script
- `layouts/` — maze layouts used by the game
- `test_cases/` — test inputs and expected outputs for assignment questions
- `README.md` — project documentation

## Search Algorithms Implemented

### Uninformed Search
- `depthFirstSearch(problem)`
- `breadthFirstSearch(problem)`
- `uniformCostSearch(problem)`

These algorithms explore the state space without using domain-specific knowledge. They are useful for finding valid solutions when heuristic information is not available or when the task is purely path-related.

### Informed Search
- `aStarSearch(problem, heuristic)`

A* uses a cost function combining the path cost so far with an estimate of the remaining cost to goal. This produces more efficient routes than blind search in many maze tasks.

### Advanced Problems
The project also includes custom search problems such as:

- Corner navigation problem
- Heuristic evaluation for visiting all corners
- Food-search heuristic for minimizing the path required to collect food

## Running the Project

From the project root, you can run the Pac-Man simulator with different search strategies.

Examples:

```bash
python pacman.py -p SearchAgent -a fn=depthFirstSearch
python pacman.py -p SearchAgent -a fn=breadthFirstSearch
python pacman.py -p SearchAgent -a fn=uniformCostSearch
python pacman.py -p SearchAgent -a fn=aStarSearch,heuristic=nullHeuristic
```

To run the full grading suite:

```bash
python autograder.py
```

## Assignment Coverage

The project follows the standard Pac-Man AI assignment structure and covers the following question groups:

- Q1 — Depth-First Search
- Q2 — Breadth-First Search
- Q3 — Uniform Cost Search
- Q4 — A* Search
- Q5 — Corners Problem
- Q6 — Corners Heuristic
- Q7 — Food Heuristic

## Team Members

| Member | Student ID | Questions | Responsibilities |
| --- | --- | --- | --- |
| P P Kavindi | IT24101611 | Q1 — DFS, Q2 — BFS | Repo setup, README, final report assembly |
| Fernando M S T | IT24101063 | Q3 — UCS, Q4 — A* Search | Git evidence screenshots, contribution table |
| Bodini G V E J | IT24101177 | Q5 — Corners Problem, Q6 — Corners Heuristic | Node-count testing for Q6 |
| De Silva T H H D | IT24101010 | Q7 — Food Heuristic | AI usage declaration, full autograder run before submission |

## Notes

This repository is designed for academic learning and follows the UC Berkeley Pac-Man AI project structure. The objective is to understand how search algorithms influence planning efficiency, cost minimization, and goal-directed behavior in an intelligent agent environment.

## License and Attribution

This project is based on the UC Berkeley Pac-Man AI projects and retains the original attribution and educational-use licensing.

---

This README provides a clear overview of the assignment, project setup, algorithm coverage, and evaluation workflow for the Pac-Man search task.
