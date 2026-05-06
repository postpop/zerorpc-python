import pytest

from . import testutils


@pytest.fixture(autouse=True)
def cleanup_ipc_endpoints():
    yield
    testutils.teardown()
