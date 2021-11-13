"""
Module for holding XML templates for DirectPayOline requests.
"""
# XML templates

# ================XML templates (header and footer)================
header_xml = """
    <?xml version="1.0" encoding="utf-8"?>
    <API3G>
    <CompanyToken>{company_token}</CompanyToken>
    <Request>{request_type}</Request>
"""

footer_xml = """
    <Services>
    <Service>
        <ServiceType>{service_type}</ServiceType>
        <ServiceDescription>{service_description}</ServiceDescription>
        <ServiceDate>{service_date}</ServiceDate>
    </Service>
    </Services>
    </API3G>
"""

# ================XML templates (create_token )================
create_token_xml_string = (
    header_xml
    + """
    <Transaction>
    <PaymentAmount>{amount}</PaymentAmount>
    <PaymentCurrency>{currency}</PaymentCurrency>
    <CompanyRef>{company_ref}</CompanyRef>
    <RedirectURL>{redirect_url}</RedirectURL>
    <BackURL>{back_url}</BackURL>
    <CompanyRefUnique>0</CompanyRefUnique>
    <PTL>5</PTL>
    <customerFirstName>{customer_first_name}</customerFirstName>
    <customerLastName>{customer_last_name}</customerLastName>
    <customerCity>{customer_city}</customerCity>
    <customerCountry>{customer_country}</customerCountry>
    <CardHolderName>{card_holder_name}</CardHolderName>
    <customerEmail>{customer_email}</customerEmail>
    <customerPhone>{customer_phone}</customerPhone>
    <DefaultPaymentCountry>{default_payment_country}</DefaultPaymentCountry>
    </Transaction>
    """
    + footer_xml
)

# ================XML templates (email_to_token )================
email_to_token_xml_string = (
    header_xml
    + """
    <TransactionToken>{transtoken}</TransactionToken>
    </API3G>
    """
)

# company_token: str
# request_type: str = "refundToken"
# transaction_token: str
# amount: float
# description: str = None

# ================XML templates (refund_token )================
refund_token_xml_string = (
    header_xml
    + """
    <TransactionToken>{transtoken}</TransactionToken>
    <refundAmount>{amount}</refundAmount>
    <refundDetails>{description}</refundDetails>
    </API3G>
    """
)

# ============== XML templates (update_token) ======================
update_token_xml_string = (
    header_xml
    + """ 
  <TransactionToken>{transtoken}</TransactionToken>
  <PaymentAmount>{amount}</PaymentAmount>
  <CompanyRef>{company_ref}</CompanyRef>
  <CustomerEmail>{customer_email}</CustomerEmail>
  <CustomerFirstName>{customer_first_name}</CustomerFirstName>
  <CustomerLastName>{customer_last_name}</CustomerLastName>
  <CustomerAddress>{customer_address}</CustomerAddress>
  <CustomerCity>{customer_city}</CustomerCity>
  <CustomerCountry>{customer_country}</CustomerCountry>
  <CustomerDialCode>{customer_dial_code}</CustomerDialCode>
  <CustomerPhone>{customer_phone}</CustomerPhone>
  <CustomerZip>{customer_zipcode}</CustomerZip>
  <CompanyAccRef>{company_accref}</CompanyAccRef>
  <UserToken>{user_token}</UserToken>
  </API3G>
    """
)

# ============ XML templates (verify_token) ======================
verify_token_xml_tring = header_xml + (
    """
    <TransactionToken>{transtoken}</TransactionToken>
    </API3G>
    """
)

# ============= XML template (verify_xpay) ======================
verify_xpay_xml_string = (
    header_xml
    + """
    <XpayId>{xpay_id}</XpayId>
    </API3G>
    """
)

# ============== XML template (charge_credit card )==============
credit_card_xml_string = (
    header_xml
    + """
    <TransactionToken>{transtoken}</TransactionToken>
    <CreditCardNumber>{card_number}</CreditCardNumber>
    <CreditCardExpiry>{card_expiry}</CreditCardExpiry>
    <CreditCardCVV>{card_cvv}</CreditCardCVV>
    <CardHolderName>{card_holder_name}</CardHolderName>
    </API3G>
    """
)


def remove_none_tags(xml_string: str) -> str:
    """
    Function for removing tags with None values.
    """
    xml_string_splitted = xml_string.split("\n")
    xml_string_cleaned = []
    for line in xml_string_splitted:
        if not line.strip() or ">None</" in line:
            continue
        xml_string_cleaned.append(line.strip())
    return "\n".join(xml_string_cleaned)


def create_email_to_token_xml(data: dict) -> str:
    """
    Function for creating XML for creating email to token requests
    """
    data = email_to_token_xml_string.format(**data)
    return remove_none_tags(data)


def create_token_xml(data: dict) -> str:
    """
    Function for creating XML for creating token request.
    """
    data = create_token_xml_string.format(**data)
    return remove_none_tags(data)


def create_mvisa_qrcode_xml(data: dict) -> str:
    """
    Function for creating XML for creating token request.
    """
    data = email_to_token_xml_string.format(**data)
    return remove_none_tags(data)


def create_refund_token_xml(data: dict) -> str:
    """
    Function for creating XML for creating refund token request.
    """
    data = refund_token_xml_string.format(**data)
    return remove_none_tags(data)


def create_update_token_xml(data: dict) -> str:
    """
    Function for creating XML for updating token request.
    """
    data = update_token_xml_string.format(**data)
    return remove_none_tags(data)


def create_verify_token_xml(data: dict) -> str:
    """
    Function for creating XML for verifying the token request.
    """
    data = verify_token_xml_tring.format(**data)
    return remove_none_tags(data)


def create_verify_xpay_xml(data: dict) -> str:
    """
    Function for creating XML for verifying the token request.
    """
    data = verify_xpay_xml_string.format(**data)
    return remove_none_tags(data)


def create_cancel_token_xml(data: dict) -> str:
    """
    Function for creating XML for cancelling token request.
    """
    data = verify_token_xml_tring.format(**data)
    return remove_none_tags(data)


def create_mobile_payment_options_xml(data: dict) -> str:
    """
    Function for creating XML mobile payment options
    """
    data = verify_token_xml_tring.format(**data)
    return remove_none_tags(data)


def create_charge_token_auth_xml(data: dict) -> str:
    """
    Function for creating XML for Charge token auth
    """
    data = verify_token_xml_tring.format(**data)
    return remove_none_tags(data)


def create_bank_transfer_options_xml(data: dict) -> str:
    """
    Function for creating XML for Bank transfers options
    """
    data = verify_token_xml_tring.format(**data)
    return remove_none_tags(data)


def create_charge_credit_card_xml(data: dict) -> str:
    """
    Function for creating XML to charge credit card
    """
    data = credit_card_xml_string.format(**data)
    return remove_none_tags(data)