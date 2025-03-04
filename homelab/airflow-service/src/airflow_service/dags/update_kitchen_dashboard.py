from datetime import datetime

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator


def get_server_conn_id(**kwargs):
    screen = kwargs["dag_run"].conf.get("screen")
    mapping = {
        "left": "catfordcastle",
        "right": "catfordcastlemini",
    }
    return mapping[screen]


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

update_url = SSHOperator(
    task_id="update-url",
    ssh_conn_id=get_server_conn_id(),
    command="echo 'https://departures.sussexmews.co.uk' | sudo tee /boot/fullpageos.txt > /dev/null",
    dag=dag,
)

reboot = SSHOperator(
    task_id="reboot-server",
    ssh_conn_id=get_server_conn_id(),
    command="sudo shutdown -r",
    dag=dag,
)

