import os
import datetime
from peewee import *

from conf import settings

_db = SqliteDatabase(os.path.join(settings.dbs_path, settings.db_name + ".db"))
_db.connect()


class BaseModel(Model):
    class Meta:
        database = _db
    #Meta
#BaseModel


class BaseTimeModel(BaseModel):
    created = DateTimeField()
    last_update = DateTimeField()

    def create(self, **attrs):
        self.created = datetime.datetime.now()
        super(BaseTimeModel, self).create(**attrs)
    #create()

    def update(self, **update):
        self.last_update = datetime.datetime.now()
        super(BaseTimeModel, self).update(**update)
    #update()
#BaseTimeModel
