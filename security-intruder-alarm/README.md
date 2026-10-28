# 🏠 Domestic Security: Smart Intruder Alarm System

## 📌 Project Overview
This module demonstrates advanced peripheral integration within the Embedded Systems research track. It introduces **Sensor Inputs** and **Hardware Pulse Width Modulation (PWM)** engines by constructing a responsive domestic security perimeter matrix using an **ESP32** running **MicroPython**.

The core objective is to transition from static timing loops to dynamic environment reading, establishing an asynchronous, sensor-driven execution layout.

---

## 🔌 Hardware Circuit Architecture (`diagram.json`)
The infrastructure utilizes an input telemetry sensor paired with a combined audio-visual alert mechanism (one buzzer and one LED) driven directly off safe, non-strapping GPIO lines.

### Component Breakdown
*   **Controller:** ESP32 DevKit V1 Board
*   **Telemetry Input:** `wokwi-pir-motion-sensor` — Detects ambient infrared differential spikes (movement).
*   **Visual Actuator:** `alarm_led` (Single Red LED) — High-intensity flashing strobe indicator.
*   **Audio Actuator:** `buzzer1` (Piezoelectric Buzzer) — Acoustic sound generator driven via square wave frequencies.
*   **Passives:** `220Ω` Resistor — Drop-down current control for the single LED diode.

### Pin Interconnection Map

| Microcontroller Terminal | Target Component Terminal | Wire Color | Technical Function |
| :--- | :--- | :--- | :--- |
| **`3V3`** | `pir1:VCC` | 🔴 Red | 3.3V Operational VCC supply |
| **`GPIO D13`** | `pir1:OUT` | 🟣 Purple | Logic input signal vector (High/Low) |
| **`GND.1`** | `pir1:GND` | ⚫ Black | Common Ground Path |
| **`GPIO D15`** | `alarm_led:A` | 🔴 Red | High-signal LED actuator supply |
| `alarm_led:C` | `r_alarm:1` | ⚫ Black | Anode-to-Resistor junction path |
| `r_alarm:2` | **`GND.2`** | ⚫ Black | Direct circuit path completion |
| **`GPIO D4`** | `buzzer1:2` | 🟠 Orange | Hardware PWM square wave sound feed |
| **`GND.2`** | `buzzer1:1` | ⚫ Black | Buzzer ground loop return |

---

## 🧠 Firmware Logic Execution (`main.py`)
The code relies on the `machine.PWM` internal library to generate structural frequencies directly from hardware Timers without clogging the software processing thread.

### Operational State Matrix
The system loops continuously checking the environment state:
1.  **SECURE State (`PIR == 0`):** The system polls every 100 milliseconds. Actuator lines are explicitly set to off (`duty(0)` for sound and `.off()` for the LED), saving chip computation and power.
2.  **ALERT State (`PIR == 1`):** An alert condition is processed. The code initiates a nested flashing function: snapping the single LED on/off while rapidly modulating the PWM frequencies between **`550Hz`** and **`440Hz`** to create an authentic dual-tone emergency siren.

---

## 📉 Architectural Engineering Notes
*   **Hardware Pin Safety Constraints:** Early prototypes targeted Pin `D12` for the LED actuator. This was discarded during staging because `D12` is an internal MTDI strapping pin on the ESP32. Sourcing current through it during initial script loops causes firmware panics and boot-lock crashes. The visual lane was successfully migrated to `D15`.
*   **PWM Efficiency:** Rather than generating sounds using blocking code delays (`sleep_us`), offloading acoustic signals to the hardware PWM engine guarantees uninhibited script execution and zero audio-visual lagging inside the rendering simulation.
