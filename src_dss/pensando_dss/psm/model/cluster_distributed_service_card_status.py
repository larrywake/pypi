"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from pensando_dss.psm.model_utils import (  # noqa: F401
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
    from pensando_dss.psm.model.cluster_dsc_condition import ClusterDSCCondition
    from pensando_dss.psm.model.cluster_dsc_control_plane_status import ClusterDSCControlPlaneStatus
    from pensando_dss.psm.model.cluster_dsc_info import ClusterDSCInfo
    from pensando_dss.psm.model.cluster_dss_info import ClusterDSSInfo
    from pensando_dss.psm.model.cluster_ip_config import ClusterIPConfig
    globals()['ClusterDSCCondition'] = ClusterDSCCondition
    globals()['ClusterDSCControlPlaneStatus'] = ClusterDSCControlPlaneStatus
    globals()['ClusterDSCInfo'] = ClusterDSCInfo
    globals()['ClusterDSSInfo'] = ClusterDSSInfo
    globals()['ClusterIPConfig'] = ClusterIPConfig


class ClusterDistributedServiceCardStatus(ModelNormal):
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
        ('admission_phase',): {
            'UNKNOWN': "unknown",
            'REGISTERING': "registering",
            'REJECTED': "rejected",
            'PENDING': "pending",
            'ADMITTED': "admitted",
            'DECOMMISSIONED': "decommissioned",
        },
        ('package_type',): {
            'DSC': "dsc",
            'DSS': "dss",
        },
    }

    validations = {
        ('num_mac_address',): {
            'inclusive_maximum': 256,
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
            'dsc_sku': (str,),  # noqa: E501
            'dsc_version': (str,),  # noqa: E501
            'adm_phase_reason': (str,),  # noqa: E501
            'admission_phase': (str,),  # noqa: E501
            'alom_present': (bool,),  # noqa: E501
            'conditions': ([ClusterDSCCondition],),  # noqa: E501
            'control_plane_status': (ClusterDSCControlPlaneStatus,),  # noqa: E501
            'dss_info': (ClusterDSSInfo,),  # noqa: E501
            'host': (str,),  # noqa: E501
            'inband_ip_config': (ClusterIPConfig,),  # noqa: E501
            'interfaces': ([str],),  # noqa: E501
            'ip_config': (ClusterIPConfig,),  # noqa: E501
            'is_connected_to_psm': (bool,),  # noqa: E501
            'num_mac_address': (int,),  # noqa: E501
            'package_type': (str,),  # noqa: E501
            'primary_mac': (str,),  # noqa: E501
            'secure_booted': (bool,),  # noqa: E501
            'security_policy_rule_scale_profile': (str,),  # noqa: E501
            'serial_num': (str,),  # noqa: E501
            'system_info': (ClusterDSCInfo,),  # noqa: E501
            'unhealthy_services': ([str],),  # noqa: E501
            'version_mismatch': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'dsc_sku': 'DSCSku',  # noqa: E501
        'dsc_version': 'DSCVersion',  # noqa: E501
        'adm_phase_reason': 'adm-phase-reason',  # noqa: E501
        'admission_phase': 'admission-phase',  # noqa: E501
        'alom_present': 'alom-present',  # noqa: E501
        'conditions': 'conditions',  # noqa: E501
        'control_plane_status': 'control-plane-status',  # noqa: E501
        'dss_info': 'dss-info',  # noqa: E501
        'host': 'host',  # noqa: E501
        'inband_ip_config': 'inband-ip-config',  # noqa: E501
        'interfaces': 'interfaces',  # noqa: E501
        'ip_config': 'ip-config',  # noqa: E501
        'is_connected_to_psm': 'is-connected-to-psm',  # noqa: E501
        'num_mac_address': 'num-mac-address',  # noqa: E501
        'package_type': 'package-type',  # noqa: E501
        'primary_mac': 'primary-mac',  # noqa: E501
        'secure_booted': 'secure-booted',  # noqa: E501
        'security_policy_rule_scale_profile': 'security-policy-rule-scale-profile',  # noqa: E501
        'serial_num': 'serial-num',  # noqa: E501
        'system_info': 'system-info',  # noqa: E501
        'unhealthy_services': 'unhealthy-services',  # noqa: E501
        'version_mismatch': 'version-mismatch',  # noqa: E501
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
        """ClusterDistributedServiceCardStatus - a model defined in OpenAPI

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
            dsc_sku (str): DSC SKU.. [optional]  # noqa: E501
            dsc_version (str): DSC Version.. [optional]  # noqa: E501
            adm_phase_reason (str): The reason why the DistributedServiceCard is not in ADMITTED state.. [optional]  # noqa: E501
            admission_phase (str): Current admission phase of the DistributedServiceCard. When auto-admission is enabled, AdmissionPhase will be set to NIC_ADMITTED by CMD for validated NICs. When auto-admission is not enabled, AdmissionPhase will be set to NIC_PENDING by CMD for validated NICs since it requires manual approval. To admit the NIC as a part of manual admission, user is expected to set Spec.Admit to true for the NICs that are in NIC_PENDING state. Note : Whitelist mode is not supported yet.. [optional] if omitted the server will use the default value of "unknown"  # noqa: E501
            alom_present (bool): ALOMPresent true value indicates ALOM cable is present.. [optional]  # noqa: E501
            conditions ([ClusterDSCCondition]): List of current NIC conditions.. [optional]  # noqa: E501
            control_plane_status (ClusterDSCControlPlaneStatus): [optional]  # noqa: E501
            dss_info (ClusterDSSInfo): [optional]  # noqa: E501
            host (str): The name of the host this DistributedServiceCard is plugged into.. [optional]  # noqa: E501
            inband_ip_config (ClusterIPConfig): [optional]  # noqa: E501
            interfaces ([str]): Network Interfaces.. [optional]  # noqa: E501
            ip_config (ClusterIPConfig): [optional]  # noqa: E501
            is_connected_to_psm (bool): IsConnectedToPSM is set to true if connected to PSM.. [optional]  # noqa: E501
            num_mac_address (int): NumMacAddress has the number of mac addresses that is available on this DSC. Value should be between 0 and 256.. [optional] if omitted the server will use the default value of 24  # noqa: E501
            package_type (str): Type of DSC.. [optional] if omitted the server will use the default value of "dsc"  # noqa: E501
            primary_mac (str): PrimaryMAC is the MAC address of the primary PF exposed by DistributedServiceCard. Should be a valid MAC address.. [optional]  # noqa: E501
            secure_booted (bool): SecureBooted a true value indicates, secure boot is enabled.. [optional]  # noqa: E501
            security_policy_rule_scale_profile (str): SecurityPolicyRuleScaleProfile is the active security policy rule scale profile in the DSE.. [optional]  # noqa: E501
            serial_num (str): Serial number.. [optional]  # noqa: E501
            system_info (ClusterDSCInfo): [optional]  # noqa: E501
            unhealthy_services ([str]): Lists the unhealthy services of a distributed service card.. [optional]  # noqa: E501
            version_mismatch (bool): Set to true if venice and dsc versions are incompatible.. [optional]  # noqa: E501
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
