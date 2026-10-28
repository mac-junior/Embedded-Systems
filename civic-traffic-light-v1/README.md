# 🏙️ Civic Infrastructure: Single-Lane Traffic Light Controller (v1)

## 📌 Project Overview
This project serves as the foundational baseline module for the Embedded Systems and Internet of Things (IoT) training track. It simulates a standard single-lane civic traffic signal layout using an **ESP32 microcontroller** running **MicroPython**. 

The main objective of this introductory sub-system is to demonstrate basic General-Purpose Input/Output (GPIO) digital configuration, electrical current manipulation via resistors, and simple synchronous execution tracking.

---

## 🔌 Hardware Circuit Architecture (`diagram.json`)
The physical configuration consists of three separate Light Emitting Diodes (LEDs) mapped to distinct digital pins on the ESP32 DevKit V1 module. Each circuit requires a current-limiting resistor to protect the components from excessive electrical flow.

### Component Breakdown
*   **Controller:** ESP32 DevKit V1 Board
*   **Actuators:** 
    *   `led1` (Red LED) — Signals structural halt phase.
    *   `led2` (Yellow LED) — Signals state transition warning phase.
    *   `led3` (Green LED) — Signals active traversal phase.
*   **Passives:** 3x `220Ω` Resistors (Protects individual LED junctions from over-current destruction).

### Pin Interconnection Map

| Microcontroller Terminal | Target Component | Wire Color | Purpose |
| :--- | :--- | :--- | :--- |
| **`GPIO D15`** | `led1:A` (Red Anode) | 🔴 Red | High-signal feed for Red phase |
| `led1:C` (Red Cathode) | `r1:1` (Resistor Pin 1) | ⚫ Black | Directional path to ground |
| `r1:2` (Resistor Pin 2) | **`esp:GND.1`** | ⚫ Black | Complete return circuit path |
| **`GPIO D2`** | `led2:A` (Yellow Anode) | 🟡 Yellow | High-signal feed for Yellow phase |
| `led2:C` (Yellow Cathode) | `r2:1` (Resistor Pin 1) | ⚫ Black | Directional path to ground |
| `r2:2` (Resistor Pin 2) | **`esp:GND.1`** | ⚫ Black | Complete return circuit path |
| **`GPIO D4`** | `led3:A` (Green Anode) | 🟢 Green | High-signal feed for Green phase |
| `led3:C` (Green Cathode) | `r3:1` (Resistor Pin 1) | ⚫ Black | Directional path to ground |
| `r3:2` (Resistor Pin 2) | **`esp:GND.1`** | ⚫ Black | Complete return circuit path |

---

## 🧠 Firmware Logic Execution (`main.py`)
The logic implementation uses MicroPython's native `machine.Pin` framework to manipulate electronic pin states.

```python
from machine import Pin
import time
```

### Execution Flow Pattern
The execution uses a synchronous blocking loop (`while True`) that enforces a static timing window:

1.  **Green Traversal Phase (5 Seconds):** GPIO Pin `D4` is driven `HIGH` (`3.3V`), illuminating the green LED while pins `D2` and `D15` remain `LOW` (`0V`).
2.  **Yellow Transition Phase (2 Seconds):** Pin `D4` collapses to `LOW`. Pin `D2` drives `HIGH`, alerting oncoming actors of an impending structural phase change.
3.  **Red Halt Phase (5 Seconds):** Pin `D2` collapses to `LOW`. Pin `D15` drives `HIGH`, enforcing a systemic pause condition across the simulated corridor.

---

## 📉 Architectural Tradeoffs & Constraints (Research Evaluation)
While functional for basic validation, this **v1 baseline** has significant real-world engineering flaws that will be addressed in future iterations:

*   **Blocking Sub-Routines:** The use of `time.sleep()` halts the entire central processing unit (CPU). If an emergency vehicle sensor, pedestrian push button, or network packet arrives while the controller is sleeping, the system will completely miss it.
*   **Static Windows:** The timing matrix is rigid. It cannot adapt to changing vehicle counts, peak hours, or live environmental data streams.

### Future Research Vectors
*   **v2 Progression:** Migrate from `time.sleep()` loops to an asynchronous state machine leveraging `time.ticks_ms()` to establish non-blocking intervals.
*   **Sensor Integration:** Intercept state transitions using hardware interrupts linked to pedestrian crosswalk buttons.
