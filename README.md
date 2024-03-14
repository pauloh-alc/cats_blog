# Cats Blog

## Descrição

Este é um projeto de desenvolvimento de um blog para compartilhamento de posts relacionados a gatos. O objetivo principal é fornecer uma plataforma onde os usuários possam se cadastrar, fazer login, criar, editar e excluir posts, bem como gerenciar informações sobre seus próprios gatos.


## Requisitos de forma resumida

Aqui estão os requisitos detalhados para o Cats Blog:

1. **Registro de Usuário:**
   - Os usuários devem ser capazes de se registrar fornecendo as seguintes informações: username, password, nome do gato e sexo do gato.

2. **Login de Usuário:**
   - Os usuários devem poder fazer login usando seu username e password.

3. **Visualização de Perfil:**
   - Usuários logados devem poder visualizar os dados do seu perfil, incluindo username, nome do gato e sexo do gato.

4. **Edição de Perfil:**
   - Os usuários devem poder editar algumas informações do seu perfil, como nome do gato e sexo do gato.

5. **Exclusão de Conta:**
   - Os usuários devem poder excluir sua conta do blog. Ao excluir a conta, todos os posts associados ao usuário devem ser removidos.

6. **Gerenciamento de Posts:**
   - Usuários logados devem poder criar, editar ou excluir posts. Eles só devem ser capazes de editar ou excluir os posts que eles mesmos criaram.


## DER – diagrama de entidade e relacionamento
![Screenshot](img/der.png)

## No banco
![Screenshot](img/relacionamento-banco.png)

## Instalação e Uso

Para executar o Cats Blog em seu ambiente local, siga estas etapas:

1. Clone este repositório em sua máquina local:

    ```
    git clone git@github.com:pauloh-alc/cats_blog.git
    ```

    ou

    ```
    git clone https://github.com/pauloh-alc/cats_blog.git
    ```

2. Acesse a pasta do projeto:

    bash```
    cd cats_blog
    
3. Crie e ative o ambiente virtual:
   bash```


   bash```
    souce .venv/bin/activate
   
4. Instale as dependências:
   bash```
    pip install -r requirements.txt
   



