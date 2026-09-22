
# Search Algorithms in Pac-Man

**IT3012 Intelligent Systems — Group Assignment (Group AI49)**
Faculty of Computing, SLIIT · Year 3 · 2026

## About the Project

This project applies classic AI search algorithms to the Pac-Man game, based on the UC Berkeley CS188 Pac-Man AI projects. Pac-Man uses these algorithms to plan paths through mazes to reach food and complete structured goals.

We implement:

- **Uninformed search:** Depth First Search (DFS), Breadth First Search (BFS) and Uniform Cost Search (UCS), all as graph search
- **Informed search:** A* Search with pluggable heuristics
- **Corners Problem:** a search problem where Pac-Man must visit all four corners of the maze, plus an admissible and consistent heuristic for it
- **Food Search Problem:** an admissible and consistent heuristic that helps Pac-Man eat all the food dots efficiently

All work is done in `search.py` (Q1–Q4) and `searchAgents.py` (Q5–Q7), and is verified with the provided autograder.

## Work Division

| Member          | Student ID   | Questions                                      | Additional Responsibilities                                 |
| --------------- | ------------ | ---------------------------------------------- | ----------------------------------------------------------- |
| [Member 1 Name] | [ITXXXXXXXX] | Q1 — DFS, Q2 — BFS                           | Repo setup, README, final report assembly                   |
| [Member 2 Name] | [ITXXXXXXXX] | Q3 — UCS, Q4 — A* Search                     | Git evidence screenshots, contribution table                |
| [Member 3 Name] | [ITXXXXXXXX] | Q5 — Corners Problem, Q6 — Corners Heuristic | Node-count testing for Q6                                   |
| [Member 4 Name] | [ITXXXXXXXX] | Q7 — Food Heuristic                           | AI usage declaration, full autograder run before submission |
