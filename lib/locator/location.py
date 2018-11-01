import json


class Location(object):
  """The location model that includes network information."""

  def __init__(self, **kwargs):
    """The location object.
    Args:
      name: Location name of the this machine.
    """
    # The name to associate with this location.
    self.name = None
    if 'name' in kwargs:
      self.name = kwargs['name']

    # The Local (Internal) IP Address. If your computer is connected to a
    # router with default settings, that router will automatically assign a
    # local IP address to your computer. Your local IP address is hidden
    # from the outside world and used only inside your private network.
    #
    # https://goo.gl/txEmRd
    self.local_ip_address = None
    if 'local_ip_address' in kwargs:
      self.local_ip_address = kwargs['local_ip_address']

    # The External (Public) IP Address. The Internet Service Provider (ISP)
    # assigns you an external IP address when you connect to the Internet.
    # When your browser requests a webpage, it sends this IP address
    # along with it.
    #
    # https://goo.gl/txEmRd
    self.external_ip_address = None
    if 'external_ip_address' in kwargs:
      self.external_ip_address = kwargs['external_ip_address']

    self.metadata = None
    if 'metadata' in kwargs:
      self.metadata = kwargs['metadata']

  def to_json(self):
    """Convert this object to json.
    Returns:
      A json representation of this object.
    """
    return json.loads(json.dumps(self.__dict__))