import pandas as pd
import os
import re

def extract_hms_id(filename):
    match = re.search(r'(\d+)$', filename.split('.')[0])
    if match:
        return match.group()
    else:
        return None

# Define the filename
# Define the filename
directory=os.getcwd()
print(directory)
for root, dirs, files in os.walk(directory):
                for filename in files:
                   if filename.lower().endswith(('.csv')):
                        print ('------'+filename)
                        base_name, _ = os.path.splitext(filename)
                        # Construct the new filename with the new extension
                        new_filename = base_name + '.csv'
                        hms_id = extract_hms_id(new_filename)
                        if hms_id:
                                print(f"Extracted HMS_ID: {hms_id}")
                        else:
                                raise ValueError("HMS_ID could not be extracted from the filename")

                        # Extract HMS_ID from the filename
                        hms_id = extract_hms_id(new_filename)
                        if hms_id:
                            print(f"Extracted HMS_ID: {hms_id}")
                        else:
                            raise ValueError("HMS_ID could not be extracted from the filename")
                        # Create the 'id' value
                        id_value = f"velverde_{new_filename.split('.')[0]}"
                        print(f"Generated id value: {id_value}")
                        # Read the CSV file into a DataFrame
                        df = pd.read_csv(filename)
                        # Add the new columns
                        df['TS_id'] = id_value
                        df['HMS_id']= hms_id
                        df['id'] = range(1, len(df) + 1)
                        # Save the modified DataFrame to a new CSV file
                        output_filename = "modified_" + new_filename
                        df.to_csv(output_filename, index=False)
                        print(f"Modified CSV saved as: {output_filename}")
                        



                    