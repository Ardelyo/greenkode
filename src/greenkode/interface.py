"""
GreenKode Interface
-------------------
This module provides the user-facing decorators and context managers.
It connects the GreenEngine with the Reporter.
"""

import functools
from .engine import GreenEngine
from .reporter import print_dashboard

def green_audit(func):
    """
    Decorator that measures the carbon footprint of the decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        engine = GreenEngine()
        engine.start_tracking(project_name=f"Function: {func.__name__}")
        
        try:
            result = func(*args, **kwargs)
        finally:
            metrics = engine.stop_tracking()
            emissions_g = metrics.get("emissions_kg", 0.0) * 1000
            grade = engine.get_grade(emissions_g)
            print_dashboard(metrics, grade)
            
        return result
    return wrapper

class GreenScope:
    """
    Context manager for measuring a specific block of code.
    Usage:
        with GreenScope("My Block"):
            # heavy code
    """
    def __init__(self, name: str = "Scoped Block"):
        self.name = name
        self.engine = GreenEngine()

    def __enter__(self):
        self.engine.start_tracking(project_name=self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        metrics = self.engine.stop_tracking()
        emissions_g = metrics.get("emissions_kg", 0.0) * 1000
        grade = self.engine.get_grade(emissions_g)
        print_dashboard(metrics, grade)
