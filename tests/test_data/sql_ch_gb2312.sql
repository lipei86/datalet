SELECT name��
	CASE sex 
		WHEN 0 THEN '��'
		WHEN 1 THEN 'Ů'
		ELSE '���'
	END AS sex_ch_name
FROM��users