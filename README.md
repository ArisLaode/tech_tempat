# Spesifikasi script:
  - Python 3.5.2
  - Postgresql 12.1
  - psycopg2 2.8.4

# Running Script
  - Open directory script || example command: cd/home/aris/tempat.com
  - Command to run script --> python test_backend.py

# Explain Script
  in this script there are 4 important points that must be run 
  1. CRUD simple object
     - create, read, update & delete must run in accordance with the functions that have been made
     - check class ModelBranch to see the detailed function of the script

  2. CRUD simple ORM
     - create database postgresql with name db "test_tech"
     - when you running this script, table will be creta and you can see insert, read, update & delete records
     - check function test_your_simple_orm() in class BranchController()

  3. Grouping with value sequence
     - Grouping with add key with value sequence and will automatically be sorted by id.
     - Check function group_to_numeric in class BranchController()

  4. Parsing url & category
     - Parsing url & category with output must intance
     - Chekc function displayParsing and read script in line 145 - 157 to see the detailed.

# Video Demo Script
  - Link --> https://youtu.be/Yk3ekiJTIYI