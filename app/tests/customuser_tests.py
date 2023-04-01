import pytest
from django.contrib.auth import get_user_model


User = get_user_model()

@pytest.mark.django_db
class TestUsersManager:
    def test_create_user(self):
        user = User.objects.create_user(email="rod@example.com", password="testPass123")
        assert user.email =="rod@example.com"
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser
        
        try:
            assert user.usrname is None
        except AttributeError:
            pass
        with pytest.raises(TypeError):
            User.objects.create_user()
        with pytest.raises(TypeError):
            User.objects.create_user(email="")
        with pytest.raises(ValueError):
            User.objects.create_user(email="", password="Foo")
    
    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(email="clark@dailyplanet.com", password="TestPass123")
        assert admin_user.email == "clark@dailyplanet.com"
        assert admin_user.is_active
        assert admin_user.is_staff
        assert admin_user.is_superuser
        
        try:
            assert admin_user.username is None
        except AttributeError:
            pass
        with pytest.raises(ValueError):
            User.objects.create_superuser(email="super@user.com",password="Foo",
                is_superuser=False)