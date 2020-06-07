SELECT DISTINCT City
FROM Station
WHERE LEFT(City, 1) IN ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U') AND
      RIGHT(City, 1) IN ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U');
