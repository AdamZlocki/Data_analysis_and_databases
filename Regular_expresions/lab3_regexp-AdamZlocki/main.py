import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb',password='adb2020');


def film_in_category(category: Union[int, str]) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category, str):
        txt = """
                SELECT film.title AS title, language.name AS languge, category.name AS category
                FROM category
                INNER JOIN film_category ON category.category_id = film_category.category_id
                INNER JOIN film ON film.film_id = film_category.film_id
                INNER JOIN language ON language.language_id = film.language_id

                WHERE category.name LIKE %s

                GROUP BY film.title, language.name, category.name
                """
        df = pd.read_sql_query(txt, con=connection, params=[category])
        return df
    elif isinstance(category, int):
        txt = """
            SELECT film.title AS title, language.name AS languge, category.name AS category
            FROM category
            INNER JOIN film_category ON category.category_id = film_category.category_id
            INNER JOIN film ON film.film_id = film_category.film_id
            INNER JOIN language ON language.language_id = film.language_id

            WHERE category.category_id = %s

            GROUP BY film.title, language.name, category.name
            """
        df = pd.read_sql_query(txt, con=connection, params=[category])
        return df
    else:
        return None


def film_in_category_case_insensitive(category: Union[int, str]) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category, str):
        txt = """
                SELECT film.title AS title, language.name AS languge, category.name AS category
                FROM category
                INNER JOIN film_category ON category.category_id = film_category.category_id
                INNER JOIN film ON film.film_id = film_category.film_id
                INNER JOIN language ON language.language_id = film.language_id

                WHERE category.name ILIKE %s

                GROUP BY film.title, language.name, category.name
                """
        df = pd.read_sql_query(txt, con=connection, params=[category])
        return df
    elif isinstance(category, int):
        txt = """
            SELECT film.title AS title, language.name AS languge, category.name AS category
            FROM category
            INNER JOIN film_category ON category.category_id = film_category.category_id
            INNER JOIN film ON film.film_id = film_category.film_id
            INNER JOIN language ON language.language_id = film.language_id

            WHERE category.category_id = %s

            GROUP BY film.title, language.name, category.name
            """
        df = pd.read_sql_query(txt, con=connection, params=[category])
        return df
    else:
        return None


def film_cast(title: str) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(title, str):
        txt = """
                SELECT actor.first_name AS first_name, actor.last_name AS last_name
                FROM actor
                INNER JOIN film_actor ON film_actor.actor_id = actor.actor_id
                INNER JOIN film ON film.film_id = film_actor.film_id

                WHERE film.title LIKE %s

                GROUP BY actor.first_name, actor.last_name
                
                ORDER BY actor.last_name, actor.first_name
                """
        df = pd.read_sql_query(txt, con=connection, params=[title])
        return df

    else:
        return None


def film_title_case_insensitive(words: list):
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(words, list):
        WORD = '|'.join(words)
        txt = f"""SELECT film.title AS title
                FROM film
                WHERE film.title ~* '(?:^| )({WORD})""" + """{1,}(?:$| )'
                GROUP BY film.title
                ORDER BY film.title
                """
        df = pd.read_sql_query(txt, con=connection)
        return df
    else:
        return None
