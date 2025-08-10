# Google IT Automation

Projetos do curso "Automating Real-World Tasks with Python", o qual é parte da certificação profissional "Google IT Automation with Python", oferecida pela Google por meio da Coursera.

---

## Módulo 1 (module-1):

Neste módulo, o projeto consistiu em automatizar o processamento de imagens que foram entregues em um formato incorreto, com rotação e tamanho inadequados, para a atualização de um site. A solução implementada utiliza a biblioteca `Pillow` (PIL) para realizar as seguintes manipulações em cada imagem:

1. Rotação: As imagens são rotacionadas em 90 graus no sentido horário.

2. Redimensionamento: O tamanho de cada imagem é ajustado para 128x128 pixels.

3. Conversão e Salvamento: As imagens processadas são convertidas para o formato RGB (caso não estejam) e salvas em formato JPEG na pasta `/opt/icons`.

As imagens originais são obtidas da pasta `images`, e o script foi executado em um ambiente virtual (`.venv`).

*_Note: as pastas mencionadas (`images` e `/opt/icons`) não estão incluídas nesse repositório; a primeira por motivos de otimização e a segunda por motivos de especificidade do sistema operacional (SO)._

### Melhorias para implementar:

- [ ] Tratamento de exceções: Implementar blocos `try-except` para lidar com possíveis erros.

- [ ] Refatoração: Usar `zip` para iterar sobre nomes de arquivos e imagens simultaneamente, eliminando a dependência de índices.

- [ ] Padronização e estilo: Ajustar nomenclatura de variáveis e funções para o padrão da PEP 8.

- [ ] Docstrings: Adicionar docstrings em funções e no módulo.
