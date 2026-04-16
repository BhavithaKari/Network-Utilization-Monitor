from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.recoco import Timer
import time

log = core.getLogger()

class NetworkMonitor(object):

    def __init__(self, connection):
        self.connection = connection
        self.dpid = connection.dpid
        self.prev_stats = {}
        self.prev_time = time.time()

        connection.addListeners(self)
        Timer(2, self._request_stats, recurring=True)

        log.info("Switch %s connected", dpidToStr(self.dpid))

    def _request_stats(self):
        self.connection.send(of.ofp_port_stats_request())

    def _handle_PortStatsReceived(self, event):
        current_time = time.time()
        time_diff = current_time - self.prev_time
        self.prev_time = current_time

        for stat in event.stats:
            port_no = stat.port_no

            if port_no > 65534:
                continue

            total_bytes = stat.rx_bytes + stat.tx_bytes

            if port_no in self.prev_stats:
                byte_diff = total_bytes - self.prev_stats[port_no]

                bandwidth_bps = (byte_diff * 8.0) / time_diff
                bandwidth_mbps = bandwidth_bps / (1024 * 1024)

                link_capacity = 10  # Assume 10 Mbps link
                utilization = (bandwidth_mbps / link_capacity) * 100

                log.info("Switch %s | Port %s | %.2f Mbps | Utilization: %.2f%%",
                         dpidToStr(self.dpid),
                         port_no,
                         bandwidth_mbps,
                         utilization)

            self.prev_stats[port_no] = total_bytes


def launch():
    def start_switch(event):
        NetworkMonitor(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
    log.info("Network Utilization Monitor Started")
