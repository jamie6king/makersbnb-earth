DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS spaces CASCADE;
DROP TABLE IF EXISTS availability;
DROP TABLE IF EXISTS booking_requests;


CREATE TABLE users (

    id SERIAL PRIMARY KEY,

    name text,
    email text,
    phone_number text,
    password text
);

CREATE TABLE spaces (

    id SERIAL PRIMARY KEY,

    name text,
    description text,
    price float,
    picture_url text,

    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

CREATE TABLE availability (

    id SERIAL PRIMARY KEY,

    start_date date,
    end_date date,

    space_id int,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade
);

CREATE TABLE booking_requests (

    customer_id int,
    constraint fk_customer foreign key(customer_id)
        references users(id)
        on delete cascade,

    owner_id int,
    constraint fk_owner foreign key(owner_id)
        references users(id)
        on delete cascade,

    space_id int,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade,

    start_date date,
    end_date date,

    accepted boolean,

    PRIMARY KEY (space_id, start_date, end_date)

);