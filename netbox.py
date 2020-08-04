"""
RESTBOX
RESTful API realisation for Netbox
Methods need to work with Netbox
"""
import requests
import json
from config import Netbox


class Initiation:
    def __init__(self):
        """
        Init parameters for connect to Netbox
        """
        self.api_token = Netbox.TOKEN_MAIN
        self.nb_url = Netbox.URL_MAIN
        self.headers = {'Authorization': f'Token {self.api_token}', 'Content-Type': 'application/json',
                        'Accept': 'application/json'}


class Read:
    class TenantGroups(Initiation):
        def get_all(self):
            tenant_group_url = f"{self.nb_url}/api/tenancy/tenant-groups/"
            tenant_groups_list = requests.get(tenant_group_url, headers=self.headers)
            tenant_groups_list = json.loads(tenant_groups_list.text)
            return tenant_groups_list

        def get_by_id(self, id):
            tenant_group_url = f"{self.nb_url}/api/tenancy/tenant-groups/{id}/"
            tenant_group = requests.get(tenant_group_url, headers=self.headers)
            tenant_group = json.loads(tenant_group.text)
            return tenant_group

        def get_by_name(self, name):
            tenant_group_url = f"{self.nb_url}/api/tenancy/tenant-groups/?name={name}&limit=0"
            tenant_groups_list = requests.get(tenant_group_url, headers=self.headers)
            tenant_groups_list = json.loads(tenant_groups_list.text)
            return tenant_groups_list

        def get_by_slug(self, slug):
            tenant_group_url = f"{self.nb_url}/api/tenancy/tenant-groups/?slug={slug}&limit=0"
            tenant_groups_list = requests.get(tenant_group_url, headers=self.headers)
            tenant_groups_list = json.loads(tenant_groups_list.text)
            return tenant_groups_list

    class Tenants(Initiation):
        def get_all(self):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/?limit=0"
            tenants_list = requests.get(tenants_url, headers=self.headers)
            tenants_list = json.loads(tenants_list.text)
            return tenants_list

        def get_by_id(self, id):
            tenant_url = f"{self.nb_url}/api/tenancy/tenants/{id}/"
            tenant = requests.get(tenant_url, headers=self.headers)
            tenant = json.loads(tenant.text)
            return tenant

        def get_by_name(self, name):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/?name={name}&limit=0"
            tenants_list = requests.get(tenants_url, headers=self.headers)
            tenants_list = json.loads(tenants_list.text)
            return tenants_list

        def get_by_slug(self, slug):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/?slug={slug}&limit=0"
            tenants_list = requests.get(tenants_url, headers=self.headers)
            tenants_list = json.loads(tenants_list.text)
            return tenants_list

        def get_by_group_id(self, group_id):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/?group_id={group_id}&limit=0"
            tenants_list = requests.get(tenants_url, headers=self.headers)
            tenants_list = json.loads(tenants_list.text)
            return tenants_list

        def get_by_group_name(self, group_name):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/?group={group_name}&limit=0"
            tenants_list = requests.get(tenants_url, headers=self.headers)
            tenants_list = json.loads(tenants_list.text)
            return tenants_list

        def get_by_tag(self, tag):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/?tag={tag}&limit=0"
            tenants_list = requests.get(tenants_url, headers=self.headers)
            tenants_list = json.loads(tenants_list.text)
            return tenants_list

    class VRFS(Initiation):
        def get_all(self):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/?limit=0"
            vrfs_list = requests.get(vrfs_url, headers=self.headers)
            vrfs_list = json.loads(vrfs_list.text)
            return vrfs_list

        def get_by_id(self, id):
            vrf_url = f"{self.nb_url}/api/ipam/vrfs/{id}/"
            vrf = requests.get(vrf_url, headers=self.headers)
            vrf = json.loads(vrf.text)
            return vrf

        def get_by_name(self, name):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/?name={name}&limit=0"
            vrfs_list = requests.get(vrfs_url, headers=self.headers)
            vrfs_list = json.loads(vrfs_list.text)
            return vrfs_list

        def get_by_rd(self, rd):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/?rd={rd}&limit=0"
            vrfs_list = requests.get(vrfs_url, headers=self.headers)
            vrfs_list = json.loads(vrfs_list.text)
            return vrfs_list

        def get_by_tenant_group_slug(self, tenant_group):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/?tenant_group={tenant_group}&limit=0"
            vrfs_list = requests.get(vrfs_url, headers=self.headers)
            vrfs_list = json.loads(vrfs_list.text)
            return vrfs_list

        def get_by_tenant_id(self, tenant_id):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/?tenant_id={tenant_id}&limit=0"
            vrfs_list = requests.get(vrfs_url, headers=self.headers)
            vrfs_list = json.loads(vrfs_list.text)
            return vrfs_list

        def get_by_tenant_slug(self, tenant_slug):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/?tenant={tenant_slug}&limit=0"
            vrfs_list = requests.get(vrfs_url, headers=self.headers)
            vrfs_list = json.loads(vrfs_list.text)
            return vrfs_list

        def get_by_tag(self, tag):
            vrfs_url = f"{self.nb_url}.api/ipam/vrfs/?tag={tag}&limit=0"
            vrfs_list = requests.get(vrfs_url, headers=self.headers)
            vrfs_list = json.loads(vrfs_list.text)
            return vrfs_list

    class Prefixes(Initiation):
        def get_all(self):
            all_prefixes = f"{self.nb_url}/api/ipam/prefixes/"
            prefixes_list = requests.get(all_prefixes, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_id(self, id):
            prefix_url = f"{self.nb_url}/api/ipam/prefixes/{id}/"
            prefix = requests.get(prefix_url, headers=self.headers)
            prefix = json.loads(prefix.text)
            return prefix

        def get_by_name(self, q):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?q={q}"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_tenant_id(self, tenant_id):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?tenant_id={tenant_id}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_tenant_slug(self, tenant_slug):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?tenant={tenant_slug}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_tenant_group(self, tenant_group):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?tenant_group={tenant_group}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_vrf_id(self, vrf_id):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?vrf_id={vrf_id}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_tag_v4(self, tag):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?family=4&tag={tag}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_vrf_id_and_tag_v4(self, vrf_id, tag):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?family=4&vrf_id={vrf_id}&tag={tag}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_tag_v6(self, tag):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?family=6&tag={tag}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_two_tags_v4(self, tag1, tag2):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?family=4&tag={tag1}&tag={tag2}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_two_tags_v6(self,  tag1, tag2):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?family=6&tag={tag1}&tag={tag2}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_three_tags_v4(self, tag1, tag2, tag3):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?family=4&tag={tag1}&tag={tag2}&tag={tag3}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_vrf_id_and_three_tag_v4(self, vrf_id, tag1, tag2, tag3):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/" \
                           f"?family=4&vrf_id={vrf_id}&tag={tag1}&tag={tag2}&tag={tag3}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_by_three_tags_v6(self,  tag1, tag2, tag3):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/?family=6&tag={tag1}&tag={tag2}&tag={tag3}&limit=0"
            prefixes_list = requests.get(prefixes_url, headers=self.headers)
            prefixes_list = json.loads(prefixes_list.text)
            return prefixes_list

        def get_free_by_id(self, id):
            all_avl_prefixes = f"{self.nb_url}/api/ipam/prefixes/{id}/available-prefixes/"
            avl_prefixes = requests.get(all_avl_prefixes, headers=self.headers)
            avl_prefixes = json.loads(avl_prefixes.text)
            return avl_prefixes

    class Addresses(Initiation):
        def get_all(self):
            all_ips_url = f"{self.nb_url}/api/ipam/ip-addresses/"
            ips_list = requests.get(all_ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_id(self, id):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            ips = requests.get(ips_url, headers=self.headers)
            ips = json.loads(ips.text)
            return ips

        def get_by_tenant_id(self, tenant_id):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?tenant_id={tenant_id}&limit=0"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_tenant_id_and_prefix(self, tenant_id, prefix):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/" \
                      f"?tenant_id={tenant_id}&limit=0&parent={prefix}"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_tenant_id_and_address(self, tenant_id, address):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?tenant_id={tenant_id}&limit=0&address={address}"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_tenant_slug(self, tenant_slug):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?tenant_slug={tenant_slug}&limit=0"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_tenant_slug_and_prefix(self, tenant_slug, prefix):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?tenant={tenant_slug}&limit=0&parent={prefix}"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_tenant_slug_and_address(self, tenant_slug, address):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?tenant={tenant_slug}&limit=0&address={address}"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_address(self, address):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?address={address}&limit=0"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_mask_length(self, mask_length):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?mask_length={mask_length}&limit=0"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_tenant_id_and_mask_length(self, tenant_id, mask_length):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?tenant_id={tenant_id}&limit=0&mask_length={mask_length}"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_tenant_slug_and_mask_length(self, tenant_slug, mask_length):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?tenant={tenant_slug}&limit=0&mask_length={mask_length}"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_vrf_id(self, vrf_id):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?vrf_id={vrf_id}&limit=0"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_vrf_id_and_prefix(self, vrf_id, prefix):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?vrf_id={vrf_id}&limit=0&parent={prefix}"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_vrf_id_and_mask_length(self, vrf_id, mask_length):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?vrf_id={vrf_id}&limit=0&mask_length={mask_length}"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_vrf_id_and_address(self, vrf_id, address):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?vrf_id={vrf_id}&address={address}&limit=0"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_by_prefix(self, prefix):
            ip_url = f"{self.nb_url}/api/ipam/ip-addresses/?parent={prefix}&limit=0"
            ip = requests.get(ip_url, headers=self.headers)
            ip = json.loads(ip.text)
            return ip

        def get_by_prefix_and_address(self, prefix, address):
            ip_url = f"{self.nb_url}/api/ipam/ip-addresses/?parent={prefix}&address={address}&limit=0"
            ip = requests.get(ip_url, headers=self.headers)
            ip = json.loads(ip.text)
            return ip

        def get_by_address_and_tag(self, address, tag):
            ip_url = f"{self.nb_url}/api/ipam/ip-addresses/?address={address}&tag={tag}&limit=0"
            ip = requests.get(ip_url, headers=self.headers)
            ip = json.loads(ip.text)
            return ip

        def get_by_address_and_two_tags(self, address, tag1, tag2):
            ip_url = f"{self.nb_url}/api/ipam/ip-addresses/" \
                     f"?address={address}&tag={tag1}&tag={tag2}&limit=0"
            ip = requests.get(ip_url, headers=self.headers)
            ip = json.loads(ip.text)
            return ip

        def get_by_address_and_three_tags(self, address, tag1, tag2, tag3):
            ip_url = f"{self.nb_url}/api/ipam/ip-addresses/" \
                     f"?address={address}&tag={tag1}&tag={tag2}&tag={tag3}&limit=0"
            ip = requests.get(ip_url, headers=self.headers)
            ip = json.loads(ip.text)
            return ip

        def get_by_tag(self, tag):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/?tag={tag}&limit=0"
            ips_list = requests.get(ips_url, headers=self.headers)
            ips_list = json.loads(ips_list.text)
            return ips_list

        def get_free_ips_by_prefix_id(self, id):
            all_prefixes_avlips = f"{self.nb_url}/api/ipam/prefixes/{id}/available-ips/"
            prefixes_avlips = requests.get(all_prefixes_avlips, headers=self.headers)
            prefixes_avlips = json.loads(prefixes_avlips.text)
            return prefixes_avlips


class Create:
    """Class with Create-methods"""
    class TenantGroups(Initiation):
        """Class with Create-methods for Tenant Groups"""
        def create(self, **tenant_group):
            """Method for crating Tenant Group"""
            tenant_group_url = f"{self.nb_url}/api/tenancy/tenant-groups/"
            tenant_group_params = {"name": tenant_group['name'],
                                   "slug": tenant_group['slug']}
            new_tenant_group = requests.post(tenant_group_url, headers=self.headers, json=tenant_group_params)
            return new_tenant_group.json()

    class Tenants(Initiation):
        def create(self, **tenants):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/"
            tenants_params = {
                "name": tenants['name'],
                "slug": tenants['slug'],
                "group": tenants['tenant_group_id'],
                "description": tenants['description'],
                "comments": tenants['comments'],
                "custom_fields": tenants['custom_fields']}
            new_tenants = requests.post(tenants_url, headers=self.headers, json=tenants_params)
            return new_tenants.json()

    class VRFS(Initiation):
        def create(self, **vrfs):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/"
            vrfs_params = {"name": vrfs['name'],
                           "rd": vrfs['rd'],
                           "tenant": vrfs['tenant_id'],
                           "enforce_unique": True,
                           "description": vrfs['description'],
                           "custom_fields": vrfs['custom_fields']}
            new_vrf = requests.post(vrfs_url, headers=self.headers, json=vrfs_params)
            return new_vrf.json()

    class Prefixes(Initiation):
        def create(self, **prefixes):
            prefixes_url = f"{self.nb_url}/api/ipam/prefixes/"
            prefixes_params = {"prefix": prefixes['prefix'],
                               "vrf": prefixes['vrf_id'],
                               "tenant": prefixes['tenant_id'],
                               "status": 1,
                               "is_pool": False,
                               "description": prefixes['description'],
                               "custom_fields": prefixes['custom_fields']}
            new_prefixes = requests.post(prefixes_url, headers=self.headers, json=prefixes_params)
            return new_prefixes.json()

        def create_free_prefix(self, id, **avlprefixes):
            avlprefixes_url = f"{self.nb_url}/api/ipam/prefixes/{id}/available-prefixes/"
            avlprefixes_params = {"prefix": avlprefixes['prefix'],
                                  "vrf": avlprefixes['vrf_id'],
                                  "tenant": avlprefixes['tenant_id'],
                                  "status": 1,
                                  "is_pool": False,
                                  "description": avlprefixes['description'],
                                  "custom_fields": {}}
            new_avlprefixes = requests.post(avlprefixes_url, headers=self.headers,
                                            json=avlprefixes_params)
            return new_avlprefixes.json()

    class Addresses(Initiation):
        def create(self, address, vrf_id=None, tenant_id=None, description="", custom_fields={}, tags=None):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/"
            ips_params = {"address": address,
                          "vrf": vrf_id,
                          'tenant': tenant_id,
                          "status": 1,
                          "description": description,
                          "tags": tags,
                          "custom_fields": custom_fields}
            new_ips = requests.post(ips_url, headers=self.headers, json=ips_params)
            return new_ips.json()

        def create_free_ip(self, id, **avlips):
            avlips_url = f"{self.nb_url}/api/ipam/prefixes/{id}/available-ips/"
            avlips_params = {"prefix": avlips['prefix'],
                             "vrf": avlips['vrf_id'],
                             "tenant": avlips['tenant_id'],
                             "status": 1,
                             "is_pool": False,
                             "description": avlips['description'],
                             "custom_fields": {}}
            new_avlips = requests.post(avlips_url, headers=self.headers, json=avlips_params)
            return new_avlips.json()


class Update:
    class TenantGroups(Initiation):
        def update_by_id(self, id, **tenant_group):
            tenant_group_url = f"{self.nb_url}/api/tenancy/tenant-groups/{id}/"
            tenant_group_params = {"name": tenant_group['name'],
                                   "slug": tenant_group['slug']}
            update_tenant_group = requests.put(tenant_group_url, headers=self.headers, json=tenant_group_params)
            return update_tenant_group.json()

    class Tenants(Initiation):
        def update_by_id(self, id, **tenants):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/{id}/"
            tenants_params = {"name": tenants['name'],
                              "slug": tenants['name_company'],
                              "group": tenants['tenant_group_id'],
                              "description": tenants['description'],
                              "comments": tenants['comments'],
                              "custom_fields": tenants['custom_fields']}
            update_tenants = requests.put(tenants_url, headers=self.headers, json=tenants_params)
            return update_tenants.json()

    class VRFS(Initiation):
        def update_by_id(self, id, **vrfs):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/{id}/"
            vrfs_params = {"name": vrfs['name'],
                           "rd": vrfs['rd'],
                           "tenant": vrfs['tenant_id'],
                           "enforce_unique": True,
                           "description": vrfs['description'],
                           "custom_fields": vrfs['custom_fields']}
            update_vrfs = requests.put(vrfs_url, headers=self.headers, json=vrfs_params)
            return update_vrfs.json()

    class Prefixes(Initiation):
        def update_by_id(self, id, **prefixes):
            prefixes_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            prefixes_params = {"prefix": prefixes['prefix'],
                               "vrf": prefixes['vrf_id'],
                               "tenant": prefixes['tenant_id'],
                               "status": 1,
                               "is_pool": False,
                               "description": prefixes['description'],
                               "custom_fields": {}}
            update_prefixes = requests.put(prefixes_url, headers=self.headers, json=prefixes_params)
            return update_prefixes.json()

    class Addresses(Initiation):
        def update_by_id(self, id, **ips):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            ips_params = {"address": ips['address'],
                          "vrf": ips['vrf_id'],
                          "tenant": ips['tenant_id'],
                          "status": ips['status'],
                          "description": ips['description'],
                          "custom_fields": ips['custom_fields']}
            update_ips = requests.put(ips_url, headers=self.headers, json=ips_params)
            return update_ips.json()


class Patch:
    class TenantGroups(Initiation):
        def patch_name_by_id(self, id, **tenant_group):
            tenant_group_url = f"{self.nb_url}/api/tenancy/tenant-groups/{id}/"
            tenant_group_params = {"name": tenant_group['name']}
            patch_tenant_group = requests.patch(tenant_group_url, headers=self.headers, json=tenant_group_params)
            return patch_tenant_group.json()

        def patch_slug_by_id(self, id, **tenant_group):
            tenant_group_url = f"{self.nb_url}/api/tenancy/tenant-groups/{id}/"
            tenant_group_params = {"slug": tenant_group['slug']}
            patch_tenant_group = requests.patch(tenant_group_url, headers=self.headers, json=tenant_group_params)
            return patch_tenant_group.json()

    class Tenants(Initiation):
        def patch_name_by_id(self, id, **tenants):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/{id}/"
            tenants_params = {"name": tenants['name']}
            patch_tenants = requests.patch(tenants_url, headers=self.headers, json=tenants_params)
            return patch_tenants.json()

        def patch_slug_by_id(self, id, **tenants):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/{id}/"
            tenants_params = {"slug": tenants['name_company']}
            patch_tenants = requests.patch(tenants_url, headers=self.headers, json=tenants_params)
            return patch_tenants.json()

        def patch_group_by_id(self, id, **tenants):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/{id}/"
            tenants_params = {"group": tenants['tenant_group_id']}
            patch_tenants = requests.patch(tenants_url, headers=self.headers, json=tenants_params)
            return patch_tenants.json()

        def patch_description_by_id(self, id, **tenants):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/{id}/"
            tenants_params = {"description": tenants['description']}
            patch_tenants = requests.patch(tenants_url, headers=self.headers, json=tenants_params)
            return patch_tenants.json()

        def patch_comments_by_id(self, id, **tenants):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/{id}/"
            tenants_params = {"comments": tenants['comments']}
            patch_tenants = requests.patch(tenants_url, headers=self.headers, json=tenants_params)
            return patch_tenants.json()

        def patch_customer_id_by(self, id, **tenants):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/{id}/"
            tenants_params = {"custom_fields": {'customer_id': tenants['customer_id']}}
            patch_tenants = requests.patch(tenants_url, headers=self.headers, json=tenants_params)
            return patch_tenants.json()

        def patch_profile_id_by_id(self, id, **tenants):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/{id}/"
            tenants_params = {"custom_fields": {"profile_id": tenants['profile_id']}}
            patch_tenants = requests.patch(tenants_url, headers=self.headers, json=tenants_params)
            return patch_tenants.json()

    class VRFS(Initiation):
        def patch_name_by_id(self, id, **vrfs):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/{id}/"
            vrfs_params = {"name": vrfs['name']}
            patch_vrfs = requests.patch(vrfs_url, headers=self.headers, json=vrfs_params)
            return patch_vrfs.json()

        def patch_rd_by_id(self, id, **vrfs):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/{id}/"
            vrfs_params = {"rd": vrfs['rd']}
            patch_vrfs = requests.patch(vrfs_url, headers=self.headers, json=vrfs_params)
            return patch_vrfs.json()

        def patch_tenant_by_id(self, id, **vrfs):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/{id}/"
            vrfs_params = {"tenant": vrfs['tenant_id']}
            patch_vrfs = requests.patch(vrfs_url, headers=self.headers, json=vrfs_params)
            return patch_vrfs.json()

        def patch_description_by_id(self, id, **vrfs):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/{id}/"
            vrfs_params = {"description": vrfs['description']}
            patch_vrfs = requests.patch(vrfs_url, headers=self.headers, json=vrfs_params)
            return patch_vrfs.json()

        def patch_custom_fields_by_id(self, id, **vrfs):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/{id}/"
            vrfs_params = {"custom_fields": vrfs['custom_fields']}
            patch_vrfs = requests.patch(vrfs_url, headers=self.headers, json=vrfs_params)
            return patch_vrfs.json()

        def patch_context_by_id(self, id, **vrfs):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/{id}/"
            vrfs_params = {"custom_fields": {'context': vrfs['context']}}
            patch_vrfs = requests.patch(vrfs_url, headers=self.headers, json=vrfs_params)
            return patch_vrfs.json()

        def patch_rt_by_id(self, id, **vrfs):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/{id}/"
            vrfs_params = {"custom_fields": {'rt': vrfs['rt']}}
            patch_vrfs = requests.patch(vrfs_url, headers=self.headers, json=vrfs_params)
            return patch_vrfs.json()

        def patch_tags_by_id(self, id, **vrfs):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/{id}/"
            vrfs_params = {"tags": vrfs['tags']}
            patch_vrfs = requests.patch(vrfs_url, headers=self.headers, json=vrfs_params)
            return patch_vrfs.json()

    class Prefixes(Initiation):
        def patch_prefix_by_id(self, id, **prefixes):
            prefixes_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            prefixes_params = {"prefix": prefixes['prefix']}
            patch_prefixes = requests.patch(prefixes_url, headers=self.headers, json=prefixes_params)
            return patch_prefixes.json()

        def patch_vrf_by_id(self, id, **prefixes):
            prefixes_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            prefixes_params = {"vrf": prefixes['vrf_id']}
            patch_prefixes = requests.patch(prefixes_url, headers=self.headers, json=prefixes_params)
            return patch_prefixes.json()

        def patch_tenant_by_id(self, id, **prefixes):
            prefixes_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            prefixes_params = {"tenant": prefixes['tenant_id']}
            patch_prefixes = requests.patch(prefixes_url, headers=self.headers, json=prefixes_params)
            return patch_prefixes.json()

        def patch_status_by_id(self, id, **prefixes):
            prefixes_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            prefixes_params = {"status": prefixes['status']}
            patch_prefixes = requests.patch(prefixes_url, headers=self.headers, json=prefixes_params)
            return patch_prefixes.json()

        def patch_description_by_id(self, id, **prefixes):
            prefixes_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            prefixes_params = {"description": prefixes['description']}
            patch_prefixes = requests.patch(prefixes_url, headers=self.headers, json=prefixes_params)
            return patch_prefixes.json()

        def patch_custom_fields_by_id(self, id, **prefixes):
            prefixes_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            prefixes_params = {"custom_fields": prefixes['custom_fields']}
            patch_prefixes = requests.patch(prefixes_url, headers=self.headers, json=prefixes_params)
            return patch_prefixes.json()

    class Addresses(Initiation):
        def patch_address_by_id(self, id, **ips):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            ips_params = {"address": ips['address']}
            patch_ips = requests.patch(ips_url, headers=self.headers, json=ips_params)
            return patch_ips.json()

        def patch_vrf_by_id(self, id, **ips):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            ips_params = {"vrf": ips['vrf_id']}
            patch_ips = requests.patch(ips_url, headers=self.headers, json=ips_params)
            return patch_ips.json()

        def patch_tenant_by_id(self, id, **ips):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            ips_params = {"tenant": ips['tenant_id']}
            patch_ips = requests.patch(ips_url, headers=self.headers, json=ips_params)
            return patch_ips.json()

        def patch_status_by_id(self, id, **ips):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            ips_params = {"status": ips['status']}
            patch_ips = requests.patch(ips_url, headers=self.headers, json=ips_params)
            return patch_ips.json()

        def patch_description_by_id(self, id, **ips):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            ips_params = {"description": ips['description']}
            patch_ips = requests.patch(ips_url, headers=self.headers, json=ips_params)
            return patch_ips.json()

        def patch_tags_by_id(self, id, **ips):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            ips_params = {"tags": ips['tags']}
            patch_ips = requests.patch(ips_url, headers=self.headers, json=ips_params)
            return patch_ips.json()


class Delete:
    class TenantGroups(Initiation):
        def delete_by_id(self, id):
            tenant_group_url = f"{self.nb_url}/api/tenancy/tenant-groups/{id}/"
            delete_tenant_group = requests.delete(tenant_group_url, headers=self.headers)
            return delete_tenant_group.text

    class Tenants(Initiation):
        def delete_by_id(self, id):
            tenants_url = f"{self.nb_url}/api/tenancy/tenants/{id}/"
            delete_tenants = requests.delete(tenants_url, headers=self.headers)
            return delete_tenants.text

    class VRFS(Initiation):
        def delete_by_id(self, id):
            vrfs_url = f"{self.nb_url}/api/ipam/vrfs/{id}/"
            delete_vrfs = requests.delete(vrfs_url, headers=self.headers)
            return delete_vrfs.text

    class Prefixes(Initiation):
        def delete_by_id(self, id):
            prefixes_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            delete_prefixes = requests.delete(prefixes_url, headers=self.headers)
            return delete_prefixes.text

    class Addresses(Initiation):
        def delete_by_id(self, id):
            ips_url = f"{self.nb_url}/api/ipam/ip-addresses/{id}/"
            delete_ips = requests.delete(ips_url, headers=self.headers)
            return delete_ips.text
