# psm.MonitoringV1Api

All URIs are relative to *https://PSM-IP-addr*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_alert_destination**](MonitoringV1Api.md#add_alert_destination) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations | Create AlertDestination object
[**add_alert_destination1**](MonitoringV1Api.md#add_alert_destination1) | **POST** /configs/monitoring/v1/alertDestinations | Create AlertDestination object
[**add_alert_policy**](MonitoringV1Api.md#add_alert_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies | Create AlertPolicy object
[**add_alert_policy1**](MonitoringV1Api.md#add_alert_policy1) | **POST** /configs/monitoring/v1/alertPolicies | Create AlertPolicy object
[**add_archive_request**](MonitoringV1Api.md#add_archive_request) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/archive-requests | Create ArchiveRequest object
[**add_archive_request1**](MonitoringV1Api.md#add_archive_request1) | **POST** /configs/monitoring/v1/archive-requests | Create ArchiveRequest object
[**add_audit_policy**](MonitoringV1Api.md#add_audit_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/audit-policy | Create AuditPolicy object
[**add_audit_policy1**](MonitoringV1Api.md#add_audit_policy1) | **POST** /configs/monitoring/v1/audit-policy | Create AuditPolicy object
[**add_event_policy**](MonitoringV1Api.md#add_event_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy | Create EventPolicy object
[**add_event_policy1**](MonitoringV1Api.md#add_event_policy1) | **POST** /configs/monitoring/v1/event-policy | Create EventPolicy object
[**add_flow_export_policy**](MonitoringV1Api.md#add_flow_export_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy | Create FlowExportPolicy object
[**add_flow_export_policy1**](MonitoringV1Api.md#add_flow_export_policy1) | **POST** /configs/monitoring/v1/flowExportPolicy | Create FlowExportPolicy object
[**add_fwlog_policy**](MonitoringV1Api.md#add_fwlog_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy | Create FwlogPolicy object
[**add_fwlog_policy1**](MonitoringV1Api.md#add_fwlog_policy1) | **POST** /configs/monitoring/v1/fwlogPolicy | Create FwlogPolicy object
[**add_mirror_session**](MonitoringV1Api.md#add_mirror_session) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession | Create MirrorSession object
[**add_mirror_session1**](MonitoringV1Api.md#add_mirror_session1) | **POST** /configs/monitoring/v1/MirrorSession | Create MirrorSession object
[**add_stats_alert_policy**](MonitoringV1Api.md#add_stats_alert_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies | Create StatsAlertPolicy object
[**add_stats_alert_policy1**](MonitoringV1Api.md#add_stats_alert_policy1) | **POST** /configs/monitoring/v1/statsAlertPolicies | Create StatsAlertPolicy object
[**add_tech_support_request**](MonitoringV1Api.md#add_tech_support_request) | **POST** /configs/monitoring/v1/techsupport | Create TechSupportRequest object
[**add_troubleshooting_session**](MonitoringV1Api.md#add_troubleshooting_session) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession | Create TroubleshootingSession object
[**add_troubleshooting_session1**](MonitoringV1Api.md#add_troubleshooting_session1) | **POST** /configs/monitoring/v1/TroubleshootingSession | Create TroubleshootingSession object
[**cancel**](MonitoringV1Api.md#cancel) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/archive-requests/{O.Name}/Cancel | 
[**cancel1**](MonitoringV1Api.md#cancel1) | **POST** /configs/monitoring/v1/archive-requests/{O.Name}/Cancel | 
[**delete_alert_destination**](MonitoringV1Api.md#delete_alert_destination) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations/{O.Name} | Delete AlertDestination object
[**delete_alert_destination1**](MonitoringV1Api.md#delete_alert_destination1) | **DELETE** /configs/monitoring/v1/alertDestinations/{O.Name} | Delete AlertDestination object
[**delete_alert_policy**](MonitoringV1Api.md#delete_alert_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies/{O.Name} | Delete AlertPolicy object
[**delete_alert_policy1**](MonitoringV1Api.md#delete_alert_policy1) | **DELETE** /configs/monitoring/v1/alertPolicies/{O.Name} | Delete AlertPolicy object
[**delete_archive_request**](MonitoringV1Api.md#delete_archive_request) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/archive-requests/{O.Name} | Delete ArchiveRequest object
[**delete_archive_request1**](MonitoringV1Api.md#delete_archive_request1) | **DELETE** /configs/monitoring/v1/archive-requests/{O.Name} | Delete ArchiveRequest object
[**delete_audit_policy**](MonitoringV1Api.md#delete_audit_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/audit-policy | Delete AuditPolicy object
[**delete_audit_policy1**](MonitoringV1Api.md#delete_audit_policy1) | **DELETE** /configs/monitoring/v1/audit-policy | Delete AuditPolicy object
[**delete_event_policy**](MonitoringV1Api.md#delete_event_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy/{O.Name} | Delete EventPolicy object
[**delete_event_policy1**](MonitoringV1Api.md#delete_event_policy1) | **DELETE** /configs/monitoring/v1/event-policy/{O.Name} | Delete EventPolicy object
[**delete_flow_export_policy**](MonitoringV1Api.md#delete_flow_export_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy/{O.Name} | Delete FlowExportPolicy object
[**delete_flow_export_policy1**](MonitoringV1Api.md#delete_flow_export_policy1) | **DELETE** /configs/monitoring/v1/flowExportPolicy/{O.Name} | Delete FlowExportPolicy object
[**delete_fwlog_policy**](MonitoringV1Api.md#delete_fwlog_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy/{O.Name} | Delete FwlogPolicy object
[**delete_fwlog_policy1**](MonitoringV1Api.md#delete_fwlog_policy1) | **DELETE** /configs/monitoring/v1/fwlogPolicy/{O.Name} | Delete FwlogPolicy object
[**delete_mirror_session**](MonitoringV1Api.md#delete_mirror_session) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession/{O.Name} | Delete MirrorSession object
[**delete_mirror_session1**](MonitoringV1Api.md#delete_mirror_session1) | **DELETE** /configs/monitoring/v1/MirrorSession/{O.Name} | Delete MirrorSession object
[**delete_stats_alert_policy**](MonitoringV1Api.md#delete_stats_alert_policy) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies/{O.Name} | Delete StatsAlertPolicy object
[**delete_stats_alert_policy1**](MonitoringV1Api.md#delete_stats_alert_policy1) | **DELETE** /configs/monitoring/v1/statsAlertPolicies/{O.Name} | Delete StatsAlertPolicy object
[**delete_tech_support_request**](MonitoringV1Api.md#delete_tech_support_request) | **DELETE** /configs/monitoring/v1/techsupport/{O.Name} | Delete TechSupportRequest object
[**delete_troubleshooting_session**](MonitoringV1Api.md#delete_troubleshooting_session) | **DELETE** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession/{O.Name} | Delete TroubleshootingSession object
[**delete_troubleshooting_session1**](MonitoringV1Api.md#delete_troubleshooting_session1) | **DELETE** /configs/monitoring/v1/TroubleshootingSession/{O.Name} | Delete TroubleshootingSession object
[**get_alert**](MonitoringV1Api.md#get_alert) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alerts/{O.Name} | Get Alert object
[**get_alert1**](MonitoringV1Api.md#get_alert1) | **GET** /configs/monitoring/v1/alerts/{O.Name} | Get Alert object
[**get_alert_destination**](MonitoringV1Api.md#get_alert_destination) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations/{O.Name} | Get AlertDestination object
[**get_alert_destination1**](MonitoringV1Api.md#get_alert_destination1) | **GET** /configs/monitoring/v1/alertDestinations/{O.Name} | Get AlertDestination object
[**get_alert_policy**](MonitoringV1Api.md#get_alert_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies/{O.Name} | Get AlertPolicy object
[**get_alert_policy1**](MonitoringV1Api.md#get_alert_policy1) | **GET** /configs/monitoring/v1/alertPolicies/{O.Name} | Get AlertPolicy object
[**get_archive_request**](MonitoringV1Api.md#get_archive_request) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/archive-requests/{O.Name} | Get ArchiveRequest object
[**get_archive_request1**](MonitoringV1Api.md#get_archive_request1) | **GET** /configs/monitoring/v1/archive-requests/{O.Name} | Get ArchiveRequest object
[**get_audit_policy**](MonitoringV1Api.md#get_audit_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/audit-policy | Get AuditPolicy object
[**get_audit_policy1**](MonitoringV1Api.md#get_audit_policy1) | **GET** /configs/monitoring/v1/audit-policy | Get AuditPolicy object
[**get_event_policy**](MonitoringV1Api.md#get_event_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy/{O.Name} | Get EventPolicy object
[**get_event_policy1**](MonitoringV1Api.md#get_event_policy1) | **GET** /configs/monitoring/v1/event-policy/{O.Name} | Get EventPolicy object
[**get_flow_export_policy**](MonitoringV1Api.md#get_flow_export_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy/{O.Name} | Get FlowExportPolicy object
[**get_flow_export_policy1**](MonitoringV1Api.md#get_flow_export_policy1) | **GET** /configs/monitoring/v1/flowExportPolicy/{O.Name} | Get FlowExportPolicy object
[**get_fwlog_policy**](MonitoringV1Api.md#get_fwlog_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy/{O.Name} | Get FwlogPolicy object
[**get_fwlog_policy1**](MonitoringV1Api.md#get_fwlog_policy1) | **GET** /configs/monitoring/v1/fwlogPolicy/{O.Name} | Get FwlogPolicy object
[**get_mirror_session**](MonitoringV1Api.md#get_mirror_session) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession/{O.Name} | Get MirrorSession object
[**get_mirror_session1**](MonitoringV1Api.md#get_mirror_session1) | **GET** /configs/monitoring/v1/MirrorSession/{O.Name} | Get MirrorSession object
[**get_stats_alert_policy**](MonitoringV1Api.md#get_stats_alert_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies/{O.Name} | Get StatsAlertPolicy object
[**get_stats_alert_policy1**](MonitoringV1Api.md#get_stats_alert_policy1) | **GET** /configs/monitoring/v1/statsAlertPolicies/{O.Name} | Get StatsAlertPolicy object
[**get_tech_support_request**](MonitoringV1Api.md#get_tech_support_request) | **GET** /configs/monitoring/v1/techsupport/{O.Name} | Get TechSupportRequest object
[**get_troubleshooting_session**](MonitoringV1Api.md#get_troubleshooting_session) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession/{O.Name} | Get TroubleshootingSession object
[**get_troubleshooting_session1**](MonitoringV1Api.md#get_troubleshooting_session1) | **GET** /configs/monitoring/v1/TroubleshootingSession/{O.Name} | Get TroubleshootingSession object
[**label_alert**](MonitoringV1Api.md#label_alert) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/alerts/{O.Name}/label | Label Alert object
[**label_alert1**](MonitoringV1Api.md#label_alert1) | **POST** /configs/monitoring/v1/alerts/{O.Name}/label | Label Alert object
[**label_alert_destination**](MonitoringV1Api.md#label_alert_destination) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations/{O.Name}/label | Label AlertDestination object
[**label_alert_destination1**](MonitoringV1Api.md#label_alert_destination1) | **POST** /configs/monitoring/v1/alertDestinations/{O.Name}/label | Label AlertDestination object
[**label_alert_policy**](MonitoringV1Api.md#label_alert_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies/{O.Name}/label | Label AlertPolicy object
[**label_alert_policy1**](MonitoringV1Api.md#label_alert_policy1) | **POST** /configs/monitoring/v1/alertPolicies/{O.Name}/label | Label AlertPolicy object
[**label_event_policy**](MonitoringV1Api.md#label_event_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy/{O.Name}/label | Label EventPolicy object
[**label_event_policy1**](MonitoringV1Api.md#label_event_policy1) | **POST** /configs/monitoring/v1/event-policy/{O.Name}/label | Label EventPolicy object
[**label_flow_export_policy**](MonitoringV1Api.md#label_flow_export_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy/{O.Name}/label | Label FlowExportPolicy object
[**label_flow_export_policy1**](MonitoringV1Api.md#label_flow_export_policy1) | **POST** /configs/monitoring/v1/flowExportPolicy/{O.Name}/label | Label FlowExportPolicy object
[**label_fwlog_policy**](MonitoringV1Api.md#label_fwlog_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy/{O.Name}/label | Label FwlogPolicy object
[**label_fwlog_policy1**](MonitoringV1Api.md#label_fwlog_policy1) | **POST** /configs/monitoring/v1/fwlogPolicy/{O.Name}/label | Label FwlogPolicy object
[**label_mirror_session**](MonitoringV1Api.md#label_mirror_session) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession/{O.Name}/label | Label MirrorSession object
[**label_mirror_session1**](MonitoringV1Api.md#label_mirror_session1) | **POST** /configs/monitoring/v1/MirrorSession/{O.Name}/label | Label MirrorSession object
[**label_stats_alert_policy**](MonitoringV1Api.md#label_stats_alert_policy) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies/{O.Name}/label | Label StatsAlertPolicy object
[**label_stats_alert_policy1**](MonitoringV1Api.md#label_stats_alert_policy1) | **POST** /configs/monitoring/v1/statsAlertPolicies/{O.Name}/label | Label StatsAlertPolicy object
[**label_troubleshooting_session**](MonitoringV1Api.md#label_troubleshooting_session) | **POST** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession/{O.Name}/label | Label TroubleshootingSession object
[**label_troubleshooting_session1**](MonitoringV1Api.md#label_troubleshooting_session1) | **POST** /configs/monitoring/v1/TroubleshootingSession/{O.Name}/label | Label TroubleshootingSession object
[**list_alert**](MonitoringV1Api.md#list_alert) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alerts | List Alert objects
[**list_alert1**](MonitoringV1Api.md#list_alert1) | **GET** /configs/monitoring/v1/alerts | List Alert objects
[**list_alert_destination**](MonitoringV1Api.md#list_alert_destination) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations | List AlertDestination objects
[**list_alert_destination1**](MonitoringV1Api.md#list_alert_destination1) | **GET** /configs/monitoring/v1/alertDestinations | List AlertDestination objects
[**list_alert_policy**](MonitoringV1Api.md#list_alert_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies | List AlertPolicy objects
[**list_alert_policy1**](MonitoringV1Api.md#list_alert_policy1) | **GET** /configs/monitoring/v1/alertPolicies | List AlertPolicy objects
[**list_archive_request**](MonitoringV1Api.md#list_archive_request) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/archive-requests | List ArchiveRequest objects
[**list_archive_request1**](MonitoringV1Api.md#list_archive_request1) | **GET** /configs/monitoring/v1/archive-requests | List ArchiveRequest objects
[**list_event_policy**](MonitoringV1Api.md#list_event_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy | List EventPolicy objects
[**list_event_policy1**](MonitoringV1Api.md#list_event_policy1) | **GET** /configs/monitoring/v1/event-policy | List EventPolicy objects
[**list_flow_export_policy**](MonitoringV1Api.md#list_flow_export_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy | List FlowExportPolicy objects
[**list_flow_export_policy1**](MonitoringV1Api.md#list_flow_export_policy1) | **GET** /configs/monitoring/v1/flowExportPolicy | List FlowExportPolicy objects
[**list_fwlog_policy**](MonitoringV1Api.md#list_fwlog_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy | List FwlogPolicy objects
[**list_fwlog_policy1**](MonitoringV1Api.md#list_fwlog_policy1) | **GET** /configs/monitoring/v1/fwlogPolicy | List FwlogPolicy objects
[**list_mirror_session**](MonitoringV1Api.md#list_mirror_session) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession | List MirrorSession objects
[**list_mirror_session1**](MonitoringV1Api.md#list_mirror_session1) | **GET** /configs/monitoring/v1/MirrorSession | List MirrorSession objects
[**list_stats_alert_policy**](MonitoringV1Api.md#list_stats_alert_policy) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies | List StatsAlertPolicy objects
[**list_stats_alert_policy1**](MonitoringV1Api.md#list_stats_alert_policy1) | **GET** /configs/monitoring/v1/statsAlertPolicies | List StatsAlertPolicy objects
[**list_tech_support_request**](MonitoringV1Api.md#list_tech_support_request) | **GET** /configs/monitoring/v1/techsupport | List TechSupportRequest objects
[**list_troubleshooting_session**](MonitoringV1Api.md#list_troubleshooting_session) | **GET** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession | List TroubleshootingSession objects
[**list_troubleshooting_session1**](MonitoringV1Api.md#list_troubleshooting_session1) | **GET** /configs/monitoring/v1/TroubleshootingSession | List TroubleshootingSession objects
[**update_alert**](MonitoringV1Api.md#update_alert) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/alerts/{O.Name} | Update Alert object
[**update_alert1**](MonitoringV1Api.md#update_alert1) | **PUT** /configs/monitoring/v1/alerts/{O.Name} | Update Alert object
[**update_alert_destination**](MonitoringV1Api.md#update_alert_destination) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/alertDestinations/{O.Name} | Update AlertDestination object
[**update_alert_destination1**](MonitoringV1Api.md#update_alert_destination1) | **PUT** /configs/monitoring/v1/alertDestinations/{O.Name} | Update AlertDestination object
[**update_alert_policy**](MonitoringV1Api.md#update_alert_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/alertPolicies/{O.Name} | Update AlertPolicy object
[**update_alert_policy1**](MonitoringV1Api.md#update_alert_policy1) | **PUT** /configs/monitoring/v1/alertPolicies/{O.Name} | Update AlertPolicy object
[**update_audit_policy**](MonitoringV1Api.md#update_audit_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/audit-policy | Update AuditPolicy object
[**update_audit_policy1**](MonitoringV1Api.md#update_audit_policy1) | **PUT** /configs/monitoring/v1/audit-policy | Update AuditPolicy object
[**update_event_policy**](MonitoringV1Api.md#update_event_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/event-policy/{O.Name} | Update EventPolicy object
[**update_event_policy1**](MonitoringV1Api.md#update_event_policy1) | **PUT** /configs/monitoring/v1/event-policy/{O.Name} | Update EventPolicy object
[**update_flow_export_policy**](MonitoringV1Api.md#update_flow_export_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/flowExportPolicy/{O.Name} | Update FlowExportPolicy object
[**update_flow_export_policy1**](MonitoringV1Api.md#update_flow_export_policy1) | **PUT** /configs/monitoring/v1/flowExportPolicy/{O.Name} | Update FlowExportPolicy object
[**update_fwlog_policy**](MonitoringV1Api.md#update_fwlog_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/fwlogPolicy/{O.Name} | Update FwlogPolicy object
[**update_fwlog_policy1**](MonitoringV1Api.md#update_fwlog_policy1) | **PUT** /configs/monitoring/v1/fwlogPolicy/{O.Name} | Update FwlogPolicy object
[**update_mirror_session**](MonitoringV1Api.md#update_mirror_session) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/MirrorSession/{O.Name} | Update MirrorSession object
[**update_mirror_session1**](MonitoringV1Api.md#update_mirror_session1) | **PUT** /configs/monitoring/v1/MirrorSession/{O.Name} | Update MirrorSession object
[**update_stats_alert_policy**](MonitoringV1Api.md#update_stats_alert_policy) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/statsAlertPolicies/{O.Name} | Update StatsAlertPolicy object
[**update_stats_alert_policy1**](MonitoringV1Api.md#update_stats_alert_policy1) | **PUT** /configs/monitoring/v1/statsAlertPolicies/{O.Name} | Update StatsAlertPolicy object
[**update_troubleshooting_session**](MonitoringV1Api.md#update_troubleshooting_session) | **PUT** /configs/monitoring/v1/tenant/{O.Tenant}/TroubleshootingSession/{O.Name} | Update TroubleshootingSession object
[**update_troubleshooting_session1**](MonitoringV1Api.md#update_troubleshooting_session1) | **PUT** /configs/monitoring/v1/TroubleshootingSession/{O.Name} | Update TroubleshootingSession object
[**watch_alert**](MonitoringV1Api.md#watch_alert) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/alerts | Watch Alert objects. Supports WebSockets or HTTP long poll
[**watch_alert1**](MonitoringV1Api.md#watch_alert1) | **GET** /configs/monitoring/v1/watch/alerts | Watch Alert objects. Supports WebSockets or HTTP long poll
[**watch_alert_destination**](MonitoringV1Api.md#watch_alert_destination) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/alertDestinations | Watch AlertDestination objects. Supports WebSockets or HTTP long poll
[**watch_alert_destination1**](MonitoringV1Api.md#watch_alert_destination1) | **GET** /configs/monitoring/v1/watch/alertDestinations | Watch AlertDestination objects. Supports WebSockets or HTTP long poll
[**watch_alert_policy**](MonitoringV1Api.md#watch_alert_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/alertPolicies | Watch AlertPolicy objects. Supports WebSockets or HTTP long poll
[**watch_alert_policy1**](MonitoringV1Api.md#watch_alert_policy1) | **GET** /configs/monitoring/v1/watch/alertPolicies | Watch AlertPolicy objects. Supports WebSockets or HTTP long poll
[**watch_archive_request**](MonitoringV1Api.md#watch_archive_request) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/archive-requests | Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll
[**watch_archive_request1**](MonitoringV1Api.md#watch_archive_request1) | **GET** /configs/monitoring/v1/watch/archive-requests | Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll
[**watch_audit_policy**](MonitoringV1Api.md#watch_audit_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/audit-policy | Watch AuditPolicy objects. Supports WebSockets or HTTP long poll
[**watch_audit_policy1**](MonitoringV1Api.md#watch_audit_policy1) | **GET** /configs/monitoring/v1/watch/audit-policy | Watch AuditPolicy objects. Supports WebSockets or HTTP long poll
[**watch_event_policy**](MonitoringV1Api.md#watch_event_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/event-policy | Watch EventPolicy objects. Supports WebSockets or HTTP long poll
[**watch_event_policy1**](MonitoringV1Api.md#watch_event_policy1) | **GET** /configs/monitoring/v1/watch/event-policy | Watch EventPolicy objects. Supports WebSockets or HTTP long poll
[**watch_flow_export_policy**](MonitoringV1Api.md#watch_flow_export_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/flowExportPolicy | Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll
[**watch_flow_export_policy1**](MonitoringV1Api.md#watch_flow_export_policy1) | **GET** /configs/monitoring/v1/watch/flowExportPolicy | Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll
[**watch_fwlog_policy**](MonitoringV1Api.md#watch_fwlog_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/fwlogPolicy | Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll
[**watch_fwlog_policy1**](MonitoringV1Api.md#watch_fwlog_policy1) | **GET** /configs/monitoring/v1/watch/fwlogPolicy | Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll
[**watch_mirror_session**](MonitoringV1Api.md#watch_mirror_session) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/MirrorSession | Watch MirrorSession objects. Supports WebSockets or HTTP long poll
[**watch_mirror_session1**](MonitoringV1Api.md#watch_mirror_session1) | **GET** /configs/monitoring/v1/watch/MirrorSession | Watch MirrorSession objects. Supports WebSockets or HTTP long poll
[**watch_stats_alert_policy**](MonitoringV1Api.md#watch_stats_alert_policy) | **GET** /configs/monitoring/v1/watch/tenant/{O.Tenant}/statsAlertPolicies | Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll
[**watch_stats_alert_policy1**](MonitoringV1Api.md#watch_stats_alert_policy1) | **GET** /configs/monitoring/v1/watch/statsAlertPolicies | Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll
[**watch_tech_support_request**](MonitoringV1Api.md#watch_tech_support_request) | **GET** /configs/monitoring/v1/watch/techsupport | Watch TechSupportRequest objects. Supports WebSockets or HTTP long poll


# **add_alert_destination**
> MonitoringAlertDestination add_alert_destination(o_tenant, body)

Create AlertDestination object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_destination import MonitoringAlertDestination
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringAlertDestination(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertDestinationSpec(
            email_export=MonitoringEmailExport(
                email_list=[
                    "email_list_example",
                ],
            ),
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            snmp_export=MonitoringSNMPExport(
                snmp_trap_servers=[
                    MonitoringSNMPTrapServer(
                        auth_config=MonitoringAuthConfig(
                            algo="md5",
                            password="password_example",
                        ),
                        community_or_user="community_or_user_example",
                        host="host_example",
                        port="162",
                        privacy_config=MonitoringPrivacyConfig(
                            algo="des56",
                            password="password_example",
                        ),
                        version="v2c",
                    ),
                ],
            ),
            syslog_export=MonitoringSyslogExport(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
        ),
        status=MonitoringAlertDestinationStatus(
            total_notifications_sent=1,
        ),
    ) # MonitoringAlertDestination | 

    # example passing only required values which don't have defaults set
    try:
        # Create AlertDestination object
        api_response = api_instance.add_alert_destination(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_alert_destination: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringAlertDestination**](MonitoringAlertDestination.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_destination1**
> MonitoringAlertDestination add_alert_destination1(body)

Create AlertDestination object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_destination import MonitoringAlertDestination
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringAlertDestination(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertDestinationSpec(
            email_export=MonitoringEmailExport(
                email_list=[
                    "email_list_example",
                ],
            ),
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            snmp_export=MonitoringSNMPExport(
                snmp_trap_servers=[
                    MonitoringSNMPTrapServer(
                        auth_config=MonitoringAuthConfig(
                            algo="md5",
                            password="password_example",
                        ),
                        community_or_user="community_or_user_example",
                        host="host_example",
                        port="162",
                        privacy_config=MonitoringPrivacyConfig(
                            algo="des56",
                            password="password_example",
                        ),
                        version="v2c",
                    ),
                ],
            ),
            syslog_export=MonitoringSyslogExport(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
        ),
        status=MonitoringAlertDestinationStatus(
            total_notifications_sent=1,
        ),
    ) # MonitoringAlertDestination | 

    # example passing only required values which don't have defaults set
    try:
        # Create AlertDestination object
        api_response = api_instance.add_alert_destination1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_alert_destination1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringAlertDestination**](MonitoringAlertDestination.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_policy**
> MonitoringAlertPolicy add_alert_policy(o_tenant, body)

Create AlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            message="message_example",
            requirements=[
                FieldsRequirement(
                    key="key_example",
                    operator="equals",
                    values=[
                        "values_example",
                    ],
                ),
            ],
            resource="resource_example",
            severity="info",
        ),
        status=MonitoringAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create AlertPolicy object
        api_response = api_instance.add_alert_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_policy1**
> MonitoringAlertPolicy add_alert_policy1(body)

Create AlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            message="message_example",
            requirements=[
                FieldsRequirement(
                    key="key_example",
                    operator="equals",
                    values=[
                        "values_example",
                    ],
                ),
            ],
            resource="resource_example",
            severity="info",
        ),
        status=MonitoringAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create AlertPolicy object
        api_response = api_instance.add_alert_policy1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_archive_request**
> MonitoringArchiveRequest add_archive_request(o_tenant, body)

Create ArchiveRequest object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringArchiveRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringArchiveRequestSpec(
            query=MonitoringArchiveQuery(
                end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                fields=FieldsSelector(
                    requirements=[
                        FieldsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[],
                        ),
                    ],
                ),
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                tenants=[
                    "tenants_example",
                ],
                texts=[
                    SearchTextRequirement(
                        text=[
                            "text_example",
                        ],
                    ),
                ],
            ),
            type="event",
        ),
        status=MonitoringArchiveRequestStatus(
            reason="reason_example",
            status="scheduled",
            uri="uri_example",
        ),
    ) # MonitoringArchiveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create ArchiveRequest object
        api_response = api_instance.add_archive_request(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_archive_request: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_archive_request1**
> MonitoringArchiveRequest add_archive_request1(body)

Create ArchiveRequest object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringArchiveRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringArchiveRequestSpec(
            query=MonitoringArchiveQuery(
                end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                fields=FieldsSelector(
                    requirements=[
                        FieldsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[],
                        ),
                    ],
                ),
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                tenants=[
                    "tenants_example",
                ],
                texts=[
                    SearchTextRequirement(
                        text=[
                            "text_example",
                        ],
                    ),
                ],
            ),
            type="event",
        ),
        status=MonitoringArchiveRequestStatus(
            reason="reason_example",
            status="scheduled",
            uri="uri_example",
        ),
    ) # MonitoringArchiveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create ArchiveRequest object
        api_response = api_instance.add_archive_request1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_archive_request1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_audit_policy**
> MonitoringAuditPolicy add_audit_policy(o_tenant, body)

Create AuditPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_audit_policy import MonitoringAuditPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringAuditPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAuditPolicySpec(
            syslog_auditor=MonitoringSyslogAuditor(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                enabled=True,
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
        ),
        status={},
    ) # MonitoringAuditPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create AuditPolicy object
        api_response = api_instance.add_audit_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_audit_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)|  |

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_audit_policy1**
> MonitoringAuditPolicy add_audit_policy1(body)

Create AuditPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_audit_policy import MonitoringAuditPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringAuditPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAuditPolicySpec(
            syslog_auditor=MonitoringSyslogAuditor(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                enabled=True,
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
        ),
        status={},
    ) # MonitoringAuditPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create AuditPolicy object
        api_response = api_instance.add_audit_policy1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_audit_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)|  |

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_event_policy**
> MonitoringEventPolicy add_event_policy(o_tenant, body)

Create EventPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy import MonitoringEventPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringEventPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringEventPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            format="syslog-bsd",
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
        ),
        status={},
    ) # MonitoringEventPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create EventPolicy object
        api_response = api_instance.add_event_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_event_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringEventPolicy**](MonitoringEventPolicy.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_event_policy1**
> MonitoringEventPolicy add_event_policy1(body)

Create EventPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy import MonitoringEventPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringEventPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringEventPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            format="syslog-bsd",
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
        ),
        status={},
    ) # MonitoringEventPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create EventPolicy object
        api_response = api_instance.add_event_policy1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_event_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringEventPolicy**](MonitoringEventPolicy.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_flow_export_policy**
> MonitoringFlowExportPolicy add_flow_export_policy(o_tenant, body)

Create FlowExportPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringFlowExportPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFlowExportPolicySpec(
            disabled=True,
            exports=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
            format="ipfix",
            interval="60s",
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            template_interval="60s",
        ),
        status=MonitoringFlowExportPolicyStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            state="disabled",
        ),
    ) # MonitoringFlowExportPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create FlowExportPolicy object
        api_response = api_instance.add_flow_export_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_flow_export_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_flow_export_policy1**
> MonitoringFlowExportPolicy add_flow_export_policy1(body)

Create FlowExportPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringFlowExportPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFlowExportPolicySpec(
            disabled=True,
            exports=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
            format="ipfix",
            interval="60s",
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            template_interval="60s",
        ),
        status=MonitoringFlowExportPolicyStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            state="disabled",
        ),
    ) # MonitoringFlowExportPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create FlowExportPolicy object
        api_response = api_instance.add_flow_export_policy1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_flow_export_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fwlog_policy**
> MonitoringFwlogPolicy add_fwlog_policy(o_tenant, body)

Create FwlogPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringFwlogPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFwlogPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            filter=[
                "filter_example",
            ],
            format="syslog-bsd",
            psm_target=MonitoringPSMExportTarget(
                enable=True,
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
            vrf_name="vrf_name_example",
        ),
        status={},
    ) # MonitoringFwlogPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create FwlogPolicy object
        api_response = api_instance.add_fwlog_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_fwlog_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_fwlog_policy1**
> MonitoringFwlogPolicy add_fwlog_policy1(body)

Create FwlogPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringFwlogPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFwlogPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            filter=[
                "filter_example",
            ],
            format="syslog-bsd",
            psm_target=MonitoringPSMExportTarget(
                enable=True,
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
            vrf_name="vrf_name_example",
        ),
        status={},
    ) # MonitoringFwlogPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create FwlogPolicy object
        api_response = api_instance.add_fwlog_policy1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_fwlog_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_mirror_session**
> MonitoringMirrorSession add_mirror_session(o_tenant, body)

Create MirrorSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringMirrorSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringMirrorSessionSpec(
            collectors=[
                MonitoringMirrorCollector(
                    export_config=MonitoringMirrorExportConfig(
                        destination="10.1.1.1 ",
                        gateway="gateway_example",
                        virtual_router="virtual_router_example",
                    ),
                    strip_vlan_hdr=True,
                    type="erspan_type_3",
                ),
            ],
            disabled=True,
            interfaces=MonitoringInterfaceMirror(
                direction="both",
                selectors=[
                    LabelsSelector(
                        requirements=[
                            LabelsRequirement(
                                key="key_example",
                                operator="equals",
                                values=[
                                    "values_example",
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            packet_filters=[
                "packet_filters_example",
            ],
            packet_size=64,
            source=MonitoringMirrorSource(
                direction="both",
                target_selectors=[
                    LabelsSelector(
                        requirements=[],
                    ),
                ],
                target_type="none",
            ),
            span_id=1,
            start_condition=MonitoringMirrorStartConditions(
                schedule_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            workloads=MonitoringWorkloadMirror(
                direction="both",
                selectors=[],
            ),
        ),
        status=MonitoringMirrorSessionStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            schedule_state="none",
            started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # MonitoringMirrorSession | 

    # example passing only required values which don't have defaults set
    try:
        # Create MirrorSession object
        api_response = api_instance.add_mirror_session(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_mirror_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringMirrorSession**](MonitoringMirrorSession.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_mirror_session1**
> MonitoringMirrorSession add_mirror_session1(body)

Create MirrorSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringMirrorSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringMirrorSessionSpec(
            collectors=[
                MonitoringMirrorCollector(
                    export_config=MonitoringMirrorExportConfig(
                        destination="10.1.1.1 ",
                        gateway="gateway_example",
                        virtual_router="virtual_router_example",
                    ),
                    strip_vlan_hdr=True,
                    type="erspan_type_3",
                ),
            ],
            disabled=True,
            interfaces=MonitoringInterfaceMirror(
                direction="both",
                selectors=[
                    LabelsSelector(
                        requirements=[
                            LabelsRequirement(
                                key="key_example",
                                operator="equals",
                                values=[
                                    "values_example",
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            packet_filters=[
                "packet_filters_example",
            ],
            packet_size=64,
            source=MonitoringMirrorSource(
                direction="both",
                target_selectors=[
                    LabelsSelector(
                        requirements=[],
                    ),
                ],
                target_type="none",
            ),
            span_id=1,
            start_condition=MonitoringMirrorStartConditions(
                schedule_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            workloads=MonitoringWorkloadMirror(
                direction="both",
                selectors=[],
            ),
        ),
        status=MonitoringMirrorSessionStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            schedule_state="none",
            started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # MonitoringMirrorSession | 

    # example passing only required values which don't have defaults set
    try:
        # Create MirrorSession object
        api_response = api_instance.add_mirror_session1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_mirror_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringMirrorSession**](MonitoringMirrorSession.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_stats_alert_policy**
> MonitoringStatsAlertPolicy add_stats_alert_policy(o_tenant, body)

Create StatsAlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringStatsAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringStatsAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            instance_selector=MonitoringInstanceSelector(
                kind="kind_example",
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                names=[
                    "names_example",
                ],
            ),
            measurement_criteria=MonitoringMeasurementCriteria(
                function="none_function",
                window="window_example",
            ),
            message_template="message_template_example",
            metric=MonitoringMetricIdentifier(
                field_name="field_name_example",
                group="group_example",
                kind="kind_example",
            ),
            thresholds=MonitoringThresholds(
                operator="less_or_equal_than",
                values=[
                    MonitoringThreshold(
                        raise_value="raise_value_example",
                        severity="info",
                    ),
                ],
            ),
        ),
        status=MonitoringStatsAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringStatsAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create StatsAlertPolicy object
        api_response = api_instance.add_stats_alert_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_stats_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_stats_alert_policy1**
> MonitoringStatsAlertPolicy add_stats_alert_policy1(body)

Create StatsAlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringStatsAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringStatsAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            instance_selector=MonitoringInstanceSelector(
                kind="kind_example",
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                names=[
                    "names_example",
                ],
            ),
            measurement_criteria=MonitoringMeasurementCriteria(
                function="none_function",
                window="window_example",
            ),
            message_template="message_template_example",
            metric=MonitoringMetricIdentifier(
                field_name="field_name_example",
                group="group_example",
                kind="kind_example",
            ),
            thresholds=MonitoringThresholds(
                operator="less_or_equal_than",
                values=[
                    MonitoringThreshold(
                        raise_value="raise_value_example",
                        severity="info",
                    ),
                ],
            ),
        ),
        status=MonitoringStatsAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringStatsAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Create StatsAlertPolicy object
        api_response = api_instance.add_stats_alert_policy1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_stats_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tech_support_request**
> MonitoringTechSupportRequest add_tech_support_request(body)

Create TechSupportRequest object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_tech_support_request import MonitoringTechSupportRequest
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringTechSupportRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringTechSupportRequestSpec(
            collection_selector=LabelsSelector(
                requirements=[
                    LabelsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            node_selector=TechSupportRequestSpecNodeSelectorSpec(
                labels=LabelsSelector(
                    requirements=[],
                ),
                names=[
                    "names_example",
                ],
            ),
            skip_cores=False,
            verbosity=1,
        ),
        status=MonitoringTechSupportRequestStatus(
            ctrlr_node_results={
                "key": MonitoringTechSupportNodeResult(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    status="scheduled",
                    uri="uri_example",
                ),
            },
            dsc_results={
                "key": MonitoringTechSupportNodeResult(
                    end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    reason="reason_example",
                    start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    status="scheduled",
                    uri="uri_example",
                ),
            },
            instance_id="instance_id_example",
            reason="reason_example",
            status="scheduled",
        ),
    ) # MonitoringTechSupportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create TechSupportRequest object
        api_response = api_instance.add_tech_support_request(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_tech_support_request: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringTechSupportRequest**](MonitoringTechSupportRequest.md)|  |

### Return type

[**MonitoringTechSupportRequest**](MonitoringTechSupportRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_troubleshooting_session**
> MonitoringTroubleshootingSession add_troubleshooting_session(o_tenant, body)

Create TroubleshootingSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringTroubleshootingSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringTroubleshootingSessionSpec(
            enable_mirroring=True,
            flow_selector=MonitoringMatchRule(
                app_protocol_selectors=MonitoringAppProtoSelector(
                    applications=[
                        "applications_example",
                    ],
                    proto_ports=[
                        "udp/1234",
                    ],
                ),
                destination=MonitoringMatchSelector(
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_addresses=[
                        "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    ],
                ),
                source=MonitoringMatchSelector(
                    ip_addresses=[],
                    mac_addresses=[],
                ),
            ),
            repeat_every="repeat_every_example",
            time_window=MonitoringTimeWindow(
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
        status=MonitoringTroubleshootingSessionStatus(
            state="running",
            troubleshooting_results=[
                MonitoringTsResult(
                    report_url="report_url_example",
                    time_window=MonitoringTimeWindow(
                        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ),
            ],
        ),
    ) # MonitoringTroubleshootingSession | 

    # example passing only required values which don't have defaults set
    try:
        # Create TroubleshootingSession object
        api_response = api_instance.add_troubleshooting_session(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_troubleshooting_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_troubleshooting_session1**
> MonitoringTroubleshootingSession add_troubleshooting_session1(body)

Create TroubleshootingSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringTroubleshootingSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringTroubleshootingSessionSpec(
            enable_mirroring=True,
            flow_selector=MonitoringMatchRule(
                app_protocol_selectors=MonitoringAppProtoSelector(
                    applications=[
                        "applications_example",
                    ],
                    proto_ports=[
                        "udp/1234",
                    ],
                ),
                destination=MonitoringMatchSelector(
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_addresses=[
                        "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    ],
                ),
                source=MonitoringMatchSelector(
                    ip_addresses=[],
                    mac_addresses=[],
                ),
            ),
            repeat_every="repeat_every_example",
            time_window=MonitoringTimeWindow(
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
        status=MonitoringTroubleshootingSessionStatus(
            state="running",
            troubleshooting_results=[
                MonitoringTsResult(
                    report_url="report_url_example",
                    time_window=MonitoringTimeWindow(
                        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ),
            ],
        ),
    ) # MonitoringTroubleshootingSession | 

    # example passing only required values which don't have defaults set
    try:
        # Create TroubleshootingSession object
        api_response = api_instance.add_troubleshooting_session1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->add_troubleshooting_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel**
> MonitoringArchiveRequest cancel(o_tenant, body)



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_cancel_archive_request import MonitoringCancelArchiveRequest
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringCancelArchiveRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
    ) # MonitoringCancelArchiveRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cancel(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->cancel: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringCancelArchiveRequest**](MonitoringCancelArchiveRequest.md)|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel1**
> MonitoringArchiveRequest cancel1(o_name, body)



### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_cancel_archive_request import MonitoringCancelArchiveRequest
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringCancelArchiveRequest(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
    ) # MonitoringCancelArchiveRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.cancel1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->cancel1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringCancelArchiveRequest**](MonitoringCancelArchiveRequest.md)|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_destination**
> MonitoringAlertDestination delete_alert_destination(o_tenant)

Delete AlertDestination object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_destination import MonitoringAlertDestination
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AlertDestination object
        api_response = api_instance.delete_alert_destination(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_alert_destination: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_destination1**
> MonitoringAlertDestination delete_alert_destination1(o_name)

Delete AlertDestination object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_destination import MonitoringAlertDestination
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AlertDestination object
        api_response = api_instance.delete_alert_destination1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_alert_destination1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_policy**
> MonitoringAlertPolicy delete_alert_policy(o_tenant)

Delete AlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AlertPolicy object
        api_response = api_instance.delete_alert_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_policy1**
> MonitoringAlertPolicy delete_alert_policy1(o_name)

Delete AlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AlertPolicy object
        api_response = api_instance.delete_alert_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_archive_request**
> MonitoringArchiveRequest delete_archive_request(o_tenant)

Delete ArchiveRequest object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete ArchiveRequest object
        api_response = api_instance.delete_archive_request(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_archive_request: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_archive_request1**
> MonitoringArchiveRequest delete_archive_request1(o_name)

Delete ArchiveRequest object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete ArchiveRequest object
        api_response = api_instance.delete_archive_request1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_archive_request1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_audit_policy**
> MonitoringAuditPolicy delete_audit_policy(o_tenant)

Delete AuditPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_audit_policy import MonitoringAuditPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete AuditPolicy object
        api_response = api_instance.delete_audit_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_audit_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_audit_policy1**
> MonitoringAuditPolicy delete_audit_policy1()

Delete AuditPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_audit_policy import MonitoringAuditPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete AuditPolicy object
        api_response = api_instance.delete_audit_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_audit_policy1: %s\n" % e)

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_policy**
> MonitoringEventPolicy delete_event_policy(o_tenant)

Delete EventPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy import MonitoringEventPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete EventPolicy object
        api_response = api_instance.delete_event_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_event_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_policy1**
> MonitoringEventPolicy delete_event_policy1(o_name)

Delete EventPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy import MonitoringEventPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete EventPolicy object
        api_response = api_instance.delete_event_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_event_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_flow_export_policy**
> MonitoringFlowExportPolicy delete_flow_export_policy(o_tenant)

Delete FlowExportPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete FlowExportPolicy object
        api_response = api_instance.delete_flow_export_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_flow_export_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_flow_export_policy1**
> MonitoringFlowExportPolicy delete_flow_export_policy1(o_name)

Delete FlowExportPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete FlowExportPolicy object
        api_response = api_instance.delete_flow_export_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_flow_export_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fwlog_policy**
> MonitoringFwlogPolicy delete_fwlog_policy(o_tenant)

Delete FwlogPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete FwlogPolicy object
        api_response = api_instance.delete_fwlog_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_fwlog_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fwlog_policy1**
> MonitoringFwlogPolicy delete_fwlog_policy1(o_name)

Delete FwlogPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete FwlogPolicy object
        api_response = api_instance.delete_fwlog_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_fwlog_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mirror_session**
> MonitoringMirrorSession delete_mirror_session(o_tenant)

Delete MirrorSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete MirrorSession object
        api_response = api_instance.delete_mirror_session(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_mirror_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mirror_session1**
> MonitoringMirrorSession delete_mirror_session1(o_name)

Delete MirrorSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete MirrorSession object
        api_response = api_instance.delete_mirror_session1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_mirror_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stats_alert_policy**
> MonitoringStatsAlertPolicy delete_stats_alert_policy(o_tenant)

Delete StatsAlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete StatsAlertPolicy object
        api_response = api_instance.delete_stats_alert_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_stats_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stats_alert_policy1**
> MonitoringStatsAlertPolicy delete_stats_alert_policy1(o_name)

Delete StatsAlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete StatsAlertPolicy object
        api_response = api_instance.delete_stats_alert_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_stats_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tech_support_request**
> MonitoringTechSupportRequest delete_tech_support_request(o_name)

Delete TechSupportRequest object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_tech_support_request import MonitoringTechSupportRequest
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete TechSupportRequest object
        api_response = api_instance.delete_tech_support_request(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_tech_support_request: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringTechSupportRequest**](MonitoringTechSupportRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_troubleshooting_session**
> MonitoringTroubleshootingSession delete_troubleshooting_session(o_tenant)

Delete TroubleshootingSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete TroubleshootingSession object
        api_response = api_instance.delete_troubleshooting_session(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_troubleshooting_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_troubleshooting_session1**
> MonitoringTroubleshootingSession delete_troubleshooting_session1(o_name)

Delete TroubleshootingSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete TroubleshootingSession object
        api_response = api_instance.delete_troubleshooting_session1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->delete_troubleshooting_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> MonitoringAlert get_alert(o_tenant)

Get Alert object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_state = "spec.state_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Alert object
        api_response = api_instance.get_alert(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_state** | **str**|  | [optional]

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert1**
> MonitoringAlert get_alert1(o_name)

Get Alert object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_state = "spec.state_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Alert object
        api_response = api_instance.get_alert1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_state** | **str**|  | [optional]

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_destination**
> MonitoringAlertDestination get_alert_destination(o_tenant)

Get AlertDestination object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_destination import MonitoringAlertDestination
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    email_export_email_list = [
        "email-export.email-list_example",
    ] # [str] | TODO:  format, config, SMTP config. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AlertDestination object
        api_response = api_instance.get_alert_destination(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_destination: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **email_export_email_list** | **[str]**| TODO:  format, config, SMTP config. | [optional]

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_destination1**
> MonitoringAlertDestination get_alert_destination1(o_name)

Get AlertDestination object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_destination import MonitoringAlertDestination
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    email_export_email_list = [
        "email-export.email-list_example",
    ] # [str] | TODO:  format, config, SMTP config. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AlertDestination object
        api_response = api_instance.get_alert_destination1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_destination1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **email_export_email_list** | **[str]**| TODO:  format, config, SMTP config. | [optional]

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_policy**
> MonitoringAlertPolicy get_alert_policy(o_tenant)

Get AlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_destinations = [
        "spec.destinations_example",
    ] # [str] | name of the alert destinations to be used to send out notification when an alert gets generated. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AlertPolicy object
        api_response = api_instance.get_alert_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_destinations** | **[str]**| name of the alert destinations to be used to send out notification when an alert gets generated. | [optional]

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_policy1**
> MonitoringAlertPolicy get_alert_policy1(o_name)

Get AlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_destinations = [
        "spec.destinations_example",
    ] # [str] | name of the alert destinations to be used to send out notification when an alert gets generated. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AlertPolicy object
        api_response = api_instance.get_alert_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_destinations** | **[str]**| name of the alert destinations to be used to send out notification when an alert gets generated. | [optional]

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive_request**
> MonitoringArchiveRequest get_archive_request(o_tenant)

Get ArchiveRequest object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_type = "spec.type_example" # str |  (optional)
    query_tenants = [
        "query.tenants_example",
    ] # [str] | OR of tenants within the scope of which archive needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can archive logs in their tenant scope only. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get ArchiveRequest object
        api_response = api_instance.get_archive_request(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_archive_request: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_type** | **str**|  | [optional]
 **query_tenants** | **[str]**| OR of tenants within the scope of which archive needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can archive logs in their tenant scope only. | [optional]

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive_request1**
> MonitoringArchiveRequest get_archive_request1(o_name)

Get ArchiveRequest object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_archive_request import MonitoringArchiveRequest
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_type = "spec.type_example" # str |  (optional)
    query_tenants = [
        "query.tenants_example",
    ] # [str] | OR of tenants within the scope of which archive needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can archive logs in their tenant scope only. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get ArchiveRequest object
        api_response = api_instance.get_archive_request1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_archive_request1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_type** | **str**|  | [optional]
 **query_tenants** | **[str]**| OR of tenants within the scope of which archive needs to be performed. If not specified, it will be set to tenant of the logged in user. Also users in non default tenant can archive logs in their tenant scope only. | [optional]

### Return type

[**MonitoringArchiveRequest**](MonitoringArchiveRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_policy**
> MonitoringAuditPolicy get_audit_policy(o_tenant)

Get AuditPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_audit_policy import MonitoringAuditPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AuditPolicy object
        api_response = api_instance.get_audit_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_audit_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_policy1**
> MonitoringAuditPolicy get_audit_policy1()

Get AuditPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_audit_policy import MonitoringAuditPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get AuditPolicy object
        api_response = api_instance.get_audit_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_audit_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_policy**
> MonitoringEventPolicy get_event_policy(o_tenant)

Get EventPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy import MonitoringEventPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get EventPolicy object
        api_response = api_instance.get_event_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_event_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_policy1**
> MonitoringEventPolicy get_event_policy1(o_name)

Get EventPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy import MonitoringEventPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get EventPolicy object
        api_response = api_instance.get_event_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_event_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_export_policy**
> MonitoringFlowExportPolicy get_flow_export_policy(o_tenant)

Get FlowExportPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_format = "spec.format_example" # str |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FlowExportPolicy object
        api_response = api_instance.get_flow_export_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_flow_export_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_format** | **str**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_export_policy1**
> MonitoringFlowExportPolicy get_flow_export_policy1(o_name)

Get FlowExportPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_format = "spec.format_example" # str |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FlowExportPolicy object
        api_response = api_instance.get_flow_export_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_flow_export_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_format** | **str**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fwlog_policy**
> MonitoringFwlogPolicy get_fwlog_policy(o_tenant)

Get FwlogPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_filter = [
        "spec.filter_example",
    ] # [str] | filter firewall logs, FWLOG_ALL default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FwlogPolicy object
        api_response = api_instance.get_fwlog_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_fwlog_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_filter** | **[str]**| filter firewall logs, FWLOG_ALL default. | [optional]

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fwlog_policy1**
> MonitoringFwlogPolicy get_fwlog_policy1(o_name)

Get FwlogPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_filter = [
        "spec.filter_example",
    ] # [str] | filter firewall logs, FWLOG_ALL default. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get FwlogPolicy object
        api_response = api_instance.get_fwlog_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_fwlog_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_filter** | **[str]**| filter firewall logs, FWLOG_ALL default. | [optional]

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mirror_session**
> MonitoringMirrorSession get_mirror_session(o_tenant)

Get MirrorSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    start_condition_schedule_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    spec_packet_filters = [
        "spec.packet-filters_example",
    ] # [str] |  (optional)
    interfaces_direction = "interfaces.direction_example" # str |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get MirrorSession object
        api_response = api_instance.get_mirror_session(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_mirror_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **start_condition_schedule_time** | **datetime**|  | [optional]
 **spec_packet_filters** | **[str]**|  | [optional]
 **interfaces_direction** | **str**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mirror_session1**
> MonitoringMirrorSession get_mirror_session1(o_name)

Get MirrorSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    start_condition_schedule_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    spec_packet_filters = [
        "spec.packet-filters_example",
    ] # [str] |  (optional)
    interfaces_direction = "interfaces.direction_example" # str |  (optional)
    propagation_status_pending_dscs = [
        "propagation-status.pending-dscs_example",
    ] # [str] | list of DSCs where propagation did not complete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get MirrorSession object
        api_response = api_instance.get_mirror_session1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_mirror_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **start_condition_schedule_time** | **datetime**|  | [optional]
 **spec_packet_filters** | **[str]**|  | [optional]
 **interfaces_direction** | **str**|  | [optional]
 **propagation_status_pending_dscs** | **[str]**| list of DSCs where propagation did not complete. | [optional]

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_alert_policy**
> MonitoringStatsAlertPolicy get_stats_alert_policy(o_tenant)

Get StatsAlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_destinations = [
        "spec.destinations_example",
    ] # [str] | name of the alert destinations to be used to send out notification when an alert gets generated. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get StatsAlertPolicy object
        api_response = api_instance.get_stats_alert_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_stats_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_destinations** | **[str]**| name of the alert destinations to be used to send out notification when an alert gets generated. | [optional]

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_alert_policy1**
> MonitoringStatsAlertPolicy get_stats_alert_policy1(o_name)

Get StatsAlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    spec_destinations = [
        "spec.destinations_example",
    ] # [str] | name of the alert destinations to be used to send out notification when an alert gets generated. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get StatsAlertPolicy object
        api_response = api_instance.get_stats_alert_policy1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_stats_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **spec_destinations** | **[str]**| name of the alert destinations to be used to send out notification when an alert gets generated. | [optional]

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tech_support_request**
> MonitoringTechSupportRequest get_tech_support_request(o_name)

Get TechSupportRequest object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_tech_support_request import MonitoringTechSupportRequest
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    node_selector_names = [
        "node-selector.names_example",
    ] # [str] |  (optional)
    status_instance_id = "status.instance-id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get TechSupportRequest object
        api_response = api_instance.get_tech_support_request(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_tech_support_request: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **node_selector_names** | **[str]**|  | [optional]
 **status_instance_id** | **str**|  | [optional]

### Return type

[**MonitoringTechSupportRequest**](MonitoringTechSupportRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_troubleshooting_session**
> MonitoringTroubleshootingSession get_troubleshooting_session(o_tenant)

Get TroubleshootingSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    source_ip_addresses = [
        "source.ip-addresses_example",
    ] # [str] | IP address list, example [\"10.1.1.10\",\"10.1.1.15\"]. (optional)
    spec_repeat_every = "spec.repeat-every_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get TroubleshootingSession object
        api_response = api_instance.get_troubleshooting_session(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_troubleshooting_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **source_ip_addresses** | **[str]**| IP address list, example [\&quot;10.1.1.10\&quot;,\&quot;10.1.1.15\&quot;]. | [optional]
 **spec_repeat_every** | **str**|  | [optional]

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_troubleshooting_session1**
> MonitoringTroubleshootingSession get_troubleshooting_session1(o_name)

Get TroubleshootingSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    t_kind = "T.kind_example" # str | Kind represents the type of the API object. (optional)
    meta_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    source_ip_addresses = [
        "source.ip-addresses_example",
    ] # [str] | IP address list, example [\"10.1.1.10\",\"10.1.1.15\"]. (optional)
    spec_repeat_every = "spec.repeat-every_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get TroubleshootingSession object
        api_response = api_instance.get_troubleshooting_session1(o_name)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->get_troubleshooting_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **t_kind** | **str**| Kind represents the type of the API object. | [optional]
 **meta_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **source_ip_addresses** | **[str]**| IP address list, example [\&quot;10.1.1.10\&quot;,\&quot;10.1.1.15\&quot;]. | [optional]
 **spec_repeat_every** | **str**|  | [optional]

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_alert**
> MonitoringAlert label_alert(o_tenant, body)

Label Alert object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label Alert object
        api_response = api_instance.label_alert(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_alert1**
> MonitoringAlert label_alert1(o_name, body)

Label Alert object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label Alert object
        api_response = api_instance.label_alert1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_alert_destination**
> MonitoringAlertDestination label_alert_destination(o_tenant, body)

Label AlertDestination object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.monitoring_alert_destination import MonitoringAlertDestination
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label AlertDestination object
        api_response = api_instance.label_alert_destination(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert_destination: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_alert_destination1**
> MonitoringAlertDestination label_alert_destination1(o_name, body)

Label AlertDestination object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.monitoring_alert_destination import MonitoringAlertDestination
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label AlertDestination object
        api_response = api_instance.label_alert_destination1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert_destination1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_alert_policy**
> MonitoringAlertPolicy label_alert_policy(o_tenant, body)

Label AlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label AlertPolicy object
        api_response = api_instance.label_alert_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_alert_policy1**
> MonitoringAlertPolicy label_alert_policy1(o_name, body)

Label AlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label AlertPolicy object
        api_response = api_instance.label_alert_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_event_policy**
> MonitoringEventPolicy label_event_policy(o_tenant, body)

Label EventPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy import MonitoringEventPolicy
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label EventPolicy object
        api_response = api_instance.label_event_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_event_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_event_policy1**
> MonitoringEventPolicy label_event_policy1(o_name, body)

Label EventPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy import MonitoringEventPolicy
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label EventPolicy object
        api_response = api_instance.label_event_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_event_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_flow_export_policy**
> MonitoringFlowExportPolicy label_flow_export_policy(o_tenant, body)

Label FlowExportPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label FlowExportPolicy object
        api_response = api_instance.label_flow_export_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_flow_export_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_flow_export_policy1**
> MonitoringFlowExportPolicy label_flow_export_policy1(o_name, body)

Label FlowExportPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label FlowExportPolicy object
        api_response = api_instance.label_flow_export_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_flow_export_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_fwlog_policy**
> MonitoringFwlogPolicy label_fwlog_policy(o_tenant, body)

Label FwlogPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label FwlogPolicy object
        api_response = api_instance.label_fwlog_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_fwlog_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_fwlog_policy1**
> MonitoringFwlogPolicy label_fwlog_policy1(o_name, body)

Label FwlogPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label FwlogPolicy object
        api_response = api_instance.label_fwlog_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_fwlog_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_mirror_session**
> MonitoringMirrorSession label_mirror_session(o_tenant, body)

Label MirrorSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label MirrorSession object
        api_response = api_instance.label_mirror_session(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_mirror_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_mirror_session1**
> MonitoringMirrorSession label_mirror_session1(o_name, body)

Label MirrorSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label MirrorSession object
        api_response = api_instance.label_mirror_session1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_mirror_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_stats_alert_policy**
> MonitoringStatsAlertPolicy label_stats_alert_policy(o_tenant, body)

Label StatsAlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label StatsAlertPolicy object
        api_response = api_instance.label_stats_alert_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_stats_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_stats_alert_policy1**
> MonitoringStatsAlertPolicy label_stats_alert_policy1(o_name, body)

Label StatsAlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label StatsAlertPolicy object
        api_response = api_instance.label_stats_alert_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_stats_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_troubleshooting_session**
> MonitoringTroubleshootingSession label_troubleshooting_session(o_tenant, body)

Label TroubleshootingSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label TroubleshootingSession object
        api_response = api_instance.label_troubleshooting_session(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_troubleshooting_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_troubleshooting_session1**
> MonitoringTroubleshootingSession label_troubleshooting_session1(o_name, body)

Label TroubleshootingSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pensando_dss.psm.model.api_label import ApiLabel
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = ApiLabel(
        api_version="api_version_example",
        creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        generation_id="generation_id_example",
        kind="kind_example",
        labels={
            "key": "key_example",
        },
        mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        name="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        namespace="g6bUUGjjNSwg0_bs9ZayIMrKdgNvb",
        resource_version="resource_version_example",
        self_link="self_link_example",
        tenant="C",
        uuid="uuid_example",
    ) # ApiLabel | 

    # example passing only required values which don't have defaults set
    try:
        # Label TroubleshootingSession object
        api_response = api_instance.label_troubleshooting_session1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->label_troubleshooting_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**ApiLabel**](ApiLabel.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert**
> MonitoringAlertList list_alert(o_tenant)

List Alert objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_list import MonitoringAlertList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Alert objects
        api_response = api_instance.list_alert(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAlertList**](MonitoringAlertList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert1**
> MonitoringAlertList list_alert1()

List Alert objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_list import MonitoringAlertList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Alert objects
        api_response = api_instance.list_alert1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAlertList**](MonitoringAlertList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_destination**
> MonitoringAlertDestinationList list_alert_destination(o_tenant)

List AlertDestination objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_destination_list import MonitoringAlertDestinationList
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List AlertDestination objects
        api_response = api_instance.list_alert_destination(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert_destination: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAlertDestinationList**](MonitoringAlertDestinationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_destination1**
> MonitoringAlertDestinationList list_alert_destination1()

List AlertDestination objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_destination_list import MonitoringAlertDestinationList
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List AlertDestination objects
        api_response = api_instance.list_alert_destination1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert_destination1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAlertDestinationList**](MonitoringAlertDestinationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_policy**
> MonitoringAlertPolicyList list_alert_policy(o_tenant)

List AlertPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_policy_list import MonitoringAlertPolicyList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List AlertPolicy objects
        api_response = api_instance.list_alert_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAlertPolicyList**](MonitoringAlertPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_policy1**
> MonitoringAlertPolicyList list_alert_policy1()

List AlertPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_policy_list import MonitoringAlertPolicyList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List AlertPolicy objects
        api_response = api_instance.list_alert_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAlertPolicyList**](MonitoringAlertPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_archive_request**
> MonitoringArchiveRequestList list_archive_request(o_tenant)

List ArchiveRequest objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_archive_request_list import MonitoringArchiveRequestList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List ArchiveRequest objects
        api_response = api_instance.list_archive_request(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_archive_request: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringArchiveRequestList**](MonitoringArchiveRequestList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_archive_request1**
> MonitoringArchiveRequestList list_archive_request1()

List ArchiveRequest objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_archive_request_list import MonitoringArchiveRequestList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List ArchiveRequest objects
        api_response = api_instance.list_archive_request1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_archive_request1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringArchiveRequestList**](MonitoringArchiveRequestList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_policy**
> MonitoringEventPolicyList list_event_policy(o_tenant)

List EventPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy_list import MonitoringEventPolicyList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List EventPolicy objects
        api_response = api_instance.list_event_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_event_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringEventPolicyList**](MonitoringEventPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_policy1**
> MonitoringEventPolicyList list_event_policy1()

List EventPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy_list import MonitoringEventPolicyList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List EventPolicy objects
        api_response = api_instance.list_event_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_event_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringEventPolicyList**](MonitoringEventPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_flow_export_policy**
> MonitoringFlowExportPolicyList list_flow_export_policy(o_tenant)

List FlowExportPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy_list import MonitoringFlowExportPolicyList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List FlowExportPolicy objects
        api_response = api_instance.list_flow_export_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_flow_export_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringFlowExportPolicyList**](MonitoringFlowExportPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_flow_export_policy1**
> MonitoringFlowExportPolicyList list_flow_export_policy1()

List FlowExportPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy_list import MonitoringFlowExportPolicyList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List FlowExportPolicy objects
        api_response = api_instance.list_flow_export_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_flow_export_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringFlowExportPolicyList**](MonitoringFlowExportPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fwlog_policy**
> MonitoringFwlogPolicyList list_fwlog_policy(o_tenant)

List FwlogPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy_list import MonitoringFwlogPolicyList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List FwlogPolicy objects
        api_response = api_instance.list_fwlog_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_fwlog_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringFwlogPolicyList**](MonitoringFwlogPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fwlog_policy1**
> MonitoringFwlogPolicyList list_fwlog_policy1()

List FwlogPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy_list import MonitoringFwlogPolicyList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List FwlogPolicy objects
        api_response = api_instance.list_fwlog_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_fwlog_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringFwlogPolicyList**](MonitoringFwlogPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mirror_session**
> MonitoringMirrorSessionList list_mirror_session(o_tenant)

List MirrorSession objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session_list import MonitoringMirrorSessionList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List MirrorSession objects
        api_response = api_instance.list_mirror_session(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_mirror_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringMirrorSessionList**](MonitoringMirrorSessionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mirror_session1**
> MonitoringMirrorSessionList list_mirror_session1()

List MirrorSession objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session_list import MonitoringMirrorSessionList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List MirrorSession objects
        api_response = api_instance.list_mirror_session1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_mirror_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringMirrorSessionList**](MonitoringMirrorSessionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stats_alert_policy**
> MonitoringStatsAlertPolicyList list_stats_alert_policy(o_tenant)

List StatsAlertPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_stats_alert_policy_list import MonitoringStatsAlertPolicyList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List StatsAlertPolicy objects
        api_response = api_instance.list_stats_alert_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_stats_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringStatsAlertPolicyList**](MonitoringStatsAlertPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stats_alert_policy1**
> MonitoringStatsAlertPolicyList list_stats_alert_policy1()

List StatsAlertPolicy objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_stats_alert_policy_list import MonitoringStatsAlertPolicyList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List StatsAlertPolicy objects
        api_response = api_instance.list_stats_alert_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_stats_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringStatsAlertPolicyList**](MonitoringStatsAlertPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tech_support_request**
> MonitoringTechSupportRequestList list_tech_support_request()

List TechSupportRequest objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_tech_support_request_list import MonitoringTechSupportRequestList
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List TechSupportRequest objects
        api_response = api_instance.list_tech_support_request()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_tech_support_request: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringTechSupportRequestList**](MonitoringTechSupportRequestList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_troubleshooting_session**
> MonitoringTroubleshootingSessionList list_troubleshooting_session(o_tenant)

List TroubleshootingSession objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session_list import MonitoringTroubleshootingSessionList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List TroubleshootingSession objects
        api_response = api_instance.list_troubleshooting_session(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_troubleshooting_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringTroubleshootingSessionList**](MonitoringTroubleshootingSessionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_troubleshooting_session1**
> MonitoringTroubleshootingSessionList list_troubleshooting_session1()

List TroubleshootingSession objects

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session_list import MonitoringTroubleshootingSessionList
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List TroubleshootingSession objects
        api_response = api_instance.list_troubleshooting_session1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->list_troubleshooting_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringTroubleshootingSessionList**](MonitoringTroubleshootingSessionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert**
> MonitoringAlert update_alert(o_tenant, body)

Update Alert object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringAlert(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertSpec(
            state="open",
        ),
        status=MonitoringAlertStatus(
            acknowledged=MonitoringAuditInfo(
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                user="user_example",
            ),
            event_uri="event_uri_example",
            message="message_example",
            object_ref=ApiObjectRef(
                kind="kind_example",
                name="name_example",
                namespace="namespace_example",
                tenant="tenant_example",
                uri="uri_example",
            ),
            reason=MonitoringAlertReason(
                alert_policy_id="alert_policy_id_example",
                matched_requirements=[
                    MonitoringMatchedRequirement(
                        key="key_example",
                        observed_value="observed_value_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            resolved=MonitoringAuditInfo(
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                user="user_example",
            ),
            severity="info",
            source=MonitoringAlertSource(
                component="component_example",
                node_name="node_name_example",
            ),
            total_hits=1,
        ),
    ) # MonitoringAlert | 

    # example passing only required values which don't have defaults set
    try:
        # Update Alert object
        api_response = api_instance.update_alert(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringAlert**](MonitoringAlert.md)|  |

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert1**
> MonitoringAlert update_alert1(o_name, body)

Update Alert object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert import MonitoringAlert
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringAlert(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertSpec(
            state="open",
        ),
        status=MonitoringAlertStatus(
            acknowledged=MonitoringAuditInfo(
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                user="user_example",
            ),
            event_uri="event_uri_example",
            message="message_example",
            object_ref=ApiObjectRef(
                kind="kind_example",
                name="name_example",
                namespace="namespace_example",
                tenant="tenant_example",
                uri="uri_example",
            ),
            reason=MonitoringAlertReason(
                alert_policy_id="alert_policy_id_example",
                matched_requirements=[
                    MonitoringMatchedRequirement(
                        key="key_example",
                        observed_value="observed_value_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            resolved=MonitoringAuditInfo(
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                user="user_example",
            ),
            severity="info",
            source=MonitoringAlertSource(
                component="component_example",
                node_name="node_name_example",
            ),
            total_hits=1,
        ),
    ) # MonitoringAlert | 

    # example passing only required values which don't have defaults set
    try:
        # Update Alert object
        api_response = api_instance.update_alert1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringAlert**](MonitoringAlert.md)|  |

### Return type

[**MonitoringAlert**](MonitoringAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_destination**
> MonitoringAlertDestination update_alert_destination(o_tenant, body)

Update AlertDestination object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_destination import MonitoringAlertDestination
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringAlertDestination(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertDestinationSpec(
            email_export=MonitoringEmailExport(
                email_list=[
                    "email_list_example",
                ],
            ),
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            snmp_export=MonitoringSNMPExport(
                snmp_trap_servers=[
                    MonitoringSNMPTrapServer(
                        auth_config=MonitoringAuthConfig(
                            algo="md5",
                            password="password_example",
                        ),
                        community_or_user="community_or_user_example",
                        host="host_example",
                        port="162",
                        privacy_config=MonitoringPrivacyConfig(
                            algo="des56",
                            password="password_example",
                        ),
                        version="v2c",
                    ),
                ],
            ),
            syslog_export=MonitoringSyslogExport(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
        ),
        status=MonitoringAlertDestinationStatus(
            total_notifications_sent=1,
        ),
    ) # MonitoringAlertDestination | 

    # example passing only required values which don't have defaults set
    try:
        # Update AlertDestination object
        api_response = api_instance.update_alert_destination(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert_destination: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringAlertDestination**](MonitoringAlertDestination.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_destination1**
> MonitoringAlertDestination update_alert_destination1(o_name, body)

Update AlertDestination object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_alert_destination import MonitoringAlertDestination
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringAlertDestination(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertDestinationSpec(
            email_export=MonitoringEmailExport(
                email_list=[
                    "email_list_example",
                ],
            ),
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            snmp_export=MonitoringSNMPExport(
                snmp_trap_servers=[
                    MonitoringSNMPTrapServer(
                        auth_config=MonitoringAuthConfig(
                            algo="md5",
                            password="password_example",
                        ),
                        community_or_user="community_or_user_example",
                        host="host_example",
                        port="162",
                        privacy_config=MonitoringPrivacyConfig(
                            algo="des56",
                            password="password_example",
                        ),
                        version="v2c",
                    ),
                ],
            ),
            syslog_export=MonitoringSyslogExport(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
        ),
        status=MonitoringAlertDestinationStatus(
            total_notifications_sent=1,
        ),
    ) # MonitoringAlertDestination | 

    # example passing only required values which don't have defaults set
    try:
        # Update AlertDestination object
        api_response = api_instance.update_alert_destination1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert_destination1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringAlertDestination**](MonitoringAlertDestination.md)|  |

### Return type

[**MonitoringAlertDestination**](MonitoringAlertDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_policy**
> MonitoringAlertPolicy update_alert_policy(o_tenant, body)

Update AlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            message="message_example",
            requirements=[
                FieldsRequirement(
                    key="key_example",
                    operator="equals",
                    values=[
                        "values_example",
                    ],
                ),
            ],
            resource="resource_example",
            severity="info",
        ),
        status=MonitoringAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update AlertPolicy object
        api_response = api_instance.update_alert_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_policy1**
> MonitoringAlertPolicy update_alert_policy1(o_name, body)

Update AlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_alert_policy import MonitoringAlertPolicy
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            message="message_example",
            requirements=[
                FieldsRequirement(
                    key="key_example",
                    operator="equals",
                    values=[
                        "values_example",
                    ],
                ),
            ],
            resource="resource_example",
            severity="info",
        ),
        status=MonitoringAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update AlertPolicy object
        api_response = api_instance.update_alert_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)|  |

### Return type

[**MonitoringAlertPolicy**](MonitoringAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_audit_policy**
> MonitoringAuditPolicy update_audit_policy(o_tenant, body)

Update AuditPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_audit_policy import MonitoringAuditPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringAuditPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAuditPolicySpec(
            syslog_auditor=MonitoringSyslogAuditor(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                enabled=True,
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
        ),
        status={},
    ) # MonitoringAuditPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update AuditPolicy object
        api_response = api_instance.update_audit_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_audit_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)|  |

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_audit_policy1**
> MonitoringAuditPolicy update_audit_policy1(body)

Update AuditPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_audit_policy import MonitoringAuditPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    body = MonitoringAuditPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringAuditPolicySpec(
            syslog_auditor=MonitoringSyslogAuditor(
                config=MonitoringSyslogExportConfig(
                    facility_override="user",
                    prefix="prefix_example",
                ),
                enabled=True,
                format="syslog-bsd",
                targets=[
                    MonitoringExportConfig(
                        destination="10.1.1.1 ",
                        gateway="10.1.1.1 ",
                        transport="udp/1234",
                        virtual_router="virtual_router_example",
                    ),
                ],
            ),
        ),
        status={},
    ) # MonitoringAuditPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update AuditPolicy object
        api_response = api_instance.update_audit_policy1(body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_audit_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)|  |

### Return type

[**MonitoringAuditPolicy**](MonitoringAuditPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_policy**
> MonitoringEventPolicy update_event_policy(o_tenant, body)

Update EventPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy import MonitoringEventPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringEventPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringEventPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            format="syslog-bsd",
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
        ),
        status={},
    ) # MonitoringEventPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update EventPolicy object
        api_response = api_instance.update_event_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_event_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringEventPolicy**](MonitoringEventPolicy.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_policy1**
> MonitoringEventPolicy update_event_policy1(o_name, body)

Update EventPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_event_policy import MonitoringEventPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringEventPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringEventPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            format="syslog-bsd",
            selector=FieldsSelector(
                requirements=[
                    FieldsRequirement(
                        key="key_example",
                        operator="equals",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
        ),
        status={},
    ) # MonitoringEventPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update EventPolicy object
        api_response = api_instance.update_event_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_event_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringEventPolicy**](MonitoringEventPolicy.md)|  |

### Return type

[**MonitoringEventPolicy**](MonitoringEventPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_export_policy**
> MonitoringFlowExportPolicy update_flow_export_policy(o_tenant, body)

Update FlowExportPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringFlowExportPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFlowExportPolicySpec(
            disabled=True,
            exports=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
            format="ipfix",
            interval="60s",
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            template_interval="60s",
        ),
        status=MonitoringFlowExportPolicyStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            state="disabled",
        ),
    ) # MonitoringFlowExportPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update FlowExportPolicy object
        api_response = api_instance.update_flow_export_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_flow_export_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_export_policy1**
> MonitoringFlowExportPolicy update_flow_export_policy1(o_name, body)

Update FlowExportPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_flow_export_policy import MonitoringFlowExportPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringFlowExportPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFlowExportPolicySpec(
            disabled=True,
            exports=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
            format="ipfix",
            interval="60s",
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            template_interval="60s",
        ),
        status=MonitoringFlowExportPolicyStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            state="disabled",
        ),
    ) # MonitoringFlowExportPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update FlowExportPolicy object
        api_response = api_instance.update_flow_export_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_flow_export_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)|  |

### Return type

[**MonitoringFlowExportPolicy**](MonitoringFlowExportPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fwlog_policy**
> MonitoringFwlogPolicy update_fwlog_policy(o_tenant, body)

Update FwlogPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringFwlogPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFwlogPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            filter=[
                "filter_example",
            ],
            format="syslog-bsd",
            psm_target=MonitoringPSMExportTarget(
                enable=True,
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
            vrf_name="vrf_name_example",
        ),
        status={},
    ) # MonitoringFwlogPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update FwlogPolicy object
        api_response = api_instance.update_fwlog_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_fwlog_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fwlog_policy1**
> MonitoringFwlogPolicy update_fwlog_policy1(o_name, body)

Update FwlogPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_fwlog_policy import MonitoringFwlogPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringFwlogPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringFwlogPolicySpec(
            config=MonitoringSyslogExportConfig(
                facility_override="user",
                prefix="prefix_example",
            ),
            filter=[
                "filter_example",
            ],
            format="syslog-bsd",
            psm_target=MonitoringPSMExportTarget(
                enable=True,
            ),
            targets=[
                MonitoringExportConfig(
                    destination="10.1.1.1 ",
                    gateway="10.1.1.1 ",
                    transport="udp/1234",
                    virtual_router="virtual_router_example",
                ),
            ],
            vrf_name="vrf_name_example",
        ),
        status={},
    ) # MonitoringFwlogPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update FwlogPolicy object
        api_response = api_instance.update_fwlog_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_fwlog_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)|  |

### Return type

[**MonitoringFwlogPolicy**](MonitoringFwlogPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mirror_session**
> MonitoringMirrorSession update_mirror_session(o_tenant, body)

Update MirrorSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringMirrorSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringMirrorSessionSpec(
            collectors=[
                MonitoringMirrorCollector(
                    export_config=MonitoringMirrorExportConfig(
                        destination="10.1.1.1 ",
                        gateway="gateway_example",
                        virtual_router="virtual_router_example",
                    ),
                    strip_vlan_hdr=True,
                    type="erspan_type_3",
                ),
            ],
            disabled=True,
            interfaces=MonitoringInterfaceMirror(
                direction="both",
                selectors=[
                    LabelsSelector(
                        requirements=[
                            LabelsRequirement(
                                key="key_example",
                                operator="equals",
                                values=[
                                    "values_example",
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            packet_filters=[
                "packet_filters_example",
            ],
            packet_size=64,
            source=MonitoringMirrorSource(
                direction="both",
                target_selectors=[
                    LabelsSelector(
                        requirements=[],
                    ),
                ],
                target_type="none",
            ),
            span_id=1,
            start_condition=MonitoringMirrorStartConditions(
                schedule_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            workloads=MonitoringWorkloadMirror(
                direction="both",
                selectors=[],
            ),
        ),
        status=MonitoringMirrorSessionStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            schedule_state="none",
            started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # MonitoringMirrorSession | 

    # example passing only required values which don't have defaults set
    try:
        # Update MirrorSession object
        api_response = api_instance.update_mirror_session(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_mirror_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringMirrorSession**](MonitoringMirrorSession.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mirror_session1**
> MonitoringMirrorSession update_mirror_session1(o_name, body)

Update MirrorSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_mirror_session import MonitoringMirrorSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringMirrorSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringMirrorSessionSpec(
            collectors=[
                MonitoringMirrorCollector(
                    export_config=MonitoringMirrorExportConfig(
                        destination="10.1.1.1 ",
                        gateway="gateway_example",
                        virtual_router="virtual_router_example",
                    ),
                    strip_vlan_hdr=True,
                    type="erspan_type_3",
                ),
            ],
            disabled=True,
            interfaces=MonitoringInterfaceMirror(
                direction="both",
                selectors=[
                    LabelsSelector(
                        requirements=[
                            LabelsRequirement(
                                key="key_example",
                                operator="equals",
                                values=[
                                    "values_example",
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            match_rules=[
                MonitoringMatchRule(
                    app_protocol_selectors=MonitoringAppProtoSelector(
                        applications=[
                            "applications_example",
                        ],
                        proto_ports=[
                            "udp/1234",
                        ],
                    ),
                    destination=MonitoringMatchSelector(
                        ip_addresses=[
                            "ip_addresses_example",
                        ],
                        mac_addresses=[
                            "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                        ],
                    ),
                    source=MonitoringMatchSelector(
                        ip_addresses=[],
                        mac_addresses=[],
                    ),
                ),
            ],
            packet_filters=[
                "packet_filters_example",
            ],
            packet_size=64,
            source=MonitoringMirrorSource(
                direction="both",
                target_selectors=[
                    LabelsSelector(
                        requirements=[],
                    ),
                ],
                target_type="none",
            ),
            span_id=1,
            start_condition=MonitoringMirrorStartConditions(
                schedule_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            workloads=MonitoringWorkloadMirror(
                direction="both",
                selectors=[],
            ),
        ),
        status=MonitoringMirrorSessionStatus(
            propagation_status=MonitoringPropagationStatus(
                dsc_status=[
                    MonitoringDSCStatus(
                        dsc_id="dsc_id_example",
                        dsc_info_status="dsc_info_status_example",
                    ),
                ],
                generation_id="generation_id_example",
                min_version="min_version_example",
                pending=1,
                pending_dscs=[
                    "pending_dscs_example",
                ],
                status="status_example",
                updated=1,
            ),
            schedule_state="none",
            started_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # MonitoringMirrorSession | 

    # example passing only required values which don't have defaults set
    try:
        # Update MirrorSession object
        api_response = api_instance.update_mirror_session1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_mirror_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringMirrorSession**](MonitoringMirrorSession.md)|  |

### Return type

[**MonitoringMirrorSession**](MonitoringMirrorSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stats_alert_policy**
> MonitoringStatsAlertPolicy update_stats_alert_policy(o_tenant, body)

Update StatsAlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringStatsAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringStatsAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            instance_selector=MonitoringInstanceSelector(
                kind="kind_example",
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                names=[
                    "names_example",
                ],
            ),
            measurement_criteria=MonitoringMeasurementCriteria(
                function="none_function",
                window="window_example",
            ),
            message_template="message_template_example",
            metric=MonitoringMetricIdentifier(
                field_name="field_name_example",
                group="group_example",
                kind="kind_example",
            ),
            thresholds=MonitoringThresholds(
                operator="less_or_equal_than",
                values=[
                    MonitoringThreshold(
                        raise_value="raise_value_example",
                        severity="info",
                    ),
                ],
            ),
        ),
        status=MonitoringStatsAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringStatsAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update StatsAlertPolicy object
        api_response = api_instance.update_stats_alert_policy(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_stats_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stats_alert_policy1**
> MonitoringStatsAlertPolicy update_stats_alert_policy1(o_name, body)

Update StatsAlertPolicy object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_stats_alert_policy import MonitoringStatsAlertPolicy
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringStatsAlertPolicy(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringStatsAlertPolicySpec(
            destinations=[
                "destinations_example",
            ],
            enable=True,
            instance_selector=MonitoringInstanceSelector(
                kind="kind_example",
                labels=LabelsSelector(
                    requirements=[
                        LabelsRequirement(
                            key="key_example",
                            operator="equals",
                            values=[
                                "values_example",
                            ],
                        ),
                    ],
                ),
                names=[
                    "names_example",
                ],
            ),
            measurement_criteria=MonitoringMeasurementCriteria(
                function="none_function",
                window="window_example",
            ),
            message_template="message_template_example",
            metric=MonitoringMetricIdentifier(
                field_name="field_name_example",
                group="group_example",
                kind="kind_example",
            ),
            thresholds=MonitoringThresholds(
                operator="less_or_equal_than",
                values=[
                    MonitoringThreshold(
                        raise_value="raise_value_example",
                        severity="info",
                    ),
                ],
            ),
        ),
        status=MonitoringStatsAlertPolicyStatus(
            acknowledged_alerts=1,
            open_alerts=1,
            total_hits=1,
        ),
    ) # MonitoringStatsAlertPolicy | 

    # example passing only required values which don't have defaults set
    try:
        # Update StatsAlertPolicy object
        api_response = api_instance.update_stats_alert_policy1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_stats_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)|  |

### Return type

[**MonitoringStatsAlertPolicy**](MonitoringStatsAlertPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_troubleshooting_session**
> MonitoringTroubleshootingSession update_troubleshooting_session(o_tenant, body)

Update TroubleshootingSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    body = MonitoringTroubleshootingSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringTroubleshootingSessionSpec(
            enable_mirroring=True,
            flow_selector=MonitoringMatchRule(
                app_protocol_selectors=MonitoringAppProtoSelector(
                    applications=[
                        "applications_example",
                    ],
                    proto_ports=[
                        "udp/1234",
                    ],
                ),
                destination=MonitoringMatchSelector(
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_addresses=[
                        "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    ],
                ),
                source=MonitoringMatchSelector(
                    ip_addresses=[],
                    mac_addresses=[],
                ),
            ),
            repeat_every="repeat_every_example",
            time_window=MonitoringTimeWindow(
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
        status=MonitoringTroubleshootingSessionStatus(
            state="running",
            troubleshooting_results=[
                MonitoringTsResult(
                    report_url="report_url_example",
                    time_window=MonitoringTimeWindow(
                        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ),
            ],
        ),
    ) # MonitoringTroubleshootingSession | 

    # example passing only required values which don't have defaults set
    try:
        # Update TroubleshootingSession object
        api_response = api_instance.update_troubleshooting_session(o_tenant, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_troubleshooting_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **body** | [**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_troubleshooting_session1**
> MonitoringTroubleshootingSession update_troubleshooting_session1(o_name, body)

Update TroubleshootingSession object

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_troubleshooting_session import MonitoringTroubleshootingSession
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.Name_example" # str | 
    body = MonitoringTroubleshootingSession(
        api_version="api_version_example",
        kind="kind_example",
        meta=ApiObjectMeta(
            creation_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            generation_id="generation_id_example",
            labels={
                "key": "key_example",
            },
            mod_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            name="name_example",
            namespace="namespace_example",
            resource_version="resource_version_example",
            self_link="self_link_example",
            tenant="tenant_example",
            uuid="uuid_example",
        ),
        spec=MonitoringTroubleshootingSessionSpec(
            enable_mirroring=True,
            flow_selector=MonitoringMatchRule(
                app_protocol_selectors=MonitoringAppProtoSelector(
                    applications=[
                        "applications_example",
                    ],
                    proto_ports=[
                        "udp/1234",
                    ],
                ),
                destination=MonitoringMatchSelector(
                    ip_addresses=[
                        "ip_addresses_example",
                    ],
                    mac_addresses=[
                        "aabb.ccdd.0000, aabb.ccdd.0000, aabb.ccdd.0000",
                    ],
                ),
                source=MonitoringMatchSelector(
                    ip_addresses=[],
                    mac_addresses=[],
                ),
            ),
            repeat_every="repeat_every_example",
            time_window=MonitoringTimeWindow(
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
        status=MonitoringTroubleshootingSessionStatus(
            state="running",
            troubleshooting_results=[
                MonitoringTsResult(
                    report_url="report_url_example",
                    time_window=MonitoringTimeWindow(
                        start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        stop_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ),
            ],
        ),
    ) # MonitoringTroubleshootingSession | 

    # example passing only required values which don't have defaults set
    try:
        # Update TroubleshootingSession object
        api_response = api_instance.update_troubleshooting_session1(o_name, body)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->update_troubleshooting_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**|  |
 **body** | [**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)|  |

### Return type

[**MonitoringTroubleshootingSession**](MonitoringTroubleshootingSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_alert**
> MonitoringAutoMsgAlertWatchHelper watch_alert(o_tenant)

Watch Alert objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_alert_watch_helper import MonitoringAutoMsgAlertWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Alert objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgAlertWatchHelper**](MonitoringAutoMsgAlertWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_alert1**
> MonitoringAutoMsgAlertWatchHelper watch_alert1()

Watch Alert objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_alert_watch_helper import MonitoringAutoMsgAlertWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch Alert objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgAlertWatchHelper**](MonitoringAutoMsgAlertWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_alert_destination**
> MonitoringAutoMsgAlertDestinationWatchHelper watch_alert_destination(o_tenant)

Watch AlertDestination objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_auto_msg_alert_destination_watch_helper import MonitoringAutoMsgAlertDestinationWatchHelper
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch AlertDestination objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert_destination(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert_destination: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgAlertDestinationWatchHelper**](MonitoringAutoMsgAlertDestinationWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_alert_destination1**
> MonitoringAutoMsgAlertDestinationWatchHelper watch_alert_destination1()

Watch AlertDestination objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_auto_msg_alert_destination_watch_helper import MonitoringAutoMsgAlertDestinationWatchHelper
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch AlertDestination objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert_destination1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert_destination1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgAlertDestinationWatchHelper**](MonitoringAutoMsgAlertDestinationWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_alert_policy**
> MonitoringAutoMsgAlertPolicyWatchHelper watch_alert_policy(o_tenant)

Watch AlertPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_alert_policy_watch_helper import MonitoringAutoMsgAlertPolicyWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch AlertPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgAlertPolicyWatchHelper**](MonitoringAutoMsgAlertPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_alert_policy1**
> MonitoringAutoMsgAlertPolicyWatchHelper watch_alert_policy1()

Watch AlertPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_alert_policy_watch_helper import MonitoringAutoMsgAlertPolicyWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch AlertPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_alert_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgAlertPolicyWatchHelper**](MonitoringAutoMsgAlertPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_archive_request**
> MonitoringAutoMsgArchiveRequestWatchHelper watch_archive_request(o_tenant)

Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_archive_request_watch_helper import MonitoringAutoMsgArchiveRequestWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_archive_request(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_archive_request: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgArchiveRequestWatchHelper**](MonitoringAutoMsgArchiveRequestWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_archive_request1**
> MonitoringAutoMsgArchiveRequestWatchHelper watch_archive_request1()

Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_archive_request_watch_helper import MonitoringAutoMsgArchiveRequestWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch ArchiveRequest objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_archive_request1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_archive_request1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgArchiveRequestWatchHelper**](MonitoringAutoMsgArchiveRequestWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_audit_policy**
> MonitoringAutoMsgAuditPolicyWatchHelper watch_audit_policy(o_tenant)

Watch AuditPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_auto_msg_audit_policy_watch_helper import MonitoringAutoMsgAuditPolicyWatchHelper
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch AuditPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_audit_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_audit_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgAuditPolicyWatchHelper**](MonitoringAutoMsgAuditPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_audit_policy1**
> MonitoringAutoMsgAuditPolicyWatchHelper watch_audit_policy1()

Watch AuditPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_auto_msg_audit_policy_watch_helper import MonitoringAutoMsgAuditPolicyWatchHelper
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch AuditPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_audit_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_audit_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgAuditPolicyWatchHelper**](MonitoringAutoMsgAuditPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_event_policy**
> MonitoringAutoMsgEventPolicyWatchHelper watch_event_policy(o_tenant)

Watch EventPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_event_policy_watch_helper import MonitoringAutoMsgEventPolicyWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch EventPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_event_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_event_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgEventPolicyWatchHelper**](MonitoringAutoMsgEventPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_event_policy1**
> MonitoringAutoMsgEventPolicyWatchHelper watch_event_policy1()

Watch EventPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_event_policy_watch_helper import MonitoringAutoMsgEventPolicyWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch EventPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_event_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_event_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgEventPolicyWatchHelper**](MonitoringAutoMsgEventPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_flow_export_policy**
> MonitoringAutoMsgFlowExportPolicyWatchHelper watch_flow_export_policy(o_tenant)

Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_auto_msg_flow_export_policy_watch_helper import MonitoringAutoMsgFlowExportPolicyWatchHelper
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_flow_export_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_flow_export_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgFlowExportPolicyWatchHelper**](MonitoringAutoMsgFlowExportPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_flow_export_policy1**
> MonitoringAutoMsgFlowExportPolicyWatchHelper watch_flow_export_policy1()

Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.api_status import ApiStatus
from pensando_dss.psm.model.monitoring_auto_msg_flow_export_policy_watch_helper import MonitoringAutoMsgFlowExportPolicyWatchHelper
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch FlowExportPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_flow_export_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_flow_export_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgFlowExportPolicyWatchHelper**](MonitoringAutoMsgFlowExportPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_fwlog_policy**
> MonitoringAutoMsgFwlogPolicyWatchHelper watch_fwlog_policy(o_tenant)

Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_fwlog_policy_watch_helper import MonitoringAutoMsgFwlogPolicyWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_fwlog_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_fwlog_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgFwlogPolicyWatchHelper**](MonitoringAutoMsgFwlogPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_fwlog_policy1**
> MonitoringAutoMsgFwlogPolicyWatchHelper watch_fwlog_policy1()

Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_fwlog_policy_watch_helper import MonitoringAutoMsgFwlogPolicyWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch FwlogPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_fwlog_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_fwlog_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgFwlogPolicyWatchHelper**](MonitoringAutoMsgFwlogPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_mirror_session**
> MonitoringAutoMsgMirrorSessionWatchHelper watch_mirror_session(o_tenant)

Watch MirrorSession objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_mirror_session_watch_helper import MonitoringAutoMsgMirrorSessionWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch MirrorSession objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_mirror_session(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_mirror_session: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgMirrorSessionWatchHelper**](MonitoringAutoMsgMirrorSessionWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_mirror_session1**
> MonitoringAutoMsgMirrorSessionWatchHelper watch_mirror_session1()

Watch MirrorSession objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_mirror_session_watch_helper import MonitoringAutoMsgMirrorSessionWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch MirrorSession objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_mirror_session1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_mirror_session1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgMirrorSessionWatchHelper**](MonitoringAutoMsgMirrorSessionWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_stats_alert_policy**
> MonitoringAutoMsgStatsAlertPolicyWatchHelper watch_stats_alert_policy(o_tenant)

Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_stats_alert_policy_watch_helper import MonitoringAutoMsgStatsAlertPolicyWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_tenant = "O.Tenant_example" # str | 
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_stats_alert_policy(o_tenant)
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_stats_alert_policy: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_tenant** | **str**|  |
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgStatsAlertPolicyWatchHelper**](MonitoringAutoMsgStatsAlertPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_stats_alert_policy1**
> MonitoringAutoMsgStatsAlertPolicyWatchHelper watch_stats_alert_policy1()

Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_stats_alert_policy_watch_helper import MonitoringAutoMsgStatsAlertPolicyWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch StatsAlertPolicy objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_stats_alert_policy1()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_stats_alert_policy1: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgStatsAlertPolicyWatchHelper**](MonitoringAutoMsgStatsAlertPolicyWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_tech_support_request**
> MonitoringAutoMsgTechSupportRequestWatchHelper watch_tech_support_request()

Watch TechSupportRequest objects. Supports WebSockets or HTTP long poll

### Example

Ensure that `PSM_USER` and `PSM_PASSWORD` are set in your environment

```python
import time
import os
import pensando_dss
import pensando_dss.psm
from pensando_dss.psm.api import monitoring_v1_api
from pensando_dss.psm.models.monitoring import *
from pensando_dss.psm.model.monitoring_auto_msg_tech_support_request_watch_helper import MonitoringAutoMsgTechSupportRequestWatchHelper
from pensando_dss.psm.model.api_status import ApiStatus
from pprint import pprint
from dateutil.parser import parse as dateutil_parser
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pensando_dss.psm.Configuration(
    psm_config_path = os.environ["HOME"] + "/.psm/config.json"
)
configuration.verify_ssl = False


# Enter a context with an instance of the API client
with pensando_dss.psm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_v1_api.MonitoringV1Api(api_client)
    o_name = "O.name_example" # str | Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. (optional)
    o_creation_time = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | CreationTime is the creation time of the object. System generated and updated, not updatable by user. (optional)
    field_change_selector = [
        "field-change-selector_example",
    ] # [str] | FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Watch TechSupportRequest objects. Supports WebSockets or HTTP long poll
        api_response = api_instance.watch_tech_support_request()
        pprint(api_response)
    except pensando_dss.psm.ApiException as e:
        print("Exception when calling MonitoringV1Api->watch_tech_support_request: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_name** | **str**| Name of the object, unique within a Namespace for scoped objects. Must start and end with alpha numeric and can have alphanumeric, -, _, . Length of string should be between 2 and 64. | [optional]
 **o_creation_time** | **datetime**| CreationTime is the creation time of the object. System generated and updated, not updatable by user. | [optional]
 **field_change_selector** | **[str]**| FieldChangeSelector specifies to generate a watch notification on change in field(s) specified. | [optional]

### Return type

[**MonitoringAutoMsgTechSupportRequestWatchHelper**](MonitoringAutoMsgTechSupportRequestWatchHelper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (streaming responses) |  -  |
**400** | Bad request parameters |  -  |
**401** | Unauthorized request |  -  |
**409** | Conflict while processing request |  -  |
**412** | Pre-condition failed |  -  |
**500** | Internal server error |  -  |
**501** | Request not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

