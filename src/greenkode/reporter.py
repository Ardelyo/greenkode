"""
GreenKode Reporter
------------------
This module handles the visual presentation of the carbon footprint data.
It uses the 'rich' library to create a professional terminal dashboard.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import BarColumn, TextColumn
from rich.layout import Layout
from rich.text import Text
from rich.align import Align
from rich.console import Group
from typing import Dict, Any

console = Console()

def print_dashboard(metrics: Dict[str, Any], grade: str) -> None:
    """
    Displays the GreenKode dashboard with metrics and eco-grade.
    
    Args:
        metrics (Dict[str, Any]): Dictionary containing 'duration', 'emissions_kg', 'cpu_energy'.
        grade (str): The calculated eco-grade (A+ to F).
    """
    emissions_g = metrics.get("emissions_kg", 0.0) * 1000
    duration = metrics.get("duration", 0.0)
    cpu_energy = metrics.get("cpu_energy", 0.0)

    # Determine colors
    color_map = {
        "A+": "bright_green", "A": "green", "B": "chartreuse1",
        "C": "yellow", "D": "orange1", "F": "red"
    }
    grade_color = color_map.get(grade, "white")

    # 1. Grade Panel (Big & Bold)
    grade_text = Text(f"{grade}", style=f"bold {grade_color} reverse", justify="center")
    grade_text.stylize("bold underline")
    
    grade_desc = ""
    if grade in ["A", "A+"]:
        grade_desc = "🌿 Excellent! Low Carbon Footprint."
    elif grade == "F":
        grade_desc = "🔥 High Emissions! Optimization Needed."
    else:
        grade_desc = "⚠️ Moderate Impact. Room for improvement."

    grade_panel = Panel(
        Align.center(
            Group(
                Text("ECO-GRADE", style="dim"),
                Text(grade, style=f"bold {grade_color}", justify="center"), # Simple text for now, figlet is external dep
                Text("\n" + grade_desc, style=f"italic {grade_color}")
            )
        ),
        border_style=grade_color,
        padding=(1, 2)
    )

    # 2. Metrics Table
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="bold white", justify="right")

    table.add_row("⏱️  Duration", f"{duration:.4f} s")
    table.add_row("💨 Emissions", f"{emissions_g:.6f} gCO2")
    table.add_row("⚡ Energy", f"{cpu_energy:.6f} kWh")

    # 3. Carbon Intensity Bar
    intensity_score = min(emissions_g * 100, 100)
    bar_length = 30
    filled_length = int(bar_length * intensity_score / 100)
    bar_str = "█" * filled_length + "░" * (bar_length - filled_length)
    
    intensity_panel = Panel(
        Group(
            Text("Carbon Intensity Meter", style="bold"),
            Text(bar_str, style=f"gradient {grade_color}"),
            Text(f"{emissions_g:.6f} gCO2eq", style="dim")
        ),
        border_style="dim"
    )

    # Final Layout
    final_dashboard = Panel(
        Group(
            Align.center(Text(" GREENKODE REPORT ", style="bold black on green")),
            Text(""),
            grade_panel,
            Text(""),
            Align.center(table),
            Text(""),
            intensity_panel
        ),
        title="[bold green]GreenKode[/bold green]",
        subtitle="Sustainable Software Engineering",
        border_style="green",
        padding=(1, 4)
    )

    console.print("\n")
    console.print(final_dashboard)
