"""
    Diagnostics API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import psm
from pensando_ent.psm.api.diagnostics_v1_api import DiagnosticsV1Api  # noqa: E501


class TestDiagnosticsV1Api(unittest.TestCase):
    """DiagnosticsV1Api unit test stubs"""

    def setUp(self):
        self.api = DiagnosticsV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_debug(self):
        """Test case for debug

        Request Diagnostics information for a module  # noqa: E501
        """
        pass

    def test_get_module(self):
        """Test case for get_module

        Get Module object  # noqa: E501
        """
        pass

    def test_label_module(self):
        """Test case for label_module

        Label Module object  # noqa: E501
        """
        pass

    def test_list_module(self):
        """Test case for list_module

        List Module objects  # noqa: E501
        """
        pass

    def test_update_module(self):
        """Test case for update_module

        Update Module object  # noqa: E501
        """
        pass

    def test_watch_module(self):
        """Test case for watch_module

        Watch Module objects. Supports WebSockets or HTTP long poll  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
