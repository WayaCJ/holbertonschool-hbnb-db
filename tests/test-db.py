# tests/test_db.py

import pytest
from app import app, db 

@pytest.fixture(scope='module')
def setup_app():
 

def test_app_creation(setup_app):
    assert app is not None

def test_db_creation(setup_app):
    assert db is not None

