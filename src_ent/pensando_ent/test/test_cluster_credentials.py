"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_ent
from pensando_ent.psm_ent.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm_ent.model.cluster_credentials_spec import ClusterCredentialsSpec
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['ClusterCredentialsSpec'] = ClusterCredentialsSpec
from pensando_ent.psm_ent.psm_ent.model.cluster_credentials import ClusterCredentials


class TestClusterCredentials(unittest.TestCase):
    """ClusterCredentials unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterCredentials(self):
        """Test ClusterCredentials"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterCredentials()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
