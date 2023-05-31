USE [master]
GO

DROP DATABASE IF EXISTS [Installing]
GO

CREATE DATABASE [Installing]
GO

USE [Installing]
GO
CREATE TABLE [User](
	Id INT IDENTITY(1, 1),
	Name NVARCHAR(100),
	Lastname NVARCHAR(100),
	Email NVARCHAR(100),
	Password NVARCHAR(100),
	CONSTRAINT PK_User_Id PRIMARY KEY (Id)
)
CREATE TABLE Word(
	Id INT IDENTITY(1, 1),
	PolishWord NVARCHAR(100),
	EnglishWord NVARCHAR(100)
)


INSERT INTO Word(PolishWord, EnglishWord)
	VALUES
		('kot', 'cat'),
		('pies', 'dog'),
		('dom', 'house'),
		('jab�ko', 'apple'),
		('samoch�d', 'car'),
		('telefon', 'phone'),
		('kawa', 'coffee'),
		('ksi��ka', 'book'),
		('kwiat', 'flower'),
		('okno', 'window'),
		('drzewo', 'tree'),
		('woda', 'water'),
		('s�o�ce', 'sun'),
		('mleko', 'milk'),
		('mi�o��', 'love'),
		('serce', 'heart'),
		('muzyka', 'music'),
		('wiatr', 'wind'),
		('chmura', 'cloud'),
		('lato', 'summer'),
		('zima', 'winter'),
		('wiosna', 'spring'),
		('jesie�', 'autumn'),
		('kobieta', 'woman'),
		('m�czyzna', 'man'),
		('rodzina', 'family'),
		('przyjaciel', 'friend'),
		('praca', 'work'),
		('szko�a', 'school'),
		('pieni�dze', 'money')
