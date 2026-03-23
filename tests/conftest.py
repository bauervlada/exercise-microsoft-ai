from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

_INITIAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activities before and after each test."""
    # Arrange
    activities.clear()
    activities.update(deepcopy(_INITIAL_ACTIVITIES))

    yield

    activities.clear()
    activities.update(deepcopy(_INITIAL_ACTIVITIES))


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)
