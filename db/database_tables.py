tables = [
    'users',
    'parties',
    'offices',
    'revoked_tokens',
    'candidates',
    'votes'
]

create_table_queries = [
    """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY NOT NULL,
        firstname VARCHAR(250) NOT NULL,
        lastname VARCHAR(250) NOT NULL,
        othername VARCHAR(250) NULL,
        password VARCHAR(250) NOT NULL,
        phonenumber VARCHAR(250) NOT NULL,
        email VARCHAR(250) NOT NULL,
        passporturl VARCHAR(250) NULL,
        isadmin BOOLEAN DEFAULT FALSE,
        ispolitician BOOLEAN DEFAULT FALSE
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS parties (
        id serial PRIMARY KEY NOT NULL,
        name VARCHAR(20) NOT NULL,
        hqaddress VARCHAR(24) NOT NULL, 
        logourl VARCHAR(256) NULL
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS offices (
        id serial PRIMARY KEY NOT NULL,
        type VARCHAR(250) NOT NULL,
        name VARCHAR(250) NOT NULL 
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS candidates (
        id SERIAL PRIMARY KEY NOT NULL,
        office INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (office) REFERENCES offices(id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS votes (
        id SERIAL PRIMARY KEY NOT NULL,
        office INTEGER NOT NULL,
        candidate INTEGER NOT NULL,
        voter INTEGER NOT NULL,
        FOREIGN KEY (office) REFERENCES offices(id) ON DELETE CASCADE,
        FOREIGN KEY (candidate) REFERENCES candidates(id) ON DELETE CASCADE,
        FOREIGN KEY (voter) REFERENCES users(id) ON DELETE CASCADE
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS revoked_tokens (
        id SERIAL PRIMARY KEY NOT NULL,
        jti VARCHAR NOT NULL
    )
    """
]
