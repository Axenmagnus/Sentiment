# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 21:52:41 2022

@author: jacob

This script is aimed to learn how to export data to an SQL server. We need to do this
to be able to store large amount of data to analyze in a later stage. 

Preferably we will store the results of our sentiment analysis on the server as
it will take a lot of memory to store text

OBS ej klar ännu, har bara samlat tankar och lite data

"""
import pandas as pd
import pyodbc


#create a df and assign it to a csv


#connect to sql:
#conn = pyodbc.connect('Driver={SQL Server};'
#                      'Server=RON\SQLEXPRESS;'
#                      'Database=test_database;'
#                      'Trusted_Connection=yes;')
#cursor = conn.cursor()


#create a table in sql:
#cursor.execute('''
#		CREATE TABLE products (
#			product_id int primary key,
#			product_name nvarchar(50),
#			price int
#			)
#              ''')   


#insert data into frame
#for row in df.itertuples():
#    cursor.execute('''
#                INSERT INTO products (product_id, product_name, price)
#                VALUES (?,?,?)
#                ''',
#                row.product_id, 
#                row.product_name,
#                row.price
#                )
#conn.commit()


#perform a test:
#select * from products




























