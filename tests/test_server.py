"""
test_server.py
====================================
Unit testing for server module
"""

import unittest
import pytest
import tempfile
from imath_requests.server import create_app


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app, api = create_app({'TESTING': True, 'DATABASE': db_path})

    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

    os.close(db_fd)
    os.unlink(db_path)


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'No entries here so far' in rv.data