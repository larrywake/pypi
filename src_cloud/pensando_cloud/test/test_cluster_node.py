"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.model.cluster_node_spec import ClusterNodeSpec
from pensando_cloud.psm_cloud.model.cluster_node_status import ClusterNodeStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['ClusterNodeSpec'] = ClusterNodeSpec
globals()['ClusterNodeStatus'] = ClusterNodeStatus
from pensando_cloud.psm_cloud.psm_cloud.model.cluster_node import ClusterNode


class TestClusterNode(unittest.TestCase):
    """ClusterNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterNode(self):
        """Test ClusterNode"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterNode()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
