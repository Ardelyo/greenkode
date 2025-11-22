"""
GreenKode Core Engine
---------------------
This module handles the core logic for tracking carbon emissions and energy usage.
It interfaces with the codecarbon library to measure the environmental impact of code execution.
"""

import os
import time
from typing import Optional, Dict, Any
from codecarbon import EmissionsTracker

class GreenEngine:
    """
    Singleton-like class to manage energy tracking and emissions calculation.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GreenEngine, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        
        self.tracker: Optional[EmissionsTracker] = None
        self.metrics: Dict[str, Any] = {
            "start_time": 0.0,
            "end_time": 0.0,
            "emissions_kg": 0.0,
            "cpu_energy": 0.0,
            "duration": 0.0
        }
        self._initialized = True

    def start_tracking(self, project_name: str = "GreenKode Project", output_dir: str = ".") -> None:
        """
        Initializes and starts the emissions tracker.
        
        Args:
            project_name (str): Name of the project for reporting.
            output_dir (str): Directory to save codecarbon reports.
        """
        try:
            # Suppress codecarbon output to keep console clean for our dashboard
            self.tracker = EmissionsTracker(
                project_name=project_name,
                output_dir=output_dir,
                log_level="error",
                save_to_file=True
            )
            self.tracker.start()
            self.metrics["start_time"] = time.time()
        except Exception as e:
            print(f"Warning: GreenKode sensors not initialized. {e}")
            self.tracker = None
            self.metrics["start_time"] = time.time()

    def stop_tracking(self) -> Dict[str, Any]:
        """
        Stops the tracker and returns the collected metrics.
        
        Returns:
            Dict[str, Any]: A dictionary containing emissions and timing data.
        """
        self.metrics["end_time"] = time.time()
        self.metrics["duration"] = self.metrics["end_time"] - self.metrics["start_time"]

        if self.tracker:
            try:
                emissions = self.tracker.stop()
                # codecarbon returns emissions in kg
                self.metrics["emissions_kg"] = emissions if emissions is not None else 0.0
                
                # Attempt to retrieve CPU energy if available in final emissions data
                # Note: codecarbon's stop() returns total emissions. 
                # Detailed energy data might need to be accessed via tracker properties if exposed,
                # but for now we will rely on the total emissions.
                # We can try to access internal buffer if needed, but let's stick to public API.
                self.metrics["cpu_energy"] = self.tracker.final_emissions_data.cpu_energy if hasattr(self.tracker, 'final_emissions_data') else 0.0
                
            except Exception as e:
                print(f"Warning: Could not stop GreenKode tracker. {e}")
        
        return self.metrics

    def get_grade(self, emissions_g: float) -> str:
        """
        Calculates an eco-grade based on emissions in grams.
        
        Args:
            emissions_g (float): Emissions in grams.
            
        Returns:
            str: Grade from 'A+' to 'F'.
        """
        # Thresholds are heuristic and illustrative
        if emissions_g < 0.0001:
            return "A+"
        elif emissions_g < 0.001:
            return "A"
        elif emissions_g < 0.01:
            return "B"
        elif emissions_g < 0.1:
            return "C"
        elif emissions_g < 1.0:
            return "D"
        else:
            return "F"
