import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope='session')
def api_request_context(
        playwright: Playwright
        ) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
            base_url = 'https://example-heroku-flask-selenium.herokuapp.com/')
    yield request_context
    request_context.dispose()

def test_should_returns_pong_if_ping(api_request_context: APIRequestContext) -> None:
    responce = api_request_context.get('/ping')
    assert responce.text() == 'pong'
