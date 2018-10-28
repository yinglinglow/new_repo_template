"""
to run tests: 
pipenv shell python -m pytest tests
"""

import pandas as pd
import pandas.util.testing as pdt
from droprows import main

def test_droprows():
    current_df = pd.DataFrame([['101', '123'],
                                ['102', '234'],
                                ['103', '345'], 
                                ['104', 'error'],
                                ['105', 'error']], columns=['id', 'value'])

    assert main.select_non_numeric(current_df) == ['104', '105']

    previous_df = pd.DataFrame([['201', '223'],
                                ['202', '334'],
                                ['203', '445'], 
                                ['104', '456']], columns=['id', 'value'])
    
    correct_df = pd.DataFrame([['101', '123'],
                                ['102', '234'],
                                ['103', '345'], 
                                ['104', '456']], columns=['id', 'value'])

    test_df = main.replace_non_numeric(current_df, previous_df)
    pdt.assert_frame_equal(test_df, correct_df)