from flask import Flask, render_template, request, redirect, url_for
from flask import session, flash
import sqlite3


# Function to get database connection
def get_db_connection():
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row
        return con
    
# Connect with db
con = sqlite3.connect("database.db")
cur = con.cursor()
# Create "users" table
cur.execute(
    """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL,
        faculty TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        phone_number TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
        )"""
)

# Create "calendar" table
cur.execute(
    """CREATE TABLE IF NOT EXISTS calendar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lecturer TEXT NOT NULL,
        event_title TEXT NOT NULL UNIQUE,
        event_date TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        FOREIGN KEY (lecturer) REFERENCES users(username)
    )"""
)


# Create "appointments" table
cur.execute(
    """CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        booking_id INTEGER NOT NULL,
        student TEXT NOT NULL,
        lecturer TEXT NOT NULL,
        event_title TEXT NOT NULL,
        event_date TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        purpose TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (student) REFERENCES users (username),
        FOREIGN KEY (lecturer) REFERENCES users (username),
        FOREIGN KEY (event_title) REFERENCES calendar(event_title),
        FOREIGN KEY (event_date) REFERENCES calendar(event_date),
        FOREIGN KEY (start_time) REFERENCES calendar(start_time),
        FOREIGN KEY (end_time) REFERENCES calendar(end_time) 
    )"""
)

# Create "facultyhub" table
cur.execute(
    """CREATE TABLE IF NOT EXISTS facultyhub (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        faculty_name TEXT NOT NULL,
        faculty_image TEXT NOT NULL
        )"""
)

con.commit()
con.close()