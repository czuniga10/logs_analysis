# Udacity FSND Project1 - Logs Analysis

## Description

The task was to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the `psycopg2` module to connect to the database.


## Assignment
Answer the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular authors of all time?
3. On which day did more than 1% of requests lead to errors?


## Required Setup 

- [Virtual Box](https://www.virtualbox.org/) (download)
- [Vagrant](https://www.vagrantup.com/) (download)
- [Vagrant Environment Setup Repository](https://github.com/udacity/fullstack-nanodegree-vm) (git clone)
- [This Repository](https://github.com/czuniga10/logs_analysis) (git clone)
- [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) (download and unzip)

## Run Project

1. Download `Virtual Box` and `Vagrant` 
2. Git Clone the `Vagrant Environment Setup Repository` onto your local machine
3. cd into the above repo, and then into the directory called, and in the terminal, run 
```
$ vagrant up
```
4. Then, run 
```
$ vagrant ssh
```
5. Give it a few minutes to initialize the data, but your Virtual Machine should be up and running<br> - NOT MANDATORY: within the VM, cd into the directory named `Vagrant` and delete the folders `catalog`, `forum`, and `tournament`
6. Download and unzip the `newsdata.sql` file and drag it into the vagrant directory, which is shared with your virtual machine
7. Connect to the Database with the command
```
psql -d news -f newsdata.sql
```
8. Git Clone `This Repository` and drag the file `analysis.py` into the vagrant directory.
9. Execute the Logs Analysis code with
```
python analysis.py
```
This should produce a result within the VM terminal that should look exactly like the `analysis.txt` file within `This Repository`

#### Exit the Virtual Machine with `CTRL+D` or running the command `exit` within the VM terminal

