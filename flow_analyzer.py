from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.recoco import Timer
import logging

logging.getLogger("packet").setLevel(logging.CRITICAL)

log = core.getLogger()

switches = {}
mac_to_port = {}  # MAC learning table


# Switch Connection
def _handle_ConnectionUp(event):
    dpid = dpidToStr(event.dpid)
    switches[event.dpid] = event.connection
    mac_to_port[event.dpid] = {}
    log.info("Switch %s connected", dpid)


# Packet-In Handler
def _handle_PacketIn(event):
    try:
        packet = event.parsed
        if not packet:
            return

        dpid = event.dpid
        in_port = event.port

        # Ignore IPv6
        if packet.type == 0x86dd:
            return

        src = packet.src
        dst = packet.dst

        # Learn MAC address
        mac_to_port[dpid][src] = in_port

        # ❌ BLOCK only IP traffic from h1
        if str(src) == "00:00:00:00:00:01" and packet.type != 0x0806:
            log.info("Blocked IP traffic from %s", src)
            return

        # Determine output port
        if dst in mac_to_port[dpid]:
            out_port = mac_to_port[dpid][dst]
        else:
            out_port = of.OFPP_FLOOD

        # ✅ Install flow rule
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet, in_port)
        msg.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(msg)

        # ✅ Forward current packet
        msg2 = of.ofp_packet_out()
        msg2.data = event.ofp
        msg2.actions.append(of.ofp_action_output(port=out_port))
        event.connection.send(msg2)

    except Exception as e:
        log.error("Packet error handled: %s", e)


# Request Flow Stats
def request_stats():
    for conn in switches.values():
        req = of.ofp_stats_request(body=of.ofp_flow_stats_request())
        conn.send(req)


# Flow Stats Handler
def _handle_FlowStatsReceived(event):
    dpid = dpidToStr(event.connection.dpid)

    active = 0
    unused = 0

    for stat in event.stats:
        if stat.packet_count == 0 and stat.byte_count == 0:
            continue

        if stat.packet_count > 0:
            active += 1
        else:
            unused += 1

    print(f"Switch {dpid} → Active: {active}, Unused: {unused}")


# Launch Controller
def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    core.openflow.addListenerByName("FlowStatsReceived", _handle_FlowStatsReceived)

    Timer(20, request_stats, recurring=True)

    log.info("....Flow Analyzer Controller Started....")
