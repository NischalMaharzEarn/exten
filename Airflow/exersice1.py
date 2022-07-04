from airflow import DAG
from airflow.models import dag
from datetime import datetime

required_data = {
    'owner' : 'nischal',
    'email' : 'nischalsunshine@gmail.com',
    'start_date': datetime(2022,6,16)
}
etl_dag = DAG('etl_work',default_args=required_data)
#airflow webserver -p 8080
#airflow db initStep 3 : Install and update PIP
#pip install apache-airflow
#Airflow Initdb 
#airflow webserver -p 8080
# http://localhost:8080/
#Create folder DAG in C:drive(C:\DAG)
#Step 9 : Add New DAG
#Run airflow initdb