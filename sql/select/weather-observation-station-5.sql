(
    SELECT City, LENGTH(City)
    FROM Station
    ORDER BY LENGTH(City) ASC, City
    LIMIT 1
) UNION (
    SELECT City, LENGTH(City)
    FROM Station
    ORDER BY LENGTH(City) DESC, City 
    LIMIT 1
);
