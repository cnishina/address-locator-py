import unittest
import network_utils
import re


class LanInterfacesTest(unittest.TestCase):
  def testGetExternalIpAddress(self):
    external_ip_address = network_utils.get_external_ip_address()
    pattern = re.compile('^[0-9]+.[0-9]+.[0-9]+.[0-9]+')
    self.assertTrue(pattern.match(external_ip_address))

  def testGetLanInterfaces(self): 
    lan_interfaces = network_utils.get_lan_interfaces()
    self.assertEqual(str(type(lan_interfaces)), '<type \'dict\'>')
    for name in lan_interfaces:
      pattern = re.compile(
        '^[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:' +
        '[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]')
      self.assertTrue(pattern.match(lan_interfaces[name]['mac_address']))
      pattern = re.compile('^[0-9]+.[0-9]+.[0-9]+.[0-9]+')
      self.assertTrue(pattern.match(lan_interfaces[name]['local_ip_address']))