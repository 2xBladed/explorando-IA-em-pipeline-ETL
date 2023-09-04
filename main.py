import pandas as pd
import openai
from dotenv import load_dotenv
import os

def generate_ai_tips(name: str) -> str:
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system',
                'content': 'Você é um Economista.'
            },
            {
                'role': 'user',
                'content': f'Apresente uma dica sobre finanças que inclua o nome {name}. (máximo de 100 caracteres)'
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')

def create_markdown_string(id_nome: list) -> str:
    string_md = "| UserID | UserName | Feed |\n|--- |--- |--- |\n"
    for tupla in id_nome:
        string_md += f'| {tupla[0]} | {tupla[1]} | {generate_ai_tips(tupla[1])} |\n'
    return string_md

def create_md(string: str):
    with open('feed.md', 'w', encoding='utf-8') as arq:
        arq.write(string)


if __name__ == '__main__':
    load_dotenv()

    users = []
    openai.api_key = os.getenv('OPENAI_API_KEY')

    tabela = pd.read_csv(os.getenv('CSV_PATH'))
    users = list(zip(tabela.UserID.tolist(), tabela.UserName.tolist()))

    create_md(create_markdown_string(users))
