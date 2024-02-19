import os
import logging


from .settings_comon import *
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()
logger.debug('===== >>>>>>  settings_comon  <<<<<<<< ========')

if os.getenv('SETTINGS') == 'local':
    from .settings_local import *
    logger.debug('===== >>>>>>  settings_local  <<<<<<<< ========')
else:
    from .settings_prod import *
    logger.debug('===== >>>>>>  settings_prod  <<<<<<<< ========')
