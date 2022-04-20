INSERT INTO usuario (idusuario, nomecompleto, cpf, telefone)
VALUES (1, 'Lucas D Pinto', 12312312313, 99999999);
INSERT INTO raca (idracapet, raca)
VALUES (1, 'pitbull');
INSERT INTO tipo_pet (idtipopet, tipopet)
VALUES (1, 'Cachorro');
INSERT INTO pet (idpet, nomepet, datanascimento, idusuario, idtipopet, idracapet)
VALUES (1, 'jose', '2022-04-17', 1, 1, 1);
INSERT INTO relatorio (idrelatorio, dadosrelatorio)
VALUES (1, '"{''metrics'': ''90%''}"');
INSERT INTO usuario_gera_relatorio (idusuario, idrelatorio)
VALUES (1, 1);
INSERT INTO cabine (idcabine, qrcabine)
VALUES (1, '<?xml version="1.0" encoding="utf-8"?><svg</svg>');