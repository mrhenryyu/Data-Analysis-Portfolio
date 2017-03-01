# SQL Exercises FROM SQLZOO 
# http://sqlzoo.net/wiki/

# 1 Modify it to show the population of Germany
SELECT population from world
  WHERE name = 'Germany';
  
# 2 Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.
SELECT name, population from world 
  WHERE name in ('Sweden', 'Norway', 'Denmark');
  
# 3 Show the country and the area for countries with an area between 200,000 and 250,000. 
SELECT name, area FROM world
  WHERE area BETWEEN 200000 AND 250000; 
  

