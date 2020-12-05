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
  <li>leitura do usuário </li>
  <li>leitura do perfil escolhido </li>
  <li>leitura do estado</li>
  <li>modificação do perfil escolhido</li>
  <li>modificação do estado</li>
  <li>modificação da senha</li>
  <li>eliminação do cadastro</li>
</ul>

#### Modelo REST API
<pre>....

</pre>
