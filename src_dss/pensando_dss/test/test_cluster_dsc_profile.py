"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_dss
from pensando_dss.psm_dss.model.api_object_meta import ApiObjectMeta
from pensando_dss.psm_dss.model.cluster_dsc_profile_spec import ClusterDSCProfileSpec
from pensando_dss.psm_dss.model.cluster_dsc_profile_status import ClusterDSCProfileStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['ClusterDSCProfileSpec'] = ClusterDSCProfileSpec
globals()['ClusterDSCProfileStatus'] = ClusterDSCProfileStatus
from pensando_dss.psm_dss.psm_dss.model.cluster_dsc_profile import ClusterDSCProfile


class TestClusterDSCProfile(unittest.TestCase):
    """ClusterDSCProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterDSCProfile(self):
        """Test ClusterDSCProfile"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterDSCProfile()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
