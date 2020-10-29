import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--online",
        action="store_true",
        default=False,
        help="run unit tests against online web content",
    )


@pytest.fixture(scope="session", autouse=True)
def configure_online(request):
    seen = {None}
    session = request.node
    online = request.config.getoption("--online")
    for item in session.items:
        cls = item.getparent(pytest.Class)
        if cls not in seen:
            if hasattr(cls.obj, "online"):
                cls.obj.online = online
            seen.add(cls)
