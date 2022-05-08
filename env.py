#READ ONLY credentials 
host = "157.230.209.171"
username = "jemison_1740"
user = username
password = "D037O1IfINb2ilBMLZlaDfVoyWXRvkl0"

def get_db_url(db_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    return url