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

import logging
import netbox
import json
import sys
import re


def get_free_ip(region, prefix_type):
    prefixes = netbox.Read().Prefixes().get_by_two_tags_v4(region, prefix_type)
    # prefix2 = netbox.Read().Prefixes().get_by_three_tags_v4("erip", region, prefix_type)
    # print(prefix2)
    if prefixes.get("count") is None:
        return {"status": "error", "message": f"Don't exist prefixes with parameters: {region}, {prefix_type}"}
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
                    "message": f"Don't exist free IPs in all prefixes with parameters: {region}, {prefix_type}"}


def get_free_ip_by_prefix(region, prefix_type, prefix):
    return {"status": "error", "message": ""}


def reserve_ip(ip):
    address = ip.get("message")
    vrf = netbox.Read().VRFS().get_by_id(address.get("vrf").get("id"))
    tenant_id = vrf.get("results").get("tenant").get("id")
    new_address = netbox.Create().Addresses().create(address=address.get("address"),
                                                     vrf=address.get("vrf").get("id"),
                                                     tenant=tenant_id,
                                                     status=1,
                                                     description="",
                                                     custom_fields="")
    return new_address


def main():
    input_data = {"region": "minsk",
                  "type": "mobile",
                  "prefix": ""}
    # try:
    #     input_string = sys.argv[1]
    #     input_data = json.loads(input_string)
    #     if not isinstance(input_data, dict):
    #         return {"status": "error", "message": "Parameters are not JSON-string. Please put JSON!"}
    # except IndexError:
    #     return {"status": "error", "message": "Missing parameters"}

    regions = ("brest", "gomel", "grodno", "minsk", "mogilev", "vitebsk")
    types = ("mobile", "fttx")
    region = input_data.get("region")
    prefix_type = input_data.get("type")
    # check region
    if input_data.get("region") not in regions:
        return {"status": "error", "message": "Region required or the entered region is invalid"}

    # check type
    if input_data.get("type") not in types:
        return {"status": "error", "message": "Prefix type required or the entered type is invalid"}

    if input_data.get("prefix"):
        # check prefix
        check_prefix = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}", str(input_data.get("prefix")))
        if not check_prefix:
            return {"status": "error", "message": "The entered prefix is invalid"}
        free_ip = get_free_ip_by_prefix(region, prefix_type, input_data.get("prefix"))
    else:
        free_ip = get_free_ip(region, prefix_type)

    if free_ip.get("status") is "error":
        return free_ip
    else:
        return reserve_ip(free_ip)


if __name__ == '__main__':
    print(main())
