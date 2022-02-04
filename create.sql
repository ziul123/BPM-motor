PRAGMA foreign_keys = TRUE;

CREATE TABLE Piscina(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	descricao VARCHAR(30)
);


CREATE TABLE Raia(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(30),
	p_id INT NOT NULL,
	FOREIGN KEY (p_id) REFERENCES Piscina(id)
);


CREATE TABLE Vertice(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	descricao VARCHAR(30),
	tipo CHAR(1) NOT NULL,
	prox INT,
	prox_true INT,
	prox_false INT,
	r_id INT NOT NULL,
	FOREIGN KEY (r_id) REFERENCES Raia(id),
	CHECK (tipo IN('I','F','T','G')),--inicio, fim, tarefa ou gateway
	CHECK ((prox ISNULL AND tipo IN('F','G')) OR (prox_true ISNULL AND prox_false ISNULL AND tipo IN('I','T','F')))
);





