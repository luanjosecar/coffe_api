
from datetime import datetime
from db_sender import send_request , get_request
from response import *

# Definir banco de dados no qual ela seram colocadas
def upload_img(image):
    pass

# Metodo para inserção de leituras dentro do sistema
def insert_reading(reading_id:str, user_id:str, cnn_id:str):
    query = f"""
        INSERT INTO reading_history (reading_id,user_id,cnn_id,reading_date, reading_status)
        VALUES ('{reading_id}', '{user_id}', '{cnn_id}', '{datetime.now()}', False)
    """
    send_request(query)
    # try:
    #     send_request(query)
    #     return sucess_resp("reading added")
    # except:
    #     return error_resp("Unable to regist reading")
    
# insere imagens para validação
def insert_imgs(reading_id: str, image_id:str):
    query = f"""
        INSERT INTO images_reading (imagem,reading_id)
        VALUES ('{image_id}', '{reading_id}')
    """
    send_request(query)

#Insere local da leitura caso exista
def insert_reading_location(reading_id:str, longitude:str, latitude:str):
    query = f"""
        INSERT INTO reading_location (reading_id,longitude, latitude)
        VALUES ('{reading_id}', '{longitude}', '{latitude}')
    """
    send_request(query)

#retorna as imagens com base no resultado
def return_imgs(reading_id:str):
    query = f"""
        SELECT * FROM images_results 
    """
    get_request(query)


