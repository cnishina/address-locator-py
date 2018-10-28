import location
import unittest


class LocationTest(unittest.TestCase):
  def testToJson(self):
    test_location = location.Location(name='foo', mac_address='bar')
    test_json = test_location.to_json()
    self.assertEqual(test_json['name'], 'foo')
    self.assertEqual(test_json['mac_address'], 'bar')
    self.assertEqual(test_json['local_ip_address'], None)
    self.assertEqual(test_json['external_ip_address'], None)