 /** DB schema for test **/

CREATE TABLE delivery_order_status (
    delivery_id SERIAL NOT NULL PRIMARY KEY,
    status CHAR(1)   -- 'd', 't', 'f'
);


CREATE TABLE dispatched (
    delivery_id INTEGER NOT NULL PRIMARY KEY REFERENCES delivery_order_status(delivery_id),
    dispatched_at TIMESTAMP WITH TIME ZONE
);


CREATE TABLE in_transit (
    delivery_id INTEGER NOT NULL PRIMARY KEY REFERENCES delivery_order_status(delivery_id),
    location VARCHAR(200)
);


CREATE TABLE finished (
    delivery_id INTEGER NOT NULL PRIMARY KEY REFERENCES delivery_order_status(delivery_id),
    delivered_at TIMESTAMP WITH TIME ZONE
);
