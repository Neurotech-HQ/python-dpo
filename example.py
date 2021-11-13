from dotenv import load_dotenv
from DirectPayOnline import DPO

# Load environment variables
load_dotenv()

gateway = DPO()
user_query = {
    "amount": 34500,
    "service_description": "Buying books",
    "customer_name": "Jordan Kalebu",
    "customer_email": "isaackeinstein@gmail.com",
}
transtoken = gateway.create_token(user_query)


# ========== create a payment url ====================
payment_url = gateway.create_payment_url(transtoken)
print(payment_url)

# ========== email to token   ====================
user_query.update({"transtoken": transtoken})
response = gateway.email_to_token(user_query)
print(response)