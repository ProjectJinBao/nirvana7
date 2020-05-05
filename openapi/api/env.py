# -*- coding: utf-8 -*-
import connexion
from openapi.service import env
from openapi.utils.exception_handle import DefalutError, IsExist, IsNotExist
from flask import g

def list(project_id, file_path, ref):
    try:
        data = env.env_list(project_id, file_path, ref, g.username)
        return {
            "data": data
        }
    except Exception as e:
        raise DefalutError(title=f'获取环境列表异常', detail=f'{e}')

def create(project_id, file_path, ref, body):
    try:
        env.create_env(project_id, file_path, ref, body, g.username)
        return {
            'title': '创建环境成功',
            'detail': '创建环境成功'
        }
    except IsExist as e:
        raise DefalutError(title=f'{e.title}', detail=f'{e.detail}')
    except Exception as e:
        raise DefalutError(title=f'创建环境异常', detail=f'{e}')