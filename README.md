# Computer Networks - Orange Problem
# SDN Multi-Switch Flow Table Analyzer (Mininet + POX)

---

##  Problem Statement

This project implements an SDN-based system to analyze flow table usage in switches. It identifies active and unused flow rules dynamically using an OpenFlow controller.

---

##  Objective

* Demonstrate controller–switch interaction
* Implement match–action flow rules
* Analyze network behavior
* Identify active vs unused flow rules

---

##  Tools Used

* Mininet
* POX Controller
* OpenFlow Protocol
* iperf

---

##  Topology

```
h1 --- s1 --- s2 --- s3 --- h2
           |       |
          h3      h4
```

---

##  Setup & Execution

### Start Controller

```bash
cd ~/pox
python3 pox.py flow_analyzer
```

### Start Mininet

```bash
sudo mn --custom topo.py --topo flowtopo --controller=remote,port=6633
```

---

##  OpenFlow Working

1. Switch connects to controller
2. Packet arrives → no rule → Packet-In
3. Controller processes packet
4. Flow rule installed (Flow-Mod)
5. Switch forwards traffic
6. Controller retrieves flow statistics

---

##  Test Scenarios

### Allowed Traffic

```bash
h2 ping h3
```

### Blocked Traffic

```bash
h1 ping h2
```

### Performance Test

```bash
iperf h2 h3
```

---

##  Expected Output

```
Switch 1 → Active: X, Unused: Y
Switch 2 → Active: X, Unused: Y
```

---

##  Observations

* Active flows increase with traffic
* Blocked traffic prevents rule installation
* Flow statistics show rule utilization
* Reactive flow setup may cause initial delay

---

##  Proof of Execution

Screenshots included:

* Topology setup
* Switch connection
* Allowed scenario
* Blocked scenario
* iperf output
* Flow analysis

---

##  References

* Mininet Documentation
* POX Documentation
* OpenFlow Specification

---

##  Conclusion

The project successfully demonstrates SDN concepts including flow rule installation, traffic control, and dynamic flow monitoring.

---

## Author
Nihira Hassan
4 B - AIML
