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
import json
import sys
import re


def get_free_ip(region, prefix_type):
    prefixes = netbox.Read().Prefixes().get_by_two_tags_v4(region, prefix_type)
    # prefix2 = netbox.Read().Prefixes().get_by_three_tags_v4("erip", region, prefix_type)
    # print(prefix2)
    if prefixes.get("count") is None:
        return {"status": "error", "message": f"Don't exist prefixes with this parameters: {region}, {prefix_type}"}
    else:
        for prefix in prefixes.get("results"):
            prefix_id = prefix.get("id")
            addresses = netbox.Read().Addresses().get_free_ips_by_prefix_id(prefix_id)
            if addresses:
                return {"status": "good", "message": addresses[0]}
            else:
                continue
        else:
            return {"status": "error",
                    "message": f"Don't exist free IPs in prefixes with this parameters: {region}, {prefix_type}"}


def get_free_ip_by_prefix(prefix):
    return {}


def reserve_ip_by_id(id):
    return {}


def main():
    try:
        input_string = sys.argv[1]
        input_data = json.loads(input_string)
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
        region = input_data.get("region")
        prefix_type = input_data.get("type")
        free_ip = get_free_ip(region, prefix_type)

    #reserve_ip_by_id(free_ip.get("results").get("id"))
    return free_ip


if __name__ == '__main__':
    print(main())
