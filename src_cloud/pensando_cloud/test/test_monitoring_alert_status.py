"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_object_ref import ApiObjectRef
from pensando_cloud.psm.model.monitoring_alert_reason import MonitoringAlertReason
from pensando_cloud.psm.model.monitoring_alert_source import MonitoringAlertSource
from pensando_cloud.psm.model.monitoring_audit_info import MonitoringAuditInfo
globals()['ApiObjectRef'] = ApiObjectRef
globals()['MonitoringAlertReason'] = MonitoringAlertReason
globals()['MonitoringAlertSource'] = MonitoringAlertSource
globals()['MonitoringAuditInfo'] = MonitoringAuditInfo
from pensando_cloud.psm.psm.model.monitoring_alert_status import MonitoringAlertStatus


class TestMonitoringAlertStatus(unittest.TestCase):
    """MonitoringAlertStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringAlertStatus(self):
        """Test MonitoringAlertStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringAlertStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
