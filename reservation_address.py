"""Method for reservation an address in the ERIP Prefixes.
All Prefixes are Private.
Two types Prefixes: mobile and fttx
Prefixes include tags: "erip", region, type

Input data: mandatory(Region, Type), additional(prefix - if client wants specific prefix)
{"region": "minsk",
"type": "mobile",
"prefix": ""}

Output data: free address - Netbox json-string)
"""


import netbox
import sys
import re


def get_free_ip():
    return {}


def get_free_ip_by_prefix(prefix):
    return {}


def main():
    try:
        input_data = sys.argv[1]
    except IndexError:
        return {"status": "error", "message": "Missing parameters"}

    regions = ("brest", "gomel", "grodno", "minsk", "mogilev", "vitebsk")
    types = ("mobile", "fttx")

    input_data = {"region": "minsk",
                  "type": "mobile",
                  "prefix": ""}

    # check region
    if input_data.get("region") not in regions:
        return {"status": "error", "message": "Region required or the entered region is invalid"}

    # check type
    if input_data.get("type") and input_data.get("type") not in types:
        return {"status": "error", "message": "Prefix type required or the entered type is invalid"}

    if input_data.get("prefix"):
        # check prefix
        check_prefix = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}", input_data.get("prefix"))
        if not check_prefix:
            return {"status": "error", "message": "The entered prefix is invalid"}
        free_ip = get_free_ip_by_prefix(input_data.get("prefix"))
    else:
        free_ip = get_free_ip()

    return {"status": "good", "message": free_ip}


if __name__ == '__main__':
    print(main())
