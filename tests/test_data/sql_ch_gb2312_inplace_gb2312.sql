SELECT name£¬
	CASE sex 
		WHEN 0 THEN 'ÄÐ'
		WHEN 1 THEN 'Å®'
		ELSE 'Äã²Â'
	END AS sex_ch_name
FROM¡¡users