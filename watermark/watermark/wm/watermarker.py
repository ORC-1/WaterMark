from utils.random_id_gen import generate_random_alphanum

async def watermarkdoc(serializer):
    """Water Mark and persist data to DataBase"""
    try:
        serializer.save(ticket_id=generate_random_alphanum(23), water_mark=True)
    except Exception as e:
        print('error at watermarkdoc:'+ str(e))
        return 0
