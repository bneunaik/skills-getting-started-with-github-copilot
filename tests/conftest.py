import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Keep tests isolated by restoring in-memory activities after each test."""
    baseline = copy.deepcopy(activities)

    yield

    activities.clear()
    activities.update(copy.deepcopy(baseline))
