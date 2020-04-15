import os
from datetime import datetime , timedelta
import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
default_args = {
 ‘owner’: ‘Airflow’ ,
 ‘depends_on_past’: False ,
 ‘start_date’: airflow.utils.dates.days_ago(2) ,
 ‘retries’: 1 ,
 ‘retry_delay’: timedelta(minutes=1) ,
}
dag = DAG(
 ‘dummy_try1’ ,
 default_args=default_args ,
 schedule_interval=None)
for i in range(50000):
    tasks = DummyOperator(task_id=’{}’.format(i),dag=dag,
                        pool=’default_pool)
