# 🚀 Getting Started with GreenKode

Welcome to **GreenKode**! This guide will help you install, configure, and run your first energy audit.

## 📋 Prerequisites

Before you begin, ensure you have the following:

-   **OS**: Linux (recommended for full RAPL support), Windows, or macOS.
    -   *Note for macOS/Windows*: Intel RAPL sensors might be restricted. GreenKode will attempt to use available sensors or fallback to estimation modes where possible.
-   **Python**: Version 3.8 or higher.
-   **Permissions**: Root/Administrator access may be required to read hardware energy sensors.

## 📦 Installation

### Option 1: Install via pip (Recommended)

```bash
pip install greenkode
```

### Option 2: Install from Source

If you want to try the latest features or contribute:

```bash
git clone https://github.com/Ardelyo/greenkode.git
cd greenkode
pip install -e .
```

## 🚦 Basic Usage

GreenKode has two main modes: **Static Check** and **Dynamic Run**.

### 1. Static Check (Pre-Flight)
Scan your code for potential inefficiencies without running it.

```bash
greenkode check path/to/your_script.py
```

**What to look for:**
-   **O(n²) Loops**: Nested loops that could be optimized.
-   **Heavy Imports**: Libraries imported but not used.

### 2. Dynamic Run (Live Audit)
Run your script and measure its actual energy consumption.

```bash
greenkode run path/to/your_script.py
```

**Output Explained:**
-   **Energy (kWh)**: Total electricity consumed by the CPU during execution.
-   **Carbon (gCO2eq)**: Estimated carbon emissions based on your local power grid.
-   **Eco-Grade**: A score (A+ to F) indicating how efficient your script is compared to benchmarks.

## 🔧 Configuration

You can configure GreenKode using a `greenkode.toml` file in your project root (Coming Soon in v1.0).

Currently, you can pass flags to the CLI:
-   `--verbose`: Show detailed logs.
-   `--region`: (Experimental) Manually set your region for carbon intensity.

## ❓ Troubleshooting

### "Permission Denied" on RAPL
**Issue**: The tool cannot read `/sys/class/powercap/intel-rapl`.
**Fix**: Run with sudo (Linux) or Administrator (Windows).
```bash
sudo greenkode run your_script.py
```

### "No Powercap Interface Found"
**Issue**: Your hardware or VM doesn't support Intel RAPL.
**Fix**: GreenKode will default to "Simulation Mode" (if enabled) or strictly track time/CPU usage.

---
Need more help? Open an issue on [GitHub](https://github.com/Ardelyo/greenkode/issues).
