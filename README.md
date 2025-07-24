
# Assistente Tupiniquim

![Demonstração](static/demo.git.gif)

📝 **Descrição**  
O Assistente Tupiniquim é um projeto de chatbot desenvolvido em Django. Ele permite que usuários se cadastrem, façam login e interajam com um assistente virtual. O histórico das conversas é salvo, permitindo que os usuários vejam suas interações passadas.

O projeto utiliza a API da OpenAI para gerar as respostas do chatbot, proporcionando conversas inteligentes e fluidas.

✨ **Funcionalidades**  
- **Autenticação de Usuários:** Sistema completo de cadastro e login.  
- **Chatbot Inteligente:** Interação em tempo real com o chatbot da OpenAI.  
- **Histórico de Conversas:** As conversas são salvas e podem ser acessadas a qualquer momento pelo usuário.  
- **Interface Simples:** Um layout limpo e intuitivo para uma melhor experiência do usuário.

🚀 **Tecnologias Utilizadas**  
- **Backend:** Python, Django  
- **Frontend:** HTML, CSS (Bootstrap)  
- **API:** OpenAI  
- **Banco de Dados:** SQLite3 (padrão do Django, pode ser alterado)

_Observação:_ O código HTML e o estilo da interface foram desenvolvidos com o auxílio de uma Inteligência Artificial, seguindo minhas instruções e refinamentos até alcançar o resultado atual.

⚙️ **Instalação e Execução**  
Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos  
- Python 3.8+  
- Pip (gerenciador de pacotes do Python)

### Passo a passo  

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/assistente-tupiniquim.git
cd assistente-tupiniquim
```

2. Crie e ative um ambiente virtual:

```bash
# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure suas variáveis de ambiente:  
Crie um arquivo `.env` na raiz do projeto (no mesmo nível que `manage.py`) e adicione sua chave da API da OpenAI:

```env
OPENAI_API_KEY="sua-chave-secreta-da-api-aqui"
```

5. Aplique as migrações do banco de dados:

```bash
python manage.py migrate
```

6. Crie um superusuário (para acessar o painel de admin):

```bash
python manage.py createsuperuser
```
Siga as instruções no terminal para criar seu usuário administrador.

7. Execute o servidor de desenvolvimento:

```bash
python manage.py runserver
```

8. Abra seu navegador e acesse:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver o projeto em ação!

📜 **Licença**  
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
