import logging


def get_module_logger(module_name):
    logger = logging.getLogger(name=module_name)
    if logger.hasHandlers():
        logger.handlers.clear()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
