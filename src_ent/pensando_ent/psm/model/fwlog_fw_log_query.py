"""
    Fwlog API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from pensando_ent.psm.model_utils import (  # noqa: F401
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


class FwlogFwLogQuery(ModelNormal):
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
        ('encryption_status',): {
            'ALL': "all",
            'IPSECPROTECTED': "ipsecprotected",
        },
        ('scroll_action',): {
            'NONE': "none",
            'REFRESH': "refresh",
            'DELETE': "delete",
        },
        ('sort_order',): {
            'ASCENDING': "ascending",
            'DESCENDING': "descending",
        },
    }

    validations = {
        ('max_results',): {
            'inclusive_maximum': 8192,
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
        return {
            'actions': ([str],),  # noqa: E501
            'batch_size': (int,),  # noqa: E501
            'count_only': (bool,),  # noqa: E501
            'destination_ips': ([str],),  # noqa: E501
            'destination_ports': ([int],),  # noqa: E501
            'encryption_status': (str,),  # noqa: E501
            'end_time': (datetime,),  # noqa: E501
            'max_results': (int,),  # noqa: E501
            'protocols': ([str],),  # noqa: E501
            'reporter_ids': ([str],),  # noqa: E501
            'scroll_action': (str,),  # noqa: E501
            'scroll_expiry': (str,),  # noqa: E501
            'scroll_id': (str,),  # noqa: E501
            'sort_order': (str,),  # noqa: E501
            'source_ips': ([str],),  # noqa: E501
            'source_ports': ([int],),  # noqa: E501
            'start_time': (datetime,),  # noqa: E501
            'tenants': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'actions': 'actions',  # noqa: E501
        'batch_size': 'batch-size',  # noqa: E501
        'count_only': 'count-only',  # noqa: E501
        'destination_ips': 'destination-ips',  # noqa: E501
        'destination_ports': 'destination-ports',  # noqa: E501
        'encryption_status': 'encryption-status',  # noqa: E501
        'end_time': 'end-time',  # noqa: E501
        'max_results': 'max-results',  # noqa: E501
        'protocols': 'protocols',  # noqa: E501
        'reporter_ids': 'reporter-ids',  # noqa: E501
        'scroll_action': 'scroll-action',  # noqa: E501
        'scroll_expiry': 'scroll-expiry',  # noqa: E501
        'scroll_id': 'scroll-id',  # noqa: E501
        'sort_order': 'sort-order',  # noqa: E501
        'source_ips': 'source-ips',  # noqa: E501
        'source_ports': 'source-ports',  # noqa: E501
        'start_time': 'start-time',  # noqa: E501
        'tenants': 'tenants',  # noqa: E501
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
        """FwlogFwLogQuery - a model defined in OpenAPI

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
            actions ([str]): OR of actions to be matched. Only one action can be specified and can only be specified if either source IP or destination IP is present.. [optional]  # noqa: E501
            batch_size (int): BatchSize is the number of results returned in one batch while scrolling.. [optional] if omitted the server will use the default value of 25  # noqa: E501
            count_only (bool): if set, returns only number of hits for the search query and not flow logs. Number of hits are greater than or equal to TotalCount value returned in list-meta.. [optional]  # noqa: E501
            destination_ips ([str]): OR of destination IPs to be matched. Only one destination IP is allowed. Should be a valid v4 or v6 IP address.. [optional]  # noqa: E501
            destination_ports ([int]): OR of destination ports to be matched. Only one port can be specified and if present, destination IP must also be specified. Value should be between 0 and 65535.. [optional]  # noqa: E501
            encryption_status (str): if set, search logs that match the specified encryption status.. [optional] if omitted the server will use the default value of "all"  # noqa: E501
            end_time (datetime): EndTime selects all logs with timestamp less than the EndTime, example 2018-09-18T00:12:00Z.. [optional]  # noqa: E501
            max_results (int): MaxResults is the max-count of search results Default value is 50 and valid range is 0..8192. Value should be between 0 and 8192.. [optional] if omitted the server will use the default value of 50  # noqa: E501
            protocols ([str]): OR of protocols to be matched. Only one protocol can be specified and can only be specified if either source IP or destination IP is present.. [optional]  # noqa: E501
            reporter_ids ([str]): OR of reporter names to be matched. Only one reporter ID can be specified.. [optional]  # noqa: E501
            scroll_action (str): ScrollAction specifies actions related to scroll if its duration needs to be extended or scroll needs to be deleted.. [optional] if omitted the server will use the default value of "none"  # noqa: E501
            scroll_expiry (str): ScrollExpiry is time duration after which scroll id expires. Default is 5 min. A duration string is a sequence of decimal number and a unit suffix, such as \"300ms\" or \"2h45m\". Valid time units are \"ns\", \"us\" (or \"µs\"), \"ms\", \"s\", \"m\", \"h\". Subsequent requests with a scroll id resets the timer for expiry. Should be a valid time duration.. [optional] if omitted the server will use the default value of "5m"  # noqa: E501
            scroll_id (str): ScrollID to scroll through results fetched by an earlier query.. [optional]  # noqa: E501
            sort_order (str): SortOrder specifies time ordering of results.. [optional] if omitted the server will use the default value of "descending"  # noqa: E501
            source_ips ([str]): OR of sources IPs to be matched. Only one source IP is allowed. Should be a valid v4 or v6 IP address.. [optional]  # noqa: E501
            source_ports ([int]): OR of source ports to be matched. Only one port can be specified and if present, source IP must also be specified. Value should be between 0 and 65535.. [optional]  # noqa: E501
            start_time (datetime): StartTime selects all logs with timestamp greater than the StartTime, example 2018-10-18T00:12:00Z.. [optional]  # noqa: E501
            tenants ([str]): OR of tenants within the scope of which search needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can search fwlogs in their tenant scope only.. [optional]  # noqa: E501
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
