"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_ent
from pensando_ent.psm_ent.model.api_list_meta import ApiListMeta
from pensando_ent.psm_ent.model.cluster_host import ClusterHost
globals()['ApiListMeta'] = ApiListMeta
globals()['ClusterHost'] = ClusterHost
from pensando_ent.psm_ent.psm_ent.model.cluster_host_list import ClusterHostList


class TestClusterHostList(unittest.TestCase):
    """ClusterHostList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterHostList(self):
        """Test ClusterHostList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterHostList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
