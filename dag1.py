from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule
 
with DAG(

    dag_id="dag_formation",

    start_date=datetime(2025, 1, 1),

    schedule=None,

    catchup=False,

    tags=["guide"],

) as dag:

    hello = BashOperator(

        task_id="hello",
        bash_command="echo 'Airflow est prêt sur cette EC2'; hostname; date",
        trigger_rule=TriggerRule.ONE_FAILED
    )

    toto = BashOperator(
        task_id="toto",
        bash_command="sleep 10"
    )

    titi = BashOperator(
        task_id="titi",
        bash_command="echo 'titi'; hostname; date"
    )

    ex_4 = BashOperator(
        task_id="ex_4",
        bash_command="exit 1"
    )

toto >> ex_4 >> [hello , titi]