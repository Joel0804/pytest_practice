import pytest
from user import User_Manager

@pytest.fixture
def user_manager():
    return User_Manager()

def test_add_user(user_manager):
    assert user_manager.add_user("joel","joel@example.com") == True
    assert user_manager.get_user("joel") == "joel@example.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("joel", "joel@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("joel", "joel@example.com")