"""
    Umweltbundesamt: Rigoletto API

    API Description  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.rigoletto.model.validation_error import ValidationError

from deutschland import rigoletto

globals()["ValidationError"] = ValidationError
from deutschland.rigoletto.model.http_validation_error import HTTPValidationError


class TestHTTPValidationError(unittest.TestCase):
    """HTTPValidationError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHTTPValidationError(self):
        """Test HTTPValidationError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HTTPValidationError()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
