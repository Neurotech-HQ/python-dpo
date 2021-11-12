import os
from datetime import datetime
from pydantic import BaseModel


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
    custom_address: str = None
    customer_email: str = None
    customer_phone: str = None
    customer_country: str = None
    customer_dial_code: str = None
    customer_zipcode: str = None
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

    @staticmethod
    def validate(body: dict):
        try:
            return CreateTokenModel(**body)
        except Exception as e:
            print(e)
            return str(e.__doc__)