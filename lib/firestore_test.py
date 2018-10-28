import firestore
import json
import location
import os
import requests
import unittest
import uuid



class FireStoreTest(unittest.TestCase):
  def setUp(self):
    service_account_json = os.path.abspath('serviceAccount.json')
    base_path = 'alt_test'
    url = ('https://%s.firebaseio.com' % json.loads(
      open(service_account_json).read())['project_id'])
    database_url = url
    self.test_url = '%s/%s/' % (url, base_path)
    self.name = str(uuid.uuid1()).replace('-', '')
    self.fs = firestore.FireStore(base_path, database_url, service_account_json)

  def testE2E(self): 
    """Should upload to firebase a location with a name."""

    # Update location.
    update_location = location.Location(name=self.name)
    self.fs.update_location(update_location)
    r = requests.get('%s/%s.json' % (self.test_url, self.name))
    self.assertEqual(json.loads(r.text)['name'], self.name)

    # Get location.
    get_location = self.fs.get_location(self.name)
    self.assertEqual(get_location.name, self.name)

    # Remove location.
    self.fs.remove_location(self.name)
    r = requests.get('%s/%s.json' % (self.test_url, self.name))
    self.assertEqual(str(r.text), 'null')