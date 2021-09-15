"""
    Fwlog API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from pensando_ent.psm_ent.model_utils import (  # noqa: F401
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
    from pensando_ent.psm_ent.model.api_object_meta import ApiObjectMeta
    globals()['ApiObjectMeta'] = ApiObjectMeta


class FwlogFwLog(ModelNormal):
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
        ('action',): {
            'ALLOW': "allow",
            'DENY': "deny",
            'REJECT': "reject",
            'IMPLICIT_DENY': "implicit_deny",
            'NONE': "none",
        },
        ('direction',): {
            'HOST': "from-host",
            'UPLINK': "from-uplink",
        },
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
            'action': (str,),  # noqa: E501
            'alg': (str,),  # noqa: E501
            'api_version': (str,),  # noqa: E501
            'app_id': (str,),  # noqa: E501
            'destination_ip': (str,),  # noqa: E501
            'destination_port': (int,),  # noqa: E501
            'destination_vrf': (str,),  # noqa: E501
            'direction': (str,),  # noqa: E501
            'flow_action': (str,),  # noqa: E501
            'icmp_code': (int,),  # noqa: E501
            'icmp_id': (int,),  # noqa: E501
            'icmp_type': (int,),  # noqa: E501
            'ipsec_protected': (bool,),  # noqa: E501
            'ipsec_rule_id': (str,),  # noqa: E501
            'kind': (str,),  # noqa: E501
            'meta': (ApiObjectMeta,),  # noqa: E501
            'policy_name': (str,),  # noqa: E501
            'protocol': (str,),  # noqa: E501
            'reporter_id': (str,),  # noqa: E501
            'rule_id': (str,),  # noqa: E501
            'session_id': (str,),  # noqa: E501
            'source_ip': (str,),  # noqa: E501
            'source_port': (int,),  # noqa: E501
            'source_vrf': (str,),  # noqa: E501
            'vnid': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'action': 'action',  # noqa: E501
        'alg': 'alg',  # noqa: E501
        'api_version': 'api-version',  # noqa: E501
        'app_id': 'app-id',  # noqa: E501
        'destination_ip': 'destination-ip',  # noqa: E501
        'destination_port': 'destination-port',  # noqa: E501
        'destination_vrf': 'destination-vrf',  # noqa: E501
        'direction': 'direction',  # noqa: E501
        'flow_action': 'flow-action',  # noqa: E501
        'icmp_code': 'icmp-code',  # noqa: E501
        'icmp_id': 'icmp-id',  # noqa: E501
        'icmp_type': 'icmp-type',  # noqa: E501
        'ipsec_protected': 'ipsec-protected',  # noqa: E501
        'ipsec_rule_id': 'ipsec-rule-id',  # noqa: E501
        'kind': 'kind',  # noqa: E501
        'meta': 'meta',  # noqa: E501
        'policy_name': 'policy-name',  # noqa: E501
        'protocol': 'protocol',  # noqa: E501
        'reporter_id': 'reporter-id',  # noqa: E501
        'rule_id': 'rule-id',  # noqa: E501
        'session_id': 'session-id',  # noqa: E501
        'source_ip': 'source-ip',  # noqa: E501
        'source_port': 'source-port',  # noqa: E501
        'source_vrf': 'source-vrf',  # noqa: E501
        'vnid': 'vnid',  # noqa: E501
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
        """FwlogFwLog - a model defined in OpenAPI

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
            action (str): Action.. [optional] if omitted the server will use the default value of "allow"  # noqa: E501
            alg (str): Appliction Layer Gateway.. [optional]  # noqa: E501
            api_version (str): [optional]  # noqa: E501
            app_id (str): Application ID.. [optional]  # noqa: E501
            destination_ip (str): Destination IP.. [optional]  # noqa: E501
            destination_port (int): Destination Port.. [optional]  # noqa: E501
            destination_vrf (str): Destination VRF,.. [optional]  # noqa: E501
            direction (str): Flow Direction.. [optional] if omitted the server will use the default value of "from-host"  # noqa: E501
            flow_action (str): Flow action.. [optional]  # noqa: E501
            icmp_code (int): icmp code.. [optional]  # noqa: E501
            icmp_id (int): icmp ID.. [optional]  # noqa: E501
            icmp_type (int): icmp type.. [optional]  # noqa: E501
            ipsec_protected (bool): If IPsec protected.. [optional]  # noqa: E501
            ipsec_rule_id (str): IPsec policy rule ID.. [optional]  # noqa: E501
            kind (str): [optional]  # noqa: E501
            meta (ApiObjectMeta): [optional]  # noqa: E501
            policy_name (str): policy name.. [optional]  # noqa: E501
            protocol (str): Protocol,.. [optional]  # noqa: E501
            reporter_id (str): Reporter ID.. [optional]  # noqa: E501
            rule_id (str): Rule ID.. [optional]  # noqa: E501
            session_id (str): Session ID.. [optional]  # noqa: E501
            source_ip (str): Source IP,.. [optional]  # noqa: E501
            source_port (int): Source Port.. [optional]  # noqa: E501
            source_vrf (str): Source VRF,.. [optional]  # noqa: E501
            vnid (str): VXLAN ID.. [optional]  # noqa: E501
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
