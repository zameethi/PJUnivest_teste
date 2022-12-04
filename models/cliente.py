from conection.conexao import db
from sqlalchemy.sql import func

class Cadastrocliente(db.Model):
    __tablename__ = 'cadastro_clientes'
    __table_args__ = {"extend_existing": True}
    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column('nome', db.String())
    razao_social = db.Column('razao_social', db.String())
    cnpj_cpf = db.Column('cnpj_cpf', db.String())
    cep = db.Column('cep', db.String())
    rua = db.Column('rua', db.String())
    numero = db.Column('numero', db.String())
    bairro = db.Column('bairro', db.String())
    cidade = db.Column('cidade', db.String())
    uf = db.Column('uf', db.String())
    email = db.Column('email', db.String())
    telefone = db.Column('telefone', db.String())
    data_cadastro = db.Column('data_cadastro', db.DateTime, default=func.now())
    
    
    def __init__(self, nome, razao_social, cnpj_cpf, cep, rua, numero, bairro, cidade, uf, email, telefone):
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj_cpf = cnpj_cpf
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.email = email
        self.telefone = telefone

