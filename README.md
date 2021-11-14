<samp>

# [python-dpo](https://github.com/Kalebu/python-dpo)

A python package to easy the integration with Direct Online Pay (DPO)  which easily allow you easily integrate  with payment options once without having to deal with each of them individually;

- [Mpesa](https://vodacom.co.tz/mpesa)
- [TigoPesa](https://www.tigo.co.tz/tigo-pesa)
- [AirtelMoney]()
- Card Payments
  - MasterCard
  - Visa
  - American Express
  - Orange Money
  - MTN MOMO

## Getting started

To gets started with [python-dpo](https://github.com/Kalebu/python-dpo) you need to install the package first, here how;

```bash
pip install DirectPayOnline --upgrade
```

## Configuring .env 

You can configure some variables directly on **.env** file and  so they will be loaded by the dotenv package.

Here some of importants of things you to configure;

```bash
COMPANY_TOKEN=9F416C11-127B-4DE2-AC7F-D5710E4C5E0A
CURRENCY=TZS
ADDRESS=Tanzania
SERVICE_TYPE=3854
COMPANY_REFERENCE=34TESTREFF
```

## How does it work ?

1. Create payment token
2. Verify token
3. Redirect to DPO payment page
4. Fetch response
5. Done

## Example of usage

```python
>>> from dotenv import load_dotenv
>>> load_dotenv() # loading environment variables 
>>> from DirectPayOnline import DPO
>>> dpo = DPO(sandbox=False)
>>> response = dpo.create_token(
    {
      'amount': 400, 
      "service_description": "Sarufi.io subscription"
    }
  )
>>> transtoken = token.get('API3G')['TransToken']
>>> dpo.create_payment_url(transtoken)
'https://secure.3gdirectpay.com/payv2.php?ID=1D0CC035-40E5-44A3-B5EF-034A34AD33E9'
```

When a user visit a payment_url, he/she will have an option to pay through preffered payment option, where if its a mastercard or visa or mobile money (Mpesa, TigoPesa, AirtelMoney).

## Issues ?

If you encounter any issue with the usage of the package, please raise one so as we can fix it as soon as possible.

## Contributions

**Python-DPO** is an opensource project under [MIT Public LICENSE](https://github.com/Kalebu/python-dpo/blob/main/LICENSE), contributions of any kind are welcomes from;

- fixing Typos
- improving documentation
- writing detailed example usecases
- fixing bugs and adding new features
- sharing with your developer friends and community

## Give it a star

Was this useful to you ? Then give it a star so that more people can make use of this.

## Credits

An inspiration for this came from [dpo-php](https://github.com/Zepson-Technologies/dpo-php) Thanks to amazing work made by [Novath Thomas](https://github.com/pro-cms) and [Alpa Olomi](https://github.com/alphaolomi).

All the credits to:

- [kalebu](https://github.com/kalebu)
- [Novath Thomas](https://github.com/pro-cms)
- and all the contributors

</samp>
