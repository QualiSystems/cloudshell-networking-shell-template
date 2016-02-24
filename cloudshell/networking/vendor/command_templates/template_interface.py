__author__ = 'g8y3e'

from abc import ABCMeta
from abc import abstractmethod

from cloudshell.networking.parameters_service.command_template import CommandTemplate
from cloudshell.networking.parameters_service.parameters_service import ParametersService
from cloudshell.networking.command_template_base import InterfaceBase

class TemplateInterface(InterfaceBase):
    __metaclass__ = ABCMeta

    COMMANDS_TEMPLATE = {
        'template_command': CommandTemplate('Enter your command here and replace incoming varaibles with {0}' +
                                            ', {1}, etc., i.e. configure interface {0}',
                                            r'\w+\s*[0-9/]+',#enter regexp or method to validate input parameters
                                            'Enter error message if validation fails')
    }

    @abstractmethod
    def get_commands_list(self, **kwargs):
        prepared_commands = []

        if 'template_command' not in kwargs:
            raise Exception('Need to set template_command parameter!')

        command_template = TemplateInterface.COMMANDS_TEMPLATE['template_command']
        prepared_commands.append(ParametersService.get_validate_list(command_template, [kwargs['template_command']]))

        return prepared_commands
