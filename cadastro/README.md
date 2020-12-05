### Cadasto

O cadastro é recurso da plataforma necessário para o registo inicial basico para o acesso do resto dos serviços de registo. Um cadastro neste contexto, é um modelo com os campos:
<ul>
  <li> usuario - representa o usuário para o acesso ao perfil que for criado.</li>
  <li> senha - representa a senha de acesso ao perfil que for criado.</li>
  <li> perfil - representa o perfil da subscrição que for criado.</li>
  <li> chave - representa a chave-parcial de desincriptacao dos dados de perfils </li>
  <li> criado_em - representa a data de criacao do perfil</li>
  <li> modificado_em - representa a data de modificação do quaisquer dados do cadastro</li>
  <li> estado - representa estado do perfil associado ao cadastro (ex.: pendente, ativo, inativo, suspenso, etc.)</li>
</ul>

### Operações sobre o cadastro

Sempre que o usuário (stakeholder) quiser subscrever os serviços será direcionado à página de cadastro - para criar um novo. Ou se tiver cadastro criado, sempre que quiser usar os serviços  subscritos, deverá optar por validar a sua autenticação através do cadastro.
<ul>
  <li>criacao do cadastro</li>
  <li>pesquisa de cadastro por usuário </li>
  <li>lpesquisa de cadastros por perfil </li>
  <li>pesquisa de cadastros por estado</li>
  <li>modificação do perfil escolhido</li>
  <li>modificação do estado</li>
  <li>modificação da senha</li>
  <li>eliminação do cadastro</li>
</ul>

### Modelo REST API de operacoes do cadastro
#### Criacao do cadastro
<pre>....
[
  {
    "descricao": "criacao de novo cadastro",
    "operacao": "novo-cadastro",
    "url" :  "/cadastro/",
    "dados" : {
      "usuario":"",
      "senha":"",
      "perfil":"",
    }
  }
] </pre>

#### Pesquisa de cadastro por usuario
<pre>....
[
  {
    "descricao": "pesquisa de cadastro por usuario",
    "operacao": "usuario",
    "url" :  "/cadastro/usuario/inscrito/",
    "dados" : {
      "usuario":"",
    }
  }
] </pre>

#### Pesquisa de cadastros por perfil
<pre>....
[
  {
    "descricao": "pesquisa de cadastros por perfil",
    "operacao": "procura_cadastros_por_perfil",
    "url" :  "/cadastro/perfil/",
    "dados" : {
      "perfil":[""],
    }
  }
] </pre>

#### Pesquisa de cadastros por estado
<pre>....
[
  {
    "descricao": "pesquisa de cadastros por estado",
    "operacao": "procura_cadastros_por_estado",
    "url" :  "/cadastro/estado/",
    "dados" : {
      "estado":[""],
    }
  }
] </pre>

#### Modificacao do perfil de cadastro
<pre>....
[
  {
    "descricao": "modificacao do perfil do cadastro",
    "operacao": "modifica_perfil_cadastro",
    "url" :  "/cadastro/usuario/perfil/",
    "dados" : {
      "usuario":"",
      "perfil":"",
    }
  }
] </pre>

#### Modificacao do estado de cadastro
<pre>....
[
  {
    "descricao": "modificacao do estado do cadastro",
    "operacao": "modifica_perfil_cadastro",
    "url" :  "/cadastro/usuario/estado/",
    "dados" : {
      "usuario":"",
      "estado":"",
    }
  }
] </pre>

#### Modificacao da senha de cadastro
<pre>....
[
  {
    "descricao": "modificacao da senha do cadastro",
    "operacao": "modifica_senha_cadastro",
    "url" :  "/cadastro/usuario/senha/",
    "dados" : {
      "usuario":"",
      "senha":"",
    }
  }
] </pre>

#### Eliminacao de cadastro
<pre>....
[
  {
    "descricao": "Eliminacao do cadastro",
    "operacao": "elimina_cadastro",
    "url" :  "/cadastro/",
    "dados" : {
      "usuario":"",
      "senha":""
    }
  }
] </pre>