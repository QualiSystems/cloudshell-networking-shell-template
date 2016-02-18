from pkgutil import extend_path

from cloudshell.networking.vendor.vendor_os_handler import VendorOSHandler
from cloudshell.shell.core.handler_factory import HandlerFactory

__path__ = extend_path(__path__, __name__)
# Make sure handler names are equal to the device names in template resource_drivers_map
HandlerFactory.handler_classes['HANDLER_NAME_HERE'] = VendorOSHandler
