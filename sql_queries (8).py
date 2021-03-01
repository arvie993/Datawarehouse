import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE staging_events IF EXISTS"
staging_songs_table_drop = "DROP TABLE staging_events IF EXISTS"
songplay_table_drop = "DROP TABLE staging_events IF EXISTS"
user_table_drop = "DROP TABLE staging_events IF EXISTS"
song_table_drop = "DROP TABLE staging_events IF EXISTS"
artist_table_drop = "DROP TABLE staging_events IF EXISTS"
time_table_drop = "DROP TABLE staging_events IF EXISTS"

# CREATE TABLES

staging_events_table_create= ("""
    CREATE TABLE IF NOT EXISTS staging_events(
    artist varchar,
    auth varchar,
    firstName varchar,
    gender varchar,
    ItemInSession varchar,
    lastName varchar,
    length float,
    level varchar,
    location varchar,
    method varchar,
    page varchar,
    registration varchar,
    sessionId varchar,
    song varchar,
    status varchar,
    ts timestamp,
    userAgent varchar,
    userId varchar
    )
""")

staging_songs_table_create = ("""
    CREATE TABLE IF NOT EXISTS staging_songs(
    num_songs int,
    artist_id varchar,
    artist_latitude varchar,
    artist_longitude varchar,
    artist_location varchar,
    artist_name varchar,
    song_id varchar,
    title varchar,
    duration float,
    year int
    )
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays(
    songplay_id varchar,
    start_time timestamp,
    user_id varchar,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id varchar,
    location varchar,
    user_agent varchar
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users(
    user_id varchar,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs(
    song_id varchar,
    title varchar,
    artist_id varchar,
    year int,
    duration timestamp
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists(
    artist_id varchar,
    name varchar,
    location varchar,
    latitude varchar,
    longitude varchar
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time(
    start_time timestamp,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
    )
""")

# STAGING TABLES

staging_events_copy = ("""
COPY staging_events
FROM {}
iam_role {}
FORMAT AS json {}
""").format(config['S3']['LOG_DATA'],config["IAM_ROLE"]["ARN"],config['S3']['LOG_JSONPATH'])

staging_songs_copy = ("""
COPY staging_songs
FROM {}
iam_role AS {}
""").format(config['S3']['SONG_DATA'],config["IAM_ROLE"]["ARN"])

# FINAL TABLES

songplay_table_insert = ("""
  
""")

user_table_insert = ("""
    INSERT INTO users(user_id, first_name, last_name, gender, level)
    SELECT 
""")

song_table_insert = ("""
    INSERT INTO songs(song_id, title, artist_id, year, duration)
    VALUES (%s,%s,%s,%s,%s)
""")

artist_table_insert = ("""
    INSERT INTO artists(artist_id, name, location, latitude, longitude)
    VALUES (%s,%s,%s,%s,%s)
""")

time_table_insert = ("""
    INSERT INTO artists(start_time, hour, day, week, month, year, weekday)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
