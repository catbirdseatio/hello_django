import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture(scope="function")
def test_user(db):
    yield User.objects.create_user(email="rod@example.com", password="testPass123")


@pytest.fixture(scope="function")
def test_adminuser(db):
    yield User.objects.create_superuser(
        email="clark@dailyplanet.com", password="TestPass123"
    )
