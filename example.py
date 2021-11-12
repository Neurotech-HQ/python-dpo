from DirectPayOnline import DPO


gateway = DPO()
transtoken = gateway.create_token(
    {"amount": 100, "service_description": "Buying books"}
)
payment_url = gateway.create_payment_url(transtoken)
print(payment_url)
