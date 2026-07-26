from httpx import Request, Response, Client
from logging import getLogger

logger = getLogger(__name__)


def request_hook(request: Request):
    print("Request url: ", request.url, 'Request method: ', request.method)
    request.extensions["rugaga"] = 'rugagashechka'


def response_hook(response: Response):
    response.read() # если необходимо прочитать json в хуках ответа, то необходимо сначала вызвать read
    print("Response: ", response.json())
    print(response.request.extensions['rugaga'])


client = Client(base_url='http://localhost:8003',
                event_hooks={'request': [request_hook], 'response': [response_hook]})

response_1 = client.get('/api/v1/users/713c5934-6312-4a9b-96f1-c2fb623b2cd1')
