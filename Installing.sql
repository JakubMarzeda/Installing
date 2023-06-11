--USE [master]
--GO

--DROP DATABASE IF EXISTS [Installing]
--GO

--CREATE DATABASE [Installing]
--GO

--USE [Installing]
--GO
--CREATE TABLE [User](
--	Id INT IDENTITY(1, 1),
--	[Name] NVARCHAR(100) NOT NULL,
--	Lastname NVARCHAR(100) NOT NULL,
--	Email NVARCHAR(100) UNIQUE NOT NULL,
--	[Password] NVARCHAR(100) CHECK(LEN([Password]) > 6) NOT NULL,
--	CONSTRAINT PK_User_Id PRIMARY KEY (Id)
--)
--CREATE TABLE UserProgress(
--	Id INT IDENTITY(1, 1),
--	UserId INT NOT NULL,
--	SumGoodAnswer INT NOT NULL,
--	CountSession INT NOT NULL,
--	CONSTRAINT PK_UserProgress_Id PRIMARY KEY(Id),
--	CONSTRAINT FK_UserProgress_UserId FOREIGN KEY (UserId) REFERENCES [User](Id)
--)
--CREATE TABLE Word(
--	Id INT IDENTITY(1, 1),
--	PolishWord NVARCHAR(100) NOT NULL,
--	EnglishWord NVARCHAR(100) NOT NULL,
--	SentenceWithGap NVARCHAR(255) NOT NULL,
--	SentenceWithoutGap NVARCHAR(255) NOT NULL,
--	CONSTRAINT PK_Word_Id PRIMARY KEY (Id)
--)

--INSERT INTO Word(PolishWord, EnglishWord, SentenceWithGap, SentenceWithoutGap)
--	VALUES
--		('kot', 'cat', 'The ___ is chasing a mouse.', 'The cat is chasing a mouse.'),
--		('pies', 'dog', 'The ___ is barking loudly.', 'The dog is barking loudly.'),
--		('dom', 'house', 'I love my cozy ____.', 'I love my cozy house.'),
--		('jab³ko', 'apple', 'She took a bite of the juicy _____.', 'She took a bite of the juicy apple.'),
--		('samochód', 'car', 'He drove his new ____ with excitement.', 'He drove his new car with excitement.'),
--		('telefon', 'phone', 'I received an important call on my ______.', 'I received an important call on my phone.'),
--		('kawa', 'coffee', 'I start my day with a cup of strong ______.', 'I start my day with a cup of strong coffee.'),
--		('ksi¹¿ka', 'book', 'She lost herself in the pages of a captivating _____.', 'She lost herself in the pages of a captivating book.'),
--		('kwiat', 'flower', 'He gave her a beautiful bouquet of _____.', 'He gave her a beautiful bouquet of flowers.'),
--		('okno', 'window', 'She looked out the ____ and admired the view.', 'She looked out the window and admired the view.'),
--		('drzewo', 'tree', 'The ____ provided shade on a hot summer day.', 'The tree provided shade on a hot summer day.'),
--		('woda', 'water', 'She drank a glass of cold ____ to quench her thirst.', 'She drank a glass of cold water to quench her thirst.'),
--		('s³oñce', 'sun', 'The ____ shone brightly in the clear blue sky.', 'The sun shone brightly in the clear blue sky.'),
--		('mleko', 'milk', 'He poured a splash of ____ into his cereal bowl.', 'He poured a splash of milk into his cereal bowl.'),
--		('mi³oœæ', 'love', 'Their ____ for each other was evident in every gesture.', 'Their love for each other was evident in every gesture.'),
--		('serce', 'heart', 'Her ____ skipped a beat when she saw him.', 'Her heart skipped a beat when she saw him.'),
--		('muzyka', 'music', 'They danced to the rhythm of the lively _____.', 'They danced to the rhythm of the lively music.'),
--		('wiatr', 'wind', 'The ____ blew through her hair as she stood on the hill.', 'The wind blew through her hair as she stood on the hill.'),
--		('chmura', 'cloud', 'The _____ floated across the sky.', 'The cloud floated across the sky.'),
--		('lato', 'summer', 'I love spending my _____ vacation at the beach.', 'I love spending my summer vacation at the beach.'),
--		('zima', 'winter', 'They built a snowman during the _____.', 'They built a snowman during the winter.'),
--		('wiosna', 'spring', 'The _____ brings blooming flowers and warm weather.', 'The spring brings blooming flowers and warm weather.'),
--		('jesieñ', 'autumn', 'The leaves change color in _____.', 'The leaves change color in autumn.'),
--		('kobieta', 'woman', 'The _____ walked gracefully down the street.', 'The woman walked gracefully down the street.'),
--		('mê¿czyzna', 'man', 'The _____ wore a suit and tie.', 'The man wore a suit and tie.'),
--		('rodzina', 'family', 'She spent quality time with her _____.', 'She spent quality time with her family.'),
--		('rodzina', 'family', 'She spent quality time with her _____.', 'She spent quality time with her family.'),
--		('przyjaciel', 'friend', 'He shared his secrets with his _____.', 'He shared his secrets with his friend.'),
--		('praca', 'work', 'She stayed late at _____ to finish the project.', 'She stayed late at work to finish the project.'),
--		('szko³a', 'school', 'The children learned new things at _____.', 'The children learned new things at school.'),
--		('pieni¹dze', 'money', 'He saved up enough _____ to buy a new car.', 'He saved up enough money to buy a new car.')

--SELECT Email, SumGoodAnswer, CountSession, ROUND(CAST(SumGoodAnswer AS decimal) / CountSession, 2) AS [Avarage good answer] FROM [User] U INNER JOIN UserProgress US
--ON U.Id = US.UserId

--SELECT * FROM [User]

--SELECT * FROM UserProgress

--INSERT INTO UserProgress(UserId, SumGoodAnswer, CountSession) VALUES((SELECT Id FROM [User] WHERE Email = 'jakub.marzeda11@gmail.com'), 17, 1)
