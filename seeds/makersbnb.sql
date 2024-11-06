DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS spaces CASCADE;
DROP TABLE IF EXISTS availability;
DROP TABLE IF EXISTS booking_requests;


CREATE TABLE users (

    id SERIAL PRIMARY KEY,

    name text,
    email text,
    phone_number text,
    hashed_password text
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

INSERT INTO users (
    name,
    email,
    phone_number,
    hashed_password
) 
  VALUES 
        ('Alice Johnson', 'alice.johnson@example.com', '+44 12345678900', '0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e'),
        ('Bob Smith', 'bob.smith@example.com', '+44 12345678901', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4'),
        ('John Doe', 'john.doe@example.com', '+44 12345678900', '0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e')

