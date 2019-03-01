"""
Class that provides methods to parse and analyze seismic data
"""

import csv
from dateutil import parser, tz
import math

from location_source import LocationSource

class EarthquakeAnalyzer(object):
  """Class that provides methods to parse and analyze seismic data"""
  def __init__(self):
    super(EarthquakeAnalyzer, self).__init__()
    self.__histogram = {}
    self.__locationSources = {}

  def parse(self, csv_file_path, *, timezone=None):
    """
    Parse csv file and store the seismic data

    Args:
        csv_file_path (String): Path to the csv file to parse
        timezone (String): Timezone used to generate the histogram

    Returns:
        None

    """
    with open(csv_file_path, 'r') as csv_file:
      csv_reader = csv.DictReader(csv_file)

      for row in csv_reader:
        self.__calculate_histogram(row['time'], timezone=timezone)

        # Report earthquake for the location source
        location_source_name = row['locationSource']
        location_source = self.__locationSources.get(
            location_source_name,
            LocationSource(name=location_source_name)
        )
        location_source.report_earthquake(row)
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

  def __calculate_histogram(self, time, *, timezone=None):
    """
    Calculate data points which represent the number of earthquakes in each
    respective day.

    Args:
        time (String): Time for the earthquake represented in RFC 3339 format
        timezone (String): Timezone used to generate the histogram

    Returns:
        None

    """
    # If not timezone specified then default to UTC
    if not timezone:
      tz_timezone = tz.gettz('UTC')
    else:
      tz_timezone = tz.gettz(timezone)

    # If user passed in an invalid timezone then return
    if not tz_timezone:
      raise ValueError('{} is an invalid timezone'.format(timezone))

    # For some reason there is no time available for this seismic data
    if not time:
      raise ValueError('No time specified')

    # Convert datestime string to datetime object
    utc_time = parser.parse(time)

    # Change the timezone to the user specified timezone
    utc_time = utc_time.astimezone(tz_timezone)

    # Get date string from the datetime object
    earthquake_date = utc_time.date().isoformat()

    # Add the counter
    self.__histogram[earthquake_date] = \
        self.__histogram.get(earthquake_date, 0) + 1
