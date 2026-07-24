from pydantic import BaseModel, HttpUrl


class DocumentDict(BaseModel):
    """
    Описание структуры документа.
    """
    url: HttpUrl
    document: str


class GetTariffDocumentResponseDict(BaseModel):
    """
    Описание структуры ответа получения документа тарифа.
    """
    tariff: DocumentDict


class GetContractDocumentResponseDict(BaseModel):
    """
    Описание структуры ответа получения документа контракта.
    """
    contract: DocumentDict