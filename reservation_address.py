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


import requests
import netbox


def get_free_ip():
    return {}


def get_free_ip_by_prefix(prefix):
    return {}


def main():
    input_data = {"region": "minsk", "type": "mobile", "prefix": ""}
    if input_data.get("prefix"):
        free_ip = get_free_ip_by_prefix(input_data.get("prefix"))
    free_ip = get_free_ip()
    return free_ip


if __name__ == '__main__':
    address = main()
