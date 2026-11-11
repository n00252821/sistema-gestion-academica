"""
Pruebas unitarias automatizadas para Innovatec Education.
Verifican el cálculo de promedios, validaciones de matrícula y casos límite.
"""
import unittest
from gestion_academica import calcular_promedio, estado_aprobacion, validar_matricula

class TestGestionAcademica(unittest.TestCase):

    def test_calcular_promedio_exitoso(self):
        notas = [14.0, 16.0, 18.0]
        self.assertEqual(calcular_promedio(notas), 16.0)

    def test_calcular_promedio_lista_vacia(self):
        with self.assertRaises(ValueError):
            calcular_promedio([])

    def test_calcular_promedio_nota_invalida(self):
        with self.assertRaises(ValueError):
            calcular_promedio([15.0, 25.0])

    def test_estado_aprobacion_aprobado(self):
        self.assertEqual(estado_aprobacion(15.5), "APROBADO")

    def test_estado_aprobacion_desaprobado(self):
        self.assertEqual(estado_aprobacion(10.0), "DESAPROBADO")

    def test_validar_matricula_exitosa(self):
        resultado = validar_matricula(20, True)
        self.assertTrue(resultado["valido"])

    def test_validar_matricula_con_deuda(self):
        resultado = validar_matricula(20, False)
        self.assertFalse(resultado["valido"])

    def test_validar_matricula_exceso_creditos(self):
        resultado = validar_matricula(30, True)
        self.assertFalse(resultado["valido"])

if __name__ == "__main__":
    unittest.main()
