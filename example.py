from __future__ import print_function

import time

import grpc
from pb.authentication import authenticationService_pb2_grpc
from pb.user import userService_pb2_grpc
from pb.roomService import roomService_pb2_grpc
from pb.common import replyInfo_pb2
from authService import auth
import os


def run():
    auth_host = os.environ.get("AUTH_HOST", "")
    user_host = os.environ.get("USER_HOST", "")
    room_host = os.environ.get("ROOM_HOST", "")
    # establish a connection to the authentication service and log in
    creds = grpc.ssl_channel_credentials()    
    auth_channel = grpc.secure_channel(auth_host, credentials=creds)
    user_channel = grpc.secure_channel(user_host, credentials=creds)
    room_channel = grpc.secure_channel(room_host, credentials=creds)

    auth_client = authenticationService_pb2_grpc.AuthenticationServiceStub(auth_channel)
    user_client = userService_pb2_grpc.UserServiceStub(user_channel)
    room_client = roomService_pb2_grpc.roomServiceStub(room_channel)
    authenticator = auth.AdminAuthenticator(username=os.environ.get("AUTH_USERNAME", ""),
                                            password=os.environ.get("AUTH_PASSWORD", ""),
                                            company_id=os.environ.get("AUTH_COMPANY_ID", ""))
    reply, success = authenticator.run(auth_client)
    if success:  # authentication succeeded
        ai = authenticator.create_access_info()
        ai.requestId = "python-bl-example-{:f}".format(time.time())
        room_list_request = roomService_pb2_grpc.RoomListRequest()
        room_list_request.accessInfo.CopyFrom(ai)
        room_list = room_client.List(room_list_request)
        if room_list.replyInfo.statusCode is replyInfo_pb2.OK:
            for room_id in room_list.rooms:
                print("Room", room_id, room_list.rooms[room_id].displayName)
        print(room_list)
    else:
        # authentication failed, inspect results
        call_results = authenticator.get_result()  # type is _Rendezvouz
        print("Authentication failed with code: {} (details: {})".format(call_results.code(), call_results.details()))


if __name__ == '__main__':
    run()
