from tdata import local
import jaqs.util as jutil
from .models import Company, Index, Fund, Concept, Industry, Product


def create_company_nodes():
    companies = local.query_stock_table()[[
        'list_date', 'market', 'name', 'symbol'
    ]]
    companies['list_date'] = companies['list_date'].apply(
        jutil.convert_int_to_datetime)
    Company.create_or_update(*companies.to_dict('records'))
