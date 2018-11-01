from context import firestore
from context import location
from context import logger
from context import network_utils
import datetime
import flags
import json
import os
import time

FLAGS = flags.FLAGS

flags.DEFINE_string('location_name', None, 'Set this location name')
flags.DEFINE_string('base_path', None, 'Set the firebase base path.')
flags.DEFINE_string('service_account_json', None,
                    'Set the file path to the service account key json file.')

timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
database_url = ('https://%s.firebaseio.com' % json.loads(
  open(FLAGS.service_account_json).read())['project_id'])
fs = firestore.FireStore(FLAGS.base_path, database_url,
  FLAGS.service_account_json)
lan_interfaces = network_utils.get_lan_interfaces()
update_location = location.Location(
  name=FLAGS.location_name,
  external_ip_address=network_utils.get_external_ip_address(),
  local_ip_address=network_utils.get_lan_interfaces(),
  metadata={'project': 'address-locator-python', 'timestamp': timestamp}
)
fs.update_location(update_location)