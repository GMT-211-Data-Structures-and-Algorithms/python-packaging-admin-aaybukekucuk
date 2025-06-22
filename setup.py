from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='shortestpath21967646',  # Değiştirme, bu TestPyPI için uygun formatta
    version='0.1.0',
    author='Aybuke Kucuk',
    author_email='aybukekucuk@example.com',
    description='Shortest path calculation using Dijkstra algorithm',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/GMT-211-Data-Structures-and-Algorithms/python-packaging-admin-aaybukekucuk',
    packages=find_packages(),
    install_requires=[
        'pytest>=8.0.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)