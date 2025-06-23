shortestpath21967646 documentation
==================================

Welcome to the shortestpath21967646 project documentation!

This package implements Dijkstra's algorithm to find the shortest paths in a directed graph.  
Here you will find usage examples, project structure, and additional info.

Features
--------

- Calculates shortest paths using Dijkstra’s algorithm  
- Takes graph input as a dictionary  
- Includes logging support  
- Tested with `pytest`  
- Includes GitHub Actions CI/CD  

Usage Example
-------------

You can import and use the `dijkstra` function like this:

.. code-block:: python

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

.. code-block:: none

    {'A': 0, 'B': 1, 'C': 3, 'D': 4}

Project Structure
-----------------

The project folder layout is:

.. code-block:: none

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
--------------------------------

This project uses GitHub Actions to:

- Automatically run tests on every push  
- Build and upload the package to TestPyPI automatically  

This helps maintain code quality and simplifies updates.

AI Usage
--------

I used ChatGPT to help with:

- Writing and debugging the Dijkstra algorithm code  
- Setting up the project structure and packaging  
- Creating test cases and CI/CD configuration  

Using AI helped me work faster and improve code quality.

Contact
-------

**Author:** Aybuke Kucuk  
**Email:** aaybukekucuk@gmail.com  
**GitHub:** https://github.com/GMT-211-Data-Structures-and-Algorithms/python-packaging-admin-aaybukekucuk


.. toctree::
   :maxdepth: 2
   :caption: Contents:
