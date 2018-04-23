from django.db import models
import neomodel as nm


# Relationship Models
class ConceptRel(nm.StructuredRel):
    updated = nm.DateTimeProperty(default_now=True)
    rating = nm.IntegerProperty()
    relevancy = nm.IntegerProperty()


class ProductRel(nm.StructuredRel):
    updated = nm.DateTimeProperty(default_now=True)
    rating = nm.IntegerProperty()
    contribution = nm.IntegerProperty()


class StakeRel(nm.StructuredRel):
    updated = nm.DateTimeProperty(default_now=True)
    shareholding_ratio = nm.FloatProperty()


# Label Models
class Company(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True, require=True)
    sid = nm.StringProperty(unique_index=True)

    concept = nm.RelationshipTo(
        'Concept', 'RELATED_TO', cardinality=nm.ZeroOrMore, model=ConceptRel)
    industry = nm.RelationshipTo(
        'Industry', 'RELATED_TO', cardinality=nm.ZeroOrMore, model=ConceptRel)
    customer = nm.RelationshipTo(
        'Company', 'SUPPLIES_TO', cardinality=nm.ZeroOrMore)
    product = nm.RelationshipTo('Product', 'PRODUCES', model=ProductRel)


class Fund(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True, require=True)
    rating = nm.IntegerProperty()

    company = nm.RelationshipTo('Company', 'STAKES', model=StakeRel)


class Concept(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True, require=True)
    rating = nm.IntegerProperty()
    heat = nm.IntegerProperty()


class Industry(Concept):
    pass


class Product(nm.StructuredNode):
    pass
