import logging
from azbankintro import card_validate, CardValidationException

try:
    card_validate('6280992042433333')
    logging.debug('کارت معتبر است.')     
except CardValidationException:
    logging.debug('کارت نا معتبر است.')
