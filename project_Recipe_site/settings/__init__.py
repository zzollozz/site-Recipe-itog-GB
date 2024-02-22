import os
import logging


from .settings_comon import *
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()

if os.getenv('SETTINGS') == 'local':
    from .settings_local import *
else:
    from .settings_prod import *
