import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sp211_21967646_98.sp211_21967646_98 import dijkstra, set_log_level

def test_dijkstra_simple():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    result = dijkstra(graph, 'A')
    assert result['D'] == 4
    assert result['C'] == 3
    assert result['B'] == 1
    assert result['A'] == 0

def test_set_log_level(caplog):
    from sp211_21967646_98.sp211_21967646_98 import set_log_level

    with caplog.at_level("INFO"):
        set_log_level("DEBUG")
        assert any(record.levelno == logging.INFO for record in caplog.records)
