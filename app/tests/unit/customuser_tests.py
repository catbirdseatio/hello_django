import pytest
from django.contrib.auth import get_user_model


User = get_user_model()


class TestUsersManager:
    def test_create_user(self, test_user):
        assert test_user.email == "rod@example.com"
        assert test_user.is_active
        assert not test_user.is_staff
        assert not test_user.is_superuser

        try:
            assert test_user.usrname is None
        except AttributeError:
            pass

    def test_create_user_empty(self):
        with pytest.raises(TypeError):
            User.objects.create_user()

    def test_create_user_empty_password(self):
        with pytest.raises(TypeError):
            User.objects.create_user(email="")

    def test_create_user_empty_email(self):
        with pytest.raises(ValueError):
            User.objects.create_user(email="", password="Foo")

    def test_create_superuser(self, test_adminuser):
        assert test_adminuser.email == "clark@dailyplanet.com"
        assert test_adminuser.is_active
        assert test_adminuser.is_staff
        assert test_adminuser.is_superuser

        try:
            assert test_adminuser.username is None
        except AttributeError:
            pass

    def test_create_superuser_must_be_superuser(self):
        with pytest.raises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="Foo", is_superuser=False
            )
