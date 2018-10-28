"""Network utils for alternative location tool."""
import json
import netifaces
import requests
import socket


def get_external_ip_address():
  """Gets the external ip address or the WAN IP address.
  Returns:
    The ip address as a string.
  """
  r = requests.get('https://api.ipify.org?format=json')
  return json.loads(r.text)['ip']

def get_lan_interfaces():
  """Gets the LAN interfaces for the mac and ip address.

  Inspired by: http://stackoverflow.com/questions/270745/
  Another option is to use the sockets module method gethostbyname.

  Returns:
    A dictionary of network interfaces.
  """
  internal_addresses = {}
  for interface in netifaces.interfaces():
    local_address = None
    mac_address = None
    ifaddresses = netifaces.ifaddresses(interface)
    try:
      local_ip_address = ifaddresses[netifaces.AF_INET][0]['addr']
      mac_address = ifaddresses[netifaces.AF_LINK][0]['addr']
      if mac_address and local_address:
        internal_addresses[interface] = {
          'local_ip_address': local_ip_address,
          'mac_address': mac_address
        }
    except KeyError:
      pass
  return internal_addresses
