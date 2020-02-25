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

	@classmethod
	def search_domain(cls, domain, active_test=True):
		has_classifier = False
		for d in domain:
			if d[0].lower() == 'classifier' and d[1] == '=':
				has_classifier = True
		if not has_classifier:
			#TODO: Use the tryond.conf file to store the default ICD classifier
			domain.append(['classifier', '=', 'ICD10'])			
		(table, expression) = \
			super(baseHealth.Pathology, cls).search_domain(
				domain, active_test)
		return table, expression

	@classmethod
	def default_classifier():
		return 'ICD10'

class PathologyCategory(baseHealth.PathologyCategory):
    __name__ = 'gnuhealth.pathology.category'
    classifier = fields.Char('classifier')

    @classmethod
    def __setup__(cls):
        super(PathologyCategory, cls).__setup__()

#TODO: Remove Deprecations
HealthIcd11 = Pathology
Category = PathologyCategory