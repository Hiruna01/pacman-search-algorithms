# Search Algorithms in Pac-Man

**IT3012 Intelligent Systems — Group Assignment (Group AI49)**

Faculty of Computing, SLIIT · Year 3 · 2026

---

## About the Project

This project applies classic AI search algorithms to the Pac-Man game, based on the UC Berkeley CS188 Pac-Man AI projects.

Pac-Man uses these algorithms to plan paths through mazes, reach food, and complete structured search goals.

The project covers:

- **Uninformed Search**
  - Depth First Search (DFS)
  - Breadth First Search (BFS)
  - Uniform Cost Search (UCS)
  - All implemented as graph-search algorithms

- **Informed Search**
  - A* Search with pluggable heuristics

- **Corners Problem**
  - A search problem where Pac-Man must visit all four corners of the maze
  - Includes a heuristic designed to be admissible and consistent

- **Food Search Problem**
  - A heuristic for efficiently finding a route that allows Pac-Man to eat all food dots

All work is implemented in the supplied project files:

- `search.py` — Q1 to Q4
- `searchAgents.py` — Q5 to Q7

The implementations are tested using the provided autograder.

---

## Work Division

| Member | Student ID | Questions | Additional Responsibilities |
|---|---|---|---|
| **P P Kavindi** | IT24101611 | Q1 — DFS, Q2 — BFS | Repository setup, README, final report assembly |
| **Fernando M S T** | IT24101063 | Q3 — UCS, Q4 — A* Search | Git evidence screenshots, contribution table |
| **Bodini G V E J** | IT24101177 | Q5 — Corners Problem, Q6 — Corners Heuristic | Node-count testing for Q6 |
| **De Silva T H H D** | IT24101010 | Q7 — Food Heuristic | AI usage declaration, full autograder run before submission |

---

## Development Environment

### Python

The project is tested using Python 3.11.

Check the Python version:

```powershell
py -3.11 --version