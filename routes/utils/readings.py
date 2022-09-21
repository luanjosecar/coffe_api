from ..database.postgres_reader import *
from datetime import datetime
from .responses import *
import os
from dotenv import load_dotenv
from google.cloud import storage
from google.oauth2 import service_account

load_dotenv()

def get_readings(user_id:str):
    query = f"select read_id, read_imp, read_date, read_status from readings where user_id = '{user_id}'"
    resp = get_request(query)
    base_list = []
    for rid, rimp, rdate, rstate in resp:
        resp_dict = {"read_id" : rid, "read_imp":rimp, "read_date":rdate.strftime('%y-%m-%d'), "read_status":rstate}
        base_list.append(resp_dict)
    return base_list


# Definir banco de dados no qual ela seram colocadas
def upload_img(image_data, reading_id, index, img_type):
    credentials = service_account.Credentials.from_service_account_file(
        'gcp_key.json')
    bucket = os.getenv('BUCKETNAME')
    project_id = os.getenv('PROJECTID')
    image_path = img_type + '/' + reading_id + str(index) + ".jpeg"
    
    client = storage.Client(project_id)
    bucket = client.get_bucket(bucket)
   
    blob = bucket.blob(image_path)
    blob.content_type = "image/jpeg"
    blob.upload_from_string(image_data, content_type="image/jpeg")
    return image_path

# Metodo para inserção de leituras dentro do sistema
def insert_reading(reading_id:str, user_id:str, cnn_id:str):
    query = f"""
        INSERT INTO readings (read_id,user_id,read_imp,read_date, read_status)
        VALUES ('{reading_id}', '{user_id}', '{cnn_id}', '{datetime.now()}', False)
    """
    send_request(query)

    
# insere imagens para validação
def insert_imgs(reading_id: str, image_dir:str):
    bucket = os.getenv('BUCKETNAME')
    image_path = f"https://storage.googleapis.com/{bucket}/{image_dir}"
    query = f"""
        INSERT INTO reading_imgs (read_id,img_location)
        VALUES ('{reading_id}', '{image_path}')
    """
    send_request(query)

#Insere local da leitura caso exista
def insert_reading_location(reading_id:str, longitude:str, latitude:str):
    query = f"""
        INSERT INTO reading_location (read_id,longitude, latitude)
        VALUES ('{reading_id}', '{longitude}', '{latitude}')
    """
    send_request(query)

#retorna as imagens com base no resultado
def return_imgs_results(reading_id:str):
    query = f"SELECT * FROM reading_result where read_id = '{reading_id}'"
    results = get_request(query)
    res_list = []
    for rid, rloc, rresult in results :
        res_dict = {"image" : rloc, "result":rresult}
        res_list.append(res_dict)
    return res_list


def return_imgs(reading_id:str):
    '''
        Retorna as imagens para a leitura do sistema
    '''
    query = f"SELECT img_location FROM reading_imgs where read_id = '{reading_id}'"
    print(query)
    loc = get_request(query)
    normalize = []
    for imgs, in loc:
        normalize.append(imgs)
    print(normalize)
    return normalize
