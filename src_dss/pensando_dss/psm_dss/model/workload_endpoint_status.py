"""
    Workload API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from pensando_dss.psm_dss.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from pensando_dss.psm_dss.model.workload_endpoint_migration_status import WorkloadEndpointMigrationStatus
    globals()['WorkloadEndpointMigrationStatus'] = WorkloadEndpointMigrationStatus


class WorkloadEndpointStatus(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'endpoint_state': (str,),  # noqa: E501
            'security_groups': ([str],),  # noqa: E501
            'homing_host_addr': (str,),  # noqa: E501
            'homing_host_name': (str,),  # noqa: E501
            'ipv4_address': (str,),  # noqa: E501
            'ipv4_addresses': ([str],),  # noqa: E501
            'ipv4_gateway': (str,),  # noqa: E501
            'ipv4_gateways': ([str],),  # noqa: E501
            'ipv6_address': (str,),  # noqa: E501
            'ipv6_addresses': ([str],),  # noqa: E501
            'ipv6_gateway': (str,),  # noqa: E501
            'ipv6_gateways': ([str],),  # noqa: E501
            'mac_address': (str,),  # noqa: E501
            'micro_segment_vlan': (int,),  # noqa: E501
            'migration': (WorkloadEndpointMigrationStatus,),  # noqa: E501
            'mirror_sessions': ([str],),  # noqa: E501
            'network': (str,),  # noqa: E501
            'node_uuid': (str,),  # noqa: E501
            'node_uuid_list': ([str],),  # noqa: E501
            'workload_attributes': ({str: (str,)},),  # noqa: E501
            'workload_name': (str,),  # noqa: E501
            'workload_names': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'endpoint_state': 'EndpointState',  # noqa: E501
        'security_groups': 'SecurityGroups',  # noqa: E501
        'homing_host_addr': 'homing-host-addr',  # noqa: E501
        'homing_host_name': 'homing-host-name',  # noqa: E501
        'ipv4_address': 'ipv4-address',  # noqa: E501
        'ipv4_addresses': 'ipv4-addresses',  # noqa: E501
        'ipv4_gateway': 'ipv4-gateway',  # noqa: E501
        'ipv4_gateways': 'ipv4-gateways',  # noqa: E501
        'ipv6_address': 'ipv6-address',  # noqa: E501
        'ipv6_addresses': 'ipv6-addresses',  # noqa: E501
        'ipv6_gateway': 'ipv6-gateway',  # noqa: E501
        'ipv6_gateways': 'ipv6-gateways',  # noqa: E501
        'mac_address': 'mac-address',  # noqa: E501
        'micro_segment_vlan': 'micro-segment-vlan',  # noqa: E501
        'migration': 'migration',  # noqa: E501
        'mirror_sessions': 'mirror-sessions',  # noqa: E501
        'network': 'network',  # noqa: E501
        'node_uuid': 'node-uuid',  # noqa: E501
        'node_uuid_list': 'node-uuid-list',  # noqa: E501
        'workload_attributes': 'workload-attributes',  # noqa: E501
        'workload_name': 'workload-name',  # noqa: E501
        'workload_names': 'workload-names',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """WorkloadEndpointStatus - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            endpoint_state (str): endpoint FSM state.. [optional]  # noqa: E501
            security_groups ([str]): security groups.. [optional]  # noqa: E501
            homing_host_addr (str): host address of the host where this endpoint exists.. [optional]  # noqa: E501
            homing_host_name (str): host name of the host where this endpoint exists.. [optional]  # noqa: E501
            ipv4_address (str): IPv4 address of the endpoint.. [optional]  # noqa: E501
            ipv4_addresses ([str]): IPv4 addresses of the endpoint.. [optional]  # noqa: E501
            ipv4_gateway (str): IPv4 gateway for the endpoint.. [optional]  # noqa: E501
            ipv4_gateways ([str]): IPv4 gateways for the endpoint.. [optional]  # noqa: E501
            ipv6_address (str): IPv6 address for the endpoint.. [optional]  # noqa: E501
            ipv6_addresses ([str]): IPv6 addresses for the endpoint.. [optional]  # noqa: E501
            ipv6_gateway (str): IPv6 gateway.. [optional]  # noqa: E501
            ipv6_gateways ([str]): IPv6 gateways.. [optional]  # noqa: E501
            mac_address (str): Mac address of the endpoint. Should be a valid MAC address.. [optional]  # noqa: E501
            micro_segment_vlan (int): micro-segment VLAN.. [optional]  # noqa: E501
            migration (WorkloadEndpointMigrationStatus): [optional]  # noqa: E501
            mirror_sessions ([str]): MirrorSessions list of mirror sessions enabled on this endpoint.. [optional]  # noqa: E501
            network (str): network this endpoint belogs to.. [optional]  # noqa: E501
            node_uuid (str): homing host's UUID.. [optional]  # noqa: E501
            node_uuid_list ([str]): NodeUUIDList has the list of DSCs where a EP is supposed to go to.. [optional]  # noqa: E501
            workload_attributes ({str: (str,)}): VM or container attribute/labels.. [optional]  # noqa: E501
            workload_name (str): VM or container name.. [optional]  # noqa: E501
            workload_names ([str]): WorkloadNames associated with endpoint.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
