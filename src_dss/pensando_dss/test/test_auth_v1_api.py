"""
    Auth API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import psm
from pensando_dss.psm.api.auth_v1_api import AuthV1Api  # noqa: E501


class TestAuthV1Api(unittest.TestCase):
    """AuthV1Api unit test stubs"""

    def setUp(self):
        self.api = AuthV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_authentication_policy(self):
        """Test case for add_authentication_policy

        Create AuthenticationPolicy object  # noqa: E501
        """
        pass

    def test_add_role(self):
        """Test case for add_role

        Create Role object  # noqa: E501
        """
        pass

    def test_add_role1(self):
        """Test case for add_role1

        Create Role object  # noqa: E501
        """
        pass

    def test_add_role_binding(self):
        """Test case for add_role_binding

        Create RoleBinding object  # noqa: E501
        """
        pass

    def test_add_role_binding1(self):
        """Test case for add_role_binding1

        Create RoleBinding object  # noqa: E501
        """
        pass

    def test_add_user(self):
        """Test case for add_user

        Create User object  # noqa: E501
        """
        pass

    def test_add_user1(self):
        """Test case for add_user1

        Create User object  # noqa: E501
        """
        pass

    def test_delete_role(self):
        """Test case for delete_role

        Delete Role object  # noqa: E501
        """
        pass

    def test_delete_role1(self):
        """Test case for delete_role1

        Delete Role object  # noqa: E501
        """
        pass

    def test_delete_role_binding(self):
        """Test case for delete_role_binding

        Delete RoleBinding object  # noqa: E501
        """
        pass

    def test_delete_role_binding1(self):
        """Test case for delete_role_binding1

        Delete RoleBinding object  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete User object  # noqa: E501
        """
        pass

    def test_delete_user1(self):
        """Test case for delete_user1

        Delete User object  # noqa: E501
        """
        pass

    def test_get_authentication_policy(self):
        """Test case for get_authentication_policy

        Get AuthenticationPolicy object  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Get Role object  # noqa: E501
        """
        pass

    def test_get_role1(self):
        """Test case for get_role1

        Get Role object  # noqa: E501
        """
        pass

    def test_get_role_binding(self):
        """Test case for get_role_binding

        Get RoleBinding object  # noqa: E501
        """
        pass

    def test_get_role_binding1(self):
        """Test case for get_role_binding1

        Get RoleBinding object  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get User object  # noqa: E501
        """
        pass

    def test_get_user1(self):
        """Test case for get_user1

        Get User object  # noqa: E501
        """
        pass

    def test_get_user_preference(self):
        """Test case for get_user_preference

        Get UserPreference object  # noqa: E501
        """
        pass

    def test_get_user_preference1(self):
        """Test case for get_user_preference1

        Get UserPreference object  # noqa: E501
        """
        pass

    def test_is_authorized(self):
        """Test case for is_authorized

        Review authorization for user  # noqa: E501
        """
        pass

    def test_is_authorized1(self):
        """Test case for is_authorized1

        Review authorization for user  # noqa: E501
        """
        pass

    def test_label_authentication_policy(self):
        """Test case for label_authentication_policy

        Label AuthenticationPolicy object  # noqa: E501
        """
        pass

    def test_label_role(self):
        """Test case for label_role

        Label Role object  # noqa: E501
        """
        pass

    def test_label_role1(self):
        """Test case for label_role1

        Label Role object  # noqa: E501
        """
        pass

    def test_label_role_binding(self):
        """Test case for label_role_binding

        Label RoleBinding object  # noqa: E501
        """
        pass

    def test_label_role_binding1(self):
        """Test case for label_role_binding1

        Label RoleBinding object  # noqa: E501
        """
        pass

    def test_label_user(self):
        """Test case for label_user

        Label User object  # noqa: E501
        """
        pass

    def test_label_user1(self):
        """Test case for label_user1

        Label User object  # noqa: E501
        """
        pass

    def test_label_user_preference(self):
        """Test case for label_user_preference

        Label UserPreference object  # noqa: E501
        """
        pass

    def test_label_user_preference1(self):
        """Test case for label_user_preference1

        Label UserPreference object  # noqa: E501
        """
        pass

    def test_ldap_bind_check(self):
        """Test case for ldap_bind_check

        Test LDAP bind operation  # noqa: E501
        """
        pass

    def test_ldap_connection_check(self):
        """Test case for ldap_connection_check

        Test LDAP connection  # noqa: E501
        """
        pass

    def test_list_role(self):
        """Test case for list_role

        List Role objects  # noqa: E501
        """
        pass

    def test_list_role1(self):
        """Test case for list_role1

        List Role objects  # noqa: E501
        """
        pass

    def test_list_role_binding(self):
        """Test case for list_role_binding

        List RoleBinding objects  # noqa: E501
        """
        pass

    def test_list_role_binding1(self):
        """Test case for list_role_binding1

        List RoleBinding objects  # noqa: E501
        """
        pass

    def test_list_user(self):
        """Test case for list_user

        List User objects  # noqa: E501
        """
        pass

    def test_list_user1(self):
        """Test case for list_user1

        List User objects  # noqa: E501
        """
        pass

    def test_password_change(self):
        """Test case for password_change

        Change user password  # noqa: E501
        """
        pass

    def test_password_change1(self):
        """Test case for password_change1

        Change user password  # noqa: E501
        """
        pass

    def test_password_reset(self):
        """Test case for password_reset

        Reset user password  # noqa: E501
        """
        pass

    def test_password_reset1(self):
        """Test case for password_reset1

        Reset user password  # noqa: E501
        """
        pass

    def test_token_secret_generate(self):
        """Test case for token_secret_generate

        Generate secret for token signing  # noqa: E501
        """
        pass

    def test_unlock(self):
        """Test case for unlock

        Unlock user  # noqa: E501
        """
        pass

    def test_unlock1(self):
        """Test case for unlock1

        Unlock user  # noqa: E501
        """
        pass

    def test_update_authentication_policy(self):
        """Test case for update_authentication_policy

        Update AuthenticationPolicy object  # noqa: E501
        """
        pass

    def test_update_role(self):
        """Test case for update_role

        Update Role object  # noqa: E501
        """
        pass

    def test_update_role1(self):
        """Test case for update_role1

        Update Role object  # noqa: E501
        """
        pass

    def test_update_role_binding(self):
        """Test case for update_role_binding

        Update RoleBinding object  # noqa: E501
        """
        pass

    def test_update_role_binding1(self):
        """Test case for update_role_binding1

        Update RoleBinding object  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update User object  # noqa: E501
        """
        pass

    def test_update_user1(self):
        """Test case for update_user1

        Update User object  # noqa: E501
        """
        pass

    def test_update_user_preference(self):
        """Test case for update_user_preference

        Update UserPreference object  # noqa: E501
        """
        pass

    def test_update_user_preference1(self):
        """Test case for update_user_preference1

        Update UserPreference object  # noqa: E501
        """
        pass

    def test_watch_authentication_policy(self):
        """Test case for watch_authentication_policy

        Watch AuthenticationPolicy objects. Supports WebSockets or HTTP long poll  # noqa: E501
        """
        pass

    def test_watch_role(self):
        """Test case for watch_role

        Watch Role objects. Supports WebSockets or HTTP long poll  # noqa: E501
        """
        pass

    def test_watch_role1(self):
        """Test case for watch_role1

        Watch Role objects. Supports WebSockets or HTTP long poll  # noqa: E501
        """
        pass

    def test_watch_role_binding(self):
        """Test case for watch_role_binding

        Watch RoleBinding objects. Supports WebSockets or HTTP long poll  # noqa: E501
        """
        pass

    def test_watch_role_binding1(self):
        """Test case for watch_role_binding1

        Watch RoleBinding objects. Supports WebSockets or HTTP long poll  # noqa: E501
        """
        pass

    def test_watch_user(self):
        """Test case for watch_user

        Watch User objects. Supports WebSockets or HTTP long poll  # noqa: E501
        """
        pass

    def test_watch_user1(self):
        """Test case for watch_user1

        Watch User objects. Supports WebSockets or HTTP long poll  # noqa: E501
        """
        pass

    def test_watch_user_preference(self):
        """Test case for watch_user_preference

        Watch UserPreference objects. Supports WebSockets or HTTP long poll  # noqa: E501
        """
        pass

    def test_watch_user_preference1(self):
        """Test case for watch_user_preference1

        Watch UserPreference objects. Supports WebSockets or HTTP long poll  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
