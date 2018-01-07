# V60F4Rt5qz

Written code with Python 3.6

Running the code 

```
>>> python main.py
1.csv
[{'day': 'mon', 'description': 'first_desc 1', 'square': 1, 'value': 1},
 {'day': 'tue', 'description': 'first_desc 25', 'square': 25, 'value': 5},
 {'day': 'wed', 'description': 'first_desc 4', 'square': 4, 'value': 2},
 {'day': 'thu', 'description': 'first_desc 6', 'double': 6, 'value': 3},
 {'day': 'fri', 'description': 'first_desc 6', 'double': 6, 'value': 3}]

2.csv
[{'day': 'mon', 'description': 'second_desc 4', 'square': 4, 'value': 2},
 {'day': 'tue', 'description': 'second_desc 4', 'square': 4, 'value': 2},
 {'day': 'wed', 'description': 'second_desc 4', 'square': 4, 'value': 2},
 {'day': 'thu', 'description': 'second_desc 4', 'double': 4, 'value': 2},
 {'day': 'fri', 'description': 'second_desc 6', 'double': 6, 'value': 3}]

3.csv
[{'day': 'mon', 'description': 'third_desc 9', 'square': 9, 'value': 3},
 {'day': 'tue', 'description': 'third_desc 9', 'square': 9, 'value': 3},
 {'day': 'wed', 'description': 'third_desc 4', 'square': 4, 'value': 2},
 {'day': 'thu', 'description': 'third_desc 4', 'double': 4, 'value': 2},
 {'day': 'fri', 'description': 'third_desc 2', 'double': 2, 'value': 1}]
```

## Unit Test

Running test 

```
>>> python test.py -v
test_csv_class_attributes (__main__.CSV1Test) ... ok
test_csv_parse_data_isinstance_of_list (__main__.CSV1Test)
test for response of render_data is list object ... ok
test_csv_read_description (__main__.CSV1Test) ... ok
test_csv_read_monday (__main__.CSV1Test) ... ok
test_csv_class_attributes (__main__.CSV2Test) ... ok
test_csv_parse_data_isinstance_of_list (__main__.CSV2Test)
test for response of render_data is list object ... ok
test_csv_read_description (__main__.CSV2Test) ... ok
test_csv_read_monday (__main__.CSV2Test) ... ok
test_csv_class_attributes (__main__.CSV3Test) ... ok
test_csv_parse_data_isinstance_of_list (__main__.CSV3Test)
test for response of render_data is list object ... ok
test_csv_read_description (__main__.CSV3Test) ... ok
test_csv_read_monday (__main__.CSV3Test) ... ok
test_invalid_dayrange_weekday (__main__.UtilsTest)
test invalid day range for weekday method ... ok
test_invalid_double (__main__.UtilsTest)
test invalid double method ... ok
test_invalid_square (__main__.UtilsTest)
test invalid square method ... ok
test_valid_dayrange_weekday (__main__.UtilsTest)
test valid day range for weekday method ... ok
test_valid_double (__main__.UtilsTest)
test valid double method ... ok
test_valid_square (__main__.UtilsTest)
test valid square method ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.020s

OK
```
