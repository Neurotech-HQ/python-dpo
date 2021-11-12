""""
Python Module for DirectPayOline

============================================================

Direct Pay Online is the payment aggregator which allows you receive payments from your customers.
From Multiple Payments Channel (Mpesa, TigoPesa, AirtelMoney) without having to deal with each of them.
"""


import os
import requests
from .utils import xml_to_dict
from .validators import CreateTokenModel
from .xml_templates import create_token_xml


class DPO(object):
    def __init__(
        self,
        company_token: str = None,
        account_type: str = None,
        redirect_url: str = None,
        back_url: str = None,
        sandbox: bool = False,
    ):
        self.__company_token = os.getenv("COMPANY_TOKEN", company_token)
        self.__account_type = os.getenv("ACCOUNT_TYPE", account_type)
        self.__redirect_url = os.getenv("REDIRECT_URL", redirect_url)
        self.__back_url = os.getenv("BACK_URL", back_url)
        self.__sandbox = sandbox

        # other configurations
        self.__base_url = "https://secure1.sandbox.directpay.online"
        self.__currency = os.getenv("CURRENCY", "TZS")
        self.__address = os.getenv("ADDRESS", "Tanzania")

        # initialization
        self.sandbox = self.__sandbox
        self.__header = {"Content-Type": "text/xml", "cache-control": "no-cache"}

    @property
    def company_token(self) -> str:
        return self.__company_token

    @company_token.setter
    def company_token(self, company_token: str) -> None:
        if not company_token:
            raise ValueError("Company Token is required")
        if not isinstance(company_token, str):
            raise TypeError("Company Token must be a string")
        self.__company_token = company_token

    @property
    def account_type(self) -> str:
        return self.__account_type

    @account_type.setter
    def account_type(self, account_type: str) -> None:
        if not account_type:
            raise ValueError("Account Type is required")
        if not isinstance(account_type, str):
            raise TypeError("Account Type must be a string")
        self.__account_type = account_type

    @property
    def redirect_url(self) -> str:
        return self.__redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url: str) -> None:
        if not redirect_url:
            raise ValueError("Redirect URL is required")
        if not isinstance(redirect_url, str):
            raise TypeError("Redirect URL must be a string")
        self.__redirect_url = redirect_url

    @property
    def back_url(self) -> str:
        return self.__back_url

    @back_url.setter
    def back_url(self, back_url: str) -> None:
        if not back_url:
            raise ValueError("Back URL is required")
        if not isinstance(back_url, str):
            raise TypeError("Back URL must be a string")
        self.__back_url = back_url

    @property
    def sandbox(self) -> bool:
        return self.__sandbox

    @sandbox.setter
    def sandbox(self, sandbox: bool) -> None:
        if sandbox is None:
            raise ValueError("Sandbox is required")
        if not isinstance(sandbox, bool):
            raise TypeError("Sandbox must be a boolean")

        if sandbox:
            self.__base_url = "https://secure1.sandbox.directpay.online"
        else:
            self.__base_url = "https://secure.3gdirectpay.com"
        self.__sandbox = sandbox

    def get_initial_config(self):
        return {
            "company_token": self.__company_token,
            "account_type": self.__account_type,
            "redirect_url": self.__redirect_url,
            "back_url": self.__back_url,
            "currency": self.__currency,
            "address": self.__address,
            "company_ref": os.getenv("COMPANY_REFERENCE"),
            "service_type": os.getenv("SERVICE_TYPE"),
        }

    def create_token(self, user_query: dict) -> dict:
        """
        Create Token

        :param query:
        :return:
        """
        if not user_query:
            raise ValueError("Query is required")
        if not isinstance(user_query, dict):
            raise TypeError("Query must be a dictionary")

        # get config query and append it to user_query
        config_query = self.get_initial_config()
        config_query.update(user_query)

        # validate query
        response = CreateTokenModel.validate(config_query)
        if not isinstance(response, CreateTokenModel):
            raise ValueError(f"Invalid Query {response}")

        # get query from modal
        query = response.dict()

        # create token
        xml = create_token_xml(query)
        result = requests.post(
            f"{self.__base_url}/API/v6/", data=xml, headers=self.__header
        )
        if result.status_code != 200:
            raise Exception(f"Error {result.status_code}")

        # print(xml)
        # convert xml to dict
        transtoken = dict(xml_to_dict(result.text)).get("API3G")["TransToken"]
        return transtoken

    def create_payment_url(self, transtoken: str) -> str:
        """
        Create Payment URL

        :param query:
        :return:
        """
        return f"{self.__base_url}/payv2.php?ID={transtoken}"
