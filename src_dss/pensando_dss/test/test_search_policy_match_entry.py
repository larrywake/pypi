"""
    Search API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_dss
from pensando_dss.psm_dss.model.security_ip_sec_policy_rule import SecurityIPSecPolicyRule
from pensando_dss.psm_dss.model.security_sg_rule import SecuritySGRule
globals()['SecurityIPSecPolicyRule'] = SecurityIPSecPolicyRule
globals()['SecuritySGRule'] = SecuritySGRule
from pensando_dss.psm_dss.psm_dss.model.search_policy_match_entry import SearchPolicyMatchEntry


class TestSearchPolicyMatchEntry(unittest.TestCase):
    """SearchPolicyMatchEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchPolicyMatchEntry(self):
        """Test SearchPolicyMatchEntry"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchPolicyMatchEntry()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
