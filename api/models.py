from datetime import date
from mongoengine import Document, IntField, DateTimeField, StringField, \
    EmailField, ReferenceField, BooleanField, EmbeddedDocumentField, \
    ListField, EmbeddedDocument, queryset_manager


class User(Document):
    email = EmailField(required=True)
    name = StringField(max_length=255, required=True)
    surname = StringField(max_length=255, required=True)


class Measurement(Document):
    MAX_SYS = 130
    MAX_DIA = 85
    MAX_PUL = 100

    sys = IntField(min_value=0, max_value=200, required=True)
    dia = IntField(min_value=0, max_value=200, required=True)
    pul = IntField(min_value=0, max_value=200, required=True)
    created = DateTimeField(default=date.today, unique=True)
    user = ReferenceField(User, required=True)

    def to_dict(self):
        return {
            'id': str(self.id),
            'sys': self.sys,
            'dia': self.dia,
            'pul': self.pul,
            'created': self.created.strftime("%Y-%m-%d"),
            'user': str(self.user.id)
        }

    def is_ok(self):
        return not (self.sys > self.MAX_SYS or self.dia > self.MAX_DIA or self.pul > self.MAX_PUL)

    @queryset_manager
    def latest(doc_cls, queryset):  # pylint: disable=no-self-argument
        """ Returns the last 10 measurements """
        return queryset.order_by('-created').limit(10)

class MeasurementValue(EmbeddedDocument):
    sys = IntField(min_value=0, max_value=200, required=True)
    dia = IntField(min_value=0, max_value=200, required=True)
    pul = IntField(min_value=0, max_value=200, required=True)
    date = DateTimeField(default=date.today, unique=True)
    ok = BooleanField(required=True, default=True)

    def to_dict(self):
        return {
            'sys': self.sys,
            'dia': self.dia,
            'pul': self.pul,
            'date': self.date.strftime("%Y-%m-%d"),
            'ok': self.ok
        }


class Report(Document):
    period = StringField(max_length=255, required=True)
    user = ReferenceField(User, required=True, unique_with='period')
    values = ListField(EmbeddedDocumentField(MeasurementValue))

    def to_dict(self):
        data = []
        for measurement in self.values:
            data.append(measurement.to_dict())

        return {
            'id': str(self.id),
            'user': str(self.user.id),
            'period': self.period,
            'values': data
        }
