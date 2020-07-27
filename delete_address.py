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
import sys


def main():
    try:
        input_data = sys.argv[1]
    except IndexError:
        return {"status": "error", "message": "Missing parameters"}

    input_data = {"address": "172.1.1.21",
                  "prefix": "172.1.1.0/28",
                  "region": "minsk",
                  "type": ""}
    if input_data.get("address") is None:
        return {"status": "error", "message": "IP-Address required"}
    if input_data.get("region") is None:
        return {"status": "error", "message": "Region required"}
    if input_data.get("type") is None:
        return {"status": "error", "message": "Prefix type required"}

    message = ""
    return {"status": "good", "message": message}


if __name__ == '__main__':
    output_data = main()
    print(output_data)
