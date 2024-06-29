USE hbnb_dev_db;

-- Create states table
CREATE TABLE IF NOT EXISTS states (
    id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    PRIMARY KEY (id)
);

-- Create cities table
CREATE TABLE IF NOT EXISTS cities (
    id VARCHAR(60) NOT NULL,
    state_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(60) NOT NULL,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    PRIMARY KEY (id)
);

-- Create places table
CREATE TABLE IF NOT EXISTS places (
    id VARCHAR(60) NOT NULL,
    city_id VARCHAR(60) NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    number_rooms INT NOT NULL DEFAULT 0,
    number_bathrooms INT NOT NULL DEFAULT 0,
    max_guest INT NOT NULL DEFAULT 0,
    price_by_night INT NOT NULL DEFAULT 0,
    latitude FLOAT,
    longitude FLOAT,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create reviews table
CREATE TABLE reviews (
    id VARCHAR(60) NOT NULL PRIMARY KEY,    
    place_id VARCHAR(60) NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    text TEXT,
    rating FLOAT,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    FOREIGN KEY (place_id) REFERENCES places(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create amenities table
CREATE TABLE amenities (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
        
    
);
