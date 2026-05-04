import sqlite3

conn = sqlite3.connect("loja_select.db")
cursor = conn.cursor()

# Remover tabelas antigas, caso existam
cursor.execute("DROP TABLE IF EXISTS venda")
cursor.execute("DROP TABLE IF EXISTS produto")
cursor.execute("DROP TABLE IF EXISTS cliente")

# Criar tabela cliente
cursor.execute("""
            CREATE TABLE cliente (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
            )   
            """)

# Criar tabela produto
cursor.execute("""
            CREATE TABLE produto (
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
            )
            """)

# Criar tabela venda
cursor.execute("""
            CREATE TABLE venda (
            id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            valor REAL NOT NULL,
            data_venda TEXT NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
            )
            """)

# Inserir clientes
clientes = [
            ("Ana Silva", "Macapá"),
            ("Bruno Costa", "Santana"),
            ("Carlos Almeida", "Macapá"),
            ("Mariana Souza", "Belém"),
            ("João Silva", "Santana"),
            ("Fernanda Lima", "Macapá"),
            ("Amanda Rocha", "Belém"),
            ("Pedro Martins", "Oiapoque"),
            ("Lucas Ferreira", "Macapá"),
            ("Aline Santos", "Santana")
            ]

cursor.executemany("""
            INSERT INTO cliente (nome, cidade)
            VALUES (?, ?)
            """, clientes)

# Inserir produtos
produtos = [
            ("Notebook Dell", 3500.00, 8),
            ("Mouse Gamer", 120.00, 25),
            ("Teclado Mecânico", 280.00, 15),
            ("Monitor 24 Polegadas", 900.00, 6),
            ("Cabo HDMI", 35.00, 50),
            ("Headset Bluetooth", 180.00, 12),
            ("Mousepad Grande", 45.00, 30),
            ("Memória RAM 8GB", 250.00, 10),
            ("SSD 480GB", 320.00, 4),
            ("Webcam Full HD", 210.00, 7),
            ("Microfone USB", 450.00, 3),
            ("Carregador Universal", 85.00, 18)
            ]

cursor.executemany("""
            INSERT INTO produto (nome, preco, estoque)
            VALUES (?, ?, ?)
            """, produtos)

# Inserir vendas
vendas = [
        (1, 3500.00, "2026-05-01"),
        (2, 120.00, "2026-05-02"),
        (3, 900.00, "2026-05-03"),
        (1, 280.00, "2026-05-04"),
        (5, 35.00, "2026-05-05"),
        (6, 180.00, "2026-05-06"),
        (7, 320.00, "2026-05-07"),
        (8, 450.00, "2026-05-08")
        ]

cursor.executemany("""
            INSERT INTO venda (id_cliente, valor, data_venda)
            VALUES (?, ?, ?)
            """, vendas)

conn.commit()

print("Banco de dados criado e populado com sucesso!")
print("Arquivo gerado: loja_select.db")
print(" ")

#Questoes da atividade
query_cliente = cursor.execute("""SELECT * FROM cliente;""")
print("1) Todos os clientes: ", query_cliente.fetchall())
print(" ")

query_produto = cursor.execute("""SELECT * FROM produto;""")
print("2) Todos os produtos: ", query_produto.fetchall())
print(" ")

query_produto1 = cursor.execute("""SELECT nome, preco FROM produto;""")
print("3) Apenas nome e preço dos produtos: ", query_produto1.fetchall())
print(" ")

query_produtogreat = cursor.execute("""SELECT nome, preco FROM produto WHERE preco > 100 ORDER BY nome ASC;""")
print("4) Produtos com preço acima de 100: ", query_produtogreat.fetchall())
print(" ")

query_produtoless = cursor.execute("""SELECT nome, preco FROM produto WHERE preco < 500 ORDER BY nome ASC;""")
print("5) Produtos com preço abaixo de 500: ", query_produtoless.fetchall())
print(" ")

query_clientecidade = cursor.execute("""SELECT * FROM cliente WHERE cidade = 'Belém';""")
print("6.1) Clientes de cidade especifica (Belém): ", query_clientecidade.fetchall())
print(" ")

query_cliente_cidade1 = cursor.execute("""SELECT * FROM cliente WHERE cidade = 'Oiapoque';""")
print("6.2) Clientes de cidade especifica (Oiapoque): ", query_cliente_cidade1.fetchall())
print(" ")

query_cliente_cidade2 = cursor.execute("""SELECT * FROM cliente WHERE cidade = 'Santana';""")
print("6.3) Clientes de cidade especifica (Santana): ", query_cliente_cidade2.fetchall())
print(" ")

query_cliente_cidade3 = cursor.execute("""SELECT * FROM cliente WHERE cidade = 'Macapá';""")
print("6.4) Clientes de cidade especifica (Macapá): ", query_cliente_cidade3.fetchall())
print(" ")

query_produtos_estoque= cursor.execute("""SELECT * FROM produto WHERE estoque > 10;""")
print("7) Produtos com estoque maior que 10: ", query_produtos_estoque.fetchall())
print(" ")

query_produtos_estoquepreco = cursor.execute("""SELECT * FROM produto WHERE estoque > 5 AND preco > 100;""")
print("8) Produtos com estoque maior que 5 e preço maior que 100: ", query_produtos_estoquepreco.fetchall())
print(" ")

query_produtos_estoquepreco1 = cursor.execute("""SELECT * FROM produto WHERE estoque > 20 AND preco < 50;""")
print("9) Produtos com estoque maior que 20 e preço menor que 50: ", query_produtos_estoquepreco1.fetchall())
print(" ")

query_clientea = cursor.execute("""SELECT * FROM cliente WHERE nome LIKE 'A%';""")
print("10) Clientes com A: ", query_clientea.fetchall())
print(" ")

query_produto_note = cursor.execute("""SELECT * FROM produto WHERE nome LIKE 'note%';""")
print("11) Produtos com note: ", query_produto_note.fetchall())
print(" ")

query_produto_between = cursor.execute("""SELECT * FROM produto WHERE preco > 100 AND preco < 500;""")
print("12) Produtos com preço entre 100 e 500: ", query_produto_between.fetchall())
print(" ")

query_produto_orderasc = cursor.execute("""SELECT nome, preco FROM produto ORDER BY preco ASC;""")
print("13) Produtos Ordernado pelo preço crescente: ", query_produto_orderasc.fetchall())
print(" ")

query_produto_orderdesc = cursor.execute("""SELECT nome, preco FROM produto ORDER BY preco DESC;""")
print("14) Produtos Ordernado pelo preço decrescente: ", query_produto_orderdesc.fetchall())
print(" ")

query_cliente_order = cursor.execute("""SELECT * FROM cliente ORDER BY nome ASC;""")
print("15) Cliente ordernado pelo nome: ", query_cliente_order.fetchall())
print(" ")


query_produto_orderpreconome = cursor.execute("""SELECT nome, preco FROM produto ORDER BY preco DESC, nome ASC;""")
print("16) Produtos Ordernado pelo preço decrescente e nome crescente: ", query_produto_orderpreconome.fetchall())
print(" ")

conn.close()
