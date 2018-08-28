INSERT INTO delivery_order_status (delivery_id, status) VALUES
    (1, 'd'),
    (2, 'd'),
    (3, 't'),
    (4, 't'),
    (5, 't'),
    (6, 't'),
    (7, 't'),
    (8, 'f'),
    (9, 'f'),
    (10, 'f'),
    (11, 'f')
;

INSERT INTO dispatched (delivery_id, dispatched_at) VALUES
    (1, '2018-08-01 22:25:12'),
    (2, '2018-08-02 14:45:18')
;

INSERT INTO in_transit(delivery_id, location) VALUES
    (3, 'at (41.3870° N, 2.1700° E)'),
    (4, 'at (41.3870° N, 2.1700° E)'),
    (5, 'at (41.3870° N, 2.1700° E)'),
    (6, 'at (41.3870° N, 2.1700° E)'),
    (7, 'at (41.3870° N, 2.1700° E)')
;

INSERT INTO finished (delivery_id, delivered_at) VALUES
    (8, '2018-08-01 22:25:12'),
    (9, '2018-08-01 22:25:12'),
    (10, '2018-08-01 22:25:12'),
    (11, '2018-08-01 22:25:12')
;
