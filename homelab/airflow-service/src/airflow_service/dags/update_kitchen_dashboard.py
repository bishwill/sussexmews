from typing import Literal
from datetime import datetime
import json

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.python import PythonOperator


SCREEN_POSITION_MAPPING = {
    "left": "catfordcastle",
    "right": "catfordcastlemini",
}


def get_run_config(**kwargs) -> None:
    """
    Pass in {"screen": "left", "url": "https://departures.sussexmews.co.uk"} for example
    """
    ti = kwargs['ti']
    conn_id = SCREEN_POSITION_MAPPING[kwargs["dag_run"].conf["screen"]]
    url = kwargs["dag_run"].conf["url"]
    payload = {"conn_id": conn_id, "url": url}
    ti.xcom_push(key='runtime-config', value=str(payload))
    return payload


dag = DAG(
    "update_kitchen_dashboard",
    default_args={
        "owner": "will",
        "retries": 0,
    },
    description="Updates the URL for a kitchen dashboard",
    schedule_interval=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
)



get_config_task = PythonOperator(
    task_id="get-run-config",
    python_callable=get_run_config,
    provide_context=True,
    dag=dag,
    do_xcom_push=True,
)

update_url = SSHOperator(
    task_id="update-url",
    ssh_conn_id="{{ ti.xcom_pull(task_ids='get-run-config')['conn_id'] }}",
    command="echo 'https://departures.sussexmews.co.uk' | sudo tee /boot/fullpageos.txt > /dev/null",
    dag=dag,
)

# reboot = SSHOperator(
#     task_id="reboot-server",
#     ssh_conn_id=get_server_conn_id(),
#     command="sudo shutdown -r",
#     dag=dag,
# )

get_config_task >> update_url
