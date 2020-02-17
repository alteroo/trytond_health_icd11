# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class HealthIcd11TestCase(ModuleTestCase):
    'Test Health Icd11 module'
    module = 'health_icd11'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            HealthIcd11TestCase))
    return suite
