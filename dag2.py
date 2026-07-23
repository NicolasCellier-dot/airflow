from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
 
with DAG(
    dag_id="dag_formation2",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["guide"],
) as dag:
    hello = BashOperator(
        task_id="hello2",
        bash_command="echo 'Airflow est prêt sur cette EC2'; hostname; date"
    )

    hello = BashOperator(
        task_id="toto2",
        bash_command="echo 'toto'; hostname; date"
    )

    hello = BashOperator(
        task_id="titi2",
        bash_command="echo 'titi'; hostname; date"
    )