from datetime import datetime
from pydantic import BaseModel
from pydantic.utils import truncate


class CreateTokenModel(BaseModel):
    request_type: str = "createToken"
    company_token: str

    # Transaction Details
    amount: float
    currency: str
    company_ref: str = None
    redirect_url: str = None
    back_url: str = None
    company_ref_unique: bool = None
    limit_time: int = None
    limit_type: str = None
    transcation_charge_type: int = None
    transaction_auto_charge_day: datetime = None
    customer_first_name: str = None
    customer_last_name: str = None
    customer_address: str = None
    customer_email: str = None
    customer_phone: str = None
    customer_country: str = None
    customer_dial_code: str = None
    customer_zipcode: str = None
    customer_city: str = None
    card_holder_name: str = None
    demand_payment_by_traveler: bool = None
    email_transaction: bool = None
    company_accref: str = None
    user_token: str = None
    default_payment: str = None
    default_payment_country: str = None
    default_payment_mno: str = None
    transaction_to_prep: str = None
    allow_recurrent: bool = None
    fraud_time_limit: float = None
    voidable: bool = None
    charge_type: str = None
    trans_marketplace: int = None
    tans_block_countries: bool = None
    meta_data: str = None
    sms_transaction: bool = None
    transaction_type: str = None
    device_id: str = None
    device_country: str = None
    transaction_source: str = None

    # Services parameters for payment
    service_description: str
    service_type: str
    service_type_name: str = None
    service_date: datetime = datetime.now().strftime("%Y/%m/%d %H:%M")
    service_from: str = None
    service_to: str = None
    service_ref: str = None

    # Allocation level (Optional)
    allocation_code: str = None
    allocation_amount: float = None
    allocation_service_type: str = None
    allocation_service_description: str = None
    allocation_invoice: str = None
    allocation_pnr: str = None
    allocation_level: str = None

    ## Additional levels (Optional)

    block_payment: str = None

    ## Travellers level

    traveller_first_name: str = None
    traveller_last_name: str = None
    traveller_phone: str = None
    traveller_phone_prefix: int = None


class UpdateTokenModel(CreateTokenModel):
    request_type = "updateToken"
    transtoken: str
    user_token: str = None


class EmailtoTokenModel(BaseModel):
    request_type: str = "emailToToken"
    company_token: str
    transtoken: str


class CreateMvisaQrcodeModel(BaseModel):
    request_type: str = "createMvisaQRcode"
    company_token: str
    transtoken: str


class RefundTokenModel(BaseModel):
    company_token: str
    request_type: str = "refundToken"
    transtoken: str
    amount: float
    description: str = None


class VerifyTokenModel(BaseModel):
    company_token: str
    request_type: str = "verifyToken"
    transtoken: str


class VerifyXpayModel(BaseModel):
    company_token: str
    request_type: str = "verifyXpay"
    xpay_id: str


class CancelTokenModel(BaseModel):
    request_type: str = "cancelToken"
    company_token: str
    transtoken: str


class MobilePaymentsOptionsModel(BaseModel):
    request_type: str = "GetMobilePaymentOptions"
    company_token: str
    transtoken: str


class ChargeTokenAuthModel(BaseModel):
    request_type: str = "chargeTokenAuth"
    company_token: str
    transtoken: str


class BankTransferOptionsModel(BaseModel):
    request_type: str = "GetBankTransferOptions"
    company_token: str
    transtoken: str


class ChargeCreditCardModel(BaseModel):
    request_type: str = "chargeTokenCreditCard"
    company_token: str
    transtoken: str
    card_number: int
    card_expiry: str
    card_cvv: str
    card_holder_name: str
    charge_type: str = None
    three_d: str = None
