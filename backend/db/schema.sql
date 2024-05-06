-- Here is the diagram for the db.
-- https://app.eraser.io/workspace/UGWcsZHI5LcDLqLktR72?origin=share
CREATE DATABASE user_authentication;

USE user_authentication
GO

CREATE SCHEMA LoginSchema
GO
CREATE TABLE LoginSchema.Users (
	user_id int PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	email varchar(100),
	isEmpty BIT DEFAULT 1
);

CREATE TABLE LoginSchema.UserLogin (
	login_id int PRIMARY KEY,
	user_id int, --FK
	login_name varchar(20),
	hashed_password varchar(250), --stores the hashed password for verification
	password_salt varchar(100), --stores the salt for verification
	isEmpty BIT DEFAULT 1,
	FOREIGN KEY (user_id) REFERENCES LoginSchema.Users(user_id) --1-to-1 relation
);
