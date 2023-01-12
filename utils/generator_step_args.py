import json

from utils.spark_steps_option import SparkStepsOption

step_option = SparkStepsOption(
    phase="prod",
    chain="cypress",
    spark_class="io.krosslab.apps.dump.DumpDBSignatures",
    jar="s3://krosslab-prod-spark/jars/juen/20221219_13/krosslab-spark-20221219_135704.jar",
    # driver_cores="1",
    # driver_memory="2g",
    # executor_cores="1",
    # executor_memory="1g",
    # num_executors="2",
    # max_attempts="1",
)
print(json.dumps(step_option.get_spark_step(), indent=4))
# clipboard.copy(json.dumps(step_option.get_spark_step(), indent=4))
