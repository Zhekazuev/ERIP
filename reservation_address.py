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

if __name__ == '__main__':
    pass
