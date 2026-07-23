from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule
 
with DAG(

    dag_id="dag_formation2",

    start_date=datetime(2025, 1, 1),

    schedule=None,

    catchup=False,

    tags=["guide"],

) as dag:

    tache1 = BashOperator(

        task_id="tache1",
        bash_command="echo 'tache1'; hostname; date"
    )

    tache2 = BashOperator(
        task_id="tache2",
        bash_command="exit 1"
    )

    tache3 = BashOperator(
        task_id="tache3",
        bash_command="echo 'tache3'; hostname; date",
        trigger_rule=TriggerRule.ONE_SUCCESS
    )

    tache4 = BashOperator(
        task_id="tache4",
        bash_command="echo 'tache4'; hostname; date",
        trigger_rule=TriggerRule.ONE_FAILED
    )

tache1 >> tache3 
tache2 >> tache4 