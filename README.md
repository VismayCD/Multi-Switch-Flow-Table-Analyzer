# Computer Networks - Orange Problem
# SDN Multi-Switch Flow Table Analyzer (Mininet + POX)

---

## Problem Statement

In Software Defined Networking (SDN), switches use flow tables to decide how packets are forwarded. However, there is no direct mechanism to analyze how effectively these flow rules are used.

This project implements an SDN-based **Multi-Switch Flow Table Analyzer** that:

* Retrieves flow entries from switches
* Displays rule usage
* Identifies active vs unused rules
* Dynamically monitors flow behavior
  
---

## Objective

* Demonstrate **controller–switch interaction** using OpenFlow
* Implement **match–action flow rules**
* Analyze **flow table usage dynamically**
* Demonstrate **network behavior (allowed vs blocked traffic)**

---

## Tools & Technologies

* **Mininet** – Network emulation
* **POX Controller** – SDN controller
* **OpenFlow Protocol** – Communication between controller & switches
* **iperf** – Performance testing
* **Python** – Implementation

---

## Network Topology

```
h1 --- s1 --- s2 --- s3 --- h2
           |       |
          h3      h4
```

---

##  Setup & Execution

### Start POX Controller 

```bash
cd ~/pox
python3 pox.py flow_analyzer
```

### Start Mininet In Another Terminal

```bash
cd ~
sudo mn --custom topo.py --topo flowtopo --controller=remote,port=6633
```

---

##  OpenFlow Working

1. Switch connects to controller
2. Packet arrives at switch
3. No matching rule → **Packet-In** sent to controller
4. Controller processes packet
5. Decision made (allow or block)
6. Controller installs rule using **Flow-Mod**
7. Switch forwards packets
8. Controller periodically requests **Flow Stats**
9. Switch replies with statistics
10. Controller analyzes rule usage

---

##  Test Scenarios

### Allowed Traffic

```bash
mininet> h2 ping h3
```
✔ Communication successful

### Blocked Traffic

```bash
mininet> h1 ping h2
```
✔ Communication fails (blocked by controller)

### Performance Test

```bash
mininet> iperf h2 h3
```
✔ Generates high traffic for analysis

---

##  Expected Output

```
Switch 1 → Active: X, Unused: Y
Switch 2 → Active: X, Unused: Y
```

---

##  Observations

* Active flow count increases with traffic
* Blocked traffic prevents rule installation
* Initial packet loss occurs due to reactive flow setup
* Flow statistics enable identification of rule utilization

---

##  Proof of Execution

Screenshots included:

* Topology setup
  ![UI](screenshots/Topology.png)
* Switch connection
  ![UI](screenshots/ControllerSwitchConnection.png)
* Allowed scenario
  ![UI](screenshots/AllowedScenario.png)
* Blocked scenario
  ![UI](screenshots/BlockedScenario.png)
* iperf output
  ![UI](screenshots/PerformanceTest.png)
* Flow analysis
  ![UI](screenshots/FlowAnalysis.png)
* pingall
  ![UI](screenshots/pingall.png)

---

##  References

* Mininet Documentation
* POX Controller Documentation
* OpenFlow Specification

---

##  Conclusion

This project successfully demonstrates an SDN-based solution that:
* Implements dynamic flow rule installation
* Enables real-time monitoring of flow usage
* Provides traffic control using controller logic

---

## Author
Nihira Hassan
4 B - AIML
