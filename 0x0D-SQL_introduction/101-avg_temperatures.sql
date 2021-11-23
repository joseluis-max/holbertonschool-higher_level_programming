-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, COUNT(value)
AS avg_temp
FROM temperatures 
GROUP BY value 
ORDER BY value DESC;