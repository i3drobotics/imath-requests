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
    app, api = create_app({'TESTING': True})

    with app.test_client() as client:
        with app.app_context():
            pass
        yield client


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_index(client):
    response = client.get('/')
    print(response)


# class TestPartDataEndpoint(unittest.TestCase):
#     """
#     Unit testing for part data endpoint in server module.

#     """
#     def part_data_post(self, data):
#         return client.post('/part_data', data=data, follow_redirects=True)

#     def part_data_get(self):
#         return client.get('/part_data', follow_redirects=True)

#     def test_part_data(self):
#         part_data = {
#             "timestamp": 1516193959559,
#             "part_id": "Part1234",
#             "source": "Camera_Control_PC_Garret",
#             "part_data": [
#                 {
#                     "key": "steel_grade",
#                     "value": "Grade01"
#                 },
#                 {
#                     "key": "heat_number",
#                     "value": "C1234566"
#                 },
#                 {
#                     "key": "rolling_schedule",
#                     "value": "Schedule1"
#                 },
#                 {
#                     "key": "analysis",
#                     "value": [
#                         {
#                             "key": "C",
#                             "value": "0.2"
#                         },
#                         {
#                             "key": "Mn",
#                             "value": "0.02"
#                         }
#                     ]
#                 }
#             ]
#         }
#         rv = self.part_data_post(part_data)
#         # TODO assert post was succesfull
#         # assert b'test' in rv.data

#         rv = self.part_data_get()
#         # TODO assert get was succesfull
#         # assert b'test' in rv.data