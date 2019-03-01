"""
Class that abstracts information about location of seismic data
"""

class LocationSource(object):
  """Abstract information about location of seismic data"""
  def __init__(self, *, name=None):
    super(LocationSource, self).__init__()
    self.__name = name
    self.__num_earthquakes = 0
    self.__avg_magnitude = 0

  @property
  def num_earthquakes(self):
    """
    Report total number of earthquakes at this location

    Args:
        None

    Returns:
        (int): Number of earthquakes

    """
    return self.__num_earthquakes

  @property
  def avg_magnitude(self):
    """
    Average earthquake magnitude for this location

    Args:
        None

    Returns:
        (float): Average earthquake magnitude

    """
    return self.__avg_magnitude

  def report_earthquake(self, seismic_data):
    """
    Report another earthquake at this location

    Args:
        seismic_data (dict): Dictionary containing seismic data for this
                             location

    Returns:
        None

    """
    if 'mag' not in seismic_data:
      raise ValueError('Magnitude value missing in the seismic data')

    # Read seismic data and convert to floating point decimal
    new_magnitude = float(seismic_data['mag'])

    # Calculate the running average of magnitude of the quake
    self.__avg_magnitude = (
        self.__avg_magnitude * self.__num_earthquakes +
        new_magnitude
    ) / (self.__num_earthquakes + 1)

    # Increment the count of earthquakes
    self.__num_earthquakes = self.__num_earthquakes  + 1
