# shortestpath21967646

[![Documentation Status](https://readthedocs.org/projects/shortestpath21967646/badge/?version=latest)](https://shortestpath21967646.readthedocs.io/en/latest/?badge=latest)


This Python package implements **Dijkstra’s algorithm** to find the shortest path in a directed graph.  
It is designed to be simple, testable, and ready for deployment on TestPyPI.

---

## Features

| Feature             | Description                               |
|---------------------|-------------------------------------------|
| Shortest path search | Finds shortest path with Dijkstra method |
| Logging             | Tracks important steps in the algorithm   |
| Unit Testing        | Tested using pytest for reliability       |
| Easy Installation   | Available on TestPyPI for quick setup     |

---

## Installation

To install the package from TestPyPI, run the following command:

```bash
pip install --index-url https://test.pypi.org/simple/ shortestpath21967646
```

---
## Read the Docs
This allows easy access to detailed information, usage instructions, and API references in a well-organized 
and user-friendly format.
You can view the latest documentation here:

![Ekran görüntüsü 2025-06-23 043255](https://github.com/user-attachments/assets/6bf0bedc-25ea-4b08-9326-7711132c249e)

By using ReadTheDocs, I ensure that the documentation is always up-to-date with the latest changes pushed to 
the repository, improving the overall usability and accessibility of the project.

---

## Usage Example

You can import and use the `dijkstra` function like this:

```python
from sp211_21967646_98.sp211_21967646_98 import dijkstra

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

distances = dijkstra(graph, 'A')
print(distances)
```

Expected output:

```
{'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

---

## Project Structure

```
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
```

---

## Screenshots

### ✅ Pytest Passed

All unit tests successfully passed.

![Ekran görüntüsü 2025-06-23 024354](https://github.com/user-attachments/assets/f87feb6f-1284-4295-91ac-80a3f3a3f8fe)

### 📦 Package Uploaded to TestPyPI

Successfully uploaded with `twine`.

![Ekran görüntüsü 2025-06-23 072211](https://github.com/user-attachments/assets/7153d6cb-d335-4e5d-acba-7a9bfe67095a)

---

## Continuous Integration / Delivery

This project uses GitHub Actions for:

- Automatically running `pytest` after every push  
- Ensuring that the package builds correctly  
- Verifying the installation and packaging process

CI configuration can be found in `.github/workflows/python-test.yml`.

---

## AI Usage

I used **ChatGPT** to:

- Write and debug the `dijkstra` function  
- Build the correct `setup.py`, `README.md`, and `requirements.txt`  
- Configure GitHub Actions  
- Prepare the project structure  
- Fix test errors and improve packaging  
- Generate full Sphinx documentation

AI support helped me write better, faster, and more organized code.
Usage Level: 4/5

---

## Logging Usage
In this project, I integrated Python's built-in **logging** module to record important events, 
informational messages, and errors during the execution of the code. This helps in debugging and monitoring 
the flow of the program effectively.

By setting different logging levels (e.g., DEBUG, INFO, WARNING), I can control the verbosity of the logs, 
allowing me to see either detailed debug information or only critical issues as needed.

Using logging improves the maintainability of the project and makes it easier to trace issues or unexpected 
behaviors during development and future updates.

---

## Author

- Name: **Aybuke Kucuk**  
- Email: [aaybukekucuk@gmail.com](mailto:aaybukekucuk@gmail.com)  
- GitHub: [Project Repo](https://github.com/GMT-211-Data-Structures-and-Algorithms/python-packaging-admin-aaybukekucuk)

---

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/i1ecLyyK)
