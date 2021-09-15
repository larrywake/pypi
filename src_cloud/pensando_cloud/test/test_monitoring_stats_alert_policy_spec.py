"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.monitoring_measurement_criteria import MonitoringMeasurementCriteria
from pensando_cloud.psm_cloud.model.monitoring_metric_identifier import MonitoringMetricIdentifier
from pensando_cloud.psm_cloud.model.monitoring_thresholds import MonitoringThresholds
globals()['MonitoringMeasurementCriteria'] = MonitoringMeasurementCriteria
globals()['MonitoringMetricIdentifier'] = MonitoringMetricIdentifier
globals()['MonitoringThresholds'] = MonitoringThresholds
from pensando_cloud.psm_cloud.psm_cloud.model.monitoring_stats_alert_policy_spec import MonitoringStatsAlertPolicySpec


class TestMonitoringStatsAlertPolicySpec(unittest.TestCase):
    """MonitoringStatsAlertPolicySpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringStatsAlertPolicySpec(self):
        """Test MonitoringStatsAlertPolicySpec"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringStatsAlertPolicySpec()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
