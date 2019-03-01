import unittest
import datetime

from earthquake_analyzer import EarthquakeAnalyzer

class TestMaxEarthquakeLocation(unittest.TestCase):

  def test_mssing_location_source(self):
    """Test missing location source"""
    earthquake_analyzer = EarthquakeAnalyzer()

    # Test missing required fields in seismic data
    self.assertRaises(ValueError, earthquake_analyzer.report_earthquake, {})

  def test_max_earthquake_location(self):
    """Test location of max earthquake"""
    seismic_data = {
      'time': datetime.datetime.now().isoformat(),
      'locationSource': 'ak',
      'mag': 1,
    }
    earthquake_analyzer = EarthquakeAnalyzer()

    # Report 2 earthquakes in ak
    earthquake_analyzer.report_earthquake(seismic_data)
    earthquake_analyzer.report_earthquake(seismic_data)

    # Report 1 earthquakes in ci
    seismic_data['locationSource'] = 'ci'
    earthquake_analyzer.report_earthquake(seismic_data)

    # Report 3 earthquakes in nc
    seismic_data['locationSource'] = 'nc'
    earthquake_analyzer.report_earthquake(seismic_data)
    earthquake_analyzer.report_earthquake(seismic_data)
    earthquake_analyzer.report_earthquake(seismic_data)

    self.assertEqual(earthquake_analyzer.get_location_of_max_earthquakes(), 'nc')

if __name__ == '__main__':
  unittest.main()
