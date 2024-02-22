from django.db import models

# Create your models here.

class Address(models.Model):
    address = models.CharField(verbose_name = 'Rua', max_length =100, null=True, blank=True)
    city = models.CharField(verbose_name = 'Cidade', max_length=50, null=True, blank=True)
    state = models.CharField(verbose_name = 'Estado', max_length=50, null=True, blank=True)
    country = models.CharField(verbose_name = 'Pais', max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = 'endereco'
        verbose_name_plural = 'enderecos'

    def __str__(self):
        return self.address
    
    
    
class Store(models.Model):
    name = models.CharField(verbose_name = "Nome da loja", max_length=150, null=False, blank=False)
    cnpj = models.CharField(verbose_name = "CNPJ", max_length = 20, null=False, blank=False, unique = True)
    date_of_fundation = models.DateField(verbose_name = 'Data da fundação', auto_now = False)
    image = models.ImageField(upload_to='media/products/%Y/%m/%d', null=True, blank=True)
    address = models.ForeignKey(Address, verbose_name = 'Endereço', on_delete= models.CASCADE)

    class Meta:
        verbose_name = 'loja'
        verbose_name_plural = 'lojas'

    def __str__(self):
        return self.name
