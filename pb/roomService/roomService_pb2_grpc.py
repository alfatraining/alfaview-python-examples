# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pb.roomService import roomService_pb2 as roomService_dot_roomService__pb2


class roomServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/roomService.roomService/Create',
                request_serializer=roomService_dot_roomService__pb2.RoomCreateRequest.SerializeToString,
                response_deserializer=roomService_dot_roomService__pb2.RoomCreateReply.FromString,
                )
        self.Update = channel.unary_unary(
                '/roomService.roomService/Update',
                request_serializer=roomService_dot_roomService__pb2.RoomUpdateRequest.SerializeToString,
                response_deserializer=roomService_dot_roomService__pb2.RoomUpdateReply.FromString,
                )
        self.List = channel.unary_unary(
                '/roomService.roomService/List',
                request_serializer=roomService_dot_roomService__pb2.RoomListRequest.SerializeToString,
                response_deserializer=roomService_dot_roomService__pb2.RoomListReply.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/roomService.roomService/Destroy',
                request_serializer=roomService_dot_roomService__pb2.RoomDestroyRequest.SerializeToString,
                response_deserializer=roomService_dot_roomService__pb2.RoomDestroyReply.FromString,
                )
        self.Status = channel.unary_unary(
                '/roomService.roomService/Status',
                request_serializer=roomService_dot_roomService__pb2.RoomStatusRequest.SerializeToString,
                response_deserializer=roomService_dot_roomService__pb2.RoomStatusReply.FromString,
                )
        self.Permissions = channel.unary_unary(
                '/roomService.roomService/Permissions',
                request_serializer=roomService_dot_roomService__pb2.RoomPermissionsRequest.SerializeToString,
                response_deserializer=roomService_dot_roomService__pb2.RoomPermissionsReply.FromString,
                )
        self.CreateJoinLink = channel.unary_unary(
                '/roomService.roomService/CreateJoinLink',
                request_serializer=roomService_dot_roomService__pb2.CreateJoinLinkRequest.SerializeToString,
                response_deserializer=roomService_dot_roomService__pb2.CreateJoinLinkReply.FromString,
                )
        self.Sort = channel.unary_unary(
                '/roomService.roomService/Sort',
                request_serializer=roomService_dot_roomService__pb2.RoomSortRequest.SerializeToString,
                response_deserializer=roomService_dot_roomService__pb2.RoomSortReply.FromString,
                )


class roomServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Create(self, request, context):
        """/ creates or replaces all values
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """/ adds or overwrites all values
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """/ list all rooms which are accessible by the current user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """/ deletes room and kicks all users
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Status(self, request, context):
        """/ return mutable room information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Permissions(self, request, context):
        """/ returns user permissions for a room
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateJoinLink(self, request, context):
        """/ creates a link to launch the client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sort(self, request, context):
        """/ changes the sorting of rooms
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_roomServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=roomService_dot_roomService__pb2.RoomCreateRequest.FromString,
                    response_serializer=roomService_dot_roomService__pb2.RoomCreateReply.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=roomService_dot_roomService__pb2.RoomUpdateRequest.FromString,
                    response_serializer=roomService_dot_roomService__pb2.RoomUpdateReply.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=roomService_dot_roomService__pb2.RoomListRequest.FromString,
                    response_serializer=roomService_dot_roomService__pb2.RoomListReply.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=roomService_dot_roomService__pb2.RoomDestroyRequest.FromString,
                    response_serializer=roomService_dot_roomService__pb2.RoomDestroyReply.SerializeToString,
            ),
            'Status': grpc.unary_unary_rpc_method_handler(
                    servicer.Status,
                    request_deserializer=roomService_dot_roomService__pb2.RoomStatusRequest.FromString,
                    response_serializer=roomService_dot_roomService__pb2.RoomStatusReply.SerializeToString,
            ),
            'Permissions': grpc.unary_unary_rpc_method_handler(
                    servicer.Permissions,
                    request_deserializer=roomService_dot_roomService__pb2.RoomPermissionsRequest.FromString,
                    response_serializer=roomService_dot_roomService__pb2.RoomPermissionsReply.SerializeToString,
            ),
            'CreateJoinLink': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateJoinLink,
                    request_deserializer=roomService_dot_roomService__pb2.CreateJoinLinkRequest.FromString,
                    response_serializer=roomService_dot_roomService__pb2.CreateJoinLinkReply.SerializeToString,
            ),
            'Sort': grpc.unary_unary_rpc_method_handler(
                    servicer.Sort,
                    request_deserializer=roomService_dot_roomService__pb2.RoomSortRequest.FromString,
                    response_serializer=roomService_dot_roomService__pb2.RoomSortReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'roomService.roomService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class roomService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/roomService.roomService/Create',
            roomService_dot_roomService__pb2.RoomCreateRequest.SerializeToString,
            roomService_dot_roomService__pb2.RoomCreateReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/roomService.roomService/Update',
            roomService_dot_roomService__pb2.RoomUpdateRequest.SerializeToString,
            roomService_dot_roomService__pb2.RoomUpdateReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/roomService.roomService/List',
            roomService_dot_roomService__pb2.RoomListRequest.SerializeToString,
            roomService_dot_roomService__pb2.RoomListReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/roomService.roomService/Destroy',
            roomService_dot_roomService__pb2.RoomDestroyRequest.SerializeToString,
            roomService_dot_roomService__pb2.RoomDestroyReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/roomService.roomService/Status',
            roomService_dot_roomService__pb2.RoomStatusRequest.SerializeToString,
            roomService_dot_roomService__pb2.RoomStatusReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Permissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/roomService.roomService/Permissions',
            roomService_dot_roomService__pb2.RoomPermissionsRequest.SerializeToString,
            roomService_dot_roomService__pb2.RoomPermissionsReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateJoinLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/roomService.roomService/CreateJoinLink',
            roomService_dot_roomService__pb2.CreateJoinLinkRequest.SerializeToString,
            roomService_dot_roomService__pb2.CreateJoinLinkReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/roomService.roomService/Sort',
            roomService_dot_roomService__pb2.RoomSortRequest.SerializeToString,
            roomService_dot_roomService__pb2.RoomSortReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
