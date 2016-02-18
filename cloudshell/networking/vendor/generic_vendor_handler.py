__author__ = 'g8y3e'
import socket

from cloudshell.cli import expected_actions
from cloudshell.networking.networking_handler_interface import NetworkingHandlerInterface
from cloudshell.shell.core.handler_base import HandlerBase
from cloudshell.networking.vendor.command_templates.template_interface import TemplateInterface
from cloudshell.networking.vendor.autoload.template_snmp_autoload import BrocadeSNMPAutoload
from cloudshell.api.cloudshell_api import CloudShellAPISession


class GenericVendorHandler(HandlerBase, NetworkingHandlerInterface):
    # Here you can specify what action will be performed in case we got certain output from device:
    EXPECTED_MAP = {'Username: *$|Login: *$': expected_actions.send_username,
                    'closed by remote host': expected_actions.do_reconnect,
                    'continue connecting': expected_actions.send_yes,
                    'Got termination signal': expected_actions.wait_prompt_or_reconnect,
                    'Broken pipe': expected_actions.send_command,
                    '[Yy]es': expected_actions.send_yes,
                    'More': expected_actions.send_empty_string,
                    '[Pp]assword: *$': expected_actions.send_password
                    }
    SPACE = '<QS_SP>'
    RETURN = '<QS_CR>'
    NEWLINE = '<QS_LF>'

    def __init__(self, connection_manager, logger=None):
        HandlerBase.__init__(self, connection_manager, logger)
        self._prompt = '.*[>#] *$'
        self.snmp_handler = None

        # make sure prompt variable corresponds to prompt on your device, otherwise it wont work

    # Here you can add some generic methods for all vendor operation systems, and implement the mandatory methods, see
    # examples below:

    def normalize_output(self, output):
        return output.replace(' ', self.SPACE).replace('\r\n', self.NEWLINE).replace('\n', self.NEWLINE). \
            replace('\r', self.NEWLINE)

    def add_vlan(self, vlan_range, port_list, port_mode, additional_info):
        """
        Add Vlan on the remote device
        :param vlan_range: range of vlans to be added, if empty, and switchport_type = trunk,
        trunk mode will be assigned
        :param port_list: List of interfaces Resource Full Address
        :param port_mode: type of adding vlan ('trunk' or 'access')
        :param additional_info: contains QNQ or CTag parameter
        :return: success message
        :rtype: string
        """
        self._logger.info('Vlan Configuration Started')
        params_map = dict()
        port_name = 'name'
        params_map['template_command'] = port_name
        self.configure_port(**params_map)
        self._logger.info('Vlan {0} was assigned to the interface {1}'.format(vlan_range, port_name))
        return 'Vlan Configuration Completed'

    def remove_vlan(self, vlan_range, port_list, port_mode, additional_info):
        """
        Remove Vlan on the remote device
        :param vlan_range: range of vlans to be added, if empty, and switchport_type = trunk,
        trunk mode will be assigned
        :param port_list: List of interfaces Resource Full Address
        :param port_mode: type of adding vlan ('trunk' or 'access')
        :param additional_info: contains QNQ or CTag parameter
        :return: success message
        :rtype: string
        """
        self._logger.info('Vlan Configuration Started')
        params_map = dict()
        port_name = 'name'
        params_map['template_command'] = port_name
        self.configure_port(**params_map)
        self._logger.info('All vlans and interface mode were removed from the interface {0}'.format(port_name))
        return 'Vlan Configuration Completed'

    def cloud_shell_api(self):
        if not self._cloud_shell_api:
            hostname = socket.gethostname()
            testshell_ip = socket.gethostbyname(hostname)
            testshell_user = self.reservation_dict['AdminUsername']
            testshell_password = self.reservation_dict['AdminPassword']
            testshell_domain = self.reservation_dict['Domain']
            self._cloud_shell_api = CloudShellAPISession(testshell_ip, testshell_user, testshell_password,
                                                         testshell_domain)
        return self._cloud_shell_api

    def configure_port(self, **kwargs):
        """
        Configures interface ethernet
        :param kwargs: dictionary of parameters
        :return: success message
        :rtype: string
        """
        port = TemplateInterface()
        commands_list = port.get_commands_list(**kwargs)
        for command in commands_list:
            self._send_command(command)

        return 'Finished configuration of ethernet interface!'

    def discover_snmp(self):
        """Load device structure, and all required Attribute according to Networking Elements Standardization design
        :return: Attributes and Resources matrix,
        currently in string format (matrix separated by '$', lines by '|', columns by ',')
        """
        self._logger.info('************************************************************************')
        self._logger.info('Start SNMP discovery process .....')
        generic_autoload = BrocadeSNMPAutoload(self.snmp_handler, self._logger)
        result = generic_autoload.discover()
        self._logger.info('Start SNMP discovery Completed')
        return result

    def update_firmware(self, remote_host, file_path):
        """Update firmware version on device by loading provided image, performs following steps:

            1. Copy bin file from remote tftp server.
            2. Clear in run config boot system section.
            3. Set downloaded bin file as boot file and then reboot device.
            4. Check if firmware was successfully installed.

        :param remote_host: host with firmware
        :param file_path: relative path on remote host
        :return: status / exception
        """
        pass

    def backup_configuration(self, destination_host, source_filename):
        """Backup 'startup-config' or 'running-config' from device to provided file_system [ftp|tftp]
        Also possible to backup config to localhost

        :param destination_host:  tftp/ftp server where file be saved
        :param source_filename: what file to backup
        :return: status message / exception
        """
        pass

    def restore_configuration(self, source_file, clear_config='override'):
        """Restore configuration on device from provided configuration file
        Restore configuration from local file system or ftp/tftp server into 'running-config' or 'startup-config'.
        :param source_file: relative path to the file on the remote host tftp://server/sourcefile
        :param clear_config: override current config or not
        :return:
        """
        pass

    def send_command(self, cmd, expected_str=None, timeout=30):
        """Send command to the device
        :param cmd: command you want to send
        :param expected_str: expected prompt
        :param timeout: timeout
        :return: output from device / exception
        """
        pass
