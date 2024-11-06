--- dummy users
INSERT INTO users (name, email, phone_number, hashed_password) VALUES ('Jamie', 'jamie@makers.tech', '01234567890', 'King1234');
INSERT INTO users (name, email, phone_number, hashed_password) VALUES ('Abdirahman', 'abdirahman@makers.tech', '09876543210', 'Aden1234');
INSERT INTO users (name, email, phone_number, hashed_password) VALUES ('Safaa', 'safaa@makers.tech', '05432167890', 'Imran1234');
INSERT INTO users (name, email, phone_number, hashed_password) VALUES ('Kelly', 'kelly@makers.tech', '06789123450', 'Howes1234');
INSERT INTO users (name, email, phone_number, hashed_password) VALUES ('Claire', 'claire@makers.tech', '0987612345', 'Siqi1234');

--- dummy spaces
INSERT INTO spaces (name, description, price, picture_url, user_id) VALUES ('Cozy Cottage', 'A charming cottage in the woods, perfect for a weekend getaway.', 120.00, 'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0', 1);
INSERT INTO spaces (name, description, price, picture_url, user_id) VALUES ('Modern Apartment', 'A stylish apartment in the heart of the city, close to all attractions.', 150.00, 'https://images.unsplash.com/photo-1560185127-6c8c1c1c1c1c', 1);
INSERT INTO spaces (name, description, price, picture_url, user_id) VALUES ('Beachfront Villa', 'Luxurious villa with stunning ocean views and private beach access.', 300.00, 'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0', 2);
INSERT INTO spaces (name, description, price, picture_url, user_id) VALUES ('Rustic Cabin', 'A rustic cabin in the mountains, ideal for hiking and nature lovers.', 100.00, 'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0', 2);
INSERT INTO spaces (name, description, price, picture_url, user_id) VALUES ('Chic Studio', 'A chic studio with a minimalist design, located near trendy cafes.', 90.00, 'https://images.unsplash.com/photo-1560185127-6c8c1c1c1c1c', 4);
INSERT INTO spaces (name, description, price, picture_url, user_id) VALUES ('Family-Friendly Home', 'Spacious home with a backyard, perfect for families with children.', 200.00, 'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0', 5);

--- dummy availability
INSERT INTO availability (start_date, end_date, space_id) VALUES ('2023-10-01', '2023-10-10', 1);
INSERT INTO availability (start_date, end_date, space_id) VALUES ('2023-10-05', '2023-10-15', 2);
INSERT INTO availability (start_date, end_date, space_id) VALUES ('2023-10-12', '2023-10-20', 3);
INSERT INTO availability (start_date, end_date, space_id) VALUES ('2023-10-01', '2023-10-30', 4);
INSERT INTO availability (start_date, end_date, space_id) VALUES ('2023-10-15', '2023-10-25', 5);

--- dummy booking requests
INSERT INTO booking_requests (customer_id, owner_id, space_id, start_date, end_date, accepted) VALUES (1, 1, 1, '2023-10-01', '2023-10-05', true);
INSERT INTO booking_requests (customer_id, owner_id, space_id, start_date, end_date, accepted) VALUES (2, 2, 2, '2023-10-06', '2023-10-10', false);
INSERT INTO booking_requests (customer_id, owner_id, space_id, start_date, end_date, accepted) VALUES (3, 3, 3, '2023-10-12', '2023-10-15', true);
INSERT INTO booking_requests (customer_id, owner_id, space_id, start_date, end_date, accepted) VALUES (4, 4, 4, '2023-10-01', '2023-10-05', false);
INSERT INTO booking_requests (customer_id, owner_id, space_id, start_date, end_date, accepted) VALUES (5, 5, 5, '2023-10-15', '2023-10-20', true);
