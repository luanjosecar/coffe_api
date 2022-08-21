
from ..database.postgres_reader import *

def get_imp_name(imp_id:str):
    query = f"select imp_name from implementations where imp_id = {imp_id}"
    resp = get_request(query)
    imp_name = resp[0]
    return imp_name


def get_implementations():
    query = "select * from implementations where imp_status is true"
    resp = get_request(query)
    imp_list = []
    for iid ,idname, istatus,iimgs, itype in resp:
        imp_dict = {"imp_id": iid, "imp_name" : idname, "images" : iimgs, "type":itype }
        imp_list = imp_list.append(imp_dict)
    return imp_list
