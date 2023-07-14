from datetime import date
import factory
from factory.fuzzy import FuzzyDate


class RamFactory(factory.Factory):

    class Meta:
        """Persistent class for factory"""
        model = Account

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    email = factory.Faker("email")
    address = factory.Faker("address")
    phone_number = factory.Faker("phone_number")
    date_joined = FuzzyDate(date(2008, 1, 1))