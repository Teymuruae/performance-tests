
from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import GetOperationResponseSchema, GetReceiptResponseSchema, \
    GetOperationsQuerySchema, GetOperationsResponseSchema, GetOperationsSummaryQuerySchema, \
    GetOperationsSummaryResponseSchema, MakeFeeOperationRequestSchema, MakeFeeOperationResponseSchema, \
    MakeTopUpOperationRequestSchema, MakeTopUpOperationResponseSchema, MakeCashbackOperationRequestSchema, \
    MakeCashbackOperationResponseSchema, MakeTransferOperationRequestSchema, MakeTransferOperationResponseSchema, \
    MakePurchaseOperationRequestSchema, MakePurchaseOperationResponseSchema, MakeBillPaymentOperationRequestSchema, \
    MakeBillPaymentOperationResponseSchema, MakeCashWithdrawalOperationRequestSchema, \
    MakeCashWithdrawalOperationResponseSchema


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции по operation_id.

        :param operation_id: id операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции по operation_id.

        :param operation_id: id операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_receipt(self, operation_id: str) -> GetReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetReceiptResponseSchema.model_validate_json(response.text)

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations(self, query: GetOperationsQuerySchema) -> GetOperationsResponseSchema:
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
           Выполняет GET-запрос на получение статистики по операциям для определенного счета.

           :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
           :return: Объект httpx.Response с данными об операции.
           """
        return self.get(f"/api/v1/operations/operations-summary.", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary(self, query: GetOperationsSummaryQuerySchema) -> GetOperationsSummaryResponseSchema:
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
          Выполняет POST-запрос для создания операции комиссии.

          :param request: Словарь с status, amount, cardId, accountId
          :return: Объект httpx.Response с результатом операции.
          """
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_fee_operation(self, request: MakeFeeOperationRequestSchema) -> MakeFeeOperationResponseSchema:
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
              Выполняет POST-запрос для создания операции пополнения.

              :param request: Словарь с status, amount, cardId, accountId
              :return: Объект httpx.Response с результатом операции.
              """
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation(self, request: MakeTopUpOperationRequestSchema) -> MakeTopUpOperationResponseSchema:
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
              Выполняет POST-запрос для создания операции кэшбэка.

              :param request: Словарь с status, amount, cardId, accountId
              :return: Объект httpx.Response с результатом операции.
              """
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation(self, request: MakeCashbackOperationRequestSchema) -> MakeCashbackOperationResponseSchema:
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
               Выполняет POST-запрос для создания операции перевода.

               :param request: Словарь с status, amount, cardId, accountId
               :return: Объект httpx.Response с результатом операции.
               """
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation(self, request: MakeTransferOperationRequestSchema) -> MakeTransferOperationResponseSchema:
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
                 Выполняет POST-запрос для создания операции покупки.

                 :param request: Словарь с status, amount, cardId, accountId, category
                 :return: Объект httpx.Response с результатом операции.
                 """
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation(self, request: MakePurchaseOperationRequestSchema) -> MakePurchaseOperationResponseSchema:
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
                       Выполняет POST-запрос для создания операции оплаты по счету.

                       :param request: Словарь с status, amount, cardId, accountId, category
                       :return: Объект httpx.Response с результатом операции.
                       """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation(self,
                                    request: MakeBillPaymentOperationRequestSchema) -> MakeBillPaymentOperationResponseSchema:
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
                           Выполняет POST-запрос для создания операции снятия наличных денег.

                           :param request: Словарь с status, amount, cardId, accountId, category
                           :return: Объект httpx.Response с результатом операции.
                           """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation(self,
                                       request: MakeCashWithdrawalOperationRequestSchema) -> MakeCashWithdrawalOperationResponseSchema:
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
