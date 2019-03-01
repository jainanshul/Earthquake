#!/usr/bin/env python3
"""
Driver program to analyze given seismic data and print statistics
"""

import argparse

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

  # Use an instance of earthquake analyzer to print stats
  earthquake_analyzer = EarthquakeAnalyzer()
  earthquake_analyzer.parse(args.csv_file_path, timezone=args.timezone)

  histogram = earthquake_analyzer.get_histogram()
  print('*********************************')
  print('Histogram data for last 30 days:')
  for key, value in histogram.items():
    print('{} : {}'.format(key, value))

  print('')
  print('Location source that had the most earthquakes: {}'.format(
      earthquake_analyzer.get_location_of_max_earthquakes()
  ))
  print('*********************************')

if __name__ == '__main__':
  main()
