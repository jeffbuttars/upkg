import logging
logger = logging.getLogger('upkg')

import os
import shutil
import datetime
from peewee import *

from conf import settings


def _connect_db():
    """todo: Docstring for _connect_db
    :return:
    :rtype:
    """

    db_file = os.path.join(settings.dbs_path, settings.db_name + ".db")
    logger.debug("db_file is %s", db_file)

    db_dir = os.path.dirname(db_file)
    if not os.path.exists(db_dir):
        shutil.os.makedirs(os.path.dirname(db_file))

    db = SqliteDatabase(db_file)
    db.connect()

    return db
#_connect_db()


_db = _connect_db()


def register_model(mdl):
    """todo: Docstring for register_model

    :param mdl: arg description
    :type mdl: type description
    :return:
    :rtype:
    """

    logger.debug("Creating table for model %s", mdl)
    mdl.create_table(True)

    return mdl
#register_model()


@register_model
class BaseModel(Model):
    class Meta:
        database = _db
    #Meta
#BaseModel


@register_model
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
