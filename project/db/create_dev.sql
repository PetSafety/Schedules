-- -----------------------------------  << Programação do SGBD (TRIGGERS) >>  -----------------------------------
--
--                                            SCRIPT DE CRIAÇÃO (DDL)                                            
--
-- Data Criacao ...........: 03/04/2022
-- Autor(es) ..............: Caio V. F. de Araujo
-- Banco de Dados .........: MySQL 8.0.22
-- Base de Dados (nome) ...: PetSafety
--
--
-- PROJETO => 01 Base de Dados
--         => z Tabelas
--
-- --------------------------------------------------------------------------------------------------------------

-- BASE DE DADOS
CREATE DATABASE PetSafety
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;
USE PetSafety;


-- TABELAS
CREATE TABLE USUARIO (
    idUsuario INT AUTO_INCREMENT NOT NULL,
    nomeCompleto VARCHAR(200) NOT NULL,
    cpf INT(11) NOT NULL,
    telefone INT(11) NOT NULL,

    CONSTRAINT USUARIO_PK PRIMARY KEY (idUsuario)
) ENGINE = InnoDB  AUTO_INCREMENT = 1;

CREATE TABLE RACA (
    idRacaPet INT AUTO_INCREMENT NOT NULL,
    raca VARCHAR(30) NOT NULL,

    CONSTRAINT RACA_PK PRIMARY KEY (idRacaPet)
) ENGINE = InnoDB  AUTO_INCREMENT = 1;

CREATE TABLE TIPO_PET (
    idTipoPet INT AUTO_INCREMENT NOT NULL,
    tipoPet ENUM('Cachorro','Gato') NOT NULL,

    CONSTRAINT TIPO_PET_PK PRIMARY KEY (idTipoPet)
) ENGINE = InnoDB  AUTO_INCREMENT = 1;

CREATE TABLE PET (
    idPet INT AUTO_INCREMENT NOT NULL,
    nomePet VARCHAR(200) NOT NULL,
    dataNascimento DATETIME NOT NULL,
    idUsuario INT NOT NULL,
    idTipoPet INT NOT NULL,
    idRacaPet INT NOT NULL,

    CONSTRAINT PET_PK PRIMARY KEY (idPet),
    CONSTRAINT USUARIO_FK FOREIGN KEY (idUsuario)
        REFERENCES USUARIO (idUsuario)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT TIPO_PET_FK FOREIGN KEY (idTipoPet)
        REFERENCES PET (idTipoPet)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT RACA_PET_FK FOREIGN KEY (idRacaPet)
        REFERENCES PET (idRacaPet)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE = InnoDB  AUTO_INCREMENT = 1;

CREATE TABLE RELATORIO (
    idRelatorio INT AUTO_INCREMENT NOT NULL,
    dadosRelatorio json NOT NULL,

    CONSTRAINT RELATORIO_PK PRIMARY KEY (idRelatorio)
) ENGINE = InnoDB  AUTO_INCREMENT = 1;

CREATE TABLE usuario_gera_relatorio (
    idUsuario INT NOT NULL,
    idRelatorio INT NOT NULL,

    CONSTRAINT possui_USUARIO_FK FOREIGN KEY (idUsuario)
        REFERENCES USUARIO (idUsuario)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT possui_RELATORIO_FK FOREIGN KEY (idRelatorio)
        REFERENCES RELATORIO (idRelatorio)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE = InnoDB  AUTO_INCREMENT = 1;


CREATE TABLE CABINE (
    idCabine INT AUTO_INCREMENT NOT NULL,
    qrCabine VARCHAR(200) NOT NULL,

    CONSTRAINT CABINE_PK PRIMARY KEY (idCabine)
) ENGINE = InnoDB  AUTO_INCREMENT = 1;

CREATE TABLE TRANSPORTE (
    idTransporte INT AUTO_INCREMENT NOT NULL,
    dataViagem TIMESTAMP NOT NULL,
    origem VARCHAR(40) NOT NULL,
    destino VARCHAR(40) NOT NULL,
    voo json NOT NULL,
    idPet INT NOT NULL,
    idCabine INT NOT NULL,

    CONSTRAINT TRANSPORTE_PK PRIMARY KEY (idTransporte),

    CONSTRAINT PET_FK FOREIGN KEY (idPet)
        REFERENCES PET (idPet)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT CABINE_FK FOREIGN KEY (idCabine)
        REFERENCES CABINE (idCabine)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE = InnoDB  AUTO_INCREMENT = 1;