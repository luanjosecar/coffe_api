
def sucess_resp(data):
    return {'status': 'Sucess', 'results': data}
    
def error_resp(message):
    return {'status': 'Fail', 'message': message}