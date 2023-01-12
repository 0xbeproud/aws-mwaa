import re


class SparkAdditionalOption:
    RE_JOB_NAME = re.compile('.*?([^.]+)$')

    def __init__(self,
                 spark_class: str,
                 jar: str,
                 max_app_attempts: str = "1",
                 ):
        self.jar = jar
        self.spark_class = spark_class
        self.max_app_attempts = max_app_attempts

    def get_step_name(self):
        return self.RE_JOB_NAME.match(self.spark_class)[1]

    def get_spark_opts(self):
        return [
            "--conf", "spark.dynamicAllocation.enabled=false",
            "--conf", "spark.serializer=org.apache.spark.serializer.KryoSerializer",
            "--conf", "spark.kryoserializer.buffer.max=128m",
            "--conf", f"spark.yarn.maxAppAttempts={self.max_app_attempts}",
        ]

    def get_job_opts(self):
        return [
            "--properties-file", "/etc/spark/conf/spark-defaults.conf",
            "--name", f"{self.get_step_name()}",
            "--class", f"{self.spark_class}",
            f"{self.jar}"
        ]
