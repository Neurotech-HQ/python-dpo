"""
Module for holding XML templates for DirectPayOline requests.
"""


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


email_to_token_xml_string = (
    header_xml
    + """
    <TransactionToken>{transtoken}</TransactionToken>
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
        xml_string_cleaned.append(line)
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