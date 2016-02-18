__author__ = 'coye'

import os


class TemplateSNMPAutoload(object):
    def __init__(self, snmp_handler, logger):
        self.snmp = snmp_handler
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mibs'))
        self.snmp.update_mib_sources(path)
        self._logger = logger

    def discover(self):
        pass

