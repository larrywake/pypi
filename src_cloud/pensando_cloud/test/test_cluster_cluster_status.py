"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.cluster_cluster_condition import ClusterClusterCondition
from pensando_cloud.psm_cloud.model.cluster_quorum_status import ClusterQuorumStatus
globals()['ClusterClusterCondition'] = ClusterClusterCondition
globals()['ClusterQuorumStatus'] = ClusterQuorumStatus
from pensando_cloud.psm_cloud.psm_cloud.model.cluster_cluster_status import ClusterClusterStatus


class TestClusterClusterStatus(unittest.TestCase):
    """ClusterClusterStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterClusterStatus(self):
        """Test ClusterClusterStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterClusterStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
