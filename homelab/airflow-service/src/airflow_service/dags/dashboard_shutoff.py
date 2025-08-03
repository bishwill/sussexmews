from pendulum import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.models import Variable


BASE_URL = Variable.get("SUSSEXMEWS_API_BASE_URL")
HEADERS = "-H 'accept: application/json' -H 'Content-Type: application/json'"
DATA = """-d '{"screen": "right"}'"""


dag = DAG(
    "dashboard_shutoff",
    default_args={
        "owner": "will",
        "retries": 0,
    },
    description="Shuts down the Raspberry Pis running the kitchen dashboard.",
    schedule_interval="0 22 * * *",
    start_date=datetime(2025, 1, 1, tz="Europe/London"),
    catchup=False,
)

for screen_side in ("left", "right"):
    task = BashOperator(
        task_id=f"shutoff_{screen_side}_screen",
        bash_command=f"curl --fail -X 'POST' '{BASE_URL}/kitchen-dashboard/shutdown' {HEADERS} {DATA}",
        dag=dag,
    )
