from kidneyTumorDetection.config.configuration import ConfigurationManager
from kidneyTumorDetection.components.prepare_base_model import PrepareBaseModel
from kidneyTumorDetection import logger


STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        parepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        parepare_base_model.get_base_model()
        parepare_base_model.update_base_model()
    


try:
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()
except Exception as e:
    raise e