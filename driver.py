#!/usr/bin/env python3
"""
Driver program to analyze given seismic data and print statistics
"""

import argparse
import csv

from earthquake_analyzer import EarthquakeAnalyzer

def main():
  """Main function of the script"""
  args_parser = argparse.ArgumentParser(
      description='Analyze given seismic data and print statistics',
  )
  args_parser.add_argument(
      '--csv_file_path',
      required=True,
      type=str,
      help='Location of the CSV file containing seismic data'
  )
  args_parser.add_argument(
      '--timezone',
      required=False,
      default='UTC',
      type=str,
      help='Compute number of earthquakes in this Timezone'
  )

  args = args_parser.parse_args()
  earthquake_analyzer = EarthquakeAnalyzer(timezone=args.timezone)

  # Read all csv data one row at a time and report to EarthquakeAnalyzer
  with open(args.csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for seismic_data in csv_reader:
      earthquake_analyzer.report_earthquake(seismic_data)

  histogram = earthquake_analyzer.get_histogram()
  print('*********************************')
  print('Number of earthquakes per day for last 30 days ({}):'.format(args.timezone))
  for key, value in histogram.items():
    print('{} : {}'.format(key, value))

  print('')
  print('Location that had the most earthquakes: {}'.format(
      earthquake_analyzer.get_location_of_max_earthquakes()
  ))

  print('')
  magnitudes = earthquake_analyzer.get_average_earthquake_magnitudes()
  print('Average earthquake magnitudes per location:')
  for key, value in magnitudes.items():
    print('{} : {}'.format(key, value))
  print('*********************************')

if __name__ == '__main__':
  main()
