"""
    Network API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.model.network_service_spec import NetworkServiceSpec
from pensando_cloud.psm_cloud.model.network_service_status import NetworkServiceStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['NetworkServiceSpec'] = NetworkServiceSpec
globals()['NetworkServiceStatus'] = NetworkServiceStatus
from pensando_cloud.psm_cloud.psm_cloud.model.network_service import NetworkService


class TestNetworkService(unittest.TestCase):
    """NetworkService unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNetworkService(self):
        """Test NetworkService"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NetworkService()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
