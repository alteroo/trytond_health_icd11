# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.health_icd11.tests.test_health_icd11 import suite
except ImportError:
    from .test_health_icd11 import suite

__all__ = ['suite']
