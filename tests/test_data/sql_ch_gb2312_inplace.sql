SELECT name，
	CASE sex 
		WHEN 0 THEN '男'
		WHEN 1 THEN '女'
		ELSE '你猜'
	END AS sex_ch_name
FROM　users