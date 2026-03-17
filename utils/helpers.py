import logging

logger = logging.getLogger(__name__)

def log_exception(exception):
    logger.error(exception)