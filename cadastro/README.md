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

### Descrição de operações sobre o cadastro

Sempre que o usuário (stakeholder) quiser subscrever os serviços será direcionado à página de cadastro - para criar um novo. Ou se tiver cadastro criado, sempre que quiser usar os serviços 
subscritos, deverá optar por validar a sua autenticação através do cadastro.

##### Operações básicos de carácter público
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
....
<code>
swagger: "2.0"
info:
  description: "Modelo API do servidor da platforma - DeMoTo Entregas.  Para mais detalhes veja o repositorio DeMoTo - [https://github.com/Lorioux/DeMoto](https://github.com/Lorioux/DeMoto). Para este modelo podera usar chave api `chave-especial` para testar os filtros de autenticacao."
  version: "1.0.0"
  title: "DeMoTo Delivery"
  termsOfService: "http://demoto.io/terms/"
  contact:
    email: "demoto.api@demoto.io"
  license:
    name: "Apache 2.0"
    url: "http://www.apache.org/licenses/LICENSE-2.0.html"
host: "services.nutrilife.io"
basePath: "/v1"
tags:
- name: "cadastro"
  description: "Tudo sobre o seu cadastro"
  externalDocs:
    description: "Detalhes "
    url: "https://github.com/Lorioux/DeMoto/cadastro"
schemes:
- "https"
- "http"
paths:
  /cadastro:
    post:
      tags:
      - "cadastro"
      summary: "Cria novo cadastro de base."
      description: "Operacao de criacao de cadastro com informacao base `usuario, senha, perfil` fornecido atraves do corpo do requisicao (obtidos, por exemplo, a partir de um formulario)."
      operationId: "cria_cadastro"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        description: "Objeto do cadastro que sera adicionado no registros de usuarios da plataforma."
        required: true
        schema:
          $ref: "#/definitions/Cadastro"
      responses:
        "405":
          description: "Entrada de dados envalidos."
      security:
      - demoto_auth:
        - "write:cadastro"
        - "read:cadastro"
    delete:
      tags:
      - "cadastro"
      summary: "Eliminar o cadastro e respetivo perfil."
      description: "Operacao de eliminacao do cadastro relativo a um usuario."
      operationId: "elimina_cadastro"
      consumes:
      - "application/json"
      produces:
      - "application/json"
      parameters:
      - in: "body"
        name: "body"
        description: "Pet object that needs to be added to the store"
        required: true
        schema:
          $ref: "#/definitions/Cadastro"
      responses:
        "400":
          description: "Invalid ID supplied"
        "404":
          description: "Pet not found"
        "405":
          description: "Validation exception"
      security:
      - demoto_auth:
        - "write:cadastro"
        - "read:cadastro"
  /cadastro/usuario:
    get:
      tags:
      - "pet"
      summary: "Procura cadastro por usuario"
      description: "Multiple status values can be provided with comma separated strings"
      operationId: "findPetsByStatus"
      produces:
      - "application/xml"
      - "application/json"
      parameters:
      - name: "status"
        in: "query"
        description: "Status values that need to be considered for filter"
        required: true
        type: "array"
        items:
          type: "string"
          enum:
          - "available"
          - "pending"
          - "sold"
          default: "available"
        collectionFormat: "multi"
      responses:
        "200":
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/Cadastro"
        "400":
          description: "Invalid status value"
      security:
      - demoto_auth:
        - "write:cadastro"
        - "read:cadastro"
  /cadastro/estado:
    get:
      tags:
      - "pet"
      summary: "Finds Pets by tags"
      description: "Muliple tags can be provided with comma separated strings. Use         tag1, tag2, tag3 for testing."
      operationId: "findPetsByTags"
      produces:
      - "application/xml"
      - "application/json"
      parameters:
      - name: "tags"
        in: "query"
        description: "Tags to filter by"
        required: true
        type: "array"
        items:
          type: "string"
        collectionFormat: "multi"
      responses:
        "200":
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: "#/definitions/Pet"
        "400":
          description: "Invalid tag value"
      security:
      - petstore_auth:
        - "write:pets"
        - "read:pets"
      deprecated: true
  /cadastro/{usuario}:
    get:
      tags:
      - "cadastro"
      summary: "Procura o cadastro por usuario"
      description: "Returns a single pet"
      operationId: "procura_usuario"
      produces:
      - "application/json"
      parameters:
      - name: "usuario"
        in: "path"
        description: "ID of pet to return"
        required: true
        type: "string"
        format: "String"
      responses:
        "200":
          description: "successful operation"
          schema:
            $ref: "#/definitions/Cadastro"
        "400":
          description: "Invalid ID supplied"
        "404":
          description: "Pet not found"
      security:
      - api_key: []
    post:
      tags:
      - "cadastro"
      summary: "Updates a pet in the store with form data"
      description: ""
      operationId: "updatePetWithForm"
      consumes:
      - "application/x-www-form-urlencoded"
      produces:
      - "application/json"
      parameters:
      - name: "usuario"
        in: "path"
        description: "ID of pet that needs to be updated"
        required: true
        type: "string"
        format: "String"
      - name: "name"
        in: "formData"
        description: "Updated name of the pet"
        required: false
        type: "string"
      - name: "status"
        in: "formData"
        description: "Updated status of the pet"
        required: false
        type: "string"
      responses:
        "405":
          description: "Invalid input"
      security:
      - petstore_auth:
        - "write:pets"
        - "read:pets"
    delete:
      tags:
      - "pet"
      summary: "Deletes a pet"
      description: ""
      operationId: "deletePet"
      produces:
      - "application/xml"
      - "application/json"
      parameters:
      - name: "api_key"
        in: "header"
        required: false
        type: "string"
      - name: "petId"
        in: "path"
        description: "Pet id to delete"
        required: true
        type: "integer"
        format: "int64"
      responses:
        "400":
          description: "Invalid ID supplied"
        "404":
          description: "Pet not found"
      security:
      - petstore_auth:
        - "write:pets"
        - "read:pets"
  /cadastro/{usuario}/uploadImage:
    post:
      tags:
      - "usuario"
      summary: "uploads an image"
      description: ""
      operationId: "uploadFile"
      consumes:
      - "multipart/form-data"
      produces:
      - "application/json"
      parameters:
      - name: "usuario"
        in: "path"
        description: "ID of pet to update"
        required: true
        type: "integer"
        format: "int64"
      - name: "additionalMetadata"
        in: "formData"
        description: "Additional data to pass to server"
        required: false
        type: "string"
      - name: "file"
        in: "formData"
        description: "file to upload"
        required: false
        type: "file"
      responses:
        "200":
          description: "successful operation"
          schema:
            $ref: "#/definitions/ApiResponse"
      security:
      - petstore_auth:
        - "write:pets"
        - "read:pets"
