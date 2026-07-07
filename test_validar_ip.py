import unittest

from validar_ip import es_ip_valida 

class TestValidarIP(unittest.TestCase):

    def test_ip_valida(self):
        """Probar una IP completamente válida"""
        self.assertTrue(es_ip_valida("192.168.1.1"))
        self.assertTrue(es_ip_valida("0.0.0.0"))

    def test_ip_octeto_mayor_255(self):
        """Probar IP con un octeto fuera de rango (>255)"""
        self.assertFalse(es_ip_valida("192.168.1.300"))
        self.assertFalse(es_ip_valida("256.100.10.1"))

    def test_ip_con_letras(self):
        """Probar IP que contiene caracteres alfabéticos"""
        self.assertFalse(es_ip_valida("192.168.1.abc"))
        self.assertFalse(es_ip_valida("192.1a.1.1"))

    def test_ip_partes_incorrectas(self):
        """Probar IPs con más o menos de 4 partes (octetos)"""
        self.assertFalse(es_ip_valida("192.168.1"))       # 3 partes
        self.assertFalse(es_ip_valida("192.168.1.1.1"))   # 5 partes

    def test_ip_ceros_a_la_izquierda(self):
        """Probar casos con ceros a la izquierda (leading zeros)"""
        # Tu función actual rechaza "192.168.01.1" porque len > 1 y empieza con '0'
        self.assertFalse(es_ip_valida("192.168.01.1"))

if __name__ == "__main__":
    unittest.main()