from app.core.logger import get_logger

logger = get_logger("TEST_LOGGER")

logger.info("This is an INFO log")
logger.warning("This is a WARNING log")
logger.error("This is an ERROR log")
