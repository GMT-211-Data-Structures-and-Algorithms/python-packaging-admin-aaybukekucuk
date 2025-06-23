# shortestpath21967646

This Python package implements **Dijkstra’s algorithm** to find the shortest path in a directed graph.  
It is designed for easy use, testing, and deployment.

---

## Features

| Feature              | Description                                |
|----------------------|--------------------------------------------|
| Shortest path search  | Finds shortest path with Dijkstra method  |
| Logging              | Tracks important steps in the algorithm   |
| Unit Testing         | Tested using pytest for reliability        |
| Easy Installation    | Available on TestPyPI for quick setup      |

---

## Screenshots

![Tests Passed](./screenshots/pytest_passed.png)  
*All tests passed with pytest.*

![Package Uploaded](./screenshots/twine_uploaded.png)  
*Package uploaded successfully to TestPyPI.*

---

## Installation

You can install the package from TestPyPI using:

```bash
pip install --index-url https://test.pypi.org/simple/ shortestpath21967646

Usage Example
from sp211_21967646_98.sp211_21967646_98 import dijkstra

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

distances = dijkstra(graph, 'A')
print(distances)

Expected output:

{'A': 0, 'B': 1, 'C': 3, 'D': 4}

Project Structure

sp211_21967646_98_(2)/
├── sp211_21967646_98/
│   ├── __init__.py
│   └── sp211_21967646_98.py      # Dijkstra algorithm implementation
├── tests/
│   └── test_sp211_21967646_98.py # Unit tests for the package
├── setup.py                      # Package configuration
├── requirements.txt              # Dependencies list
├── README.md                    # Project description and instructions
├── .github/
│   └── workflows/
│       └── python-test.yml      # GitHub Actions workflow for CI/CD
├── dist/                        # Distribution files for packaging
└── docs/                        # Documentation files (Sphinx)

Continuous Integration / Delivery
This project uses GitHub Actions to:

Automatically run tests on every push

Build and upload the package to TestPyPI automatically

This helps maintain code quality and simplifies updates.

AI Usage
I used ChatGPT to help with:

Writing and debugging the Dijkstra algorithm code

Setting up the project structure and packaging

Creating test cases and CI/CD configuration

Using AI helped me to work faster and improve code quality.

Contact
Author: Aybuke Kucuk
Email: aaybukekucuk@gmail.com
GitHub: https://github.com/GMT-211-Data-Structures-and-Algorithms/python-packaging-admin-aaybukekucuk

=======
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/i1ecLyyK)
>>>>>>> 7bcf8f4beab1045827e7435a462c0f52e8a17316
