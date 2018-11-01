import location
import unittest


class LocationTest(unittest.TestCase):
  def testToJson(self):
    test_location = location.Location(name='foo',
      local_ip_address={'en0': {'local_ip_address': '1.2.3.4'}})
    test_json = test_location.to_json()
    self.assertEqual(test_json['name'], 'foo')
    self.assertEqual(test_json['local_ip_address']['en0']['local_ip_address'],
      '1.2.3.4')
