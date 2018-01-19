#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import InstanceCommunication_pb2 as InstanceCommunication__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class InstanceControlStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFunctionStatus = channel.unary_unary(
        '/proto.InstanceControl/GetFunctionStatus',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=InstanceCommunication__pb2.FunctionStatus.FromString,
        )
    self.GetAndResetMetrics = channel.unary_unary(
        '/proto.InstanceControl/GetAndResetMetrics',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=InstanceCommunication__pb2.MetricsData.FromString,
        )


class InstanceControlServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetFunctionStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAndResetMetrics(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InstanceControlServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFunctionStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetFunctionStatus,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=InstanceCommunication__pb2.FunctionStatus.SerializeToString,
      ),
      'GetAndResetMetrics': grpc.unary_unary_rpc_method_handler(
          servicer.GetAndResetMetrics,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=InstanceCommunication__pb2.MetricsData.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.InstanceControl', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
