from datetime import date
from mongoengine import Document, IntField, DateTimeField, StringField, \
    EmailField, ReferenceField


class User(Document):
    email = EmailField(required=True)
    name = StringField(max_length=255, required=True)
    surname = StringField(max_length=255, required=True)


class Measurement(Document):
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
