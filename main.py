"""Summary

Attributes:
    ignore_list (list): Description
"""
import csv
import utils
import os
import calendar
from collections import OrderedDict
import json
import pprint

ignore_list = ['some_data', 'some_column1', 'another_column2']


class ParseCSV(object):

    """Summary

    Attributes:
        data (TYPE): Description
    """

    def __init__(self, data):
        """Summary

        Args:
            data (TYPE): Description
        """
        self.data = data

    def parse_data(self):
        """
        Parsing CSV file
        :return: list of csv data

        Returns:
            TYPE: Description
        """
        with open(self.data, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                for key, value in row.items():
                    if key not in ignore_list:
                        if '-' in key:
                            weekdays = utils.weekday(key)
                            for item in weekdays:
                                setattr(self, item, value)

                        else:
                            setattr(self, key, value)

       
    def render_data(self):
        """Summary
        """
        row_list = []
        weekdays = [d[:3].lower() for d in calendar.day_name if d not in [
            'Saturday', 'Sunday']]

        for day in weekdays:
            row = OrderedDict()
            item = int(getattr(self,  day, None))
            row.update({'day': day})
            if day in ['thu', 'fri']:
                double_value = utils.double(item)
                row.update({'description': ' '.join(
                    [getattr(self,  'description', None), str(double_value)])})
                row.update({'double': double_value})

            else:
                square_value = utils.square(item)
                row.update({'description': ' '.join(
                    [getattr(self,  'description', None), str(square_value)])})
                row.update({'square': square_value})

            row.update({'value': item})
            row_list.append(row)
        
        return json.loads(json.dumps(row_list))


if __name__ == "__main__":
    for subdir, dirs, files in os.walk('csv_files/'):
        for file in files:
            if file.endswith('.csv'):
                print(file)
                csv_file = ParseCSV('csv_files/' + file)
                csv_file.parse_data()
                pprint.pprint(csv_file.render_data())
                print('', end='\n')

