# Metpy Monday
# 83 - Logging
# https://www.youtube.com/watch?v=5FEHUOXklCI

import logging

logging.basicConfig(filename = 'myapp.log', level = logging.DEBUG)

logging.debug('Application started at 0x6A78F.')
logging.info('Opening model output data file.')
logging.warning('Wind speeds greater than mach 1 found - results may be incorrect.')
logging.error('Cannot calculate vorticity parameters.')
logging.critical('Physics kernel failed.')
