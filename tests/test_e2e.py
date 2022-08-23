import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope='session')
def api_request_context(
        playwright: Playwright,
        base_url: str
        ) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
            base_url = base_url)
    yield request_context
    request_context.dispose()

def test_scraping(api_request_context: APIRequestContext) -> None:
    responce = api_request_context.get('/')
    assert '60 page' in responce.text()
