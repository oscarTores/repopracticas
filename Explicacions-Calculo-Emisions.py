#!/usr/bin/env python
# coding: utf-8

# # Calculo de emisiones

# El script hace un calculos de las emisiones de CO2 de un transporte para ir al trabajo

# In[1]:


#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 0
DIAS_LABORAIS_SEMANAIS = 0
SEMANAS = 0

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM = 121

cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM
print('O teu consumo é:', cantidade_de_emisions, 'gC02')


# * Script para realizar o cálculo de emisións anuais dunha persoa que viaxa en coche 100kms diarios, 5 días á semana durante 48 semanas do ano

# In[15]:


#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 100
DIAS_LABORAIS_SEMANAIS = 5
SEMANAS = 48

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM = 121

cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM
print('O teu consumo é:', cantidade_de_emisions, 'gC02')


#  * Script para realizar o cálculo de emisións anuais dunha persoa que viaxa en moto 20kms diarios, 3 días á semana, durante 40 semanas do ano

# In[14]:


#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 20
DIAS_LABORAIS_SEMANAIS = 3
SEMANAS = 40

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM = 121

cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM
print('O teu consumo é:', cantidade_de_emisions, 'gC02')


# * Calcula aproximadamente as "túas emisións" para desprazarte ao Wirtz durante todo o curso (aproxima a 24 semanas). Compara os resultados con diferentes medios de transporte

# In[11]:


#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 84.7
DIAS_LABORAIS_SEMANAIS = 2
SEMANAS = 28

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
# Tren de cercanías
EMISION_X_KM = 33
EMISION_X_KM_COCHE = 121
EMISION_X_KM_MOTO = 53

cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM
print('O teu consumo é:', cantidade_de_emisions, 'gC02')
cantidade_de_emisions_coche = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_COCHE
print('O teu consumo se viaxaras en coche sería:', cantidade_de_emisions_coche, 'gC02')
cantidade_de_emisions_moto = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_MOTO
print('O teu consumo se viaxaras en moto sería:', cantidade_de_emisions_moto, 'gC02')


# * Modifica o código do notebook para que calcule o aforro en emisións para un caso definido ao mudar de medio de transporte. É dicir, dados kms, dias e semanas, indica a diferencia entre emisións usando dous medios

# In[18]:


#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 84.7
DIAS_LABORAIS_SEMANAIS = 2
SEMANAS = 28

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
# Tren de cercanías
EMISION_X_KM_USUARIO = 33
EMISION_X_KM_COCHE = 121

def emisiones():
    cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_USUARIO
    print('O teu consumo é:', cantidade_de_emisions, 'gC02')
    cantidade_de_emisions_coche = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_COCHE
    print('O teu ahorro de consumo comparado co coche sería:', (cantidade_de_emisions_coche - cantidade_de_emisions), 'gC02')
emisiones()


# In[ ]:




