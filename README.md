# shortestpath21967646

This Python package implements **Dijkstra’s algorithm** to find the shortest path in a directed graph.  
It is designed to be simple, testable, and ready for deployment on TestPyPI.

---

## Features

- Calculates shortest paths using Dijkstra’s algorithm  
- Takes graph input as a dictionary  
- Includes logging support  
- Tested with `pytest`  
- Includes GitHub Actions CI/CD  
- Packaged and published to TestPyPI  
- Sphinx documentation support  
- AI-assisted code development (with ChatGPT)

---

## Installation

To install the package from TestPyPI, run the following command:

```bash
pip install --index-url https://test.pypi.org/simple/ shortestpath21967646

---

## Usage Example

You can import and use the dijkstra function like this:

from sp211_21967646_98.sp211_21967646_98 import dijkstra

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

distances = dijkstra(graph, 'A')
print(distances)

---

## Expected output:

{'A': 0, 'B': 1, 'C': 3, 'D': 4}

---

## Project Structure

sp211_21967646_98_(2)/
├── sp211_21967646_98/
│   ├── __init__.py
│   └── sp211_21967646_98.py      # Dijkstra algorithm implementation
├── tests/
│   └── test_sp211_21967646_98.py # Unit tests
├── setup.py                      # Package config
├── requirements.txt              # Dependencies
├── README.md                     # Project documentation
├── dist/                         # Distribution files
├── docs/                         # Sphinx docs
└── .github/
    └── workflows/
        └── python-test.yml       # GitHub Actions CI

---

## Pytest Passed

---

## Package Uploaded to TestPyPI
Successfully uploaded with twine.

---

## Continuous Integration / Delivery

This project uses GitHub Actions for:

*Automatically running pytest after every push

*Ensuring that the package builds correctly

*Verifying the installation and packaging process

CI configuration can be found in .github/workflows/python-test.yml.

---

## AI Usage

I used ChatGPT to:

*Write and debug the dijkstra function
*Build the correct setup.py, README.md, and requirements.txt
*Configure GitHub Actions
*Prepare the project structure
*Fix test errors and improve packaging
*Generate full Sphinx documentation

AI support helped me write better, faster, and more organized code.

---

## Author

*Name: Aybuke Kucuk
*Email: aaybukekucuk@gmail.com
*GitHub: Project Repo
*DD Code: 98

---