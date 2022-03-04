from youtube_transcript_api import YouTubeTranscriptApi as yta
import nltk
print("Bem-vindo ao contador de palavras do Youtube")
print('Insira um endereço de um vídeo do youtube e a palavra desejada')
print('o programa vai contar quantas vezes é dita a palavra no vídeo')
## recebe os parâmetros
url = input("Digite o endereço do vídeo:")
palavraoriginal = input("Digite a palvra a ser contada:")
palavra = palavraoriginal.lower()
separador = (url.find('='))+1
## extrai a id do vídeo do endereço
vid_id = url[separador:]
dados = yta.list_transcripts(vid_id).find_transcript(['pt', 'en']).fetch()
## gera um dict com os parâmetros de legenda
transcricao = ''
for valor in dados:
    for key,val in valor.items():
        if key == 'text':
            transcricao += val
## separa apenas o texto dos parâmetros de legenda
transcricao = transcricao.lower()
## normaliza o texto
lista_tokens = nltk.tokenize.word_tokenize(transcricao)
lista_palavras =[]
for token in lista_tokens:
    if token.isalpha():
        lista_palavras.append(token)
## separa o texto em tokens e remove pontucao
numero_ocorrencias = lista_palavras.count(palavra)
## conta o número de vezes que a palvra aparece na listagem de tokens
print(f'No vídeo foram ditas {len(lista_palavras)}, palvras !!!')
print(f"Foram ditas {numero_ocorrencias} vezes a palavra {palavraoriginal}")
## exibe o resiltado