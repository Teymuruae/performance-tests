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
        return self.get(f"/api/v1/operations/operations-summary.",
                        params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary(self, query: GetOperationsSummaryQuerySchema) -> GetOperationsSummaryResponseSchema:
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation_api(self, card_id: str, account_id: str) -> Response:
        """
          Выполняет POST-запрос для создания операции комиссии.

          :params card_id, account_id
          :return: Объект httpx.Response с результатом операции.
          """
        request = MakeFeeOperationRequestSchema(card_id=card_id, account_id=account_id)
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        response = self.make_fee_operation_api(card_id, account_id)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation_api(self, card_id: str, account_id: str) -> Response:
        """
              Выполняет POST-запрос для создания операции пополнения.

              :params card_id, account_id
              :return: Объект httpx.Response с результатом операции.
              """
        request = MakeTopUpOperationRequestSchema(card_id=card_id, account_id=account_id)
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        response = self.make_top_up_operation_api(card_id, account_id)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation_api(self, card_id: str, account_id: str) -> Response:
        """
              Выполняет POST-запрос для создания операции кэшбэка.

              :params card_id, account_id
              :return: Объект httpx.Response с результатом операции.
              """
        request = MakeCashbackOperationRequestSchema(card_id=card_id, account_id=account_id)
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        response = self.make_cashback_operation_api(card_id, account_id)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation_api(self, card_id: str, account_id: str) -> Response:
        """
               Выполняет POST-запрос для создания операции перевода.

               :params card_id, account_id
               :return: Объект httpx.Response с результатом операции.
               """
        request = MakeTransferOperationRequestSchema(card_id=card_id, account_id=account_id)
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        response = self.make_transfer_operation_api(card_id, account_id)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation_api(self, card_id: str, account_id: str) -> Response:
        """
                 Выполняет POST-запрос для создания операции покупки.

                 :params card_id, account_id
                 :return: Объект httpx.Response с результатом операции.
                 """
        request = MakePurchaseOperationRequestSchema(card_id=card_id, account_id=account_id)
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        response = self.make_purchase_operation_api(card_id, account_id)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation_api(self, card_id: str, account_id: str) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :params card_id, account_id
        :return: Объект httpx.Response с результатом операции.
        """
        request = MakeBillPaymentOperationRequestSchema(card_id=card_id, account_id=account_id)
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        response = self.make_bill_payment_operation_api(card_id, account_id)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation_api(self, card_id: str, account_id: str) -> Response:
        """
                           Выполняет POST-запрос для создания операции снятия наличных денег.

                           :params card_id, account_id
                           :return: Объект httpx.Response с результатом операции.
                           """
        request = MakeCashWithdrawalOperationRequestSchema(card_id=card_id, account_id=account_id)
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation(self, card_id: str,
                                       account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        response = self.make_cash_withdrawal_operation_api(card_id, account_id)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
