# school-form-db-population
Populates the school-form database prior to submitting the form to the students to be answered.

Designed as a helper to set up: [https://github.com/Marcos-A/school-form](https://github.com/Marcos-A/school-form)

---

### Requirements:
1. Install:

```
sudo apt-get install python3	
sudo apt-get install libpq-dev python-dev
sudo apt install python3-pip
pip3 install psycopg2
```

2. Set up your "database.ini" file and place it in the project's root folder:

```
[postgresql]
host=YOUR-HOST
database=YOUR-DATABASE
user=YOUR-USER
password=YOUR-PASSWORD
port=YOUR-PORT
options=-c search_path=dbo,YOUR-SCHEMA
```

3. Place your 4 data CSV files in the "input" folder following this pattern:

cf_students.csv file

```
contains the into about CF students

header: ALUMNE,CORREU,GRUP,MP01,MP02,MP03,MP04,MP05,MP06,MP07,MP08,MP09,MP10,MP11,MP12,MP13,MP14,MP15

MP columnes must contain 'X' to determine if the student is enrolled.
```

degrees.csv file

``` 
contains the into about the degrees

header: Abreviatura,Nom,Família
```

eso-batx_students.csv file

``` 
contains the into about the ESO and Batxillerat students

header: Adreça electrònica,Nom,Cognoms,Nivell,Grup
```

subjects.csv file

``` 
contains the into about the subjects

header: MP,Nom,Cicle
```

---

### How to run
From within the project's root folder, run:

`python3 insert_data.py`
