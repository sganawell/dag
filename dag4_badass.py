from datetime import datetime

from airflow import DAG

from airflow.operators.python_operator import PythonOperator


def create_dag(dag_id,
               schedule,
               dag_number,
               default_args):

    def print_context(ds, **kwargs):
        print(ds)
        return 'Whatever you return gets printed in the logs'

    dag = DAG(dag_id,
              schedule_interval=schedule,
              is_paused_upon_creation=False,
              default_args=default_args)

    with dag:
        t1 = PythonOperator(
            task_id='print_the_context',
            python_callable=print_context,
            provide_context=True,
            dag_number=dag_number, dag=dag)

    return dag


# build a dag for each number in range(10)
for n in range(1, 10):
    dag_id = 'test3_{}'.format(str(n))

    default_args = {'owner': 'airflow',
                    'start_date': datetime(2020, 4, 15),
                    }

    schedule = '@once'

    dag_number = n

    globals()[dag_id] = create_dag(dag_id,
                                  schedule,
                                  dag_number,
                                  default_args
                                  )