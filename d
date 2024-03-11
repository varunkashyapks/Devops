from airflow import DAG
from airflow.models import BaseOperator
from airflow.utils.dates import days_ago
from google.cloud import storage

# Define the Excel files and their corresponding sheet names and destination CSV filenames
excel_files = {
    "EXCEL_FILE_1.xlsx": [{'sheetname':'Destination_FileName.csv'}],
    "EXCEL_FILE_2.xlsx": [{'sheetname_1':'Destination_FileName_1.csv','sheetname_2':'Destination_FileName_2.csv'}]
}

# Define the input and output GCS bucket details
input_gcs_bucket = 'INPUT_GCS_BUCKET'
input_folder_name = '/input_folder'
output_gcs_bucket = 'OUTPUT_GCS_BUCKET'
output_folder_name = '/output_folder'

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'excel_to_csv_to_gcs',
    default_args=default_args,
    description='Transfer Excel files to CSV and move to GCS',
    schedule_interval=None,
    start_date=days_ago(1),
    tags=['excel', 'gcs']
)

# Function to convert Excel to CSV
def excel_to_csv(excel_blob, sheetname, destination_filename):
    with pd.ExcelFile(excel_blob.open()) as xls:
        df = pd.read_excel(xls, sheet_name=sheetname)
        csv_data = df.to_csv(index=False)

    return csv_data

# Custom operator for transferring files from GCS to GCS
class CustomGCSOperator(BaseOperator):
    def execute(self, context):
        # Instantiate a client
        client = storage.Client()

        # Get the source bucket
        source_bucket = client.bucket(input_gcs_bucket)

        # Get the destination bucket
        destination_bucket = client.bucket(output_gcs_bucket)

        # Iterate through Excel files and their sheets
        for excel_file, sheets in excel_files.items():
            for sheet_details in sheets:
                for sheetname, destination_filename in sheet_details.items():
                    # Source blob path
                    source_blob = source_bucket.blob(f"{input_folder_name}/{excel_file}")

                    # Read Excel file directly without downloading
                    csv_data = excel_to_csv(source_blob, sheetname, destination_filename)

                    # Upload CSV data to destination bucket
                    destination_blob = destination_bucket.blob(f"{output_folder_name}/{destination_filename}")
                    destination_blob.upload_from_string(csv_data)

# Task to transfer files from GCS to GCS
transfer_task = CustomGCSOperator(task_id='transfer_files', dag=dag)

# Set task dependencies
transfer_task










