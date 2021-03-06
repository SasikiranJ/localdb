from sys import exit
from argparse import ArgumentParser
from datastore.configs import configurations
from datastore.CRD.functions import DataStoreCRD
from datastore.utils.filehandler import FilePreprocess


# Adding/Enabling CommandLineArguments: --datastore
parser = ArgumentParser()
parser.add_argument('--datastore', help='Enter the datastore absolute path.')
args = parser.parse_args()

# Selecting the DataStore Directory.
# Select user provided datastore path else, select the default path.
if args.datastore:
    db_path = args.datastore
else:
    db_path = configurations.DB_DEFAULT_PATH

# Create a datastore directory.
directory_created = FilePreprocess(db_path).create_folder()
if not directory_created:
    print(f"Permission denied: You can not create the directory `{db_path}`.\n")
    exit(0)


key = 'abc'


################################
''' READ DATA FROM DATASTORE '''
_data_found, message = DataStoreCRD().check_read_data(key, db_path)
print(message)
################################
