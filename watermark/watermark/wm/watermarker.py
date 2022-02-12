from core.models import Document
from utils.random_id_gen import generate_random_alphanum

def watermarkdoc(serializer):
    try:
        serializer.save(ticket_id=generate_random_alphanum(23), water_mark=True)
    except Exception as e:
        return 0
