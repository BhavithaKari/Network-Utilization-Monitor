# 📡 SDN Network Utilization Monitor (POX + Mininet)

## 📌 Project Description

This project implements a **Software Defined Networking (SDN)** based **Network Utilization Monitor** using the **POX controller** and **Mininet** network emulator.

The controller periodically collects OpenFlow port statistics from switches, estimates bandwidth usage, calculates link utilization percentage, and displays results in real-time.

---

## 🎯 Key Features

- 📊 Collects byte counters from OpenFlow switches
- 📶 Estimates bandwidth usage (Mbps)
- 📈 Calculates link utilization (%)
- ⏱️ Updates statistics every **2 seconds**
- 🔁 Works with **linear Mininet topology**

---

## 🏗️ System Architecture

```
Mininet Topology:

  h1 ──── s1 ──── s2 ──── h2
           │       │
           └───────┘
           OpenFlow 1.0
               │
           POX Controller
```

| Component   | Role                         |
|-------------|------------------------------|
| `h1`, `h2`  | Hosts (traffic endpoints)    |
| `s1`, `s2`  | OpenFlow-enabled switches    |
| POX         | SDN Controller               |
| OpenFlow    | Control protocol (v1.0)      |

---

## ⚙️ Technologies Used

| Technology       | Purpose                        |
|------------------|--------------------------------|
| Ubuntu Linux     | Host OS                        |
| Mininet          | Network emulation              |
| POX Controller   | OpenFlow SDN controller        |
| Python           | Controller module language     |
| OpenFlow 1.0     | Switch–controller protocol     |

---

## 🚀 Setup Instructions

### ✅ Step 1 — Install Required Tools

```bash
sudo apt update
sudo apt install git
sudo apt install mininet
```
<img width="502" height="411" alt="image" src="https://github.com/user-attachments/assets/cd204632-44e6-4a2d-88d3-c9f1cfea48f5" />

**Verify Mininet:**
```bash
sudo mn --test pingall
```
> If hosts ping each other → Mininet is working ✔
---
<img width="316" height="364" alt="image" src="https://github.com/user-attachments/assets/ad286aee-ef46-48c3-9681-8a4b6a303a82" />

### ✅ Step 2 — Download POX Controller

```bash
git clone https://github.com/noxrepo/pox
cd pox
./pox.py
```
> If you see `POX is up.` → POX is working ✔  
> Press `Ctrl + C` to stop.

---

### ✅ Step 3 — Create the Network Monitor Module

```bash
cd ~/pox/pox
nano network_monitor.py
```
<img width="263" height="26" alt="image" src="https://github.com/user-attachments/assets/6265d345-e9e9-4a82-983e-a13a0ea425de" />

---

### ✅ Step 4 — Run the POX Controller

```bash
cd ~/pox
./pox.py openflow.of_01 network_monitor
```

**Expected output:**
```
Network Utilization Monitor Started
```
<img width="469" height="278" alt="image" src="https://github.com/user-attachments/assets/1cd21b90-57b8-4586-b85e-2b0232ea2099" />

> Leave this terminal open.

---

### ✅ Step 5 — Start Mininet (New Terminal)

```bash
sudo mn --topo linear,2 --controller remote
```

**Expected output:**
```
*** Starting CLI:
mininet>
```
<img width="345" height="199" alt="image" src="https://github.com/user-attachments/assets/f3547352-5892-410b-8aaf-d8f9984b554f" />

---

### ✅ Step 6 — Generate Traffic

**Small traffic test (inside Mininet CLI):**
```
mininet> pingall
```
<img width="215" height="56" alt="image" src="https://github.com/user-attachments/assets/af53e00e-9aac-4b99-88f5-bec413a5f7b5" />

**High traffic test:**
```
mininet> iperf h1 h2
```
<img width="269" height="26" alt="image" src="https://github.com/user-attachments/assets/e98e2b63-8e22-4846-9065-4fb3e8c5f6ad" />

**Example output in POX terminal:**
```
Switch 00-00-00-00-00-01 | Port 1 | 8.45 Mbps | Utilization: 84.5%
```
<img width="479" height="201" alt="image" src="https://github.com/user-attachments/assets/fb9bf30d-8af4-4b1a-aa86-d2de72e9c636" />

---

### ✅ Step 7 — Stop Everything Properly

```bash
# In Mininet:
exit

# Clean up:
sudo mn -c

# Stop POX:
Ctrl + C
```
<img width="814" height="277" alt="image" src="https://github.com/user-attachments/assets/0fa5a831-d52f-41f5-a5fd-b37f2641e438" />

<img width="283" height="34" alt="image" src="https://github.com/user-attachments/assets/364e7cbe-7fe0-439b-8cc0-c5940eb317b2" />

---

## 🧠 How It Works

```
1. POX registers a listener for switch connections (ConnectionUp)
2. On each switch connect → NetworkMonitor instance created
3. Every 2 seconds → OpenFlow Port Stats Request sent to switch
4. Switch replies with byte counters (rx_bytes + tx_bytes)
5. Controller calculates:
      byte_diff = current_bytes - previous_bytes
      bandwidth_mbps = (byte_diff × 8) / time_diff / 1M
      utilization % = (bandwidth_mbps / 10 Mbps) × 100
6. Results are logged to the terminal
```

---

## 📁 Project Structure

```
pox/
└── pox/
    └── network_monitor.py   ← Our custom SDN monitoring module
```

---

## 🎓 Concepts Demonstrated

| Concept                   | Implementation                          |
|---------------------------|-----------------------------------------|
| SDN Controller            | POX with custom Python module           |
| OpenFlow Protocol         | Port Statistics Request/Response        |
| Bandwidth Estimation      | Byte-delta over time interval           |
| Link Utilization          | % of assumed 10 Mbps link capacity      |
| Periodic Polling          | POX `Timer` (every 2 seconds)           |
| Network Emulation         | Mininet linear topology                 |

---
