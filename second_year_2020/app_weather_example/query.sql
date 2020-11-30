-- CREAZIONE TABELLE
DROP TABLE Auto;
CREATE TABLE Auto (
    Targa VARCHAR(7),
    Marca VARCHAR(10),
    Cilindrata INT,
    Potenza INT,
    CodF VARCHAR(5),
    CodAss VARCHAR(5),
    PRIMARY KEY(Targa)
);

-- POPOLAZIONE TABELLE
INSERT INTO Auto(Targa, Marca, Cilindrata, Potenza, CodF, CodAss) VALUES ('AB123CC', 'Toyota', 2200, 180, 'PCC21', 'CC123');

-- QUERY
SELECT targa, Marca
FROM Auto
WHERE Cilindrata > 2000 OR Potenza > 120;

SELECT a.Targa, p.Nome
FROM Auto a 
INNER JOIN Proprietari p
ON a.CodF = p.CodF
WHERE Cilindrata > 2000 OR Potenza > 120;