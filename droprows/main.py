"""
to run:
pipenv shell main.py

"""
import sys
import pandas as pd

def select_non_numeric(current_df):
    current_df_num = current_df.copy()
    current_df_num['value_num'] = current_df_num['value'].apply(pd.to_numeric, errors='coerce')
    non_numeric_ids = list(current_df_num[current_df_num['value_num'].isnull()]['id'])
    return non_numeric_ids

def replace_non_numeric(current_df, previous_df):
    non_numeric_ids = select_non_numeric(current_df)

    for error_id in non_numeric_ids:
        if error_id in list(previous_df['id']):
            current_df.loc[current_df['id'] == error_id, 'value'] = previous_df.loc[previous_df['id'] == error_id, 'value']
        else:
            current_df = current_df[current_df['id'] != error_id]
    
    return current_df

if __name__ == '__main__':
    # for debug
    # filepath = 'C:\\blahblah\\filename.csv'
    # sys.stdout = open("C:/check/stdout.txt", "w")
    # sys.stderr = open("C:/check/stderr.txt", "w")
    # end debug
    
    # read in variables
    filepath_current = sys.argv[1]
    filepath_previous = sys.argv[2]
    
    # run function
    previous_df = pd.read_csv(filepath_previous)
    current_df = pd.read_csv(filepath_current)
    current_df = replace_non_numeric(current_df, previous_df)

