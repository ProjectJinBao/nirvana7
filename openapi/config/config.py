import os
from openapi.utils.common import is_exist_python_path, is_exist_path

class NirvanaConfig(object):

    def postgres_config(self):
        pg_provider = os.getenv('PG_PROVIDER') if  os.getenv('PG_PROVIDER') else 'postgres'
        pg_host = os.getenv('PG_HOST') if os.getenv('PG_HOST') else '127.0.0.1'
        pg_user = os.getenv('PG_USER') if  os.getenv('PG_USER') else 'postgres'
        pg_password = os.getenv('PG_PASSWORD') if  os.getenv('PG_PASSWORD') else '123456'
        pg_database = os.getenv('PG_NAME') if  os.getenv('PG_NAME') else 'nirvana04'
        pg_port = int(os.getenv('PG_PORT')) or 5432
        return pg_provider, pg_host, pg_user, pg_password, pg_database

    def workspace_path(self):
        work_space = os.getenv('SCRIPT_SAVE_PATH') if os.getenv(
            'SCRIPT_SAVE_PATH') else '/Users/xumin/jo/workspace'
        return work_space

    def script_save_path(self, project_id):
        script_save_path = os.getenv('SCRIPT_SAVE_PATH') if  os.getenv('SCRIPT_SAVE_PATH') else f'{os.getcwd()}/openapi/script/{project_id}'
        return script_save_path

    def script_save_fold(self):
        script_fold = os.getenv('SCRIPT_SAVE_PATH') if os.getenv(
            'SCRIPT_SAVE_PATH') else f'{os.getcwd()}/openapi/script'
        return script_fold

    def httprunner_log_save_path(self):
        httprunner_log_path = os.getenv('SCRIPT_SAVE_PATH') if os.getenv(
            'HTTPRUNNER_LOG_SAVE_PATH') else f'{os.getcwd()}/openapi/httprunner_log'
        return httprunner_log_path


    def report_save_path(self):
        report_save_path = os.getenv('REPORT_SAVE_PATH') if  os.getenv('REPORT_SAVE_PATH') else f'{os.getcwd()}/openapi/report'
        return report_save_path

    def report_ip(self):
        report_ip = os.getenv('REPORT_IP') if  os.getenv('REPORT_IP') else f'http://127.0.0.1:9090'
        return report_ip

    def gitlab_config(self):
        gitlab_url = os.getenv('GITLAB_URL') if  os.getenv('GITLAB_URL') else 'gitlab.daocloud.io'
        return {
            'gitlab_url': gitlab_url
        }

def check_config_path():
    script_save_fold = NirvanaConfig().script_save_fold()
    is_exist_python_path(script_save_fold)

def check_httprunner_log_path():
    httprunner_log_save_path = NirvanaConfig().httprunner_log_save_path()
    is_exist_path(httprunner_log_save_path)
