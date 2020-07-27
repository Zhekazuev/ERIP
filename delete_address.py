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


import requests
import netbox

if __name__ == '__main__':
    pass
