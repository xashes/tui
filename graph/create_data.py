from tdata import local
import jaqs.util as jutil
from .models import Company, Index, Fund, Concept, Industry, Product


def create_nodes(df):
    nodes = df.loc[:, ['list_date', 'market', 'name', 'symbol']]
    Index.create_or_update(*nodes.to_dict('records'))
