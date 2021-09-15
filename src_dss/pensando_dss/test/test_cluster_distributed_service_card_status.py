"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_dss
from pensando_dss.psm_dss.model.cluster_dsc_condition import ClusterDSCCondition
from pensando_dss.psm_dss.model.cluster_dsc_control_plane_status import ClusterDSCControlPlaneStatus
from pensando_dss.psm_dss.model.cluster_dsc_info import ClusterDSCInfo
from pensando_dss.psm_dss.model.cluster_ip_config import ClusterIPConfig
globals()['ClusterDSCCondition'] = ClusterDSCCondition
globals()['ClusterDSCControlPlaneStatus'] = ClusterDSCControlPlaneStatus
globals()['ClusterDSCInfo'] = ClusterDSCInfo
globals()['ClusterIPConfig'] = ClusterIPConfig
from pensando_dss.psm_dss.psm_dss.model.cluster_distributed_service_card_status import ClusterDistributedServiceCardStatus


class TestClusterDistributedServiceCardStatus(unittest.TestCase):
    """ClusterDistributedServiceCardStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterDistributedServiceCardStatus(self):
        """Test ClusterDistributedServiceCardStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterDistributedServiceCardStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
