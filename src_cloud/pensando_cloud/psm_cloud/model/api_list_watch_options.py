"""
    Workload API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from pensando_cloud.psm_cloud.model_utils import (  # noqa: F401
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


class ApiListWatchOptions(ModelNormal):
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
        ('sort_order',): {
            'NONE': "none",
            'BY-NAME': "by-name",
            'BY-NAME-REVERSE': "by-name-reverse",
            'BY-VERSION': "by-version",
            'BY-VERSION-REVERSE': "by-version-reverse",
            'BY-CREATION-TIME': "by-creation-time",
            'BY-CREATION-TIME-REVERSE': "by-creation-time-reverse",
            'BY-MOD-TIME': "by-mod-time",
            'BY-MOD-TIME-REVERSE': "by-mod-time-reverse",
        },
    }

    validations = {
        ('name',): {
            'max_length': 64,
        },
        ('namespace',): {
            'max_length': 64,
        },
        ('tenant',): {
            'max_length': 48,
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
            'creation_time': (datetime,),  # noqa: E501
            'field_change_selector': ([str],),  # noqa: E501
            'field_selector': (str,),  # noqa: E501
            '_from': (int,),  # noqa: E501
            'generation_id': (str,),  # noqa: E501
            'label_selector': (str,),  # noqa: E501
            'labels': ({str: (str,)},),  # noqa: E501
            'max_results': (int,),  # noqa: E501
            'mod_time': (datetime,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'namespace': (str,),  # noqa: E501
            'resource_version': (str,),  # noqa: E501
            'self_link': (str,),  # noqa: E501
            'sort_order': (str,),  # noqa: E501
            'tenant': (str,),  # noqa: E501
            'uuid': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'creation_time': 'creation-time',  # noqa: E501
        'field_change_selector': 'field-change-selector',  # noqa: E501
        'field_selector': 'field-selector',  # noqa: E501
        '_from': 'from',  # noqa: E501
        'generation_id': 'generation-id',  # noqa: E501
        'label_selector': 'label-selector',  # noqa: E501
        'labels': 'labels',  # noqa: E501
        'max_results': 'max-results',  # noqa: E501
        'mod_time': 'mod-time',  # noqa: E501
        'name': 'name',  # noqa: E501
        'namespace': 'namespace',  # noqa: E501
        'resource_version': 'resource-version',  # noqa: E501
        'self_link': 'self-link',  # noqa: E501
        'sort_order': 'sort-order',  # noqa: E501
        'tenant': 'tenant',  # noqa: E501
        'uuid': 'uuid',  # noqa: E501
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
        """ApiListWatchOptions - a model defined in OpenAPI

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
            creation_time (datetime): [optional]  # noqa: E501
            field_change_selector ([str]): FieldChangeSelector specifies to generate a watch notification on change in field(s) specified.. [optional]  # noqa: E501
            field_selector (str): FieldSelector to select on field values in list or watch results.. [optional]  # noqa: E501
            _from (int): From represents the start index number (1 based - first object starts from index 1), of the results list. The results returned would be in the range [from ... (from + (max-results - 1))]. If From = 0, the server will attempt to return all the results in the list without pagination.. [optional]  # noqa: E501
            generation_id (str): [optional]  # noqa: E501
            label_selector (str): LabelSelector to select on labels in list or watch results.. [optional]  # noqa: E501
            labels ({str: (str,)}): [optional]  # noqa: E501
            max_results (int): MaxResults is the maximum number of results to be returned as part of the response, per page If MaxResults is more than the maximum number of results per page supported by the server, the server will return an err If MaxResults is 0, the server will return all the results without pagination.. [optional]  # noqa: E501
            mod_time (datetime): [optional]  # noqa: E501
            name (str): Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]  # noqa: E501
            namespace (str): Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64.. [optional]  # noqa: E501
            resource_version (str): [optional]  # noqa: E501
            self_link (str): [optional]  # noqa: E501
            sort_order (str): order to sort List results in.. [optional] if omitted the server will use the default value of "none"  # noqa: E501
            tenant (str): Must be alpha-numerics. Length of string should be between 1 and 48.. [optional]  # noqa: E501
            uuid (str): [optional]  # noqa: E501
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
