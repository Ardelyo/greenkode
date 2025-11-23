import re

def test_inefficient_concat():
    s = ""
    for i in range(10):
        s += "a"  # Should trigger warning

def test_efficient_concat():
    parts = []
    for i in range(10):
        parts.append("a")
    s = "".join(parts)

def test_inefficient_regex():
    data = ["abc", "123"]
    for item in data:
        # Should trigger warning
        re.search(r"\d+", item)

def test_efficient_regex():
    pattern = re.compile(r"\d+")
    data = ["abc", "123"]
    for item in data:
        pattern.search(item)

def test_nested_loops():
    for i in range(5):
        for j in range(5):
            pass # Should trigger nested loop warning
