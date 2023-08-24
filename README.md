# Tecmie Python API Library

[![PyPI version](https://img.shields.io/pypi/v/tecmie.svg)](https://pypi.org/project/tecmie/)

The Tecmie Python library provides convenient access to the Tecmie REST API from any Python 3.7+
application. It includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Documentation

The API documentation can be found [here](https://docs.tecmie.com).

## Installation

```sh
pip install tecmie
```

## Usage

```python
from tecmie import Tecmie

client = Tecmie(
    # defaults to os.environ.get("TECMIE_API_KEY")
    api_key="my api key",
    # defaults to "production".
    environment="environment_1",
)

root = client.root.retrieve()
```

While you can provide an `api_key` keyword argument, we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
and adding `TECMIE_API_KEY="my api key"` to your `.env` file so that your API Key is not stored in source control.

## Async Usage

Simply import `AsyncTecmie` instead of `Tecmie` and use `await` with each API call:

```python
from tecmie import AsyncTecmie

client = AsyncTecmie(
    # defaults to os.environ.get("TECMIE_API_KEY")
    api_key="my api key",
    # defaults to "production".
    environment="environment_1",
)


async def main():
    root = await client.root.retrieve()
    print(root)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Using Types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict), while responses are [Pydantic](https://pydantic-docs.helpmanual.io/) models. This helps provide autocomplete and documentation within your editor.

If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `"basic"`.

## Pagination

List methods in the Tecmie API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
import tecmie

client = Tecmie()

all_members = []
# Automatically fetches more pages as needed.
for member in client.space.members.list(
    "REPLACE_ME",
):
    # Do something with member here
    all_members.append(member)
print(all_members)
```

Or, asynchronously:

```python
import asyncio
import tecmie

client = AsyncTecmie()


async def main() -> None:
    all_members = []
    # Iterate through items across all pages, issuing requests as needed.
    async for member in client.space.members.list(
        "REPLACE_ME",
    ):
        all_members.append(member)
    print(all_members)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from tecmie import Tecmie

client = Tecmie()

client.root.retrieve(
    params={},
)
```

## Handling errors

When the library is unable to connect to the API (e.g., due to network connection problems or a timeout), a subclass of `tecmie.APIConnectionError` is raised.

When the API returns a non-success status code (i.e., 4xx or 5xx
response), a subclass of `tecmie.APIStatusError` will be raised, containing `status_code` and `response` properties.

All errors inherit from `tecmie.APIError`.

```python
import tecmie
from tecmie import Tecmie

client = Tecmie()

try:
    client.root.retrieve()
except tecmie.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except tecmie.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except tecmie.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors will be automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 409 Conflict, 429 Rate Limit,
and >=500 Internal errors will all be retried by default.

You can use the `max_retries` option to configure or disable this:

```python
from tecmie import Tecmie

# Configure the default for all requests:
client = Tecmie(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).root.retrieve()
```

### Timeouts

Requests time out after 1 minute by default. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration):

```python
from tecmie import Tecmie

# Configure the default for all requests:
client = Tecmie(
    # default is 60s
    timeout=20.0,
)

# More granular control:
client = Tecmie(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5 * 1000).root.retrieve()
```

On timeout, an `APITimeoutError` is thrown.

Note that requests which time out will be [retried twice by default](#retries).

## Advanced: Configuring custom URLs, proxies, and transports

You can configure the following keyword arguments when instantiating the client:

```python
import httpx
from tecmie import Tecmie

client = Tecmie(
    # Use a custom base URL
    base_url="http://my.test.server.example.com:8083",
    proxies="http://my.test.proxy.example.com",
    transport=httpx.HTTPTransport(local_address="0.0.0.0"),
)
```

See the httpx documentation for information about the [`proxies`](https://www.python-httpx.org/advanced/#http-proxying) and [`transport`](https://www.python-httpx.org/advanced/#custom-transports) keyword arguments.

## Advanced: Managing HTTP resources

By default we will close the underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__) is called but you can also manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

## Versioning

This package generally attempts to follow [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/tecmie/tecmie-python/issues) with questions, bugs, or suggestions.

## Requirements

Python 3.7 or higher.
