from App.DB import DB


class UserModel:

    @staticmethod
    def get(user_pin):
        return DB().run_fr("SELECT nome, batalhao, patente FROM user WHERE pin = {};".format(user_pin))

    @staticmethod
    def get_id_by_pin(user_pin):
        return DB().run_fv("SELECT id FROM user WHERE pin = {};".format(user_pin), "id")
