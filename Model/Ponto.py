from App.DB import DB
from Model.User import UserModel


class PontoModel:

    @staticmethod
    def baterPonto(user_pin, tipo):
        user_id = UserModel.get_id_by_pin(user_pin)
        if tipo == "entrar":
            DB().run("INSERT INTO ponto (user_id) VALUES ({});".format(user_id))
        else:
            DB().run("UPDATE ponto SET fim = CURRENT_TIMESTAMP WHERE user_id = {} AND fim IS NULL;".format(user_id))

    @staticmethod
    def pontoAberto(user_pin):
        user_id = UserModel.get_id_by_pin(user_pin)
        ponto = DB().run_fr("SELECT inicio FROM ponto WHERE user_id = {} AND fim is NULL;".format(user_id))
        if ponto is None:
            return False
        return True
