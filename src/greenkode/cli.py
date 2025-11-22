"""
GreenKode CLI
-------------
Command Line Interface for GreenKode.
Supports static analysis ('check') and dynamic execution ('run').
"""

import typer
import sys
import subprocess
import os
import time
from .analyzer import CodeInspector
from .engine import GreenEngine
from .reporter import print_dashboard
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

app = typer.Typer(
    help="GreenKode: Measure and Optimize your Code's Carbon Footprint.",
    no_args_is_help=True,
    rich_markup_mode="rich"
)
console = Console()

@app.command()
def check(file_path: str = typer.Argument(..., help="Path to the Python file to analyze.")):
    """
    Perform static analysis on a Python file to detect energy inefficiencies.
    """
    if not os.path.exists(file_path):
        console.print(f"[bold red]❌ Error:[/bold red] File '{file_path}' not found.")
        raise typer.Exit(code=1)

    console.print(Panel(f"[bold blue]🔍 GreenKode Static Scan[/bold blue]\nTarget: [cyan]{file_path}[/cyan]", border_style="blue"))

    with console.status("[bold green]Scanning AST for inefficiencies...[/bold green]", spinner="dots"):
        time.sleep(0.8) # Fake delay for UX (to show off the spinner)
        inspector = CodeInspector(file_path)
        suggestions = inspector.analyze()

    if not suggestions:
        console.print(Panel("[bold green]✅ Clean Code![/bold green]\nNo obvious energy inefficiencies detected.", border_style="green"))
    else:
        table = Table(title="[bold yellow]⚠️ Potential Inefficiencies Detected[/bold yellow]", border_style="yellow")
        table.add_column("Issue Type", style="cyan", no_wrap=True)
        table.add_column("Suggestion", style="white")

        for tip in suggestions:
            # Simple parsing to categorize (for demo purposes)
            issue_type = "Optimization"
            if "Nested loop" in tip:
                issue_type = "Complexity (O(n^2))"
            elif "Heavy library" in tip:
                issue_type = "Memory/Import"
            
            table.add_row(issue_type, tip)

        console.print(table)
        console.print("\n[dim]Tip: Use 'greenkode run' to measure actual energy usage.[/dim]")

@app.command()
def run(file_path: str = typer.Argument(..., help="Path to the Python file to execute.")):
    """
    Execute a Python file and measure its carbon footprint.
    """
    if not os.path.exists(file_path):
        console.print(f"[bold red]❌ Error:[/bold red] File '{file_path}' not found.")
        raise typer.Exit(code=1)

    console.print(Panel(f"[bold blue]🚀 GreenKode Live Audit[/bold blue]\nTarget: [cyan]{file_path}[/cyan]", border_style="blue"))
    
    # Initialize Engine
    engine = GreenEngine()
    engine.start_tracking(project_name=f"CLI Run: {os.path.basename(file_path)}")

    try:
        with console.status(f"[bold green]Executing {file_path}...[/bold green]", spinner="runner"):
            # Run the target script as a subprocess
            result = subprocess.run(
                [sys.executable, file_path],
                capture_output=False, # Let stdout/stderr flow to console
                text=True
            )
        
        if result.returncode != 0:
            console.print(f"\n[bold red]❌ Script exited with error code {result.returncode}[/bold red]")

    except KeyboardInterrupt:
        console.print("\n[bold yellow]⚠️ Execution interrupted by user.[/bold yellow]")
    except Exception as e:
        console.print(f"\n[bold red]❌ Error running script: {e}[/bold red]")
    finally:
        # Stop tracking and report
        with console.status("[bold green]Calculating Emissions...[/bold green]", spinner="earth"):
            time.sleep(0.5) # UX delay
            metrics = engine.stop_tracking()
            emissions_g = metrics.get("emissions_kg", 0.0) * 1000
            grade = engine.get_grade(emissions_g)
        
        print_dashboard(metrics, grade)

if __name__ == "__main__":
    app()
