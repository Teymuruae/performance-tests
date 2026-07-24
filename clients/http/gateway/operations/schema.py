from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class GetOperationsQuerySchema(BaseModel):
    """
      Структура данных для получения операции по id счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias='accountId')


class GetOperationsSummaryQuerySchema(BaseModel):
    """
        Структура данных для получения статистики операции по id счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias='accountId')


class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias='cardId')
    category: str
    created_at: str = Field(alias='createdAt')
    account_id: str = Field(alias='accountId')


class MakeOperationRequestSchema(BaseModel):
    """
         Базовая структура данных для создания операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default=OperationStatus.COMPLETED)
    amount: int = Field(default=1400)
    card_id: str = Field(alias='cardId')
    account_id: str = Field(alias='accountId')


class MakeOperationResponseSchema(BaseModel):
    """
         Базовая структура для получения данных об операции.
    """
    operation: OperationSchema


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
           Структура данных для создания операции комиссии.
    """
    ...


class MakeFeeOperationResponseSchema(MakeOperationResponseSchema):
    """
           Структура данных для получения данных об операции комиссии.
    """
    ...


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
             Структура данных для создания операции пополнения.
    """
    ...


class MakeTopUpOperationResponseSchema(MakeOperationResponseSchema):
    """
           Структура данных для получения данных об операции пополнения.
    """
    ...


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
                Структура данных для создания операции кэшбэка.
    """
    ...


class MakeCashbackOperationResponseSchema(MakeOperationResponseSchema):
    """
           Структура данных для получения данных об операции кэшбэка.
    """
    ...


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
                 Структура данных для создания операции перевода.
    """
    ...


class MakeTransferOperationResponseSchema(MakeOperationResponseSchema):
    """
           Структура данных для получения данных об операции перевода.
    """
    ...


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
                   Структура данных для создания операции покупки.
    """
    category: str = Field(default='taxi')


class MakePurchaseOperationResponseSchema(MakeOperationResponseSchema):
    """
           Структура данных для получения данных об операции покупки.
    """
    ...


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
                   Структура данных для создания операции оплаты по счету.
    """
    ...


class MakeBillPaymentOperationResponseSchema(MakeOperationResponseSchema):
    """
           Структура данных для получения данных об операции по счету.
    """
    ...


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
                   Структура данных для создания операции снятия наличных денег.
    """
    ...


class MakeCashWithdrawalOperationResponseSchema(MakeOperationResponseSchema):
    """
           Структура данных для получения данных об операции по снятию наличных денег.
    """
    ...


class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения одной операции.
    """
    operation: OperationSchema


class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка операций.
    """
    operations: list[OperationSchema]


class ReceiptSchema(BaseModel):
    """
    Описание структуры квитанции.
    """
    url: HttpUrl
    document: str


class GetReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа получения квитанции.
    """
    receipt: ReceiptSchema


class SummarySchema(BaseModel):
    """
    Описание структуры статистики.
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias='spentAmount')
    received_amount: float = Field(alias='receivedAmount')
    cashback_amount: float = Field(alias='cashbackAmount')


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа получения статистики.
    """
    summary: SummarySchema
