#!/usr/bin/env python3

import argparse
import csv

def parse_csv_file(csv_file_path):
  with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    next(csv_reader) # Skip the first row that contains column names
    for row in csv_reader:
      print(row)

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

  parse_csv_file(args.csv_file_path)

if __name__ == '__main__':
  main()
