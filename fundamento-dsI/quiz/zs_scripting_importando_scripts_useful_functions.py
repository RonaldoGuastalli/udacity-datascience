"""Tente você mesmo!Aqui está o código que eu usei no vídeo acima. Crie esses scripts no mesmo diretório e os execute
em seu terminal! Experimente com o bloco if main e acesse objetos do módulo importado!"""

import zt_scripting_importando_scripts_demo as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)

