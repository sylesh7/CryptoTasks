# coding: utf-8

"""
    Coinbase Developer Platform APIs

    The Coinbase Developer Platform APIs - leading the world's transition onchain.

    The version of the OpenAPI document: 2.0.0
    Contact: cdp@coinbase.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cdp.openapi_client.models.common_swap_response_issues_balance import CommonSwapResponseIssuesBalance

class TestCommonSwapResponseIssuesBalance(unittest.TestCase):
    """CommonSwapResponseIssuesBalance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonSwapResponseIssuesBalance:
        """Test CommonSwapResponseIssuesBalance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonSwapResponseIssuesBalance`
        """
        model = CommonSwapResponseIssuesBalance()
        if include_optional:
            return CommonSwapResponseIssuesBalance(
                token = '0x62ECB020842930cc01FFCCfeEe150AC32DcAEc8a',
                current_balance = '10000000',
                required_balance = '1000000000000000000'
            )
        else:
            return CommonSwapResponseIssuesBalance(
                token = '0x62ECB020842930cc01FFCCfeEe150AC32DcAEc8a',
                current_balance = '10000000',
                required_balance = '1000000000000000000',
        )
        """

    def testCommonSwapResponseIssuesBalance(self):
        """Test CommonSwapResponseIssuesBalance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
