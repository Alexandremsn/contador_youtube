# contador_youtube
aplicação simples, que conta quantas vezes uma palavra específica é dita em um vídeo do youtube

nesta aplicação ela usa uma api da biblioteca youtuvbe transcript api, e extrai a legenda automática do vídeo
ela possui duas grandes limitações a primeira é refente a própria legenda automática que algumas vezes apresenta falhas.
a segunda seria em virtude do fato de estar setada para o portugês, assim vídeos de outras linguas não vão funcionar.

ela pega a api que gera um dict com texto, tempo de legenda e outros parâmtros comuns a um arquivo de legenda tipo srt
depois extrai o texto, normaliza, elimina pontuações e converte em uma lista de palavras
assim realiza a busca pela palavra e retorna o resultado.
