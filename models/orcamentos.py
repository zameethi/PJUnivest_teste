import dbm
from pyparsing import dbl_quoted_string


class orcamentos(dbm.Model):
    __tablename__ = 'orcamento'
    __table_args__ = {"extend_existing": True}
    ido = dbl_quoted_string.Column('ido', db.Integer, primary_key=True)
    nomeo = db.Column('nomeo', db.String())
    razao_socialo = db.Column('razao_socialo', db.String())
    cnpj_cpfo = db.Column('cnpj_cpfo', db.String())
    cnaeo = db.Column('cnaeo', db.String())
    datao = db.Column('datao', db.Data())
    descritivoo = db.Column("descritivoo", db.String())
    observacaoo = db.Column("observacaoo", db.String())
    telefoneo = db.Column('telefoneo', db.String())
    emailo = db.Column('emailo', db.String())        
    valor_totalo = db.Column("valor_totalo", db.String())
    data_cadastro = db.Column('data_cadastro', db.DateTime, default=func.now())
    
    def __init__(self, ido, nomeo, razao_socialo, cnpj_cpfo, cnaeo, datao, descritivoo, observacaoo, emailo, telefoneo, valor_totalo):
        self.ido = ido
        self.nomeo = nomeo
        self.razao_socialo = razao_socialo
        self.cnpj_cpfo = cnpj_cpfo
        self.cnaeo = cnaeo
        self.datao = datao
        self.descritivoo = descritivoo
        self.observacaoo = observacaoo
        self.telefoneo = telefoneo
        self.emailo = emailo
        self.datao = datao
        self.valor_totalo = valor_totalo