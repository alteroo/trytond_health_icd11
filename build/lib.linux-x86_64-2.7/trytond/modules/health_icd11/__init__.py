# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from .health_icd11 import *

def register():
    """Registers classes to tryton's pool"""
    Pool.register(
    	HealthIcd11,
      Category,
		 module='health_icd11',
		type_='model')

    Pool.register(module='health_icd11',type_="wizard")

    Pool.register(module='health_icd11',type_="report")