"""
test_server.py
====================================
Unit testing for server module
"""

import unittest
from imath_requests.server import create_app


class TestPartDataEndpoint(unittest.TestCase):
    """
    Unit testing for part data endpoint of app in Server module.

    """
    def setUp(self):
        self.endpoint = '/imath-rest-backend/part'
        app, _ = create_app({'TESTING': True})
        self.client = app.test_client()

    def test_part_data_get(self):
        self.client.get(self.endpoint, follow_redirects=True)

    def test_part_data_post(self):
        json_data = {
            "partId": "Part_I3DR_test_003",
            "source": "I3DR_test",
            "identifiedTime": 1647606457463.4841,
            "partData": [
                {
                    "key": "supplier",
                    "string": "I3DR"
                }
            ],
            "images": [
                {
                    "imageFileName": "I3DR_test_003.tif",
                    "capturedBy": "I3DR_test_camera",
                    "capturedTime": 1647606457463.4841,
                    "positionX": 0,
                    "positionY": 0,
                    "positionZ": 0,
                    "dimensionX": 5000,
                    "dimensionY": 1,
                    "dimensionZ": 0,
                    "defects": [
                        {
                            "defectType": {
                                "code": "315"
                            },
                            "identifiedBy": "I3DR_test_user",
                            "identifiedTime": 1647606457463.4841,
                            "positionX": 0, "positionY": 0,
                            "positionZ": 0, "dimensionX": 0,
                            "dimensionY": 0, "dimensionZ": 0
                        }
                    ]
                }
            ]}
        self.client.post(self.endpoint, data=json_data, follow_redirects=True)
