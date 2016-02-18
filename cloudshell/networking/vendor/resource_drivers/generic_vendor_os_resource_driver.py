# required import! Contains handler map
import cloudshell.networking.vendor.resource_drivers
from cloudshell.shell.core.driver_builder_wrapper import DriverFunction
from cloudshell.networking.resource_driver.networking_generic_resource_dirver import networking_generic_resource_driver


class generic_vendor_os_resource_driver(networking_generic_resource_driver):
    @DriverFunction(extraMatrixRows={"resource": ["ResourceAddress", "User", "Password", "Enable Password",
                                                  "Console Server IP Address",
                                                  "Console User", "Console Password", "Console Port", "Connection Type",
                                                  "SNMP Version", "SNMP Read Community", "SNMP V3 User",
                                                  "SNMP V3 Password", "SNMP V3 Private Key"]})
    def Init(self, matrixJSON):
        self.handler_name = 'DEFAULT_HANDLER_NAME'
        networking_generic_resource_driver.Init(self, matrixJSON)

    # To suppress command just make them hidden
    @DriverFunction(category='Hidden Commands')
    def Add_VLAN(self, matrixJSON, ports, vlan_range, switchport_type, additional_info):
        pass
