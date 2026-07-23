from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient


class GetOperationsQueryDict(TypedDict):
    """
      Структура данных для получения операции по id счета.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
        Структура данных для получения статистики операции по id счета.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
         Базовая структура данных для создания операции.
    """
    status: str
    amount: int
    cardId: str
    accountId: str


class MakeFreeOperationRequestDict(MakeOperationRequestDict):
    """
           Структура данных для создания операции комиссии.
    """
    ...


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
             Структура данных для создания операции пополнения.
    """
    ...


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
                Структура данных для создания операции кэшбэка.
    """
    ...


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
                 Структура данных для создания операции перевода.
    """
    ...


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
                   Структура данных для создания операции покупки.
    """
    category: str


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
                   Структура данных для создания операции оплаты по счету.
    """
    ...


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
                   Структура данных для создания операции снятия наличных денег.
    """
    ...


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

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции по operation_id.

        :param operation_id: id операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
           Выполняет GET-запрос на получение статистики по операциям для определенного счета.

           :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
           :return: Объект httpx.Response с данными об операции.
           """
        return self.get(f"/api/v1/operations/operations-summary.", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFreeOperationRequestDict) -> Response:
        """
          Выполняет POST-запрос для создания операции комиссии.

          :param request: Словарь с status, amount, cardId, accountId
          :return: Объект httpx.Response с результатом операции.
          """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
              Выполняет POST-запрос для создания операции пополнения.

              :param request: Словарь с status, amount, cardId, accountId
              :return: Объект httpx.Response с результатом операции.
              """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
              Выполняет POST-запрос для создания операции кэшбэка.

              :param request: Словарь с status, amount, cardId, accountId
              :return: Объект httpx.Response с результатом операции.
              """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
               Выполняет POST-запрос для создания операции перевода.

               :param request: Словарь с status, amount, cardId, accountId
               :return: Объект httpx.Response с результатом операции.
               """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
                 Выполняет POST-запрос для создания операции покупки.

                 :param request: Словарь с status, amount, cardId, accountId, category
                 :return: Объект httpx.Response с результатом операции.
                 """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
                       Выполняет POST-запрос для создания операции оплаты по счету.

                       :param request: Словарь с status, amount, cardId, accountId, category
                       :return: Объект httpx.Response с результатом операции.
                       """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
                           Выполняет POST-запрос для создания операции снятия наличных денег.

                           :param request: Словарь с status, amount, cardId, accountId, category
                           :return: Объект httpx.Response с результатом операции.
                           """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)
