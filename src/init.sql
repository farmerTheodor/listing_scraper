CREATE Table listings (
    id SERIAL NOT NULL PRIMARY KEY,
    query_id INT,
    item_type_id VARCHAR(4),
    name_of_listing VARCHAR(200),
    date_of_listing DATE,
    price FLOAT,
    lat FLOAT,
    lon FLOAT,
    details TEXT,
    link TEXT
);

CREATE Table query (
    query_id SERIAL NOT NULL PRIMARY KEY,
    query_string VARCHAR(400)
)