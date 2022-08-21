create table implementations 
(
    imp_id varchar,
    imp_name varchar,
    imp_status boolean,
    num_imgs int,
    img_type json,
    constraint imp_id_unique unique (imp_id)
);
