# school-form-db-population
Populates the school-form database prior to submitting the form to the students to be answered.

Designed as a helper to set up: [https://github.com/Marcos-A/teaching-stats](https://github.com/Marcos-A/teaching-stats).

---

### Requirements:
1. Install:

```
sudo apt-get install python3	
sudo apt-get install libpq-dev python-dev
sudo apt install python3-pip
pip3 install psycopg2
```

2. Set up your "database.ini" file and place it in the project's root folder. Note the schema should be set to "master" as seen here:

```
[postgresql]
host=YOUR-HOST
database=YOUR-DATABASE
user=YOUR-USER
password=YOUR-PASSWORD
port=YOUR-PORT
options=-c search_path=dbo,master
```

3. Modify your 8 data input CSV files content according to your needs. Make sure to keep the headers.

---

### How to run
From within the project's root folder, run:

`python3 insert_data.py`
