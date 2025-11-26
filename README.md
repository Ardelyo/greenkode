# 🌿 GreenKode
### *Sustainable Software Engineering for a World of 8 Billion*

![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Carbon Neutral](https://img.shields.io/badge/Carbon-Neutral-brightgreen?style=for-the-badge&logo=leaf&logoColor=white)
![Competition](https://img.shields.io/badge/World_of_8_Billion-Contestant-orange?style=for-the-badge)

---

> **"The greenest energy is the energy we don't use."**

**GreenKode** is a professional CLI tool that empowers developers to measure, analyze, and optimize the carbon footprint of their code. By bridging the gap between hardware sensors and high-level Python, we make sustainability a core part of the development lifecycle.

---

## 🚀 Features at a Glance

| Feature | Description | Tech Stack |
| :--- | :--- | :--- |
| **🔍 Static Scan** | Detects inefficient patterns (e.g., O(n²) loops) *before* execution. | `ast`, `typer` |
| **⚡ Live Audit** | Measures real-time CPU energy usage and CO2 emissions. | `codecarbon`, `Intel RAPL` |
| **📊 Rich Dashboard** | Professional terminal UI with "Eco-Grades" (A+ to F). | `rich` |
| **🌍 Universal CLI** | Single command access for any Python script. | `pip`, `poetry` |

---

## 📦 Quick Start

### 1. Installation
```bash
pip install greenkode
```
*(Requires `codecarbon`, `rich`, `typer`)*

### 2. Usage
**Option A: Static Analysis (Pre-Flight Check)**
Instantly find bad code patterns without running the script.
```bash
greenkode check my_script.py
```

**Option B: Live Energy Audit (Flight Recorder)**
Run your script and see the energy cost.
```bash
greenkode run my_script.py
```

### 3. Help
```bash
greenkode --help
```

---

## 🔬 The Science Behind GreenKode
GreenKode leverages **Intel RAPL (Running Average Power Limit)** sensors to measure the exact energy consumption of the CPU in joules.
1.  **Measurement**: We track the power draw of the specific process ID (PID).
2.  **Conversion**: Joules are converted to kWh.
3.  **Carbon Intensity**: We apply the local grid's carbon intensity factor (gCO2/kWh) to calculate the final carbon footprint.

---

## 👤 Author & Competition Context

**Created by:** Ardellio Satria Anindito  
**Location:** Bandung, Jawa Barat, Indonesia 🇮🇩  
**Competition:** [World of 8 Billion](https://www.worldof8billion.org/) (Energy & Climate Change)

### 📚 Documentation / Dokumentasi

We have comprehensive documentation for users, developers, and judges:

#### 🏁 For Users
- [**🚀 Getting Started**](docs/GETTING_STARTED.md): Installation, usage, and troubleshooting.

#### 🧠 For Developers & Judges
- [**📄 Technical Whitepaper (English)**](docs/DOCUMENTATION_EN.md): Deep dive into the problem, solution, and impact.
- [**📄 Kertas Putih Teknis (Bahasa Indonesia)**](docs/DOCUMENTATION_ID.md): Penjelasan lengkap dalam Bahasa Indonesia.
- [**🏗️ Architecture**](docs/ARCHITECTURE.md): System design and component interaction.
- [**🤝 Contributing**](docs/CONTRIBUTING.md): How to build and contribute to GreenKode.

---
<div align="center">
  <sub>Built with ❤️ for a greener planet.</sub>
</div>
