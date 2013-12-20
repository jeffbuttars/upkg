from peewee import *


class Repo(BaseTimeModel):
    # Full URL that is cloned
    url = CharField(max_length=256)

    # Shortname of repo
    name = CharField(max_length=128)

    # What type of VCS: git, hg, etc..
    vcs = CharField(max_length=64)

    # Last commit id
    last_commit = CharField(max_length=128)
#Repo


class Audit(BaseTimeModel):
    action_choices = (
        ('CLONE', 'Clone'),
        ('UPDATE', 'Update'),
        ('REMOVE', 'Remove'),
        ('STATUS', 'Status'),
        ('ERROR', 'Error'),
    )

    repo = ForeignKeyField(Repo)
    commit = CharField(max_length=128)
    action = CharField(max_length=16)
    message = TextField()
    ctx_id = CharField(max_length=64)
#Audit
