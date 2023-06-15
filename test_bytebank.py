from bytebank import Funcionario
import pytest
from pytest import mark

#Método de desenvolvimento ágil de testes Given-When-then
class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = "13/03/2000" #Given-Context
        saida_esperada = 23


        funcionario_teste = Funcionario("Teste", entrada, 1117)
        resultado = funcionario_teste.idade() #When-ação

        assert resultado == saida_esperada #Then-desfecho

    
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho(self):
        entrada = " Lucas Carvalho " #Given
        saida_esperada = "Carvalho"


        lucas = Funcionario(entrada, "11/11/2000", 1117)
        resultado = lucas.sobrenome() #When

        assert resultado == saida_esperada #Then

    @mark.skip
    def test_quando_decrescimo_salario_recebe_cem_mil_deve_retornar_noventa_mil(self):
        entrada_salario = 100000 #Given
        entrada_nome = "Paulo Bragança"
        saida_esperada = 90000

        funcionario_teste = Funcionario(entrada_nome, "11/11/2003", entrada_salario)
        funcionario_teste.decrescimo_salario() #when
        resultado = funcionario_teste.salario()

        assert resultado == saida_esperada #then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 #Given
        saida_esperada = 100

        funcionario_teste = Funcionario('teste', '11/12/2007', entrada)
        resultado = funcionario_teste.calcular_bonus() #when

        assert resultado == saida_esperada #then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000 #Given

            funcionario_teste = Funcionario('teste', '11/11/2001', entrada)
            resultado = funcionario_teste.calcular_bonus() #when

            assert resultado


    def test_retorno_str(self):
        nome, data_nascimento, salario = 'Teste', '11/04/1977', 3500 #given
        saida_esperada = 'Funcionario(Teste, 11/04/1977, 3500)'

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__() #when

        assert resultado == saida_esperada #then