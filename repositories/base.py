from databases import Database


class BaseRepository:
    """ Базовый класс для работы с данными """

    async def get_all(self, *args, **kwargs):
        raise NotImplementedError
    
    async def get_by_id(self, id : int):
        raise NotImplementedError
    
    async def create(self, *args, **kwargs):
        raise NotImplementedError

    async def update(self, *args, **kwargs):
        raise NotImplementedError


class BaseDbRepository(BaseRepository):
    """ Базовый класс для работы с базой данных"""
    
    def __init__(self, database :Database):
        self.database = database
        
        
class BaseFileRepository(BaseRepository):
    """ Базовый класс для работы с файлами"""
    
    def __init__(self, file_path :str):
        self.file_path = file_path