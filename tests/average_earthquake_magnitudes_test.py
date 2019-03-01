import unittest
import datetime

from lib.earthquake_analyzer import EarthquakeAnalyzer

class TestAverageEarthquakeMagnitudes(unittest.TestCase):

  def test_average_earthquake_magnitudes(self):
    """Test average earthquake magnitudes"""
    seismic_data = {
      'time': datetime.datetime.now().isoformat(),
      'locationSource': 'ak',
      'mag': 1,
    }
    earthquake_analyzer = EarthquakeAnalyzer()

    # Report 2 earthquakes in ak
    earthquake_analyzer.report_earthquake(seismic_data)
    seismic_data['mag'] = 2
    earthquake_analyzer.report_earthquake(seismic_data)

    # Report 1 earthquakes in ci
    seismic_data['locationSource'] = 'ci'
    seismic_data['mag'] = 1
    earthquake_analyzer.report_earthquake(seismic_data)

    # Report 3 earthquakes in nc
    seismic_data['locationSource'] = 'nc'
    seismic_data['mag'] = 1
    earthquake_analyzer.report_earthquake(seismic_data)
    seismic_data['mag'] = 2
    earthquake_analyzer.report_earthquake(seismic_data)
    seismic_data['mag'] = 3
    earthquake_analyzer.report_earthquake(seismic_data)

    expected_magnitudes = {
      'ak': 1.5,
      'ci': 1,
      'nc': 2,
    }
    self.assertEqual(
        earthquake_analyzer.get_average_earthquake_magnitudes(),
        expected_magnitudes
    )

if __name__ == '__main__':
  unittest.main()
