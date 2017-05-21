# Notavampire.com

This is practice for setting up a full site in Python using django.

## DB Set-up
psql  
create user notavampire with password 'secretsauce';  
create database notavampire;  
grant all on database notavampire to notavampire;  
alter user notavampire createdb;  
