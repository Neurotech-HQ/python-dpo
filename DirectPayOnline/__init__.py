""""
Python Module for DirectPayOline

============================================================

Direct Pay Online is the payment aggregator which allows you receive payments from your customers.
From Multiple Payments Channel (Mpesa, TigoPesa, AirtelMoney) without having to deal with each of them.
"""


import os
import requests
from .utils import xml_to_dict
from .validators import (
    CreateTokenModel,
    EmailtoTokenModel,
    CreateMvisaQrcodeModel,
    RefundTokenModel,
    UpdateTokenModel,
    VerifyTokenModel,
    VerifyXpayModel,
    CancelTokenModel,
    MobilePaymentsOptionsModel,
    ChargeTokenAuthModel,
    BankTransferOptionsModel,
    ChargeCreditCardModel,
)
from .xml_templates import (
    create_token_xml,
    create_email_to_token_xml,
    create_mvisa_qrcode_xml,
    create_refund_token_xml,
    create_update_token_xml,
    create_verify_token_xml,
    create_verify_xpay_xml,
    create_cancel_token_xml,
    create_mobile_payment_options_xml,
    create_charge_token_auth_xml,
    create_bank_transfer_options_xml,
    create_charge_credit_card_xml,
)


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

    def get_final_query(self, user_query: dict) -> dict:
        """
        Get Final Query

        :param query:
        :return:
        """
        # get config query and append it to user_query
        config_query = self.get_initial_config()
        config_query.update(user_query)
        return config_query

    def post(self, xml_data):
        response = requests.post(
            f"{self.__base_url}/API/v6/", data=xml_data, headers=self.__header
        )
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}, {response.text}")
        # convert xml response  to dict
        return dict(xml_to_dict(response.text))

    def create_token(self, user_query: dict) -> dict:
        """
        Create Token

        :param query:
        :return:
        """
        # get final query
        final_query = self.get_final_query(user_query)

        # validate query
        query = CreateTokenModel(**final_query).dict()

        # construct xml request body and send it to DPO API
        xml_data = create_token_xml(query)
        return self.post(xml_data)

    def create_payment_url(self, transtoken: str) -> str:
        """
        Create Payment URL

        :param query:
        :return:
        """
        return f"{self.__base_url}/payv2.php?ID={transtoken}"

    def email_to_token(self, query: dict) -> str:
        # get final query
        final_query = self.get_final_query(query)

        # validate query
        query = EmailtoTokenModel(**final_query).dict()

        # construct xml request body and send it to DPO API
        xml_data = create_email_to_token_xml(query)
        return self.post(xml_data)

    def create_mvisa_qrcode(self, user_query: dict) -> str:
        """
        Create Mvisa Qrcode

        :param query:
        :return:
        """

        # get final query
        final_query = self.get_final_query(user_query)

        # validate query
        query = CreateMvisaQrcodeModel(**final_query).dict()

        # construct xml request body and send it to DPO API
        xml_data = create_mvisa_qrcode_xml(query)
        response = self.post(xml_data)

    def refund_token(self, query: dict) -> str:
        # get final query
        final_query = self.get_final_query(query)

        # validate query
        query = RefundTokenModel(**final_query).dict()

        # construct xml request body and send it to DPO API
        xml_data = create_refund_token_xml(query)
        return self.post(xml_data)

    def update_token(self, query: dict) -> str:
        # get final query
        final_query = self.get_final_query(query)

        # validate query
        query = UpdateTokenModel(**final_query).dict()

        # construct xml request body and send it to DPO API
        xml_data = create_update_token_xml(query)
        return self.post(xml_data)

    def verify_token(self, user_query: dict):
        # get final query
        final_query = self.get_final_query(user_query)

        # validate query
        query = VerifyTokenModel(**final_query).dict()

        # construct xml request body and send it to DPO API
        xml_data = create_verify_token_xml(query)
        return self.post(xml_data)

    def verify_xpay(self, user_query: dict):
        # get final query
        final_query = self.get_final_query(user_query)

        # validate query
        query = VerifyXpayModel(**final_query).dict()

        # construct xml request body and send it to DPO API
        xml_data = create_verify_xpay_xml(query)
        return self.post(xml_data)

    def cancel_token(self, user_query: dict):
        # get final query
        final_query = self.get_final_query(user_query)

        # validate query
        query = CancelTokenModel(**final_query).dict()

        # construct xml request body and send it to DPO API
        xml_data = create_cancel_token_xml(query)
        return self.post(xml_data)

    # ====================================================
    # ============ TRANSCATION + PAYMENTS ================
    # ============      OPTIONS            ================
    # ====================================================

    def mobile_payment_options(self, user_query: dict):
        # get final query
        final_query = self.get_final_query(user_query)

        # validate the query
        query = MobilePaymentsOptionsModel(**final_query).dict()
        print(query)
        # construct xml and send request to DPO API
        xml_data = create_mobile_payment_options_xml(query)
        return self.post(xml_data)

    def charge_token_auth(self, user_query: dict):
        # get final query
        final_query = self.get_final_query(user_query)

        # validate the query
        query = ChargeTokenAuthModel(**final_query)

        # construct xml and send it to DPO API
        xml = create_charge_token_auth_xml(query)
        return self.post(xml)

    def bank_transfer_options(self, user_query: dict):
        # get final query
        final_query = self.get_final_query(user_query)

        # validate the query
        query = BankTransferOptionsModel(**final_query).dict()

        # construct xml and send it to DPO API
        xml = create_bank_transfer_options_xml(query)
        return self.post(xml)

    def charge_credit_card(self, user_query: dict):
        # get the final query
        final_query = self.get_final_query(user_query)

        # validate the query
        query = ChargeCreditCardModel(**final_query).dict()

        # construct xml and send it to DPO
        xml = create_charge_credit_card_xml(query)
        return self.post(xml)
