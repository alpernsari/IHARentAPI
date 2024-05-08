from IHAModule.models import IHA
from table import Table
from table.columns import Column

class IHATable(Table):
    id = Column(field='id')
    brand = Column(field='brand')
    model = Column(field='model')
    weight = Column(field='weight')
    category = Column(field='category')
    class Meta:
        model = IHA
