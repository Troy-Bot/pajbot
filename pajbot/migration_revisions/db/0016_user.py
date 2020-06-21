import logging

log = logging.getLogger("pajbot")


def up(cursor, bot):
    cursor.execute('ALTER TABLE "user" ADD COLUMN IF NOT EXISTS tier INTEGER NOT NULL DEFAULT 0')
    cursor.execute('ALTER TABLE "user" ADD COLUMN IF NOT EXISTS founder BOOLEAN NOT NULL DEFAULT FALSE')
    cursor.execute('ALTER TABLE "user" ADD COLUMN IF NOT EXISTS vip BOOLEAN NOT NULL DEFAULT FALSE')
