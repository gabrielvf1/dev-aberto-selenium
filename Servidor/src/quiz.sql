DROP TABLE IF EXISTS USER;
CREATE TABLE USER(
user TEXT NOT NULL PRIMARY KEY,
pass TEXT NOT NULL,
type TEXT NOT NULL);

DROP TABLE IF EXISTS QUIZ;
CREATE TABLE QUIZ(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
numb INTEGER NOT NULL,
release TEXT NOT NULL,
expire TEXT NOT NULL,
problem TEXT NOT NULL,
tests TEXT NOT NULL,
results TEXT NOT NULL,
diagnosis TEXT NOT NULL);

DROP TABLE IF EXISTS USERQUIZ;
CREATE TABLE USERQUIZ(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
userid TEXT NOT NULL,
quizid INTEGER NOT NULL,
sent TEXT NOT NULL,
answer TEXT NOT NULL,
result TEXT NOT NULL);

Delete from USER;
Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values (1, '2018-08-01','2020-12-31 23:59:59','Exemplo de problema','[[1],[2],[3]]','[0, 0, 0]','["a","b","c"]');
Insert into QUIZ(numb, release, expire, problem, tests, results, diagnosis) values (5, '2018-08-01','2020-12-31 23:59:59','Exemplo de problema','[[1],[2],[3]]','[0, 0, 0]','["a","b","c"]');
