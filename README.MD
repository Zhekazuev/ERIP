# ERIP

ERIP reserve and delete addresses.

  - Reservation an address in the ERIP Prefixes
  - Removing an address in the ERIP Prefixes

### Installation

Git clone from repo
```sh
git clone https://github.com/Zhekazuev/ERIP.git erip
```

Install the dependencies from requirements.txt. 
```sh
cd erip
cat requirements.txt
source install.sh
```

Start script
```sh
python reservation_address.py '{"region": "minsk", "type": "mobile", "vrf": {"name": "Name", "rd": 1}}'
python delete_address.py '{"address": "1.1.1.1", "region": "minsk", "type": "mobile", "vrf": {"name": "Name", "rd": 1}}'
```

Example:
```console
[root@server1 erip]# python reservation_address.py '{"region": "minsk", "type": "mobile", "vrf": {"name": "Name", "rd": 1}}'
{'status': 'good', 'message': {'address': {'id': 1, 'family': {'value': 4, 'label': 'IPv4'}, 'address': '1.1.1.1/14', 'vrf': {'id': 1, 'url': 'http://1.1.1.1/api/ipam/vrfs/1/', 'name': 'Name', 'rd': '1:1'}, 'tenant': None, 'status': {'value': 'active', 'label': 'Active', 'id': 1}, 'role': None, 'interface': None, 'nat_inside': None, 'nat_outside': None, 'dns_name': '', 'description': '', 'tags': ['staros', 'erip', 'minsk', 'mobile'], 'custom_fields': {}, 'created': '2020-07-31', 'last_updated': '2020-07-31T00:37:34.478617+03:00'}, 'prefix': {'id': 1, 'family': {'value': 4, 'label': 'IPv4'}, 'prefix': '1.1.1.1/14', 'site': {'id': 1, 'url': 'http://1.1.1.1/api/dcim/sites/1/', 'name': 'Name', 'slug': 'name'}, 'vrf': {'id': 1, 'url': 'http://1.1.1.1/api/ipam/vrfs/1/', 'name': 'Name', 'rd': '1:1'}, 'tenant': None, 'vlan': None, 'status': {'value': 'active', 'label': 'Active', 'id': 1}, 'role': None, 'is_pool': False, 'description': 'RG01 CONS-PRIV-NAT-RANGE-7', 'tags': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 'custom_fields': {'rrpp_domain_num': None}, 'created': '2020-06-22', 'last_updated': '2020-07-30T16:28:58.692138+03:00'}, 'vrf': {'id': 1, 'name': 'Name', 'rd': '1:1', 'tenant': None, 'enforce_unique': True, 'description': '', 'tags': [], 'display_name': 'Name (1:1)', 'custom_fields': {}, 'created': '2018-07-18', 'last_updated': '2018-07-18T21:45:15.862454+03:00', 'ipaddress_count': 535, 'prefix_count': 426}}}
```
```console
[root@server1 erip]# python delete_address.py '{"address": "1.1.1.1", "region": "minsk", "type": "mobile", "vrf": {"name": "Name", "rd": 1}}'
{'status': 'good', 'message': 'Address 1.1.1.1 in VRF Name deleted'}
```

License
----
Free Software