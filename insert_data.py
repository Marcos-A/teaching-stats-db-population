# -*- coding: UTF-8 -*-
from config import config
import csv
import os
import psycopg2
import sys


sys.path.append(os.path.dirname(__file__))
CF_STUDENTS = 'input/cf_students.csv'
DEGREES_FILE = 'input/degrees.csv'
ESO_BATX_STUDENTS_FILE = 'input/eso-batx_students.csv'
SUBJECTS_FILE = 'input/subjects.csv'


def read_degrees(input_file):
    degrees = ()
    with open(input_file, 'r', encoding='utf-8') as degrees_file:
        degrees_reader = csv.DictReader(degrees_file)

        for degree in degrees_reader:
            short_name = degree['Abreviatura']
            full_name = degree['Nom']
            department = degree['Família']

            degrees += ((short_name, full_name, department,),)

        return degrees


def insert_degrees(degrees):
    sql = """
             INSERT INTO forms_degree(short_name, long_name, department)
             VALUES(%s, %s, %s);
          """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(**params)
        cursor = conn.cursor()

        cursor.executemany(sql, degrees)

        cursor.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def read_subjects(input_file):
    subjects = ()
    evaluable_items = (('Centre',), ('Tutoria',),)
    with open(input_file, 'r', encoding='utf-8') as subjects_file:
        subjects_reader = csv.DictReader(subjects_file)

        for subject in subjects_reader:
            short_name = subject['MP']
            full_name = subject['Nom']
            degree = subject['Cicle']

            subjects += ((short_name, full_name, degree,),)
            evaluable_items_list = [evaluable_item[0] for evaluable_item in evaluable_items]
            if short_name not in evaluable_items_list:
                evaluable_items += ((short_name,),)

        return subjects, evaluable_items


def insert_evaluable_items(evaluable_items):
    sql = """
             INSERT INTO forms_evaluableitem(item)
             VALUES(%s);
          """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(**params)
        cursor = conn.cursor()

        cursor.executemany(sql, evaluable_items)

        cursor.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def insert_subjects(subjects):
    sql = """
             INSERT INTO forms_subject(short_name_id, long_name, degree_id)
             VALUES(%s, %s, %s);
          """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(**params)
        cursor = conn.cursor()

        cursor.executemany(sql, subjects)

        cursor.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def read_ESOBatx_students(input_file):
    students = ()
    with open(input_file, 'r', encoding='utf-8') as students_file:
        students_reader = csv.DictReader(students_file)

        for student in students_reader:
            email = student['Adreça electrònica']
            name = student['Nom']
            surname = student['Cognoms']
            level = student['Nivell']
            classgroup = student['Grup']

            students += ((email, name, surname, level, classgroup,),)

        return students


def insert_ESOBatx_students(students):
    sql = """
             INSERT INTO forms_enrolledstudent(email, name, surname,
                                               level, classgroup)
             VALUES(%s, %s, %s, %s, %s);
          """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(**params)
        cursor = conn.cursor()

        cursor.executemany(sql, students)

        cursor.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def read_cf_students(input_file):
    students = ()
    with open(input_file, 'r', encoding='utf-8') as students_file:
        students_reader = csv.DictReader(students_file)

        for student in students_reader:
            email = student['CORREU']
            level = 'CF'
            classgroup = student['GRUP']
            enrolled_subjects = ','.join([key for key in student
                                          if 'mp' in key.lower() and
                                          student[key].lower() == 'x'])
            degree = student['CICLE']

            students += ((email, level, classgroup, enrolled_subjects, degree,),)

        return students


def insert_cf_students(students):
    sql = """
             INSERT INTO forms_enrolledstudent(email, level, classgroup,
                                               enrolled_subjects, degree_id)
             VALUES(%s, %s, %s, %s, %s);
          """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(**params)
        cursor = conn.cursor()

        cursor.executemany(sql, students)

        cursor.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    degrees = read_degrees(DEGREES_FILE)
    insert_degrees(degrees)
    subjects, evaluable_items = read_subjects(SUBJECTS_FILE)
    insert_evaluable_items(evaluable_items)
    insert_subjects(subjects)
    eso_batx_students = read_ESOBatx_students(ESO_BATX_STUDENTS_FILE)
    insert_ESOBatx_students(eso_batx_students)
    cf_students = read_cf_students(CF_STUDENTS)
    insert_cf_students(cf_students)
