# explorando-IA-em-pipeline-ETL

Repositório destinado ao desafio de projeto da DIO: Explorando IA Generativa em um Pipeline de ETL com Python

# Documentação gerada pelo chatGPT

O script a seguir é responsável por criar um documento Markdown contendo uma tabela com informações sobre usuários e dicas financeiras personalizadas geradas por um modelo de linguagem GPT-3.5 Turbo da OpenAI. O script é destinado a criar uma representação visualmente amigável dessas informações em um arquivo Markdown chamado "feed.md". O script consiste em três funções principais e um bloco condicional que executa o script quando o arquivo é chamado diretamente.

1. Importa os módulos necessários, como os, pandas e dotenv, disponíveis no arquivo **requirements.txt** que são usados para configurar as variáveis de ambiente e ler um arquivo CSV.

2. Configura a chave de API da OpenAI a partir de uma variável de ambiente (**OPENAI_API_KEY**) no arquivo **.env** usando a biblioteca dotenv.

3. **(Extract)** Lê os dados de um arquivo CSV cujo caminho é especificado em uma variável de ambiente (**CSV_PATH**).

4. Cria uma lista de tuplas contendo informações de usuário (UserID e UserName) a partir dos dados lidos do arquivo CSV.

5. **(Transform)** Chama a função **create_markdown_string** para criar a tabela Markdown com dicas financeiras personalizadas.

6. **(Load)** Chama a função **create_md** para salvar a tabela Markdown em um arquivo chamado **"feed.md"**.

### Exemplo de arquivo **feed.md**

| UserID | UserName | Feed |
|--- |--- |--- |
| 1 | Maria | Maria, diversifique seus investimentos para reduzir riscos. |
| 2 | Arthur | Arthur, planeje seu orçamento e evite gastos supérfluos. |
| 3 | Gabriel | Gabriel, invista com sabedoria e pense no longo prazo. |
| 4 | Ícaro | Ícaro, evite dívidas altas e mantenha um fundo de emergência. |
| 5 | Camila | Camila, controle os gastos e poupe para seus objetivos financeiros. |
