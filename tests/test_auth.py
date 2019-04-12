# -*- coding: utf-8 -*-

import grpc
from pb.authentication import authenticationService_pb2_grpc
from pb.common import replyInfo_pb2
from authService import auth
import unittest
import os

auth_host_staging = os.environ.get("AUTH_HOST_STAGING", "")
auth_host_production = os.environ.get("AUTH_HOST_PRODUCTION", "")
creds = grpc.ssl_channel_credentials()
staging_auth_channel = grpc.secure_channel(auth_host_staging, credentials=creds)
staging_auth_client = authenticationService_pb2_grpc.AuthenticationServiceStub(staging_auth_channel)
prod_auth_channel = grpc.secure_channel(auth_host_production, credentials=creds)
prod_auth_client = authenticationService_pb2_grpc.AuthenticationServiceStub(prod_auth_channel)
authenticator = auth.AdminAuthenticator(username=os.environ.get("AUTH_USERNAME", ""),
                                        password=os.environ.get("AUTH_PASSWORD", ""),
                                        company_id=os.environ.get("AUTH_COMPANY_ID", ""))


class AuthTestSuite(unittest.TestCase):
    """Basic authentication test cases."""

    @staticmethod
    def test_staging_authentication():
        assert authenticator is not None
        reply, success = authenticator.run(staging_auth_client)
        assert success is True
        assert reply.replyInfo.statusCode == replyInfo_pb2.OK
        call_result = authenticator.get_result()
        assert call_result is not None
        assert call_result.code() == grpc.StatusCode.OK
        ai = authenticator.create_access_info()
        assert ai is not None
        reply = staging_auth_client.isAuthenticated(ai)
        assert reply.statusMessage == "You were authenticated successfully"
        assert reply.statusCode == replyInfo_pb2.OK

    @staticmethod
    def test_prod_authentication_with_tls():
        authenticator.run(prod_auth_client)
        ai = authenticator.create_access_info()
        reply = prod_auth_client.isAuthenticated(ai)
        assert reply.statusMessage == "You were authenticated successfully"


if __name__ == '__main__':
    unittest.main()
