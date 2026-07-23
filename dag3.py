from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule
from airflow.utils.task_group import TaskGroup
 
with DAG(

    dag_id="dag_formation3",

    start_date=datetime(2025, 1, 1),

    schedule=None,

    catchup=False,

    tags=["guide"],

) as dag:

    with TaskGroup(group_id="groupe_1") as groupe_1:

        tache01 = BashOperator(

            task_id="tache01",
            bash_command="echo 'tache01'; hostname; date"
        )

        tache02 = BashOperator(
            task_id="tache02",
            bash_command="exit 1"
        )

        [tache01 , tache02]

    with TaskGroup(group_id="groupe_2") as groupe_2:
        tache03 = BashOperator(
            task_id="tache03",
            bash_command="echo 'tache03'; hostname; date"
        )

        tache04 = BashOperator(
            task_id="tache04",
            bash_command="echo 'tache04'; hostname; date"
        )

        [tache03 , tache04]

groupe_1 >> groupe_2
