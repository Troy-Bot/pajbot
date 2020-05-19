import logging

log = logging.getLogger("pajbot")


def up(cursor, bot):
    cursor.execute(
        """
    CREATE TABLE songrequest_song_info (
        video_id TEXT PRIMARY KEY NOT NULL,
        title TEXT NOT NULL,
        duration INT NOT NULL,
        default_thumbnail TEXT NOT NULL,
        banned boolean ,
        favourite boolean
    )
    """
    )
    cursor.execute(
        """
    CREATE TABLE songrequest_queue (
        id SERIAL PRIMARY KEY,
        video_id TEXT NOT NULL REFERENCES "songrequest_song_info"(video_id) ON DELETE CASCADE,
        date_added timestamp with time zone DEFAULT NULL,
        skip_after INT,
        requested_by_id TEXT REFERENCES "user"(id) ON DELETE CASCADE,
        date_resumed timestamp with time zone,
        played_for REAL NOT NULL DEFAULT 0
    )
    """
    )
    cursor.execute(
        """
    CREATE TABLE songrequest_history (
        id SERIAL PRIMARY KEY,
        stream_id INT,
        video_id TEXT NOT NULL REFERENCES "songrequest_song_info"(video_id) ON DELETE CASCADE,
        date_finished timestamp with time zone DEFAULT NULL,
        requested_by_id TEXT REFERENCES "user"(id) ON DELETE CASCADE,
        skipped_by_id TEXT REFERENCES "user"(id) ON DELETE CASCADE,
        skip_after INT
    )
    """
    )
