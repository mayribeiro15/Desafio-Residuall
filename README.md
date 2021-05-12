# Desafio-Residuall
 
O código em Python se refere a resolução do desafio de BackEnd da Residuall, com o objetivo de criar um pequeno servidor que retorna se um email é válido ou não.

O servidor tem duas rotas de acesso ("/" e "/health") simplificadas para criação e teste, que se referem a tarefa 1 do desafio. Além disso, a aplicação criada contempla duas versões de validação do email chamadas V1 e V3. Foi criado também um bando de dados MongDB chamado Validation para armazenamento das respostas a cada requisição.

■ A validação V1 ocorre na rota "/mail/validation/v1" e considera válidos os emails terminados em: ".com.br", ".com", ".gov.br" e ".org". Os resultados são armazenados em uma tabela chamada Validation_V1 no banco de dados. A requisição passa os endereços de email como um array, assim múltiplos emails podem ser avaliados e armazenados com apenas uma requisição. A resposta HTTP foi obtida corretamente.

■ A validação V3 ocorre na rota "/mail/validation/v3" e analisa o emails utilizando a api pública EVA https://eva.pingutil.com/.
A resposta HTTP da API foi obtida corretamenta, entretanto a resposta HTTP final não foi bem sucedida devido a dificuldade de recuperar cada parâmetro no código. A requisição passa os endereços de email como um array, assim múltiplos emails podem ser avaliados com apenas uma requisição (é importante ressaltar que esse detalhe não interferiu no erro da resposta HTTP).

A implementação descrita acima contempla as tarefas 1, 2, 3, 4 e 5 do desafio. As tarefas 6 e 7, que se relacionavam ao banco de dados para a validação V3, não foram implementadas por dificuldades relacionadas a sintaxe e a estrutura da API na passagem das informações. As tarefas 8, 9 e 10 foram deixadas como última prioridade pois não havia experiência prévia com as ferramentas utilizadas, por isso não foram implementadas. 
Portanto, ficou faltando implementar as tarefas restantes e corrigir os erros apresentados.
