from utils.spark_additional_option import SparkAdditionalOption


class SparkStepsOption:
    def __init__(self,
                 spark_class: str,
                 jar: str,
                 deploy_mode: str = "cluster",
                 driver_cores: str = "1",
                 driver_memory: str = "2g",
                 executor_cores: str = "1",
                 executor_memory: str = "1g",
                 num_executors: str = "1",
                 max_attempts: str = "1",
                 yarn_queue: str = "root.default",
                 ) -> None:
        self.run_options = SparkAdditionalOption(
            spark_class=spark_class,
            jar=jar,
        )
        self.deploy_mode = deploy_mode
        self.driver_cores = driver_cores
        self.driver_memory = driver_memory
        self.executor_cores = executor_cores
        self.nun_executors = num_executors
        self.executor_memory = executor_memory
        self.max_attempts = max_attempts
        self.yarn_queue = yarn_queue

    def get_spark_step(self):
        args = [
            'spark-submit',
            '--deploy-mode', self.deploy_mode,
            '--driver-cores', str(self.driver_cores),
            '--driver-memory', self.driver_memory,
            '--num-executors', str(self.nun_executors),
            '--executor-cores', str(self.executor_cores),
            '--executor-memory', self.executor_memory,
        ]
        args.extend(self.run_options.get_spark_opts())
        args.extend(self.run_options.get_job_opts())

        return {
            'Name': f"{self.run_options.spark_class}-{self.run_options.phase}-{self.run_options.chain}",
            'ActionOnFailure': 'CONTINUE',
            'HadoopJarStep': {
                'Jar': 'command-runner.jar',
                'Args': args,
            },
        }
