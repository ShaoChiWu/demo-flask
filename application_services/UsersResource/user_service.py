from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class UserResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def get_data_resource_info(cls):
        return 'e6156', 'basic_info'
    
    @classmethod
    def get_by_uni(cls, uni):
        db_name, table = cls.get_data_resource_info()
        res = RDBService.get_by_prefix(db_name, table,
                                      "uni", uni)
        return res
    
    @classmethod
    def get_user_and_gender(cls, template):
        db_name, table = cls.get_data_resource_info()
        wc, args = RDBService.get_where_clause_args(template)
        sql = f"select * from {db_name}.{table} left join {db_name}.gender_info on " + \
                f"{db_name}.{table}.uni = {db_name}.gender_info.uni"

        res = RDBService.run_sql(sql, args, fetch=True)
        return res
