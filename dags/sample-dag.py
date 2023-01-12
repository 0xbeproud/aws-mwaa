from datetime import timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

from sqlalchemy_utils.types.enriched_datetime.pendulum_date import pendulum

# plugins를 제거해야함.
from operators.custom_operator import CustomOperator

## Variables
variables = Variable.get("sample_variable", deserialize_json=True)
value = variables["key"]

default_args = {
    "depends_on_past": False,
    "email": ["logan.beproud@krosslab.io"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
    "catchup": False,
}

## DAG
with DAG(
        dag_id="sample_dag",
        start_date=pendulum.datetime(2023, 1, 10, tz="UTC"),
        schedule_interval="@once",
        default_args=default_args,
) as dag:
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    op1 = BashOperator(task_id='op1', bash_command='echo Hello World 111')
    op2 = BashOperator(task_id='op2', bash_command='echo Hello World 222')
    op3 = BashOperator(task_id='op3', bash_command='echo Hello World 333')

    custom = CustomOperator(task_id='custom', name="CustomOperator")

    start >> op1 >> op2 >> op3 >> custom >> end
