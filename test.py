"""Summary
"""
import unittest
from main import ParseCSV
import utils


class CSV1Test(unittest.TestCase):

    """CSV 1 Test

    Attributes:
        csv_file (TYPE): Description
        data (str): Description
    """

    def setUp(self):
        """
        Setup for 1.csv unit test
        """
        self.data = 'csv_files/1.csv'
        self.csv_file = ParseCSV(self.data)

    def test_csv_read_monday(self):
        """
        Test for CSV to have all required columns
        """
        self.csv_file.parse_data()
        self.assertEqual(self.csv_file.mon, '1')

    def test_csv_read_description(self):
        """
        Test for for column data
        """
        self.csv_file.parse_data()
        self.assertEqual(self.csv_file.description, 'first_desc')

    def test_csv_class_attributes(self):
        """
        Test for CSV to have all required columns
        """
        self.csv_file.parse_data()
        self.assertTrue(self.csv_file.mon)
        self.assertTrue(self.csv_file.tue)
        self.assertTrue(self.csv_file.wed)
        self.assertTrue(self.csv_file.thu)
        self.assertTrue(self.csv_file.fri)
        self.assertTrue(self.csv_file.description)

    def test_csv_parse_data_isinstance_of_list(self):
        """test for response of render_data is list object
        """
        self.csv_file.parse_data()
        self.assertIsInstance(self.csv_file.render_data(), list)


class CSV2Test(unittest.TestCase):

    """CSV 2 Test

    Attributes:
        csv_file (TYPE): Description
        data (str): Description
    """

    def setUp(self):
        """
        Setup for unit test
        """
        self.data = 'csv_files/2.csv'
        self.csv_file = ParseCSV(self.data)

    def test_csv_read_monday(self):
        """
        Test for CSV to have all required columns
        """
        self.csv_file.parse_data()
        self.assertEqual(self.csv_file.mon, '2')

    def test_csv_class_attributes(self):
        """
        Test for CSV to have all required columns
        """
        self.csv_file.parse_data()
        self.assertTrue(self.csv_file.mon)
        self.assertTrue(self.csv_file.tue)
        self.assertTrue(self.csv_file.wed)
        self.assertTrue(self.csv_file.thu)
        self.assertTrue(self.csv_file.fri)
        self.assertTrue(self.csv_file.description)

    def test_csv_read_description(self):
        """
        Test for for column data
        """
        self.csv_file.parse_data()
        self.assertEqual(self.csv_file.description, 'second_desc')

    def test_csv_parse_data_isinstance_of_list(self):
        """test for response of render_data is list object
        """
        self.csv_file.parse_data()
        self.assertIsInstance(self.csv_file.render_data(), list)


class CSV3Test(unittest.TestCase):

    """CSV 3 Test

    Attributes:
        csv_file (TYPE): Description
        data (str): Description
    """

    def setUp(self):
        """
        Setup for unit test
        """
        self.data = 'csv_files/3.csv'
        self.csv_file = ParseCSV(self.data)

    def test_csv_read_monday(self):
        """
        Test for CSV to have all required columns
        """
        self.csv_file.parse_data()
        self.assertEqual(self.csv_file.mon, '3')

    def test_csv_read_description(self):
        """
        Test for for column data
        """
        self.csv_file.parse_data()
        self.assertEqual(self.csv_file.description, 'third_desc')

    def test_csv_class_attributes(self):
        """
        Test for CSV to have all required columns
        """
        self.csv_file.parse_data()
        self.assertTrue(self.csv_file.mon)
        self.assertTrue(self.csv_file.tue)
        self.assertTrue(self.csv_file.wed)
        self.assertTrue(self.csv_file.thu)
        self.assertTrue(self.csv_file.fri)
        self.assertTrue(self.csv_file.description)

    def test_csv_parse_data_isinstance_of_list(self):
        """test for response of render_data is list object
        """
        self.csv_file.parse_data()
        self.assertIsInstance(self.csv_file.render_data(), list)


class UtilsTest(unittest.TestCase):

    """Utility method test
    """

    def test_valid_dayrange_weekday(self):
        """test valid day range for weekday method
        """
        dayrange = 'mon-thu'
        self.assertEqual(len(utils.weekday(dayrange)), 4)

    def test_invalid_dayrange_weekday(self):
        """test invalid day range for weekday method
        """
        dayrange = 'monthu'
        with self.assertRaises(ValueError):
            utils.weekday(dayrange)

    def test_valid_square(self):
        """test valid square method
        """
        self.assertEqual(utils.square(3), 9)

    def test_invalid_square(self):
        """test invalid square method
        """
        with self.assertRaises(ValueError):
            utils.square('invalid_input')

    def test_valid_double(self):
        """test valid double method
        """
        self.assertEqual(utils.double(3), 6)

    def test_invalid_double(self):
        """test invalid double method
        """
        with self.assertRaises(ValueError):
            utils.double('invalid_input')


if __name__ == '__main__':
    unittest.main()
