import pytest
from mongoengine import connect, disconnect
from models import User

def setup_module(module):
    connect('mongoenginetest', host='mongomock://localhost')


def teardown_module(module):
    disconnect()


@pytest.fixture
def user():
    return User.objects(email='foo@bar.org').modify(
            upsert=True,
            new=True,
            set__email='foo@bar.org',
            set__name='Foo',
            set__surname='Bar'
    )


def test_user_data(user):
    db_user = User.objects(email='foo@bar.org').first()
    assert user.name == db_user.name


