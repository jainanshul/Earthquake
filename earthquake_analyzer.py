#!/usr/bin/env python3
"""
Class that provides methods to parse and analyze seismic data
"""

import csv
from dateutil import parser, tz

class EarthquakeAnalyzer(object):
  """Class that provides methods to parse and analyze seismic data"""
  def __init__(self):
    super(EarthquakeAnalyzer, self).__init__()
    self.__histogram = {}

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

  def get_histogram(self):
    """
    Return data points which represent the number of earthquakes in each
    respective day.

    Args:
        None

    Returns:
        (dict): Dictionary with key as the date and the value as the number of
                earthquake for that day

    """
    return self.__histogram

  def __calculate_histogram(self, time, *, timezone=None):
    """
    Calcuate data points which represent the number of earthquakes in each
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
      print('{} is an invalid timezone'.format(timezone))
      return

    # For some reason there is no time available for this seismic data
    if not time:
      print('No time specified')
      return

    # Convert datestime string to datetime object
    utc_time = parser.parse(time)

    # Change the timezone to the user specified timezone
    utc_time = utc_time.astimezone(tz_timezone)

    # Get date string from the datetime object
    earthquake_date = utc_time.date().isoformat()

    # Add the counter
    self.__histogram[earthquake_date] = \
        self.__histogram.get(earthquake_date, 0) + 1
