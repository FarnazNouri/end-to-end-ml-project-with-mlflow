from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger
import os


STAGE_NAME = 'Model Evaluation stage'

class ModelEvaluationPipeline:
    def __init__(self):
     pass

    def main(self):

        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()

        os.environ["MLFLOW_TRACKING_URL"] = model_evaluation_config.mlflow_uri
        os.environ["MLFLOW_TRACKING_USERNAME"] = model_evaluation_config.mlflow_username
        os.environ["MLFLOW_TRACKING_PASSWORD"] = model_evaluation_config.mlflow_password

        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
      obj = ModelEvaluationPipeline()
      obj.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx=====================x")
    except Exception as e:
      logger.exception(e)

