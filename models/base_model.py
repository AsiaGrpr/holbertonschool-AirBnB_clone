#!/usr/bin/python3
'''class base_model'''

import uuid
from datetime import datetime


'''def class'''

class BaseModel:
    
    def __init__(self, id):
        '''constructor'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''def str'''
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''def save'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''def to_dict'''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
