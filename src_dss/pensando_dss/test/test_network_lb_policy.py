"""
    Network API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_dss
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.model.network_lb_policy_spec import NetworkLbPolicySpec
from pensando_dss.psm_dss.model.network_lb_policy_status import NetworkLbPolicyStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['NetworkLbPolicySpec'] = NetworkLbPolicySpec
globals()['NetworkLbPolicyStatus'] = NetworkLbPolicyStatus
from pensando_dss.psm_dss.psm_dss.model.network_lb_policy import NetworkLbPolicy


class TestNetworkLbPolicy(unittest.TestCase):
    """NetworkLbPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNetworkLbPolicy(self):
        """Test NetworkLbPolicy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NetworkLbPolicy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
