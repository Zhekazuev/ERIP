#!/usr/bin/env python
"""
Method for reservation an address in the ERIP Prefixes.
All Prefixes are Private.
Two types Prefixes: mobile and fttx
Prefixes include tags: "erip", region, type

Input data: mandatory(Region, Type, vrf name, vrf rd, vrf rt)
Two types Prefixes: mobile and fttx
        {"region": "minsk",
         "type": "mobile",
         "vrf": {"name": "Gn",
                 "rd": 1}
         }

Output data: address, prefix, vrf and gateway(opt) - JSON-string)
"""
from log import logger
import netbox
import json
import sys


def get_free_ip(region, prefix_type, in_vrf):
    vrf_rd = "25106:" + str(in_vrf.get("rd"))
    vrf = netbox.Read().VRFS().get_by_rd(vrf_rd)
    if vrf.get("count") is None:
        return {"status": "error", "message": f"No VRF with such RD {vrf_rd}"}
    else:
        try:
            vrf_id = vrf.get("results")[0].get("id")
        except IndexError as index_error:
            return {"status": "error", "message": index_error}
    prefixes = netbox.Read().Prefixes().get_by_vrf_id_and_three_tag_v4(vrf_id, "erip", region, prefix_type)
    if prefixes.get("count") is None:
        return {"status": "error",
                "message": f"There are not Prefixes in VRF {in_vrf.get('name')} with such parameters: "
                           f"erip, {region}, {prefix_type}"}
    else:
        for prefix in prefixes.get("results"):
            prefix_id = prefix.get("id")
            addresses = netbox.Read().Addresses().get_free_ips_by_prefix_id(prefix_id)
            if addresses:
                return {"status": "good",
                        "message": {"address": addresses[0], "prefix": prefix, "vrf": vrf.get("results")[0]}}
            else:
                continue
        else:
            return {"status": "error",
                    "message": f"There are not Addresses in VRF {in_vrf.get('name')} with such parameters: "
                               f"erip, {region}, {prefix_type}"}


def get_free_ip_global_vrf(region, prefix_type):
    prefixes = netbox.Read().Prefixes().get_by_three_tags_v4("erip", region, prefix_type)
    if prefixes.get("count") is None:
        return {"status": "error",
                "message": f"There are not Prefixes in GRT with such parameters: "
                           f"erip, {region}, {prefix_type}"}
    else:
        for prefix in prefixes.get("results"):
            prefix_id = prefix.get("id")
            addresses = netbox.Read().Addresses().get_free_ips_by_prefix_id(prefix_id)
            if addresses:
                return {"status": "good",
                        "message": {"address": addresses[0], "prefix": prefix}}
            else:
                continue
        else:
            return {"status": "error",
                    "message": f"There are not Addresses in GRT with such parameters: "
                               f"erip, {region}, {prefix_type}"}


def get_gateway(prefix):
    addresses = netbox.Read().Addresses().get_by_prefix(prefix.get("prefix"))
    if addresses.get("count") is None:
        return None
    else:
        for address in addresses.get('results'):
            if "gateway" in address.get("tags"):
                return address
            else:
                continue
        else:
            return None


def reserve_ip(ip, region, prefix_type):
    """Reservation IP in netbox by input parameters"""
    address = ip.get("message").get("address")
    vrf = ip.get("message").get("address").get("vrf")
    tenant = ip.get("message").get("prefix").get("tenant")

    # getting tennant id
    if tenant:
        tenant_id = vrf.get("tenant").get("id")
    else:
        tenant_id = None

    # the decision to add a tag - staros
    if prefix_type is "mobile":
        tags = ["erip", region, prefix_type, "staros"]
    else:
        tags = ["erip", region, prefix_type]

    # creating new address
    new_address = netbox.Create().Addresses().create(address=address.get("address"),
                                                     vrf_id=address.get("vrf").get("id"),
                                                     tenant_id=tenant_id,
                                                     description="",
                                                     tags=tags,
                                                     custom_fields={})

    # add new ip information in ip(json string with information with address, prefix, vrf)
    ip.get("message").update({'address': new_address})

    # add gateway
    if prefix_type is "fttx":
        prefix = ip.get("message").get("prefix")
        gateway = get_gateway(prefix)
        ip.get("message").update({'gateway': gateway})

    return ip


def reserve_ip_global_vrf(ip, region, prefix_type):
    """Reservation IP in netbox by input parameters"""
    address = ip.get("message").get("address")
    vrf = ip.get("message").get("address").get("vrf")
    tenant = ip.get("message").get("prefix").get("tenant")

    # getting tennant id
    if tenant:
        tenant_id = vrf.get("tenant").get("id")
    else:
        tenant_id = None

    # the decision to add a tag - staros
    if prefix_type is "mobile":
        tags = ["erip", region, prefix_type, "staros"]
    else:
        tags = ["erip", region, prefix_type]

    # creating new address
    new_address = netbox.Create().Addresses().create(address=address.get("address"),
                                                     vrf_id=vrf,
                                                     tenant_id=tenant_id,
                                                     description="",
                                                     tags=tags,
                                                     custom_fields={})

    # add new ip information in ip(json string with information with address, prefix, vrf)
    ip.get("message").update({'address': new_address})

    # add gateway
    if prefix_type is "fttx":
        prefix = ip.get("message").get("prefix")
        gateway = get_gateway(prefix)
        ip.get("message").update({'gateway': gateway})

    return ip


@logger.catch()
def main():
    """
    Main logic
    Get input JSON-string
    Lots of checks
    Return output data with address, prefix, vrf and gateway(opt)
    """
    # checking parameter passing
    try:
        input_string = sys.argv[1]
    except IndexError:
        return {"status": "error", "message": "Parameters required"}
    # checking if the passed parameter is correct - need json string
    try:
        input_data = json.loads(input_string)
    except json.decoder.JSONDecodeError as json_error:
        return {"status": "error", "message": str(json_error)}

    # list with correct regions and types
    regions = ("brest", "gomel", "grodno", "minsk", "mogilev", "vitebsk")
    types = ("mobile", "fttx")

    # checking region
    if input_data.get("region") not in regions:
        return {"status": "error",
                "message": f"You are required to enter a region or the entered region is incorrect. "
                           f"Enter one of the suggested regions: {regions}"}

    # checking type
    if input_data.get("type") not in types:
        return {"status": "error",
                "message": f"You are required to enter a type or the entered type is incorrect. "
                           f"Enter one of the suggested types: {types}"}

    region = input_data.get("region")
    prefix_type = input_data.get("type")

    if input_data.get("vrf") is None:
        message = get_free_ip_global_vrf(region, prefix_type)
        if message.get("status") is "error":
            return message
        else:
            return reserve_ip_global_vrf(message, region, prefix_type)
    else:
        # checking vrf name type
        if not isinstance(input_data.get("vrf").get("name"), str):
            return {"status": "error", "message": "The entered VRF Name is not str type"}
        # checking rd type
        if not isinstance(input_data.get("vrf").get("rd"), int):
            return {"status": "error", "message": "The entered RD is not int type"}

        in_vrf = input_data.get("vrf")
        message = get_free_ip(region, prefix_type, in_vrf)
        if message.get("status") is "error":
            return message
        else:
            return reserve_ip(message, region, prefix_type)


if __name__ == '__main__':
    print(main())