securityDefinitions:
  demoto_auth:
    type: "oauth2"
    authorizationUrl: "http://auth.demoto.io/oauth/dialog"
    flow: "implicit"
    scopes:
      write:cadastro: "modify pets in your account"
      read:cadastro: "read your pets"
  api_key:
    type: "apiKey"
    name: "api_key"
    in: "header"
definitions:
  Order:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      petId:
        type: "integer"
        format: "int64"
      quantity:
        type: "integer"
        format: "int32"
      shipDate:
        type: "string"
        format: "date-time"
      status:
        type: "string"
        description: "Order Status"
        enum:
        - "placed"
        - "approved"
        - "delivered"
      complete:
        type: "boolean"
        default: false
    xml:
      name: "Order"
  Category:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      name:
        type: "string"
    xml:
      name: "Category"
  User:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      username:
        type: "string"
      firstName:
        type: "string"
      lastName:
        type: "string"
      email:
        type: "string"
      password:
        type: "string"
      phone:
        type: "string"
      userStatus:
        type: "integer"
        format: "int32"
        description: "User Status"
    xml:
      name: "User"
  Tag:
    type: "object"
    properties:
      id:
        type: "integer"
        format: "int64"
      name:
        type: "string"
    xml:
      name: "Tag"
  Cadastro:
    type: "object"
    required:
    - "usuario"
    - "senha"
    - "perfil"
    - "estado"
    properties:
      id:
        type: "integer"
        format: "int64"
      category:
        $ref: "#/definitions/Category"
      name:
        type: "string"
        example: "doggie"
      photoUrls:
        type: "array"
        xml:
          name: "photoUrl"
          wrapped: true
        items:
          type: "string"
      tags:
        type: "array"
        xml:
          name: "tag"
          wrapped: true
        items:
          $ref: "#/definitions/Tag"
      status:
        type: "string"
        description: "pet status in the store"
        enum:
        - "available"
        - "pending"
        - "sold"
    xml:
      name: "Pet"
  ApiResponse:
    type: "object"
    properties:
      code:
        type: "integer"
        format: "int32"
      type:
        type: "string"
      message:
        type: "string"
externalDocs:
  description: "Find out more about Swagger"
  url: "http://swagger.io"

</code>
