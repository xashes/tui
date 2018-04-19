from django.db import models
import neomodel as neo

# Create your models here.
class Book(neo.StructuredNode):
    title = neo.StringProperty(unique_index=True)
    published = neo.DateProperty()

class Worker(neo.StructuredNode):
    uid = neo.UniqueIdProperty()
    name = neo.StringProperty()
    company = neo.StringProperty()
    age = neo.IntegerProperty()
    gender = neo.StringProperty()
