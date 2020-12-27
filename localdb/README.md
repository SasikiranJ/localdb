# OwnDB:- Simple key-value datastore  

## Steps to install library to local machine  
1) First clone or download repository  
2) Then simply run ** python setup.py install ** command to build library.  

## Using library in your code
1) We have class called DataStoreCRD in which we have threee functions corresponding to Create, Read and Delete operations

Example:-  
First import respective class  
from datastore.CRD.functions import DataStoreCRD  

## For inserting data into DataStore  
DataStoreCRD().check_create_data(json_data, db_path)  

## For Reading the data using key  
DataStoreCRD().check_read_data(key, db_path)  

## For Deleting the data using key  
DataStoreCRD().check_delete_data(key, db_path)  


## Environment Supported   
1) Linux (CentOS) 

## API based utility
We can use this db as api also by requesting to particular endpoints.  
Examples  
curl -v http://localhost:8000/datastore/read?key="abc"  For reading value associated with key "abc"  

## Tests  
In Tests folder we have three test files for checking CRD operations  
