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

**Verify Mininet:**
```bash
sudo mn --test pingall
```
> If hosts ping each other → Mininet is working ✔

---

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

> Leave this terminal open.

---

### ✅ Step 5 — Start Mininet (New Terminal)

```bash
sudo mn --topo linear,2 --controller remote,ip=127.0.0.1,port=6633
```

**Expected output:**
```
*** Starting CLI:
mininet>
```

---

### ✅ Step 6 — Generate Traffic

**Small traffic test (inside Mininet CLI):**
```
mininet> pingall
```

**High traffic test:**
```
mininet> iperf h1 h2
```

**Example output in POX terminal:**
```
Switch 00-00-00-00-00-01 | Port 1 | 8.45 Mbps | Utilization: 84.5%
```

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
