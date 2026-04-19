Computer Networks - Orange Problem SDN Multi-Switch Flow Table Analyzer
(POX + Mininet)

------------------------------------------------------------------------

Overview This project implements a Software Defined Networking (SDN)
solution using the POX controller and Mininet emulator.

The system dynamically: - Controls network traffic - Installs flow rules
in switches - Monitors flow table usage - Enforces a security policy by
blocking a specific host (h1)

------------------------------------------------------------------------

Key Features - Flow table analysis across multiple switches
- Real-time monitoring of active and unused flows
- Traffic filtering (blocks host h1)
- MAC learning for efficient forwarding
- Dynamic flow rule installation
- Performance testing using iperf

------------------------------------------------------------------------

Problem Statement In SDN, switches rely on flow tables for packet
forwarding. However, there is limited visibility into how effectively
these flow rules are utilized.

This project provides: - Real-time insight into flow usage
- Identification of active vs unused rules
- Analysis of network behavior under different traffic conditions

------------------------------------------------------------------------

Objectives - Demonstrate controller–switch interaction using OpenFlow
- Implement match–action flow rules
- Analyze flow table utilization dynamically
- Enforce traffic control policies (blocking h1)
- Evaluate network performance

------------------------------------------------------------------------

Tools & Technologies - Mininet – Network emulation
- POX Controller – SDN controller
- OpenFlow Protocol – Communication layer
- Python – Controller implementation
- iperf – Performance testing

------------------------------------------------------------------------

Network Topology

h1 — s1 — s2 — s3 — h2 | | h3 h4

------------------------------------------------------------------------

Setup & Execution

1.  Start POX Controller cd ~/pox sudo ./pox.py misc.flow_analyzer

2.  Start Mininet (New Terminal) cd
    ~/CN-SDN sudo mn –custom topo.py
    –topo flowtopo –controller remote,port=6633

------------------------------------------------------------------------

How It Works 1. Switch connects to controller
2. Packet arrives at switch
3. No matching rule → Packet sent to controller
4. Controller learns MAC and decides action
5. Controller installs flow rule
6. Current packet forwarded
7. Future packets handled by switch
8. Controller collects flow statistics

------------------------------------------------------------------------

Flow Rule Logic - Match: Source MAC, destination MAC, input port
- Action: Forward / Flood / Drop
- Counters: Packet and byte count

------------------------------------------------------------------------

Test Scenarios

Allowed Traffic: mininet> h2 ping h3

Blocked Traffic: mininet> h1 ping h2

Performance Test: mininet> h3 iperf -s & mininet> h2 iperf -c h3

------------------------------------------------------------------------

Observations - First packet delay due to controller
- Faster communication after flow installation
- MAC learning reduces flooding
- Blocking isolates h1
- Flow stats show usage

------------------------------------------------------------------------

Conclusion This project demonstrates: - Centralized SDN control
- Dynamic flow rule installation
- Traffic filtering
- Efficient forwarding
- Real-time monitoring

------------------------------------------------------------------------

Author Vismay Chandra Dev Sem 4 - J Computer Networks (SDN Project)
