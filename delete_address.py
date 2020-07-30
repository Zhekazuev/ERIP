#!/usr/bin/env python
"""Method for removing an address in the ERIP Prefixes.
All Prefixes are Private.
Two types Prefixes: mobile and fttx
Prefixes include tags: "erip", region, type

Input data: mandatory(IP-address, Prefix, Region), additional(Type)
{"address": "172.1.1.21",
"prefix": "172.1.1.0/28",
"region": "minsk",
"type": ""}

Output data: vacated address (with comparison: {"old": "", "new": ""})
"""


import netbox
import json
import sys
import re


def main():
    input_data = {"address": "172.1.1.21",
                  "prefix": "172.1.1.0/28",
                  "region": "minsk",
                  "type": ""}
    try:
        input_string = sys.argv[1]
    except IndexError:
        return {"status": "error", "message": "Missing parameters"}
    try:
        input_data = json.loads(input_string)
    except json.decoder.JSONDecodeError as json_error:
        return {"status": "error", "message": str(json_error)}
    if not isinstance(input_data, dict):
        return {"status": "error", "message": "Parameters are not JSON-string. Please put JSON!"}

    regions = ("brest", "gomel", "grodno", "minsk", "mogilev", "vitebsk")
    types = ("mobile", "fttx")

    # check ip-address
    check_address = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", str(input_data.get("address")))
    if not check_address:
        return {"status": "error", "message": "IP-Address required or the entered IP-Address is invalid"}

    # check prefix
    check_prefix = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}", str(input_data.get("prefix")))
    if not check_prefix:
        return {"status": "error", "message": "The entered prefix is invalid"}

    # check region
    if input_data.get("region") not in regions:
        return {"status": "error", "message": "Region required or the entered region is invalid"}

    # check type
    if input_data.get("type") not in types:
        return {"status": "error", "message": "Prefix type required or the entered type is invalid"}

    message = ""
    return {"status": "good", "message": message}


if __name__ == '__main__':
    print(main())
