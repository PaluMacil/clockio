import psycopg2
import os

conn = psycopg2.connect(os.getenv('DB_ALARM_OWNER'))

cur = conn.cursor()
cur.execute('SELECT * FROM alarm.alarm')
alarm = cur.fetchone()
print(alarm)

# http://hashrocket.com/blog/posts/faster-json-generation-with-postgresql
# http://www.postgresql.org/docs/9.4/static/plpgsql-statements.html

# Install PG Admin Windows
# https://www.linode.com/docs/databases/postgresql/pgadmin-windows

# PG Set default search path
# http://stackoverflow.com/questions/2875610/postgresql-schema-path-permanently#2875610

# PG auth types
# http://www.postgresql.org/docs/9.0/static/auth-methods.html

# PG keywords
# http://www.postgresql.org/docs/current/static/sql-keywords-appendix.html

# Working with dates and times
# http://www.postgresguide.com/tips/dates.html
