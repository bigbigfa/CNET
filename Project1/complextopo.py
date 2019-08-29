from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import custom
																			
# Topology to be instantiated in Mininet
class ComplexTopo(Topo):
    "Mininet Complex Topology"

    def __init__(self, cpu=.1, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)


        # Host and link configuration
        hostConfig = {'cpu': cpu}
        linkConfig_ethernet = {'bw': 25, 'delay': '2ms', 'loss': 0,
                   'max_queue_size': max_queue_size }
        linkConfig_wifi = {'bw': 10, 'delay': '6ms', 'loss': 3,
                   'max_queue_size': max_queue_size }
        linkConfig_3g = {'bw': 3, 'delay': '10ms', 'loss': 8,
                   'max_queue_size': max_queue_size }

        # Hosts and switches
        h1 = self.addHost('h1', **hostConfig)
        h2 = self.addHost('h2', **hostConfig)
        h3 = self.addHost('h3', **hostConfig)

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Connection h1 to h2
        self.addLink(h1, s1, **linkConfig_ethernet)
        self.addLink(s1, s2, **linkConfig_ethernet)
        self.addLink(s2, s3, **linkConfig_ethernet)
        self.addLink(h2, s3, **linkConfig_wifi)

        # connection to h3
        self.addLink(s2, s4, **linkConfig_ethernet);
        self.addLink(h3, s4, **linkConfig_3g);



