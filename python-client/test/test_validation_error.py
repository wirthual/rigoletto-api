"""
    Umweltbundesamt: Rigoletto API

    API Description  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.rigoletto.model.location_inner import LocationInner

from deutschland import rigoletto

globals()["LocationInner"] = LocationInner
from deutschland.rigoletto.model.validation_error import ValidationError


class TestValidationError(unittest.TestCase):
    """ValidationError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testValidationError(self):
        """Test ValidationError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ValidationError()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
