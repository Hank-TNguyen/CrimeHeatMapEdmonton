select *  from (
	select 	data.nbh as nbh, coors.lat, coors.lon, data.year, (sum(data.num_incidents)) as num
	from 	crime_data data, coordinates coors 
	where 	data.nbh = coors.nbh and data.year = 2018
	group by data.nbh, data.year
	) as temp
order by num;