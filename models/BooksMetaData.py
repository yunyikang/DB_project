import mongoengine

class BookMetaData(mongoengine.Document):
    asin = mongoengine.StringField(required=True)
    imUrl = mongoengine.StringField(required=True)
    salesRank = mongoengine.StringField(required=True)
    title = mongoengine.StringField(required=False)
    related = mongoengine.DictField()
    categories = mongoengine.ListField(required=True)
    description = mongoengine.StringField(required=True)
    price = mongoengine.FloatField(required=False)
    text = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'books_metadata',
        'strict': False,
    }

    def serialize(self):
        return {
            'asin': self.asin,
            'imUrl': self.imUrl,
            'salesRank': self.salesRank,
            'title': self.text,
            'related': self.related,
            'categories': self.categories,
            'description': self.description,
            'price': self.price
        }