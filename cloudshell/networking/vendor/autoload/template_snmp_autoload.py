__author__ = 'coye'

import os


class BrocadeSNMPAutoload(object):
    def __init__(self, snmp_handler, logger):
        self.snmp = snmp_handler
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mibs'))
        self.snmp.update_mib_sources(path)
        self._logger = logger

    def discover(self):
        """
        Loads device structure - chassis, modules, submodules, ports. And attributes for them
        :return: formatted string, matrixes separated by $ symbol.
                 Each matrix have column separator is ^ and row seprator is |
        :example:
         reources:
        Model^Name^Relative<QS_SP>Address^Unique<QS_SP>Identifier|Generic<QS_SP>Chassis^Chassis
        <QS_SP>0^0^|Generic<QS_SP>Port^GigabitEthernet0-1^0/24^|Generic<QS_SP>Port^GigabitEthernet0-2^0/25^
         attributes:
        ^System<QS_SP>Name^Boogie.Cisco2950|^OS<QS_SP>Version^12.1(22)EA14|
        ^Contact<QS_SP>Name^Omri|^Vendor^Cisco|^Location^|^Model^Catalyst2950t24|
        0^Serial<QS_SP>Number^FOC0713X1XA|0^Model^WS-C2950T-24|0/24^Auto<QS_SP>Negotiation^False|
        0/24^L2<QS_SP>Protocol<QS_SP>Type^ethernetCsmacd|0/24^Port<QS_SP>Description^|0/24^Duplex^Full|
        0/24^Bandwidth^10000000|0/24^MTU^1500|0/24^MAC<QS_SP>Address^00:0c:85:ae:67:99|
        0/24^IPv4<QS_SP>Address^|0/24^Adjacent^|0/24^IPv6<QS_SP>Address^|
        0/24^Protocol<QS_SP>Type^Transparent|
        """
        pass

