from trytond.pool import Pool
from trytond.model import ModelView, ModelSQL, fields
from trytond.modules.health.health import PathologyCategory, Pathology

class HealthIcd11(Pathology):
	'Health ICD 11'
	__name__ = 'gnuhealth.pathology'
	classifier = fields.Char('classifier')
	active = fields.Boolean('active')

	@classmethod
	def __setup__(cls):
		super(HealthIcd11, cls).__setup__()


class Category(ModelSQL, ModelView):
    'ICD 11 Categories'
    __name__ = 'gnuhealth.pathology.category'
    classifier = fields.Char('classifier')
    name = fields.Char('Category Name', required=True, translate=True)
    parent = fields.Many2One('gnuhealth.pathology.category','Parent Category',select=True)
    childs = fields.One2Many('gnuhealth.pathology.category','parent','Children Category')

    # @classmethod
    # def __setup__(cls):
    #     super(Category, cls).__setup__()
    #     cls._order.insert(0, ('name', 'ASC'))

    @classmethod
    def validate(cls, categories):
        super(Category, cls).validate(categories)
        cls.check_recursion(categories, rec_name='name')

    def get_rec_name(self, name):
        if self.parent:
            return self.parent.get_rec_name(name) + ' / ' + self.name
        else:
            return self.name

    @classmethod
    def __setup__(cls):
        super(Category, cls).__setup__()
        # cls._sql_constraints += [
        #     ('name_uniq', 'UNIQUE(name)',
        #     'The category name must be unique'),
        # ]