#!/usr/bin/env python
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
    """Input data: Region, Type)
    Two types Prefixes: mobile and fttx
        {"region": "minsk",
        "type": "mobile",
        "prefix": ""}
    """
    prefixes = netbox.Read().Prefixes().get_by_three_tags_v4("erip", region, prefix_type)
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


def get_free_ip_by_prefix(region, prefix_type, inprefix):
    """Input data: mandatory(Region, Type, prefix - if client wants specific prefix)
    Two types Prefixes: mobile and fttx
        {"region": "minsk",
        "type": "mobile",
        "prefix": "46.216.144.0/21"}
    """
    prefixes = netbox.Read().Prefixes().get_by_two_tags_v4(region, prefix_type)
    # prefixes = netbox.Read().Prefixes().get_by_three_tags_v4("erip", region, prefix_type)
    if prefixes.get("count") is None:
        return {"status": "error", "message": f"Don't exist prefixes with parameters: {region}, {prefix_type}"}
    else:
        for prefix in prefixes.get("results"):
            if prefix.get("prefix") == inprefix:
                prefix_id = prefix.get("id")
                addresses = netbox.Read().Addresses().get_free_ips_by_prefix_id(prefix_id)
                if addresses:
                    return {"status": "good", "message": addresses[0]}
                else:
                    return {"status": "error",
                            "message": f"Don't exist free IPs in all prefixes with parameters: {region}, {prefix_type}"}


def reserve_ip(ip, region, prefix_type):
    """Reservation IP in netbox by input parameters"""
    address = ip.get("message")
    vrf = netbox.Read().VRFS().get_by_id(address.get("vrf").get("id"))
    tenant = vrf.get("tenant")
    if tenant:
        tenant_id = vrf.get("tenant").get("id")
    else:
        tenant_id = None
    new_address = netbox.Create().Addresses().create(address=address.get("address"),
                                                     vrf_id=address.get("vrf").get("id"),
                                                     tenant_id=tenant_id,
                                                     description="",
                                                     tags=["erip", region, prefix_type,
                                                           "staros"],
                                                     custom_fields={})
    return new_address


def main():
    """Main logic with filters and checks"""
    try:
        input_string = sys.argv[1]
    except IndexError:
        return {"status": "error", "message": "Missing parameters"}
    try:
        input_data = json.loads(input_string)
    except json.decoder.JSONDecodeError as json_error:
        return {"status": "error", "message": str(json_error)}

    regions = ("brest", "gomel", "grodno", "minsk", "mogilev", "vitebsk")
    types = ("mobile", "fttx")

    # check region
    if input_data.get("region") not in regions:
        return {"status": "error", "message": "Region required or the entered region is invalid"}

    # check type
    if input_data.get("type") not in types:
        return {"status": "error", "message": "Prefix type required or the entered type is invalid"}

    region = input_data.get("region")
    prefix_type = input_data.get("type")

    if input_data.get("prefix"):
        # check prefix
        check_prefix = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}$", str(input_data.get("prefix")))
        if not check_prefix:
            return {"status": "error", "message": "The entered prefix is invalid"}
        message = get_free_ip_by_prefix(region, prefix_type, input_data.get("prefix"))
    else:
        message = get_free_ip(region, prefix_type)

    if message.get("status") is "error":
        return message
    else:
        return reserve_ip(message, region, prefix_type)


if __name__ == '__main__':
    print(main())
