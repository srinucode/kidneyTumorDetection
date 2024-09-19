from kidneyTumorDetection import logger
from kidneyTumorDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidneyTumorDetection.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Prepare base model"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e

