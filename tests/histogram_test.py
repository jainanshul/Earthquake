import csv
import os
import unittest

from earthquake_analyzer import EarthquakeAnalyzer

class TestHistogram(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    """Setup method that gets called once for all the tests"""
    current_dir = os.path.join(os.path.dirname(__file__))
    cls.csv_file_path = os.path.join(
        current_dir,
        '..',
        'artifacts',
        '1.0_month.csv'
    )

  def test_histogram_utc(self):
    """Test histogram in default (UTC) timezone"""
    earthquake_analyzer = EarthquakeAnalyzer()
    expected_histogram = {
      '2019-03-01' : 10,
      '2019-02-28' : 187,
      '2019-02-27' : 189,
      '2019-02-26' : 183,
      '2019-02-25' : 207,
      '2019-02-24' : 159,
      '2019-02-23' : 182,
      '2019-02-22' : 153,
      '2019-02-21' : 163,
      '2019-02-20' : 181,
      '2019-02-19' : 166,
      '2019-02-18' : 151,
      '2019-02-17' : 149,
      '2019-02-16' : 187,
      '2019-02-15' : 232,
      '2019-02-14' : 164,
      '2019-02-13' : 230,
      '2019-02-12' : 263,
      '2019-02-11' : 168,
      '2019-02-10' : 199,
      '2019-02-09' : 225,
      '2019-02-08' : 247,
      '2019-02-07' : 285,
      '2019-02-06' : 258,
      '2019-02-05' : 238,
      '2019-02-04' : 204,
      '2019-02-03' : 250,
      '2019-02-02' : 219,
      '2019-02-01' : 244,
      '2019-01-31' : 271,
      '2019-01-30' : 242,
    }

    # Default timezone of UTC
    with open(self.csv_file_path, 'r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
        earthquake_analyzer.report_earthquake(row)

    histogram = earthquake_analyzer.get_histogram()
    self.assertDictEqual(histogram, expected_histogram)

  def test_histogram_pdt(self):
    """Test histogram in PDT timezone"""
    earthquake_analyzer = EarthquakeAnalyzer(timezone='PDT')
    expected_histogram = {
      '2019-02-28' : 125,
      '2019-02-27' : 195,
      '2019-02-26' : 178,
      '2019-02-25' : 208,
      '2019-02-24' : 181,
      '2019-02-23' : 173,
      '2019-02-22' : 170,
      '2019-02-21' : 146,
      '2019-02-20' : 170,
      '2019-02-19' : 165,
      '2019-02-18' : 162,
      '2019-02-17' : 157,
      '2019-02-16' : 168,
      '2019-02-15' : 221,
      '2019-02-14' : 179,
      '2019-02-13' : 220,
      '2019-02-12' : 255,
      '2019-02-11' : 204,
      '2019-02-10' : 182,
      '2019-02-09' : 214,
      '2019-02-08' : 229,
      '2019-02-07' : 288,
      '2019-02-06' : 261,
      '2019-02-05' : 244,
      '2019-02-04' : 216,
      '2019-02-03' : 233,
      '2019-02-02' : 223,
      '2019-02-01' : 239,
      '2019-01-31' : 260,
      '2019-01-30' : 258,
      '2019-01-29' : 82,
    }

    with open(self.csv_file_path, 'r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
        earthquake_analyzer.report_earthquake(row)

    histogram = earthquake_analyzer.get_histogram()
    self.assertDictEqual(histogram, expected_histogram)

if __name__ == '__main__':
  unittest.main()
