import grpc
from clients.grpc.gateway.users.client import UsersGatewayGRPCClient


class SimpleLoggingInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request):
        # Печатаем имя вызываемого метода
        print(f"[gRPC Interceptor] Calling method: {client_call_details.method}")
        print(f"Request: ", request)
        # Выполняем реальный RPC вызов
        response = continuation(client_call_details, request)

        # return response


interceptors = [SimpleLoggingInterceptor()]
channel = grpc.insecure_channel('localhost:9003')
intercept_channel = grpc.intercept_channel(channel, *interceptors)


client = UsersGatewayGRPCClient(channel = intercept_channel)

response = client.get_user(user_id='5d67c4df-2143-46d7-b320-2323569b0979')
print("Response::: ", response)