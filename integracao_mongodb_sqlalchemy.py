""" Imports do SqlAlchemy"""
from typing import List
from typing import Optional
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase

"""Importando a engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


"""Recuperação dos dados persistidos"""
from sqlalchemy import select



engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)


# Base declarativa
class Base(DeclarativeBase):
    """SQLAlchemy DeclarativeBase"""
    pass


class Client(Base):
    """Tabela do Cliente"""
    __tablename__ = 'cliente'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(9), nullable=False)
    cpf: Mapped[Optional[str]]

    conta: Mapped[List['Conta']] = relationship('Conta', back_populates='cliente')

    def __repr__(self) -> str:
        return f"Client(id={self.id!r}, nome={self.nome!r}, cpf={self.cpf!r})"



class Conta(Base):
    """Tabela Conta"""
    __tablename__ = 'conta'

    id = mapped_column(Integer, primary_key=True)
    tipo = mapped_column(String)
    agencia = mapped_column(String)
    num = Mapped[Optional[int]]
    id_cliente = mapped_column(ForeignKey('cliente.id'), nullable=False)
    saldo = Mapped[Optional[float]]
    cliente: Mapped[List['Client']] = relationship('Client', back_populates='conta')

    def __repr__(self) -> str:
        return f"Conta(id={self.id!r}, tipo={self.tipo!r}, agencia={self.agencia!r}, num={self.num!r}, id_cliente={self.id_cliente}, saldo={self.saldo})"


Base.metadata.create_all(engine)


with Session(engine) as session:
    pablo = Client(
        nome="Hjevit",
        cpf="34422123412",
        conta=[Conta(
            tipo='corrent',
            agencia=1,
            num=90022211,
            id_cliente=0,
            saldo=1000000
        )]
    )

session.add_all([pablo])

session.commit()

session = Session(engine)

stmt = select(Client).where(Client.nome.in_(["Pablo"]))

for user in session.scalars(stmt):
    print(user)
