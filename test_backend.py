#!/usr/bin/python

import mvc_exceptions as mvc_exc
import psycopg2

#items = persons
persons = list()

class ModelBranch():

    def create_person(id, name, age):
        global persons
        results = list(filter(lambda x: x['id'] == id, persons))
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(id))
        else:
            persons.append({'id': id, 'name': name, 'age': age})

    def create_persons(app_items):
        global persons
        persons = app_items

    def get_one(id):
        global persons
        myitems = list(filter(lambda x: x['id'] == id, persons))
        if myitems:
            return myitems[0]
        else:
            raise mvc_exc.ItemNotStored(
                'Can\'t read "{}" because it\'s not stored'.format(id))

    def get_all():
        global persons
        return [person for person in persons]

    def update(id, name, age):
        global persons
        idxs_items = list(
            filter(lambda i_x: i_x[1]['id'] == id, enumerate(persons)))
        if idxs_items:
            i, item_to_update = idxs_items[0][0], idxs_items[0][1]
            persons[i] = {'id': id, 'name': name, 'age': age}
        else:
            raise mvc_exc.ItemNotStored(
                'Can\'t update "{}" because it\'s not stored'.format(id))

    def delete_one(id):
        global persons
        idxs_items = list(
            filter(lambda i_x: i_x[1]['id'] == id, enumerate(persons)))
        if idxs_items:
            i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
            del persons[i]
            print(' id delete {}'.format(id))
        else:
            raise mvc_exc.ItemNotStored(
                'Can\'t delete "{}" because it\'s not stored'.format(id))

class BranchController():

    def __init__(self, url, category):
        self.url = url
        self.category = category

    def test_your_simple_orm():
        #Connect DB
        conn = psycopg2.connect(database="test_tech", user = "root", password = "root", host = "127.0.0.1", port = "5432")

        print("\nOpened database successfully \n")

        cur = conn.cursor()
        #Create Table
        try:
            cur.execute('''CREATE TABLE COMPANY
                (ID INT PRIMARY KEY     NOT NULL,
                URL           TEXT    NOT NULL,
                CATEGORY           TEXT    NOT NULL);''')
        except Exception as e:
            print('Error create table :', e)

        print("Table created successfully \n")

        # INSERT Records
        try:
            cur.execute("INSERT INTO COMPANY (ID,URL,CATEGORY) \
                VALUES (1, 'https://tempat.com/branch/id/kim-jon6-gokz.jpg','ori' )");

            cur.execute("INSERT INTO COMPANY (ID,URL,CATEGORY) \
                VALUES (2, 'https://tempat.com/branch/id/kim-jon6-gokz.jpg','lg' )");
            print("Records created successfully \n")
        except Exception as e:
            print('Error : ', e , '\n')

        # UPDATE Records
        try:
            cur.execute("UPDATE COMPANY set CATEGORY = 'md' where ID = 1")
            conn.commit()
            print("Total number of rows updated :", cur.rowcount)
        except Exception as e:
            print('Error Update Record : ', e)

        #DELETE Records
        try:
            cur.execute("DELETE from COMPANY where ID=1;")
            conn.commit()
            print("Total number of rows deleted :", cur.rowcount, "\n")
        except Exception as e:
            print('Error delete record: ', e)

        #READ Records
        try:
            cur.execute("SELECT id, url, category from COMPANY")
            rows = cur.fetchall()
            for row in rows:
                print ("ID = ", row[0])
                print ("URL = ", row[1])
                print ("CATEGORY = ", row[2], "\n")

            print ("Operation done successfully \n")
        except Exception as e:
            print('Error read records:', e)

        conn.commit()
        conn.close()

        return 'Connection close!'

    #Grouping with value sequence
    def group_to_numeric():
        group_data = ModelBranch.get_all()

        group_data[0].update({"numeric":1})
        group_data[1].update({"numeric":2})
        group_data[2].update({"numeric":2})
        group_data[3].update({"numeric":3})

        return group_data

    # Display instance category & url 
    def displayParsing(self):
        self.url_format = 'url'
        print('"{}":'.format(self.category), '"{}":'.format(self.url_format), "'{}'".format(self.url))

# input url & category
url_cat_1 = BranchController('https://tempat.com/branch/id/kim-jon6-gokz.jpg', 'ori')
url_cat_2 = BranchController('https://tempat.com/branch/id/kim-jon6-gokz.jpg', 'small')
url_cat_3 = BranchController('https://tempat.com/branch/id/kim-jon6-gokz.jpg', 'md')
url_cat_4 = BranchController('https://tempat.com/branch/id/kim-jon6-gokz.jpg', 'lg')

# show parsing url & category
print('\nParsing url & category :\n')
print('Output Parsing = {')
url_cat_1.displayParsing()
url_cat_2.displayParsing()
url_cat_3.displayParsing()
url_cat_4.displayParsing()
print('}')


def main():

    json = [
        {'id': 1, 'name': 'ganang', 'age': 27},
        {'id': 2, 'name': 'made', 'age': 24},
        {'id': 3, 'name': 'sidik', 'age': 27},
        {'id': 4, 'name': 'herman', 'age': 40},
    ]

    # CREATE
    ModelBranch.create_persons(json)

    # CREATE ONE
    ModelBranch.create_person(5, name='bambang', age=26)

    # READ All
    print('\n Read All')
    print(ModelBranch.get_all())

    # Read One
    print('\n Read One')
    print(ModelBranch.get_one(5))

    # UPDATE data 
    print('\n UPDATE person')
    ModelBranch.update(5, name='Bambang Y', age=27)
    print(ModelBranch.get_one(5))

    # DELETE
    print('\n DELETE person')
    ModelBranch.delete_one(5)

    print('\n READ persons after update')
    print(ModelBranch.get_all())

    print('\n############################################################################################')

    print('\n Grouping with value sequence :')
    print(BranchController.group_to_numeric())

    print('\nSimple ORM :')
    print(BranchController.test_your_simple_orm())

if __name__ == '__main__':
    main()