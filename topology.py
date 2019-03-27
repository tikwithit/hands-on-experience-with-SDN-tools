from mininet.topo import Topo 
from mininet.net import Mininet 
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


from mininet.topo import Topo

class FirstTopo(Topo):
	def build(self):
        
        # Create templates
        abouthost = {'inNamespace':True}
        bw_one = {'bw': 1}
        bw_two = {'bw': 10}
        
        # Create host nodes (h1, h2, h3, h4)
        for i in range(4):
            self.addHost('h%d' % (i+1), **abouthost)

        # Create switch nodes
        self.addSwitch('s1',dpid='0000000000000001')
        self.addSwitch('s2',dpid='0000000000000002')
        self.addSwitch('s3',dpid='0000000000000003')
        self.addSwitch('s4',dpid='0000000000000004')

        
        # Add switch links 
        self.addLink('s1', 's2', **bw_one)
        self.addLink('s2', 's4', **bw_one)
        self.addLink('s1', 's3', **bw_two)
        self.addLink('s3', 's4', **bw_two)

        # Add host links
        self.addLink('h1', 's1')
        self.addLink('h2', 's1')
        self.addLink('h3', 's4')
        self.addLink('h4', 's4')

topos = { 'mytopo': ( lambda: FirstTopo())}

