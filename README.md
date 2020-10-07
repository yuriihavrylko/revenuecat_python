# revenuecat_python

A Python client library for RevenueCat REST API. Supports async/await.

## Installation

Install this library directly into an activated virtual environment:

```text
$ pip install git+https://github.com/YuraHavrylko/revenuecat_python.git
```

## Usage

### Sync usage
Every project should utilize logging, but for simple use cases, this requires a bit too much boilerplate. Instead of including all of this in your modules:

```python
from revenuecat_python.client import RevenueCatClient

client = RevenueCatClient(api_key='...', secret_key='...')
response = client.get_or_create_subscriber('...')
print(response.json_body)
```

### Async usage

AsyncRevenueCatClient client and RevenueCatClient shares exactly the same interface, method signatures.

```python
from revenuecat_python.client import AsyncRevenueCatClient

async def main():
    client = AsyncRevenueCatClient(api_key='...', secret_key='...')
    response = await client.get_or_create_subscriber('...')
    print(response.json_body)
```

### Handling Response

Responses from RevenueCat REST API are parsed as JSON and returned to you as an instance of RevenueCatResponse, 
which is just a simple class consisting of following attributes:

* json_body: JSON parsed body of the response, as a Python dictionary.
* http_status: HTTP status code of the response.
* headers: Original httpx.Response object, in case you want to access more attributes.
Sample code:

```python
from revenuecat_python.client import RevenueCatClient
from revenuecat_python.responses import RevenueCatError

client = RevenueCatClient(...)

try:
    response = client.get_or_create_subscriber(...)
    print(response.json_body) # JSON parsed response
    print(response.http_status) # Status code of response
    print(response.headers) # Response http headers
except RevenueCatError as e: # An exception is raised if response.status_code != 201 or 200
    print(e) # Error message from REST server
    print(e.json_body) # You can see the details of error by parsing original response
```

## Full documentation 

[https://docs.revenuecat.com/reference#basic](https://docs.revenuecat.com/reference#basic)

## TODO

* Add tests, integrate travis-ci
* Deploy to PyPi
* Create docs and push to readthedocs

## License

This project is under the MIT license.