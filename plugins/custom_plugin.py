from airflow.plugins_manager import AirflowPlugin

from operators.custom_operator import CustomOperator


class custom_operator(CustomOperator):
    pass


class custom_plugin(AirflowPlugin):
    name = "custom_plugin"
    operator = [custom_operator]
