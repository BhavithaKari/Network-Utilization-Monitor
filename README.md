# 📡 SDN Network Utilization Monitor (POX + Mininet)

## 📌 Project Description

This project implements a Software Defined Networking (SDN) based Network Utilization Monitor using the POX controller and Mininet network emulator.

The controller periodically collects OpenFlow port statistics from switches, estimates bandwidth usage, calculates link utilization percentage, and displays results in real-time.

---

## 🎯 Key Features

- Collects byte counters from OpenFlow switches
- Estimates bandwidth usage (Mbps)
- Calculates link utilization (%)
- Updates statistics every 2 seconds
- Works with linear Mininet topology

---

## 🏗 System Architecture

Mininet Topology:

h1 ---- s1 ---- s2 ---- h2

Components:
- Hosts: h1, h2
- Switches: s1, s2 (OpenFlow-enabled)
- Controller: POX
- Protocol: OpenFlow 1.0

---

## ⚙ Technologies Used

- Ubuntu Linux
- Mininet
- POX Controller
- Python
- OpenFlow Protocol

---

## 🚀 Setup Instructions

### 1️⃣ Install Mininet

```bash
sudo apt update
sudo apt install mininet
