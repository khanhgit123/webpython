#database helper functions
import mysql.connector

def convertFieldLisTToSQL(field_list):
    '''convert a list of FIELDS into a string that can be inserted into SQlcommand'''
    seperator = ","
    return seperator.join(field_list)
def generateInsertCommand(table_name, field_names_list):
    ''' return the insert command string with %s in place of insert values
    (used to prevent sql injection) '''
    num_parameter = len(field_names_list)
    place_holder = ""
    for _i in range(0, num_parameter):
        place_holder +="%s,"
    place_holder = place_holder[:-1]  #get rid of the final comma
    insert_command = "INSERT INTO "+ table_name + " (" + convertFieldLisTToSQL(field_names_list) + ") VALUES (" + place_holder + ")"

    return insert_command
def generateDeleteCommand(table_name, field_names_list):
    '''delete a row in the database that matches certain requirement'''
    num_parameter = len(field_names_list)
    delete_command = "DELETE FROM " + table_name + " WHERE "
    for i in range(0, num_parameter):
        delete_command += "(" + field_names_list[i] + " LIKE %s)"
        if (i != num_parameter -1):
            delete_command += " AND "
    return delete_command
def generateSelectCommand(table_name, field_names_toGet, field_names_list):
    ''' return the search command string with %s in place of insert values
    (used to prevent sql injection) '''

    num_parameter = len(field_names_list)
    search_command = "SELECT " + convertFieldLisTToSQL(field_names_toGet) + " FROM " + table_name + " WHERE "
    for i in range(0, num_parameter):
        search_command += "(" + field_names_list[i] + " LIKE %s)"
        if (i != num_parameter -1):
            search_command += " AND "
    return search_command
def generateUpdateCommand(table_name, update_field_name_list, identifier_field_name_list):
    '''create an upduate command with %s's to prevent injection attack'''
    num_identifier = len(identifier_field_name_list)
    num_update = len(update_field_name_list)
    update_command = "UPDATE " + table_name + " SET "
    for i in range(0, num_update):
        update_command += update_field_name_list[i] + " = %s "
        if i != num_update - 1:
            update_command += ", "
    update_command += "WHERE "
    for i in range(0, num_identifier):
        update_command += identifier_field_name_list[i] + " = %s "
        if i != num_identifier - 1:
            update_command += "AND "
    return update_command

class databaseManage:
    '''database management class'''
    def __init__(self):

        #names:
        self.database_name = "VAM_database"


        #database things:
        self.textEncoding = "utf8"
        self.connectionEncoding = "utf8"


        host= "vamdatabase.c6hytllht8i3.ap-southeast-1.rds.amazonaws.com"
        port=3306
        dbname= self.database_name
        user="admin"
        password="xiWes4My22ooWBthZRxs"
    
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            port=port,
            db=dbname,
            charset= self.connectionEncoding
        )
        self.cursor=self.conn.cursor()
        print("connection to main database is ready")

        return None
    
    def insertValues(self, table_name, field_names, field_values):
        '''insert value to table'''
        insert_command = generateInsertCommand(table_name,field_names)
        try:
            self.cursor.execute(insert_command, field_values)
            self.conn.commit()
        except:
            return [False, "failed to insert"]
        return [True, None]

    def updateValues(self, table_name, update_field_names, update_field_values, identifier_field_names, identifier_field_values):
        '''update certain values to table'''
        update_command = generateUpdateCommand(table_name, update_field_names, identifier_field_names)
        values_list = []
        values_list.append(update_field_values, identifier_field_values)
        try:
            self.cursor.execute(update_command, values_list)
            self.conn.commit()
        except:
            return [False, "failed to update"]
        return [True, None]
    
    def SelectRows(self, table_name, field_names_toGet, identifier_field_names, identifier_field_values):
        '''select certain rows from table'''
        select_command = generateSelectCommand(table_name, field_names_toGet, identifier_field_names)
        try:
            self.cursor.execute(select_command, identifier_field_values)
        except:
            return [False, "failed to select"]
        return [True, self.cursor.fetchall()]




