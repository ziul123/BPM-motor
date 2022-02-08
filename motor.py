import sqlite3 as sql
import time

fetch_vertice = "SELECT Vertice.descricao, Vertice.tipo, Vertice.prox, Vertice.prox_true, Vertice.prox_false, Raia.nome, Piscina.descricao FROM Vertice join Raia ON Vertice.r_id=Raia.id JOIN Piscina ON Raia.p_id=Piscina.id where Vertice.id=?"

def create(name):
	with open("create.sql", "r") as f:
		con = sql.connect(name)
		con.executescript(f.read())
		con.close()
	print("BD criado")




def insert(con):
	op = input("Comando de inserção:\n")
	try:
		con.execute(op)
		print("Valores inseridos com sucesso")
		
	except sql.Error as e:
		print(e)
	
	
def select(con):
	op = input("Comando de seleção:\n")
	try:
		cur = con.execute(op)
		print(*cur.fetchall(), sep='\n')
		
	except sql.Error as e:
		print(e)



def motor():
	con = sql.connect("bpm.db")
	v = 1
	while True:
		row = con.execute(fetch_vertice, (v,)).fetchone()
		v_desc, v_tipo, v_prox, v_prox_t, v_prox_f, r_nome, p_desc = row
		
		print(f"Executando {v_desc} da raia {r_nome} da piscina {p_desc}")
		
		if v_tipo == "G":
			cond = True if input("True or False?\n") == "True" else False
			v = v_prox_t if cond else v_prox_f
		elif v_tipo == "I" or v_tipo == "T":
			v = v_prox
		elif v_tipo == "F":
			break
		
		time.sleep(2)


def ligar_vertices(con):
	while True:
		verts = [int(x) for x in input().split()]
		if len(verts) == 2:
			con.execute("UPDATE Vertice SET prox=? WHERE id=?", tuple(verts[::-1]))
		elif len(verts) == 3:
			con.execute("UPDATE Vertice SET prox_false=?, prox_true=? WHERE id=?", tuple(verts[::-1]))
		elif len(verts) == 1:
			break



def main():
	while True:
		op = input("Selecione o que fazer:\n1:Criar DB\n2:Inserir em tabela\n3:Visualizar tabela\n4:Ligar vertices\n5:Motor\n6:Sair\n")
		con = sql.connect("bpm.db")
		if op == '1':
			create()
		elif op == '2':
			insert(con)
		elif op == '3':
			select(con)
		elif op == '4':
			ligar_vertices(con)
		elif op == '5':
			try:
				motor()
			except Exception as e:
				print(e)
		elif op == '6':
			quit()
			
		con.commit()
		con.close()
		time.sleep(2)

if __name__ == '__main__':
	main()


