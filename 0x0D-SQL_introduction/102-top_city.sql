-- Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT TOP 3 city
FROM temperatures
WHERE month = 7 or month = 8 
ORDER BY value DESC;