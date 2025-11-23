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
    Supports both real hardware sensors (RAPL) and simulation mode.
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
        self.mode = "REAL" # REAL or SIMULATION
        self.metrics: Dict[str, Any] = {
            "start_time": 0.0,
            "end_time": 0.0,
            "emissions_kg": 0.0,
            "cpu_energy": 0.0,
            "duration": 0.0,
            "simulated": False
        }
        self._initialized = True

    def start_tracking(self, project_name: str = "GreenKode Project", output_dir: str = ".", region: str = None, simulate: bool = False) -> None:
        """
        Initializes and starts the emissions tracker.
        
        Args:
            project_name (str): Name of the project for reporting.
            output_dir (str): Directory to save codecarbon reports.
            region (str): ISO code of the country/region (e.g., "US", "ID").
            simulate (bool): Force simulation mode if True.
        """
        self.metrics["start_time"] = time.time()
        
        if simulate:
            self.mode = "SIMULATION"
            return

        try:
            # Suppress codecarbon output to keep console clean for our dashboard
            # If region is provided, pass it to EmissionsTracker
            kwargs = {
                "project_name": project_name,
                "output_dir": output_dir,
                "log_level": "error",
                "save_to_file": True
            }
            if region and region != "GLOBAL":
                kwargs["country_iso_code"] = region

            self.tracker = EmissionsTracker(**kwargs)
            self.tracker.start()
            self.mode = "REAL"
        except Exception as e:
            print(f"Warning: GreenKode sensors not initialized ({e}). Switching to SIMULATION mode.")
            self.tracker = None
            self.mode = "SIMULATION"

    def stop_tracking(self) -> Dict[str, Any]:
        """
        Stops the tracker and returns the collected metrics.
        
        Returns:
            Dict[str, Any]: A dictionary containing emissions and timing data.
        """
        self.metrics["end_time"] = time.time()
        self.metrics["duration"] = self.metrics["end_time"] - self.metrics["start_time"]

        if self.mode == "SIMULATION":
            # Estimation Logic:
            # Assume average laptop CPU power: 30 Watts = 0.03 kW
            # Energy (kWh) = Power (kW) * Time (h)
            power_kw = 0.03
            duration_hours = self.metrics["duration"] / 3600.0
            energy_kwh = power_kw * duration_hours
            
            # Global Average Carbon Intensity: ~475 gCO2/kWh = 0.475 kgCO2/kWh
            carbon_intensity = 0.475
            emissions_kg = energy_kwh * carbon_intensity

            self.metrics["cpu_energy"] = energy_kwh
            self.metrics["emissions_kg"] = emissions_kg
            self.metrics["simulated"] = True
            
        elif self.tracker:
            try:
                emissions = self.tracker.stop()
                # codecarbon returns emissions in kg
                self.metrics["emissions_kg"] = emissions if emissions is not None else 0.0
                
                # Attempt to retrieve CPU energy if available
                self.metrics["cpu_energy"] = self.tracker.final_emissions_data.cpu_energy if hasattr(self.tracker, 'final_emissions_data') else 0.0
                self.metrics["simulated"] = False
                
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
