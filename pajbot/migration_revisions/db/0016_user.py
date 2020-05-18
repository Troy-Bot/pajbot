import logging

log = logging.getLogger("pajbot")


def up(cursor, bot):
    cursor.execute('ALTER TABLE "user" ADD COLUMN tier INTEGER NOT NULL DEFAULT 0')
