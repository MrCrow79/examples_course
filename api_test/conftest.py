import pytest


@pytest.fixture
def get_url():
    return "https://api.segment.io/v1/p"


@pytest.fixture(scope='session')
def get_token():

    return 'Bearer m1vmwQTUOaiNE8Ib9k-X97HpMXEq0i5lTJ4qtfBa8HQ'


@pytest.fixture
def get_entiers_url():
    return "https://cdn.contentful.com/spaces/vrc8wif0t20g/environments/master/entries"


@pytest.fixture
def get_body():
    return '{"timestamp":"2024-03-17T09:05:15.330Z","integrations":{},"anonymousId":"ac10a870-94ef-4793-80e7-e897f4c71b29","type":"page","properties":{"path":"/","referrer":"https://www.saucedemo.com/","search":"","title":"Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing","url":"https://saucelabs.com/","name":"Home"},"name":"Home","context":{"page":{"path":"/","referrer":"https://www.saucedemo.com/","search":"","title":"Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing","url":"https://saucelabs.com/"},"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36","userAgentData":{"brands":[{"brand":"Chromium","version":"122"},{"brand":"Not(A:Brand","version":"24"},{"brand":"Google Chrome","version":"122"}],"mobile":false,"platform":"Windows"},"locale":"en-US","library":{"name":"analytics.js","version":"next-1.64.0"},"timezone":"Europe/Warsaw"},"messageId":"ajs-next-353cd5c9208da004440407a571017c87","writeKey":"kEVbG4wU60CZtVVxPniyNdza7l9oAn7H","userId":null,"sentAt":"2024-03-17T09:05:15.454Z","_metadata":{"bundled":["Segment.io"],"unbundled":[],"bundledIds":[]}}'
