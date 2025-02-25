from datetime import datetime
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook
import requests

CSV_URL = Variable.get("BILLS_SPREADSHEET_CSV_URL")
EMAIL_CREDENTIALS = BaseHook.get_connection("sussexmews-email")
HOUSE_EMAILS = Variable.get("HOUSE_EMAILS", deserialize_json=True)


def send_email(email: str, balance: float):
    subject = "Sussex Mews Bill Reminder"
    sender_email = EMAIL_CREDENTIALS.login
    sender_name = "Sussex Mews Bill Reminder"
    recipients = list(set([email, HOUSE_EMAILS["will"]]))
    password = EMAIL_CREDENTIALS.password

    msg = MIMEMultipart("related")
    msg["Subject"] = subject
    msg["From"] = f"{sender_name} <{sender_email}>"
    msg["To"] = ", ".join(recipients)
    msg["Cc"] = HOUSE_EMAILS["will"]

    with open("/data/bills-notifier/email.html", "r") as f:
        html = MIMEText(f.read().replace("__balance__", f"{balance * -1:.2f}"), "html")
        msg.attach(html)

    with open("/data/bills-notifier/reminder.gif", "rb") as f:
        gif = MIMEImage(f.read())

    gif.add_header("Content-ID", "<image>")
    msg.attach(gif)

    with smtplib.SMTP_SSL(
        EMAIL_CREDENTIALS.host, EMAIL_CREDENTIALS.port
    ) as smtp_server:
        smtp_server.login(sender_email, password)
        smtp_server.sendmail(sender_email, recipients, msg.as_string())

    print("Message sent!")


def get_balances() -> dict[str, float]:
    # get data
    response = requests.get(CSV_URL)
    response.raise_for_status()

    # extract balances
    data = list(csv.reader(response.iter_lines(decode_unicode=True)))
    hattie, will, oliver = [
        float(x.replace("£", "").replace(",", "")) for x in data[1][-4:-1]
    ]

    return {
        "hattie": {"balance": hattie, "email": HOUSE_EMAILS["hattie"]},
        "will": {"balance": will, "email": HOUSE_EMAILS["will"]},
        "oliver": {"balance": oliver, "email": HOUSE_EMAILS["oliver"]},
    }


def main() -> None:
    balances = get_balances()

    for person, info in balances.items():
        if info["balance"] < 0:
            send_email(info["email"], info["balance"])


dag = DAG(
    "bills_notifier",
    default_args={
        "owner": "will",
        "retries": 0,
    },
    description="Notifies users when their bill balance goes negative.",
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
)


notify = PythonOperator(
    task_id="notify",
    python_callable=main,
    dag=dag,
)
