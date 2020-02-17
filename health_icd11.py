from trytond.pool import Pool
from trytond.model import ModelView, ModelSQL, fields
from trytond.modules.health import health as baseHealth

class Pathology(baseHealth.Pathology):
	__name__ = 'gnuhealth.pathology'
	classifier = fields.Char('classifier')
	active = fields.Boolean('active')

	@classmethod
	def __setup__(cls):
		super(Pathology, cls).__setup__()


class PathologyCategory(baseHealth.PathologyCategory):
    __name__ = 'gnuhealth.pathology.category'
    classifier = fields.Char('classifier')

    @classmethod
    def __setup__(cls):
        super(PathologyCategory, cls).__setup__()