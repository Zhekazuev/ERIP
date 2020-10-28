"""Configuration parameters"""
import os


class Netbox:
    # token and url for Test Netbox(BTS)
    TOKEN_TEST = "key"
    URL_TEST = "http://1.1.1.1"
    # TOKEN_TEST = os.environ['NETBOX_TOKEN_TEST']
    # URL_TEST = os.environ['NETBOX_URL_TEST']

    # token and url for Main Netbox(no test)
    TOKEN_MAIN = "key"
    URL_MAIN = "http://1.1.1.2"
    # TOKEN_MAIN = os.environ['NETBOX_ERIP_TOKEN_MAIN']
    # URL_MAIN = os.environ['NETBOX_URL_MAIN']
