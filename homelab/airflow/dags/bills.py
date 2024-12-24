from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

csv_url = "https://docs.google.com/spreadsheets/d/18tXZh0ogEt14yv3SnQuM2bgpLD0QgOvewrul2WCjlRA/gviz/tq?tqx=out:csv&sheet=MonzoBillsPot"
html_url = "https://docs.google.com/spreadsheets/d/18tXZh0ogEt14yv3SnQuM2bgpLD0QgOvewrul2WCjlRA/gviz/tq?tqx=out:html&sheet=MonzoBillsPot"


dag = DAG(
    "bills_history_tracker",
    default_args={
        "owner": "will",
        "retries": 0,
    },
    description="A tool to track",
    schedule_interval="@daily",
    start_date=datetime(2024, 12, 23),
    catchup=False,
)

make_folder_if_not_exists = BashOperator(
    task_id="make-folder",
    bash_command="mkdir -p /data/bills",
    dag=dag,
)

git_init = BashOperator(
    task_id="init-git-repo",
    bash_command="cd /data/bills && git init",
    dag=dag,
)

download_latest_csv_file = BashOperator(
    task_id="download-csv",
    bash_command=f"""cd /data/bills && curl -o bills.csv "{csv_url}" """,
    dag=dag,
)

download_latest_html_file = BashOperator(
    task_id="download-html",
    bash_command=f"""cd /data/bills && curl -o bills.html "{html_url}" """,
    dag=dag,
)

git_add = BashOperator(
    task_id="stage-file",
    bash_command="cd /data/bills && git add bills.csv bills.html",
    dag=dag,
)

git_commit = BashOperator(
    task_id="commit-file",
    bash_command="""cd /data/bills && git diff-index --quiet HEAD || git commit -m "daily airflow commit" """,
    dag=dag,
)

make_folder_if_not_exists >> git_init >> [download_latest_csv_file, download_latest_html_file] >> git_add >> git_commit