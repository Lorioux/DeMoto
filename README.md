# DeMoTo - plataforma de serviços de entrega para pequenos negócios 

 
 

O projeto DeMoTo é desenvolvido numa abordagem de arquitetura de microserviços de gestão de entrega de encomendas. Os principais intervenientes desse tipo de serviços são: os consumidores (que iniciam o processo), os fornecedores (que preparam as encomendas), e os condutores (que entregam as encomendas). Também, torna-se necessário a existência de agentes (intermediários na aquisição de usuários da plataforma). Alem do mais, outros intervenientes são os serviços bancários que facultam os processamentos de pagamentos. 

 

## Escopo de serviços 

### 1.0 Serviços de cadastro de usuários 

Todos os usuários da plataforma têm a possibilidade de se cadastrar para a utilização segura dos serviços oferecidos. O cadastro de cada parte interessada dos principais intervenientes, depende em parte do perfil pretendido. 
<ul>
<li>Um usuário sempre tem o nome completo, data de nascimento, a morada, os contactos, e sempre que necessário o NIF. </li>

<li>Um usuário fornecedor sempre terá que ser associado a um estabelecimento comercial registadas nos serviços das finanças. </li>
</ul>

 

### 2.0 Serviços de cadastro de produtos 

Os produtos são os principais elementos de transação e interação nesta plataforma. Antes que ocorra qualquer transação entre as partes interessadas, há um produto cadastrado ser oferecido (em venda). O cadastro de produtos, depende da sua categoria e natureza. Entretanto, todos os produtos têm o nome (opcionalmente a marca), o preço, a percentagem de desconto (opcional), a quantidade ou unidades ou volume. 

 

### 3.0 Serviço de estabelecimentos 

Além da pessoa do Fornecedor, torna-se necessário o cadastro do estabelecimento comercial (entidade comercial legal) relacionado. O estabelecimento comercial tem o nome comercial, a marca registada, a morada fiscal, morada geográfica, o NIF, o logotipo.  

 

### 4.0 Serviço de pedidos 
 

Como se pode esperar um pedido seria iniciado por um usuário (Consumidor) previamente registado na plataforma. Assim sendo, em todos pedidos feitos requer-se a autenticação do usuário. Quando validado, o usuário o pedido será registado temporariamente, de seguida procede-se a notificação de um ou vários fornecedores da existência do pedido. 

Os fornecedores avaliam pedido e propõe e o tempo de entrega da encomenda. Feita a proposta o cliente e solicitado a confirmar (aceitar a proposta), juntamente com outras propostas opcionais. Sempre que o usuário (Consumidor) aceitar a proposta, o fornecedor é notificado a preparar a encomenda e em simultâneo os condutores que se encontram nas mediações recebem a notificação para a recolha da encomenda. 

O condutor que aceitar a oferta em primeiro é atribuído a recolha da encomenda e recebe é bonificado. Daqui em diante o consumidor mantém-se informado a trajeto e estado da encomenda, por receber notificações de atualização. 

 

### 5.0 Serviço de pagamentos 

Sempre que o condutor fizer a entregada, por confirmar a morada do consumidor à porta do consumidor procede-se o registo definitivo da compra, e o processamento do pagamento. Quando terminado o processamento do pagamento com sucesso, o consumidor é notificado e recebe o recibo do seu pagamento. 

### 6.0 Serviços de reclamação 

… 

### 7.0 Serviço de publicidade 

… 

 