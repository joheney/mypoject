from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import (
    Mapped,
    mapped_as_dataclass,  # type: ignore
    mapped_column,
    registry,
    relationship,
)

table_registry = registry()


@mapped_as_dataclass(table_registry)
class Pedido:
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome_client: Mapped[str]
    forma_pagamento: Mapped[str]
    status: Mapped[str]
    pago: Mapped[bool]
    data_criacao: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    total: Mapped[float] = mapped_column(nullable=False, default=0.0)
    itens: Mapped[list["ItemPedido"]] = relationship( # type: ignore
        "ItemPedido",
        back_populates="pedido",
        cascade="all, delete-orphan",
        lazy="selectin",
    )


class ItemPedido:
    __tablename__ = "itens_pedido"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.id"))
    pedido: Mapped["Pedido"] = relationship("Pedido", back_populates="itens")
    nome: Mapped[str]
    tipo: Mapped[str]  # "pastel" ou "bebida"
    quantidade: Mapped[int]
    preco_unitario: Mapped[float]
