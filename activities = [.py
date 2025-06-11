import pandas as pd
import numpy as np
import json
import datetime 


def array_to_dicts(array):
    """
    Converts a 2D array (with header row) to a list of dictionaries.
    """
    header = array[0]
    return [dict(zip(header, row)) for row in array[1:]]

# Example usage:
array = [
    ["Activity", "Dates", "Agency", "Location", "Authority"],
    ["Re-Entry Meeting", "October, 2016", "DOJ - BOP", "Toledo, Ohio", "Probation"],
    ["Community Control", "Oct, 2017 - Sept 2019", "DOJ - BOP", "Toledo, Ohio", "Probation"],
    ["VA Medical Appointments", "October, 2016", "VAMC - Ambulatory", "Toledo, Ohio", "VAMC"],
    ["VA Medical Referral", "January, 2017", "VAMC - Neurosurgery", "Ann Arbor, MI", "VAMC"],
    ["VA Testing (MRI)", "January, 2017", "VAMC - Radiology", "Ann Arbor, MI", "VAMC"],
    ["VA Surgery", "March 9 - Mar 17, 2017", "VAMC - Neurosurgery", "Ann Arbor, MI", "VAMC"],
    ["VA Physical Rehabilitation", "April - September, 2017", "VAMC - Ambulatory", "Toledo, Ohio", "VAMC"],
    ["ProMedica: Pain Management Physical Therapy", "September-2018 to February 2019", "PT Link", "Toledo, Ohio", "Promedica"]
]

activities = array_to_dicts(array)

activities = pd.DataFrame(activities)
activities['Dates'] = pd.to_datetime(activities['Dates'], errors='coerce', format='%B, %Y')  
# Convert 'Dates' column to datetime format


print(activities)

# Convert the DataFrame to a JSON string
activities_json = activities.to_json(orient='records', date_format='iso')
print(activities_json)
# Convert the JSON string back to a Python object
activities_dict = json.loads(activities_json)
# Print the resulting list of dictionaries
print(activities_dict)
# Convert the list of dictionaries back to a DataFrame
activities_df = pd.DataFrame(activities_dict)
# Print the resulting DataFrame
print(activities_df)
# Convert the 'Dates' column back to datetime format

activities_df['Dates'] = pd.to_datetime(activities_df['Dates'], errors='coerce', format='%Y-%m-%dT%H:%M:%S.%fZ')
# Print the final DataFrame
print(activities_df)
# Convert the DataFrame back to a JSON string
activities_json_final = activities_df.to_json(orient='records', date_format='iso')
print(activities_json_final)
# Convert the JSON string back to a Python object
activities_dict_final = json.loads(activities_json_final)
# Print the final list of dictionaries
print(activities_dict_final)
# Convert the list of dictionaries back to a DataFrame
activities_df_final = pd.DataFrame(activities_dict_final)
# Print the final DataFrame
print(activities_df_final)
# Convert the 'Dates' column back to datetime format
activities_df_final['Dates'] = pd.to_datetime(activities_df_final['Dates'], errors='coerce', format='%Y-%m-%dT%H:%M:%S.%fZ')
# Print the final DataFrame
print(activities_df_final)