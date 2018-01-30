SELECT name£¨
	CASE sex 
		WHEN 0 THEN 'ń–'
		WHEN 1 THEN 'Ňģ'
		ELSE 'ń„≤¬'
	END AS sex_ch_name
FROM°°users