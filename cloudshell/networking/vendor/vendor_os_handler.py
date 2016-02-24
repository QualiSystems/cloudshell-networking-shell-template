__author__ = 'g8y3e'

from cloudshell.networking.vendor.generic_vendor_handler import GenericVendorHandler
from cloudshell.cli import expected_actions
from cloudshell.api.cloudshell_api import CloudShellAPISession


class VendorOSHandler(GenericVendorHandler):
    def __init__(self, connection_manager, logger):
        GenericVendorHandler.__init__(self, connection_manager, logger)

    # OS specific methods and override methods from parent class could be added here
