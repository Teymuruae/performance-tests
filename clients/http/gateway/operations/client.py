from enum import Enum
from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


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

class OperationType(str, Enum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(str, Enum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
         Базовая структура данных для создания операции.
    """
    status: OperationStatus
    amount: int
    cardId: str
    accountId: str


class MakeOperationResponseDict(TypedDict):
    """
         Базовая структура для получения данных об операции.
    """
    operation: OperationDict


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
           Структура данных для создания операции комиссии.
    """
    ...


class MakeFeeOperationResponseDict(MakeOperationResponseDict):
    """
           Структура данных для получения данных об операции комиссии.
    """
    ...


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
             Структура данных для создания операции пополнения.
    """
    ...


class MakeTopUpOperationResponseDict(MakeOperationResponseDict):
    """
           Структура данных для получения данных об операции пополнения.
    """
    ...


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
                Структура данных для создания операции кэшбэка.
    """
    ...


class MakeCashbackOperationResponseDict(MakeOperationResponseDict):
    """
           Структура данных для получения данных об операции кэшбэка.
    """
    ...


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
                 Структура данных для создания операции перевода.
    """
    ...


class MakeTransferOperationResponseDict(MakeOperationResponseDict):
    """
           Структура данных для получения данных об операции перевода.
    """
    ...


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
                   Структура данных для создания операции покупки.
    """
    category: str


class MakePurchaseOperationResponseDict(MakeOperationResponseDict):
    """
           Структура данных для получения данных об операции покупки.
    """
    ...


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
                   Структура данных для создания операции оплаты по счету.
    """
    ...


class MakeBillPaymentOperationResponseDict(MakeOperationResponseDict):
    """
           Структура данных для получения данных об операции по счету.
    """
    ...


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
                   Структура данных для создания операции снятия наличных денег.
    """
    ...


class MakeCashWithdrawalOperationResponseDict(MakeOperationResponseDict):
    """
           Структура данных для получения данных об операции по снятию наличных денег.
    """
    ...


class GetOperationResponseDict(TypedDict):
    """
    Описание структуры ответа получения одной операции.
    """
    operation: OperationDict


class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка операций.
    """
    operations: list[OperationDict]


class ReceiptDict(TypedDict):
    """
    Описание структуры квитанции.
    """
    url: str
    document: str


class GetReceiptResponseDict(TypedDict):
    """
    Описание структуры ответа получения квитанции.
    """
    receipt: ReceiptDict


class SummaryDict(TypedDict):
    """
    Описание структуры статистики.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Описание структуры ответа получения статистики.
    """
    summary: SummaryDict


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

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции по operation_id.

        :param operation_id: id операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_receipt(self, operation_id: str) -> GetReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations", params=QueryParams(**query))

    def get_operations(self, query: GetOperationsQueryDict) -> GetOperationsResponseDict:
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
           Выполняет GET-запрос на получение статистики по операциям для определенного счета.

           :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
           :return: Объект httpx.Response с данными об операции.
           """
        return self.get(f"/api/v1/operations/operations-summary.", params=QueryParams(**query))

    def get_operations_summary(self, query: GetOperationsSummaryQueryDict) -> GetOperationsSummaryResponseDict:
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
          Выполняет POST-запрос для создания операции комиссии.

          :param request: Словарь с status, amount, cardId, accountId
          :return: Объект httpx.Response с результатом операции.
          """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_fee_operation(self, request: MakeFeeOperationRequestDict) -> MakeFeeOperationResponseDict:
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
              Выполняет POST-запрос для создания операции пополнения.

              :param request: Словарь с status, amount, cardId, accountId
              :return: Объект httpx.Response с результатом операции.
              """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_top_up_operation(self, request: MakeTopUpOperationRequestDict) -> MakeTopUpOperationResponseDict:
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
              Выполняет POST-запрос для создания операции кэшбэка.

              :param request: Словарь с status, amount, cardId, accountId
              :return: Объект httpx.Response с результатом операции.
              """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_cashback_operation(self, request: MakeCashbackOperationRequestDict) -> MakeCashbackOperationResponseDict:
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
               Выполняет POST-запрос для создания операции перевода.

               :param request: Словарь с status, amount, cardId, accountId
               :return: Объект httpx.Response с результатом операции.
               """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_transfer_operation(self, request: MakeTransferOperationRequestDict) -> MakeTransferOperationResponseDict:
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
                 Выполняет POST-запрос для создания операции покупки.

                 :param request: Словарь с status, amount, cardId, accountId, category
                 :return: Объект httpx.Response с результатом операции.
                 """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_purchase_operation(self, request: MakePurchaseOperationRequestDict) -> MakePurchaseOperationResponseDict:
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
                       Выполняет POST-запрос для создания операции оплаты по счету.

                       :param request: Словарь с status, amount, cardId, accountId, category
                       :return: Объект httpx.Response с результатом операции.
                       """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_bill_payment_operation(self,
                                    request: MakeBillPaymentOperationRequestDict) -> MakeBillPaymentOperationResponseDict:
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
                           Выполняет POST-запрос для создания операции снятия наличных денег.

                           :param request: Словарь с status, amount, cardId, accountId, category
                           :return: Объект httpx.Response с результатом операции.
                           """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def make_cash_withdrawal_operation(self,
                                       request: MakeCashWithdrawalOperationRequestDict) -> MakeCashWithdrawalOperationResponseDict:
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
