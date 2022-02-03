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
	r_id INT NOT NULL,
	FOREIGN KEY (r_id) REFERENCES Raia(id)
);


CREATE TABLE Evento(
	v_id INT NOT NULL PRIMARY KEY,
	proc INT,
	tipo CHAR(1) CHECK (tipo IN('I','F')),
	FOREIGN KEY (v_id) REFERENCES Vertice(id),
	FOREIGN KEY (proc) REFERENCES Vertice(id)
);


CREATE TABLE Task(
	v_id INT NOT NULL PRIMARY KEY,
	proc INT,
	FOREIGN KEY (v_id) REFERENCES Vertice(id),
	FOREIGN KEY (proc) REFERENCES Vertice(id)
);


CREATE TABLE Gateway(
	v_id INT NOT NULL PRIMARY KEY,
	proc_true INT,
	proc_false INT,
	FOREIGN KEY (proc_true) REFERENCES Vertice(id),
	FOREIGN KEY (proc_false) REFERENCES Vertice(id)
);

--test


