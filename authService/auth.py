from pb.authentication import authenticationService_pb2
from pb.common import accessInfo_pb2
from pb.common import replyInfo_pb2

import grpc
from grpc._channel import _Rendezvous

_DEFAULT_TIMEOUT = 2  # timeouts are in seconds


class AdminAuthenticator:
    clientId = ""
    code = ""
    companyId = ""
    authReply = None
    result = None

    def __init__(self, username, password, company_id):
        """
        :type username: string
        :type password: string
        :type company_id: string
        """
        self.username = username
        self.password = password
        self.companyId = company_id

    def get_result(self):
        return self.result

    def run(self, stub):
        req = authenticationService_pb2.AuthenticationRequest()
        req.usernamePasswordCredentials.username = self.username
        req.usernamePasswordCredentials.password = self.password
        req.usernamePasswordCredentials.companyId = self.companyId
        try:
            authReply, result = stub.authenticate.with_call(req, _DEFAULT_TIMEOUT)
            self.authReply = authReply
            self.result = result
        except _Rendezvous as e:
            self.result = e
        return self.authReply, (self.result.code() == grpc.StatusCode.OK)

    def auth_succeeded(self):
        if self.authReply is None:
            return False
        elif self.authReply.replyInfo.statusCode is not replyInfo_pb2.OK:
            return False
        return True

    def create_access_info(self):
        if not self.auth_succeeded():
            return None
        ai = accessInfo_pb2.AccessInfo()
        ai.accessToken = self.authReply.accessToken
        return ai
