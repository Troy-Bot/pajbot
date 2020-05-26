import logging

log = logging.getLogger("pajbot")


def up(cursor, bot):
    cursor.execute('ALTER TABLE "user" ADD COLUMN IF NOT EXISTS num_paid_timeouts INTEGER NOT NULL DEFAULT 0')
    cursor.execute('DROP MATERIALIZED VIEW user_rank')
    cursor.execute(
        """
    CREATE MATERIALIZED VIEW user_rank AS (
        SELECT
            id as user_id,
            RANK() OVER (ORDER BY points DESC) points_rank,
            RANK() OVER (ORDER BY num_lines DESC) num_lines_rank
            RANK() OVER (ORDER BY num_paid_timeouts DESC) num_paid_timeouts_rank
        FROM "user"
    )
    """
    )
    cursor.execute("CREATE UNIQUE INDEX ON user_rank(user_id)")

