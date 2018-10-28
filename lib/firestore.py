import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import location
import logger

log = logger.getLogger(__name__)

class FireStore(object):

  def __init__(self, base_path, database_url, service_account_json):
    """Initializes the firebase storage admin with credentials.
    Args:
      base_path: The firebaseio base path.
      database_url: The firebaseio database url.
      service_account_json: Full path to the service account key json file.
    """
    self.base_path = base_path
    self.database_url = database_url
    self.set_credentials(database_url, service_account_json)

  def set_credentials(self, database_url, service_account_json):
    """Sets the credentials for the firebase admin db.
    Args:
      database_url: The database url.
      service_account_json: Full path to the service account key json file.
    """
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate(service_account_json)

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {'databaseURL': database_url})

  def get_location(self, name):
    """Get the location from storage.
    Args:
      name: The location name.
    Returns:
      The location.Location object.
    """
    log.info('get location %s/%s', self.base_path, name)
    ref = db.reference('%s/%s' % (self.base_path, name))
    json_location = json.loads(json.dumps(ref.get()))
    lookup_location = location.Location(name=name)
    if 'external_ip_address' in json_location:
      lookup_location.external_ip_address = json_location['external_ip_address']
    if 'local_ip_address' in json_location:
      lookup_location.local_ip_address = json_location['local_ip_address']
    if 'mac_address' in json_location:
      lookup_location.mac_address = json_location['mac_address']
    return lookup_location

  def update_location(self, save_location):
    """Update a location to storage.
    Args:
      location: A location.Location object
    """
    log.info('update location %s/%s', self.base_path, save_location.name)
    location_ref = db.reference(
      '%s/%s' % (self.base_path, save_location.name))
    location_ref.set(save_location.to_json())
  
  def remove_location(self, name):
    """Remove a location from storage.
    Args:
      name: A location name to remove
    """
    log.info('remove location: %s/%s', self.base_path, name)
    location_ref = db.reference('%s/%s' % (self.base_path, name))
    location_ref.delete()