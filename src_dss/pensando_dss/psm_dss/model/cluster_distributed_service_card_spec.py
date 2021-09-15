"""
    Cluster API reference

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
    from pensando_dss.psm_dss.model.cluster_fwlog_policy_ref import ClusterFwlogPolicyRef
    from pensando_dss.psm_dss.model.cluster_ip_config import ClusterIPConfig
    from pensando_dss.psm_dss.model.cluster_policer_ref import ClusterPolicerRef
    globals()['ClusterFwlogPolicyRef'] = ClusterFwlogPolicyRef
    globals()['ClusterIPConfig'] = ClusterIPConfig
    globals()['ClusterPolicerRef'] = ClusterPolicerRef


class ClusterDistributedServiceCardSpec(ModelNormal):
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
        ('mgmt_mode',): {
            'HOST': "host",
            'NETWORK': "network",
        },
        ('network_mode',): {
            'OOB': "oob",
            'INBAND': "inband",
        },
    }

    validations = {
        ('mgmt_vlan',): {
            'inclusive_maximum': 4095,
            'inclusive_minimum': 0,
        },
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
            'admit': (bool,),  # noqa: E501
            'controllers': ([str],),  # noqa: E501
            'dscprofile': (str,),  # noqa: E501
            'enable_fw_logging': (bool,),  # noqa: E501
            'enable_secure_boot': (bool,),  # noqa: E501
            'fwlog_policy': (ClusterFwlogPolicyRef,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'ip_config': (ClusterIPConfig,),  # noqa: E501
            'mgmt_mode': (str,),  # noqa: E501
            'mgmt_vlan': (int,),  # noqa: E501
            'network_mode': (str,),  # noqa: E501
            'policer': (ClusterPolicerRef,),  # noqa: E501
            'routing_config': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'admit': 'admit',  # noqa: E501
        'controllers': 'controllers',  # noqa: E501
        'dscprofile': 'dscprofile',  # noqa: E501
        'enable_fw_logging': 'enable-fw-logging',  # noqa: E501
        'enable_secure_boot': 'enable-secure-boot',  # noqa: E501
        'fwlog_policy': 'fwlog-policy',  # noqa: E501
        'id': 'id',  # noqa: E501
        'ip_config': 'ip-config',  # noqa: E501
        'mgmt_mode': 'mgmt-mode',  # noqa: E501
        'mgmt_vlan': 'mgmt-vlan',  # noqa: E501
        'network_mode': 'network-mode',  # noqa: E501
        'policer': 'policer',  # noqa: E501
        'routing_config': 'routing-config',  # noqa: E501
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
        """ClusterDistributedServiceCardSpec - a model defined in OpenAPI

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
            admit (bool): Admit allows a DistributedServiceCard to join the cluster.. [optional]  # noqa: E501
            controllers ([str]): Controllers contains the list of remote controllers IP addresses or hostnames.. [optional]  # noqa: E501
            dscprofile (str): [optional]  # noqa: E501
            enable_fw_logging (bool): EnableFwLogging enables flow logging on the device.. [optional]  # noqa: E501
            enable_secure_boot (bool): EnableSecureBoot a true value indicates, set lifecycle fuse to enable secure boot.. [optional] if omitted the server will use the default value of False  # noqa: E501
            fwlog_policy (ClusterFwlogPolicyRef): [optional]  # noqa: E501
            id (str): ID is used as a user friendly identifier in logs/events.. [optional]  # noqa: E501
            ip_config (ClusterIPConfig): [optional]  # noqa: E501
            mgmt_mode (str): MgmtMode defines the management mode of the DistributedServiceCard.. [optional] if omitted the server will use the default value of "host"  # noqa: E501
            mgmt_vlan (int): MgmtVlan defines the vlan to be used in network managed mode. The default of 0 means we use untagged-vlan for doing inband management. Value should be between 0 and 4095.. [optional]  # noqa: E501
            network_mode (str): MgmtMode defines the management mode of the DistributedServiceCard.. [optional] if omitted the server will use the default value of "oob"  # noqa: E501
            policer (ClusterPolicerRef): [optional]  # noqa: E501
            routing_config (str): RoutingConfig is the routing configuration for the underlay routed network that this DSC participates in.. [optional]  # noqa: E501
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
