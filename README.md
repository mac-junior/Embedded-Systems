# Embedded Systems & IoT Research Laboratory

Welcome to the central repository for advanced embedded engineering, Internet of Things (IoT), and robotics prototyping. This hub serves as a foundational proof-of-concept portfolio for training upcoming freshmen and software engineering students.

---

## 🚀 Projects Index

### 🏙️ Civic Infrastructure Systems

*   **[Traffic Light Sequence v1](./civic-traffic-light-v1)**
    *   *Overview:* Baseline 3-LED traffic timing simulation using MicroPython and an ESP32.
    *   *Key Concepts:* Digital GPIO output configuration, basic hardware wiring, and synchronous execution loops.

*   **[Multi-Way Intersection Controller](./civic-intersection-v2)**
    *   *Overview:* An advanced 4-way traffic intersection utilizing asynchronous state machines to manage concurrent lanes.
    *   *Key Concepts:* Non-blocking timing using `time.ticks_ms()`, state-machine design patterns, and hardware interrupts.

### 🏠 Domestic Security & Automation

*   **[Smart Intruder Alarm System](./security-intruder-alarm)**
    *   *Overview:* A home security module that monitors movement and alerts users to unauthorized entry.
    *   *Key Concepts:* Passive Infrared (PIR) motion sensors, hardware buzzer frequency modulation, and system status tracking.

*   **[Biometric & Keypad Access Gateway](./security-access-gateway)**
    *   *Overview:* A secure digital door lock simulation requiring a passcode entry with automatic lockout thresholds.
    *   *Key Concepts:* Matrix keypad scanning arrays, character matching algorithms, status displays, and security override routines.

### 🌊 Industrial & Environmental Monitoring

*   **[Weather & Air Quality Gateway](./iot-weather-station)**
    *   *Overview:* A remote sensing station that collects environmental metrics and telemeters data to cloud dashboards.
    *   *Key Concepts:* I2C/SPI sensor protocols, analog-to-digital conversion (ADC), and Wi-Fi network sockets.

---

## 🛠️ Core Tech Stack
*   **Microcontrollers:** ESP32 (DevKit V1)
*   **Languages:** MicroPython, C++ (FreeRTOS)
*   **Simulation Environments:** Wokwi, VS Code, Edge Impulse
