"""
    Audit API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import psm
from pensando_cloud.psm.api.audit_v1_api import AuditV1Api  # noqa: E501


class TestAuditV1Api(unittest.TestCase):
    """AuditV1Api unit test stubs"""

    def setUp(self):
        self.api = AuditV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_get_event(self):
        """Test case for get_get_event

        Fetches an audit event given its uuid  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
