"""
    Fwlog API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import psm_ent
from pensando_ent.psm_ent.api.fwlog_v1_api import FwlogV1Api  # noqa: E501


class TestFwlogV1Api(unittest.TestCase):
    """FwlogV1Api unit test stubs"""

    def setUp(self):
        self.api = FwlogV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_download_fw_log_file_content(self):
        """Test case for get_download_fw_log_file_content

        fwlog/v1/tenants/default/objects/<objectName>  # noqa: E501
        """
        pass

    def test_get_download_fw_log_file_content1(self):
        """Test case for get_download_fw_log_file_content1

        fwlog/v1/tenants/default/objects/<objectName>  # noqa: E501
        """
        pass

    def test_get_get_logs1(self):
        """Test case for get_get_logs1

        Queries firewall logs  # noqa: E501
        """
        pass

    def test_get_watch_logs(self):
        """Test case for get_watch_logs

        """
        pass

    def test_post_get_logs(self):
        """Test case for post_get_logs

        Queries firewall logs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
