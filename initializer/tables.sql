create table if not exists reading_imgs
(
    read_id varchar,
    img_location varchar 
);

create table if not exists reading_location
(
    read_id varchar,
    latitude varchar,
    longitude varchar
);


create table if not exists readings
(
    read_id varchar,
    user_id varhcar,
    read_imp varchar,
    read_date timestamp,
    read_status boolean,
    constraint read_unique unique (read_id)
);

create table if not exists reading_result
(
    read_id varchar,
    read_result text
);

create table if not exists implementations 
(
    imp_id varchar,
    imp_name varchar,
    imp_status boolean,
    num_imgs int,
    img_type json,
    constraint imp_id_unique unique (imp_id)
);
