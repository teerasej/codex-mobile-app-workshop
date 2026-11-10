-- Training database only. Run manually through the seed script, not at API startup.
CREATE TABLE IF NOT EXISTS users (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username text NOT NULL UNIQUE,
    password_hash text NOT NULL
);
CREATE TABLE IF NOT EXISTS service_requests (
    id uuid PRIMARY KEY,
    title text NOT NULL CHECK (char_length(btrim(title)) BETWEEN 5 AND 100),
    description text NOT NULL CHECK (char_length(btrim(description)) BETWEEN 10 AND 500),
    category text NOT NULL CHECK (category IN ('it', 'facility', 'equipment')),
    status text NOT NULL DEFAULT 'new' CHECK (status IN ('new', 'in_progress', 'done')),
    owner_username text NOT NULL REFERENCES users(username),
    created_at timestamptz NOT NULL DEFAULT now()
);
