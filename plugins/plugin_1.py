from airflow.plugins_manager import AirflowPlugin

class MyFirstPlugin(AirflowPlugin):
    name = "plugin_1"