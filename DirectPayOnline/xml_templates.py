"""
Module for holding XML templates for DirectPayOline requests.
"""


header_xml = """<?xml version="1.0" encoding="utf-8"?>
<API3G>
<CompanyToken>{company_token}</CompanyToken>
<Request>{request_type}</Request>
"""

footer_xml = """<Services>
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
    + """<Transaction>
<PaymentAmount>{amount}</PaymentAmount>
<PaymentCurrency>{currency}</PaymentCurrency>
<CompanyRef>{company_ref}</CompanyRef>
<RedirectURL>{redirect_url}</RedirectURL>
<BackURL>{back_url}</BackURL>
<CompanyRefUnique>0</CompanyRefUnique>
<PTL>5</PTL>
</Transaction>
"""
    + footer_xml
)


def create_token_xml(data: dict) -> str:
    """
    Function for creating XML for creating token request.
    """
    return create_token_xml_string.format(**data)