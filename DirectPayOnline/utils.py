import json
import xmltodict


def xml_to_dict(xml_string: str) -> dict:
    try:
        xml_string = xml_string.replace("utf-8", "iso-8859-1")
        xml_string = xml_string.replace("&", "")
        return xmltodict.parse(xml_string)
    except Exception as e:
        print(e)
        # print(xml_string)
        return {}