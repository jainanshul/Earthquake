import os
import unittest

from lib.location_source import LocationSource

class TestLocationSource(unittest.TestCase):
  def test_earthquake_count(self):
    """Test earthquake count"""
    location_source = LocationSource()

    location_source.report_earthquake({'mag': '2.2'})
    self.assertEqual(location_source.num_earthquakes, 1)

    location_source.report_earthquake({'mag': '2.2'})
    self.assertEqual(location_source.num_earthquakes, 2)

  def test_invalid_earthquake_data(self):
    """Test invalid earthquake data"""
    location_source = LocationSource()

    # Test missing magnitude field
    self.assertRaises(ValueError, location_source.report_earthquake, {})

    # Test invalid magnitude data
    self.assertRaises(
        ValueError,
        location_source.report_earthquake,
        {'mag': 'invalid'}
    )

  def test_average_magnitude(self):
    """Test average magnitude"""
    location_source = LocationSource()

    nums = 10
    for i in range(nums):
      location_source.report_earthquake({'mag': str(i + 1)})

    sum_nums = (nums * (nums + 1) / 2) # (n * (n + 1)) / 2
    self.assertEqual(location_source.avg_magnitude, sum_nums / nums)
    self.assertEqual(location_source.num_earthquakes, nums)

if __name__ == '__main__':
  unittest.main()
