""" from smoketest import SmokeTest
from core.models import PontoTuristico


# teste de leitura e escrita no BD
class DemoTest(SmokeTest):
    
    def test_ponto_turistico_reads(self):
        cnt = PontoTuristico.objects.all().count()
        self.assertTrue(cnt > 0)

    def test_ponto_turistico_writes(self):
        f = PontoTuristico.objects.create() """