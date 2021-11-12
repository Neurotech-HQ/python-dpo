import json
import xmltodict


def xml_to_dict(xml_string: str) -> dict:
    try:
        return xmltodict.parse(xml_string)
    except Exception as e:
        print(e)
        return {}