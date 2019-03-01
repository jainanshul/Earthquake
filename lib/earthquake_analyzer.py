"""
Class that provides methods to parse and analyze seismic data
"""

from dateutil import parser, tz
import math

from lib.location_source import LocationSource

class EarthquakeAnalyzer(object):
  """Class that provides methods to parse and analyze seismic data"""
  def __init__(self, *, timezone=None):
    super(EarthquakeAnalyzer, self).__init__()
    self.__histogram = {}
    self.__locationSources = {}
    self.__timezone = timezone

  def report_earthquake(self, seismic_data):
    """
    Analyze reported seismic data

    Args:
        seismic_data (dict): Dictionary containing seismic data

    Returns:
        None

    """
    if 'time' not in seismic_data:
      raise ValueError('time filed missing in seismic data')

    # Track seismic activity per day
    self.__count_activity_per_day(seismic_data['time'])

    # Report earthquake for a given location source
    if 'locationSource' not in seismic_data:
      raise ValueError('locationSource filed missing in seismic data')

    location_source_name = seismic_data['locationSource']
    location_source = self.__locationSources.get(
        location_source_name,
        LocationSource(name=location_source_name)
    )
    location_source.report_earthquake(seismic_data)
    self.__locationSources[location_source_name] = location_source

  def get_histogram(self):
    """
    Return data points which represent the number of earthquakes in each
    respective day.

    Args:
        None

    Returns:
        (dict): Dictionary with key as the date and the value as the number of
                earthquakes for that day

    """
    return self.__histogram

  def get_location_of_max_earthquakes(self):
    """
    Return which location source had the most earthquakes

    Args:
        None

    Returns:
        (str): Name of the location source

    """
    maxLocation = ''
    maxEarthquake = -math.inf
    for key, location_source in self.__locationSources.items():
      if (location_source.num_earthquakes > maxEarthquake):
        maxLocation = key
        maxEarthquake = location_source.num_earthquakes

    return maxLocation

  def get_average_earthquake_magnitudes(self):
    """
    Return average earthquake magnitude for each location source

    Args:
        None

    Returns:
        (dict): Dictionary with key as the location name and the value as the
                 average magnitude of earthquake at that location

    """
    return {
        key:location_source.avg_magnitude
        for key, location_source in self.__locationSources.items()
    }

  def __count_activity_per_day(self, time):
    """
    Keep track of the number of earthquakes in each respective day

    Args:
        time (String): Time for the earthquake represented in RFC 3339 format

    Returns:
        None

    """
    # If no timezone specified then default to UTC
    if not self.__timezone:
      tz_timezone = tz.gettz('UTC')
    else:
      tz_timezone = tz.gettz(self.__timezone)

    # Check if user passed in an invalid timezone
    if not tz_timezone:
      raise ValueError('{} is an invalid timezone'.format(self.__timezone))

    # Make sure there is time field available
    if not time:
      raise ValueError('No time specified')

    # Convert datestime string to a datetime object
    utc_time = parser.parse(time)

    # Change the timezone to the user specified timezone
    utc_time = utc_time.astimezone(tz_timezone)

    # Get date string from the datetime object
    earthquake_date = utc_time.date().isoformat()

    # Add the counter
    self.__histogram[earthquake_date] = \
        self.__histogram.get(earthquake_date, 0) + 1
