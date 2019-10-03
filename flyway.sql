create table if not exists coordinates (
	nbh text primary key,
	lat real not null, 
	lon real not null
	);

create table if not exists mapKeyNBH (
	nbh text primary key,
	key text not null
	);

create table if not exists crime_data (
	nbh text not null,
	crime text not null,
	year integer not null,
	quarter integer not null, 
	month integer not null,
	num_incidents integer not null,
	primary key (nbh, crime, year, quarter, month)
	);

