""" Peewee migrations. """

import datetime as dt
import peewee as pw


def migrate(migrator, app, database):
    """ Write your migrations here.

    > migrator.create_table(table_name, fields_dict)
    > migrator.drop_table(table_name, cascade=True)
    > migrator.add_column(table_name, column_name, field)
    > migrator.drop_column(table_name, column_name, field, cascade=True)
    > migrator.rename_column(table_name, old_column_name, new_column_name)
    > migrator.rename_table(old_table_name, new_table_name)
    > migrator.add_index(table_name, columns, unique=False)
    > migrator.drop_index(table_name, index_name)
    > migrator.add_not_null(table_name, column_name)
    > migrator.drop_not_null(table_name, column_name)

    """
    from mixer.backend.peewee import Mixer

    mixer = Mixer(commit=True)
    mixer.blend('example.models.User', name='user')