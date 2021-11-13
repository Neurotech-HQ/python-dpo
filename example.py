from dotenv import load_dotenv
from DirectPayOnline import DPO

# Load environment variables
load_dotenv()

gateway = DPO()
user_query = {
    "amount": 50000,
    "service_description": "A Tour  to Mbudya",
    "customer_name": "Jordan Kalebu",
    "customer_email": "isaackeinstein@gmail.com",
}
response = gateway.create_token(user_query).get("API3G")
transtoken = response.get("TransToken")


# ========== create a payment url ====================
payment_url = gateway.create_payment_url(transtoken)
print(payment_url)

# ========== email to token   ====================
user_query.update({"transtoken": transtoken})
response = gateway.email_to_token(user_query)
print(response)

# ========== createmvisaQRCODE ====================
response = gateway.create_mvisa_qrcode(user_query)
print(response)

# ========== refund_token ====================
refund_query = {
    "amount": 34500,
    "description": "Buying books",
    "transtoken": transtoken,
}
response = gateway.refund_token(refund_query)
print(response)

# ============ update token ===================
user_query.update({"customer_name": "Mikael Jordan"})
response = gateway.update_token(user_query)
print(response)


# ==============verify transaction token ============
query = {"transtoken": transtoken}
response = gateway.verify_token(query)
print(response)


# ============== verify XPay ========================
query = {"xpay_id": "124334323324"}
response = gateway.verify_xpay(query)
print(response)
print("Damn")
