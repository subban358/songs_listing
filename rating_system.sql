-- DDL COMMANDS

CREATE DATABASE RATING;
USE RATING;

CREATE TABLE IF NOT EXISTS USERS (
    USER_ID INT AUTO_INCREMENT PRIMARY KEY,
    USER_NAME VARCHAR(25) NOT NULL UNIQUE,
    FULL_NAME VARCHAR(30) NOT NULL,
    EMAIL VARCHAR(20) UNIQUE,
    PASSWRD VARCHAR(20)
)  ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS SONGS (
    SONG_ID INT AUTO_INCREMENT PRIMARY KEY,
    SONG_NAME VARCHAR(25) NOT NULL UNIQUE,
    GENRE VARCHAR(10) NOT NULL,
    DURATION TIME NOT NULL,
    RELEASE_DATE DATE NOT NULL
)  ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS ARTISTS (
    ARTIST_ID INT AUTO_INCREMENT PRIMARY KEY,
    ARTIST_NAME VARCHAR(25) NOT NULL UNIQUE,
    DOB DATE NOT NULL,
    BIO VARCHAR(100)
)  ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS RELATIONS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    SONG_ID INT NOT NULL,
    ARTIST_ID INT NOT NULL,
    FOREIGN KEY (SONG_ID) REFERENCES SONGS (SONG_ID) ON DELETE CASCADE,
    FOREIGN KEY (ARTIST_ID) REFERENCES ARTISTS (ARTIST_ID) ON DELETE CASCADE   
)  ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS RATINGS (
	RATING_ID INT AUTO_INCREMENT PRIMARY KEY,
    SONG_ID INT NOT NULL,
    USER_ID INT NOT NULL,
    RATING INT NOT NULL,
    FOREIGN KEY (SONG_ID) REFERENCES SONGS (SONG_ID),
    FOREIGN KEY (USER_ID) REFERENCES USERS (USER_ID)
);

-- DML COMMANDS  

INSERT INTO 
    USERS(USER_NAME, FULL_NAME, EMAIL, PASSWRD )
VALUES
    ('Subban358','Subham Banerjee','subham@gmail.com', 'incorrect*007'),
    ('Sourav741','Sourav Mondal','souravmon@gmail.com', 'incorrect*358'),
    ('Satyaki_004','Satyaki Sarkar','sarkar@outlook.com', 'Hero@1998'),
    ('Tamal0101','Tamal Sarkar','tamalsark@gmail.com', 'sarkar010101'),
    ('Riya_26','Riya Das','riyadas26@gmail.com', 'Riya_2000');


INSERT INTO 
    SONGS(SONG_NAME, GENRE, DURATION, RELEASE_DATE )
VALUES
    ('Dil Se','Classical','00:06:30', '1998-04-05'),
    ('My Way','Folk','00:05:30', '2001-07-16'),
    ('Bohemian Raphsody','Pop','00:07:08', '2016-10-25'),
    ('Hotel California','Hard Rock','00:06:38', '2017-11-12'),
    ('Tu Hi Re','Classical','00:04:30', '2005-06-30');
    

INSERT INTO 
    ARTISTS (ARTIST_NAME, DOB, BIO)
VALUES
    ('Elvis','1968-04-05', 'Love to sing and dance'),
	('Pete','1988-12-13', 'Singing is life'),
	('Raheman','1984-10-15', 'Musically unique'),
	('Papon','1979-07-29', 'Living the dreams'),
    ('Arijit','1992-03-02', 'Jazzing to the beats');
    
INSERT INTO 
    RELATIONS (SONG_ID, ARTIST_ID)
VALUES
    (1, 1 ),
	(2, 3 ),
	(1, 3 ),
	(3, 1 ),
    (2, 4 ),
    (4, 2 ),
    (5, 5 ),
    (5, 2 );

INSERT INTO 
    RATINGS (SONG_ID, USER_ID, RATING)
VALUES
    (1, 2, 4),
    (2, 1, 4),
    (3, 1, 3),
    (4, 5, 5),
    (5, 3, 4),
    (1, 3, 4),
    (2, 4, 2),
    (3, 3, 4),
    (4, 1, 4),
    (5, 2, 5);

-- QUERYS 

SELECT * FROM USERS;    
SELECT * FROM SONGS;
SELECT * FROM ARTISTS;
SELECT * FROM RELATIONS;
SELECT * FROM RATINGS;

-- TOP RATED SONGS AND THEIR AVERAGE RATINGS
SELECT S.SONG_NAME, ROUND(AVG(R.RATING), 1) 'Rating' FROM SONGS S 
INNER JOIN RATINGS R 
ON S.SONG_ID = R.SONG_ID
GROUP BY (R.SONG_ID)
ORDER BY Rating DESC;

-- TOP RATED ARTISTS AND THEIR AVERAGE RATINGS

SELECT A.ARTIST_NAME, ROUND(AVG(R.RATING), 1) 'Rating' FROM ARTISTS A 
INNER JOIN RELATIONS RE 
ON A.ARTIST_ID = RE.ARTIST_ID
INNER JOIN RATINGS R
ON RE.SONG_ID = R.SONG_ID
GROUP BY (RE.ARTIST_ID)
ORDER BY Rating DESC;

   
SELECT * FROM ARTISTS A 
INNER JOIN RELATIONS R 
ON A.ARTIST_ID = R.ARTIST_ID 
INNER JOIN SONGS S 
ON S.SONG_ID = R.SONG_ID;
    
    
    
    



