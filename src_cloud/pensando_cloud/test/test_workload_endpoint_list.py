"""
    Workload API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.api_list_meta import ApiListMeta
from pensando_cloud.psm_cloud.model.workload_endpoint import WorkloadEndpoint
globals()['ApiListMeta'] = ApiListMeta
globals()['WorkloadEndpoint'] = WorkloadEndpoint
from pensando_cloud.psm_cloud.psm_cloud.model.workload_endpoint_list import WorkloadEndpointList


class TestWorkloadEndpointList(unittest.TestCase):
    """WorkloadEndpointList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWorkloadEndpointList(self):
        """Test WorkloadEndpointList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WorkloadEndpointList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
