from Controlador.casa import Casa
from Controlador.departamento import Departamento
from Controlador.terreno import Terreno


casa = Casa("Casa de campo",120000)
departamento = Departamento("duplex",250000)
terreno = Terreno("terreno",80000)

casa.Vender()
departamento.Vender()
terreno.Vender()
