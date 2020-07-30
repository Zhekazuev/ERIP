#!/usr/bin/env python
"""Method for removing an address in the ERIP Prefixes.
All Prefixes are Private.
Two types Prefixes: mobile and fttx
Prefixes include tags: "erip", region, type

Input data: mandatory(IP-address, Type, Region)
{"address": "10.68.0.1",
 "region": "minsk",
 "type": "mobile",
 "vrf": {"name": "INTERNET",
         "rd": 99}
}

Output data: {'status': 'good', 'message': 'Address 10.68.0.1 in VRF None deleted'})
"""


import logging
import netbox
import json
import sys
import re


def delete_address(address, in_vrf):
    """Delete ip address from Netbox"""
    vrf_rd = "25106:" + str(in_vrf.get("rd"))
    vrf = netbox.Read().VRFS().get_by_rd(vrf_rd)
    if vrf.get("count") is None:
        return {"status": "error", "message": f"Don't exist VRF with RD={vrf_rd}"}
    else:
        try:
            vrf_id = vrf.get("results")[0].get("id")
        except IndexError as index_error:
            return {"status": "error", "message": index_error}
    address_params = netbox.Read().Addresses().get_by_vrf_id_and_address(vrf_id, address)
    if vrf.get("count") is None:
        return {"status": "error", "message": f"Address {address} in VRF {vrf.get('name')} don't deleted"}
    else:
        try:
            address_id = address_params.get("results")[0].get("id")
        except IndexError as index_error:
            return {"status": "error", "message": index_error}
        netbox.Delete().Addresses().delete_by_id(address_id)
        return {"status": "good", "message": f"Address {address} in VRF {in_vrf.get('name')} deleted"}


def main():
    """Main logic with filters and checks"""
    # checking parameter passing
    try:
        input_string = sys.argv[1]
    except IndexError:
        return {"status": "error", "message": "Missing parameters"}
    # checking if the passed parameter is correct - need json string
    try:
        input_data = json.loads(input_string)
    except json.decoder.JSONDecodeError as json_error:
        return {"status": "error", "message": str(json_error)}

    # list with correct regions and types
    regions = ("brest", "gomel", "grodno", "minsk", "mogilev", "vitebsk")
    types = ("mobile", "fttx")

    # check ip-address
    check_address = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", str(input_data.get("address")))
    if not check_address:
        return {"status": "error", "message": "IP-Address required or the entered IP-Address is invalid"}

    # check region
    if input_data.get("region") not in regions:
        return {"status": "error",
                "message": f"Region required or the entered region is invalid. Enter one of the options: {regions}"}

    # check type
    if input_data.get("type") not in types:
        return {"status": "error",
                "message": f"Prefix type required or the entered type is invalid. Enter one of the options: {types}"}

    # checking vrf name type
    if not isinstance(input_data.get("vrf").get("name"), str):
        return {"status": "error", "message": "The entered VRF Name is not str type"}

    # checking rd type
    if not isinstance(input_data.get("vrf").get("rd"), int):
        return {"status": "error", "message": "The entered RD is not int type"}

    address = input_data.get("address")
    in_vrf = input_data.get("vrf")
    message = delete_address(address, in_vrf)

    return message


if __name__ == '__main__':
    print(main())
