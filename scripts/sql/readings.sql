create table reading_imgs
(
    read_id varchar,
    img_location varchar
);

create table reading_location
(
    read_id varchar,
    latitude varchar,
    longitude varchar
);


create table readings
(
    read_id varchar,
    user_id varhcar,
    read_imp varchar,
    read_date timestamp,
    read_status boolean,
    constraint read_unique unique (read_id)
);

create table reading_result
(
    read_id varchar,
    read_result text
);