"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.cluster_node_condition import ClusterNodeCondition
globals()['ClusterNodeCondition'] = ClusterNodeCondition
from pensando_cloud.psm_cloud.psm_cloud.model.cluster_node_status import ClusterNodeStatus


class TestClusterNodeStatus(unittest.TestCase):
    """ClusterNodeStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterNodeStatus(self):
        """Test ClusterNodeStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterNodeStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
