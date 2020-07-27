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


def get_free_ip():
    return {}


def get_free_ip_by_prefix(prefix):
    return {}


def main():
    try:
        input_data = sys.argv[1]
    except IndexError:
        return {"status": "error", "message": "Missing parameters"}

    input_data = {"region": "minsk",
                  "type": "mobile",
                  "prefix": ""}
    if input_data.get("region") is None:
        return {"status": "error", "message": "Region required"}
    if input_data.get("type") is None:
        return {"status": "error", "message": "Prefix type required"}

    if input_data.get("prefix"):
        free_ip = get_free_ip_by_prefix(input_data.get("prefix"))
    else:
        free_ip = get_free_ip()
    return {"status": "good", "message": free_ip}


if __name__ == '__main__':
    print(main())
