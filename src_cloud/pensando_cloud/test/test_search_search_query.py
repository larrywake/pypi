"""
    Search API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.fields_selector import FieldsSelector
from pensando_cloud.psm.model.labels_selector import LabelsSelector
from pensando_cloud.psm.model.search_text_requirement import SearchTextRequirement
globals()['FieldsSelector'] = FieldsSelector
globals()['LabelsSelector'] = LabelsSelector
globals()['SearchTextRequirement'] = SearchTextRequirement
from pensando_cloud.psm.psm.model.search_search_query import SearchSearchQuery


class TestSearchSearchQuery(unittest.TestCase):
    """SearchSearchQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchSearchQuery(self):
        """Test SearchSearchQuery"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchSearchQuery()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
