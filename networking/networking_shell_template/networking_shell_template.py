from cloudshell.shell.core.driver_context import *
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.networking.networking_resource_driver_interface import NetworkingResourceDriverInterface


class NetworkingShellTemplate(ResourceDriverInterface, NetworkingResourceDriverInterface):
    def __init__(self):
        pass

    # Initialize the driver session, this function is called everytime a new instance of the driver is created
    # This is a good place to load and cache the driver configuration, initiate sessions etc.
    def initialize(self, context):
        """
        :type context: qualidriver.InitCommandContext
        """
        return 'Finished initializing'

    # Destroy the driver session, this function will be called each time a driver instance should be destroyed
    # This is a good place to close any open sessions, finish writing to log files
    def cleanup(self):
        """
        Close sessions, logger, etc.
        """
        pass

    # When the auto load function is triggered, CloudShell will call the get_inventory function
    # The function should discover the resource hierarchy and return back to CloudShell an instance of AutoLoadDetails
    # which includes details about the resource hierarchy and attributes
    def get_inventory(self, context):
        """
        Return device structure with all standard attributes
        :type context: qualidriver.AutoLoadCommandContext
        :return: result
        :rtype: AutoLoadDetails
        """
        resource1 = AutoLoadResource('Generic Chassis', 'Chassis 1', '1')
        resource2 = AutoLoadResource('Generic Module', 'Module 1', '1/1')
        resource3 = AutoLoadResource('Generic Port', 'Port 1', '1/1/1')
        resource4 = AutoLoadResource('Generic Port', 'Port 2', '1/1/2')
        resource5 = AutoLoadResource('Generic Power Port', 'Power Port', '1/PP1')

        resources = [resource1, resource2, resource3, resource4, resource5]

        a_root1 = AutoLoadAttribute('', 'Location', 'Santa Clara Lab')
        a_root2 = AutoLoadAttribute('', 'Model', 'Catalyst 3850')
        a_root3 = AutoLoadAttribute('', 'Vendor', 'Cisco')
        a1 = AutoLoadAttribute('1', 'Serial Number', 'JAE053002JD')
        a2 = AutoLoadAttribute('1', 'Model', 'WS-X4232-GB-RJ')
        a3 = AutoLoadAttribute('1/1', 'Model', 'WS-X4233-GB-EJ')
        a4 = AutoLoadAttribute('1/1', 'Serial Number', 'RVE056702UD')
        a5 = AutoLoadAttribute('1/1/1', 'Mac_Address', 'fe80::e10c:f055:f7f1:bb7t16')
        a6 = AutoLoadAttribute('1/1/1', 'IPv4 Address', '192.168.10.7')
        a7 = AutoLoadAttribute('1/1/2', 'Mac_Address', 'te67::e40c:g755:f55y:gh7w36')
        a8 = AutoLoadAttribute('1/1/2', 'IPv4 Address', '192.168.10.9')
        a9 = AutoLoadAttribute('1/PP1', 'Model', 'WS-X4232-GB-RJ')
        a10 = AutoLoadAttribute('1/PP1', 'Port Description', 'Power')
        a11 = AutoLoadAttribute('1/PP1', 'Serial Number', 'RVE056702UD')

        attributes = [a_root1, a_root2, a_root3, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]

        result = AutoLoadDetails(resources, attributes)
        return result

    # Used for old connectivity solutions
    def add_vlan(self, context, port, VLAN_Ranges, VLAN_Mode, Additional_Info='', qnq='', ctag=''):
        """
        Add Vlan to the interface, used for old connectivity solutions
        """
        pass

    # Used for old connectivity solutions
    def remove_vlan(self, context, port, VLAN_Ranges, VLAN_Mode, Additional_Info='', qnq='', ctag=''):
        """
        Remove Vlan to the interface, used for old connectivity solutions
        """
        pass

    # Send command to the device
    def send_custom_command(self, context, command):
        """
        Send command
        """
        pass

    # Save startup or running configuration to remote ftp
    def save(self, context, folder_path, configuration_type):
        """
        Upload startup/running configuration
        """
        filename = '<FILENAME>,'
        return filename

    # Restore startup or running configurations from path
    def restore(self, context, path, restore_method):
        """
        Upload and updates firmware on the resource
        """
        pass

    # Loads and updates firmware on the remote device
    def load_firmware(self, context, remote_host, file_path):
        """
        Upload and updates firmware on the resource
        """
        pass

    # Used for the latest connectivity solution
    def apply_connectivity_changes(self, context, json):
        """
        Add or Remove Vlans to the certain interfaces
        """
        output_json = """JSON HERE"""
        return output_json

    # Graceful shutdown of the device
    def shutdown(self):
        """
        Shutdown remote device
        """
        pass
