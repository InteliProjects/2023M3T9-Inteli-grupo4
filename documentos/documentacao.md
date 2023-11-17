# Documentação Modelo Preditivo - Inteli

## AnalisIA
### Nymbus Tech
#### Integrantes: Eduardo Henrique Dos Santos, Fernando Antonio Sampaio Cabral de Vasconcellos, Gustavo Machado Esteves, Lídia Cruz Mariano, Mateus Marçal Barbosa de Melo Góis, Paulo Octávio de Paula, Rafaella Bianca Cavalcante.

## Sumário
[1. Introdução](#c1)

[2. Objetivos e Justificativa](#c2)

[3. Metodologia](#c3)

[4. Desenvolvimento e Resultados](#c4)

[5. Conclusões e Recomendações](#c5)

[6. Referências](#c6)

[Anexos](#attachments)

## <a name="c1"></a>1. Introdução

&emsp;Este documento apresenta uma iniciativa estratégica voltada para aprimorar a tomada de decisões da empresa Mobly, referência no setor de móveis e decoração. Como um parceiro de negócio, o produto visa abordar uma questão crítica que a empresa enfrenta em sua operação de controle de demanda. Para entender melhor a relevância e a abordagem desse projeto, é essencial entender o contexto em que a Mobly está inserida atualmente.

&emsp;Fundada em 2011, a Mobly é uma renomada empresa brasileira sediada na cidade de São Paulo. O negócio se destaca pelo seu amplo catálogo de produtos de qualidade, que abrange desde móveis para todos os ambientes até artigos decorativos exclusivos. A empresa conquistou uma posição de destaque no mercado ao oferecer soluções inovadoras e sofisticadas para consumidores que buscam transformar suas casas por um preço acessível no mercado [[1]](#c7).

&emsp;A Mobly é uma empresa amplamente reconhecida como uma referência no varejo do setor de móveis e decoração. Com um catálogo extremamente abrangente, contendo aproximadamente 275 mil itens que englobam tanto mobiliários quanto objetos de decoração, a Mobly oferece aos seus clientes uma extensa variedade de opções para aprimorar seus ambientes com estilo e funcionalidade. Sua sólida posição no mercado é resultado de um compromisso inabalável com a inovação tecnológica e a qualidade dos produtos, consolidando sua reputação como uma escolha de excelência para os consumidores em busca de soluções de mobiliário e decoração [[1]](#c7). Além disso, a Mobly se destacou como pioneira ao introduzir uma experiência inovadora em seu aplicativo, incluindo recursos como realidade aumentada e cenários 3D, simplificando a visualização de móveis para os compradores e aprimorando a compreensão espacial dos produtos. A empresa atende clientes em todo o Brasil com entregas abrangentes, com lojas virtuais situadas em seu site, aplicativo e marketing places, enquanto suas lojas físicas estão localizadas exclusivamente em São Paulo [[2]](#c8).

&emsp;Apesar de sua posição privilegiada no mercado, a Mobly enfrenta um desafio significativo relacionado à gestão de estoque e previsão de demanda. Atualmente, a empresa baseia suas decisões de compra de estoque em análises retrospectivas, ou seja, considera os dados históricos de vendas para projetar suas necessidades futuras [Kickoff, 2023]. No entanto, essa abordagem não se mostra eficaz o suficiente para lidar com a dinâmica e a complexidade do mercado atual. O problema central reside na falta de uma tecnologia adequada que permita que a Mobly antecipe com precisão a demanda futura, evitando o excesso de estoque e assegurando que os produtos estejam disponíveis no momento certo e na quantidade adequada. Essa limitação pode resultar em desafios operacionais, financeiros e de competitividade, tornando essencial a busca por soluções inovadoras que otimizem a previsão de demanda e impulsionem a eficiência e rentabilidade da Mobly.

## <a name="c2"></a>2. Objetivos e Justificativa
### 2.1 Objetivos

&emsp;A Mobly, nossa parceira de negócios, está enfrentando alguns desafios relacionados ao controle de seu estoque de produtos que são vendidos. Os funcionários da empresa não têm informações precisas sobre quais produtos devem manter em estoque. Isso acontece porque eles não possuem um sistema que possa prever quanto custa manter esses produtos em estoque, nem quando esses produtos serão vendidos para gerar receita.

&emsp;Para resolver esses problemas, estamos propondo a criação de um modelo de previsão. Esse modelo vai nos ajudar a prever quanto de cada produto será necessário em nosso estoque a cada dia e semana. Cada produto tem um código único chamado de SKU (Stock Keeping Unit, ou Unidade de Manutenção de Estoque) [[3]](#c9), que nos ajuda a identificá-lo. Nosso objetivo é fazer com que esse modelo seja preciso em cerca de 70% das previsões diárias e 90% das previsões semanais.

&emsp;Com este projeto, busca-se o desenvolvimento de um sistema que auxilie a Mobly na tomada de decisões estratégicas para a gestão de seu estoque de vendas. Atingir as metas de precisão estabelecidas permitirá à empresa manter níveis de estoque mais eficientes, garantindo a disponibilidade de produtos para atender à demanda dos clientes, ao mesmo tempo em que reduz os custos operacionais. Isso possibilitará maior eficiência e aprimoramento do atendimento aos clientes.

### 2.2 Justificativa

#### Defesa da Proposta de Solução: Modelo Preditivo de Estoque para a Mobly

&emsp;Durante a entrevista de kickoff (2023), os representantes da Mobly apresentaram os problemas atualmente enfrentados pela falta de um modelo preditivo funcional. Dentre eles, o principal é o tempo decorrido desde o planejamento da compra até o reabastecimento do estoque, que se ramifica entre a utilização de parâmetros históricos para a medição de venda dos últimos 30 a 60 dias, contatação dos fornecedores e diversas reuniões para a tomada dessas decisões, além de demais etapas. A introdução do Modelo Preditivo de Estoque na Mobly representa uma abordagem inovadora e altamente eficaz para aprimorar as operações de supply chain e otimizar a gestão de inventário. Este sistema tem o potencial de revigorar a forma como a Mobly gerencia seu estoque, trazendo consigo uma série de benefícios substanciais e se destacando de outras soluções disponíveis no mercado. A seguir, apresentamos os principais pontos que demonstram o potencial, os benefícios e a diferenciação dessa proposta de solução.

**Potenciais da Proposta:**

1. **Precisão de Previsão:** O Modelo Preditivo de Estoque utiliza algoritmos avançados para prever com alta precisão as demandas futuras por produtos. Isso proporciona uma visão holística das necessidades de estoque, permitindo à Mobly tomar decisões embasadas e eficientes.
2. **Adaptação Dinâmica:** O modelo é capaz de se adaptar rapidamente às variações de demanda. Essa flexibilidade garante que as previsões permaneçam atualizadas e relevantes em um ambiente de negócios em constante evolução.
3. **Otimização de Recursos:** Ao evitar excesso ou ruptura de estoque, o modelo contribui para a otimização dos recursos financeiros da Mobly. Isso se traduz em redução de custos operacionais, evitando gastos desnecessários com armazenamento ou perdas de vendas.

**Benefícios da Proposta:**

1. **Eficiência Operacional:** Com o Modelo Preditivo de Estoque, a Mobly pode automatizar e aprimorar significativamente os processos de planejamento e recompra de estoque. Isso libera recursos e tempo para atividades estratégicas, impulsionando a eficiência geral das operações.
2. **Tomada de Decisões Informadas:** A base de dados confiável e análises precisas fornecidas pelo modelo capacitam os profissionais de supply chain a tomar decisões informadas e estratégicas. Isso resulta em um planejamento mais eficaz e assertivo.
3. **Minimização de Riscos:** A previsão precisa de demanda e recompra oportuna reduz os riscos associados a excesso ou escassez de estoque. Isso permite à Mobly responder de maneira ágil às flutuações do mercado, minimizando perdas e maximizando oportunidades.

**Diferenciação da Proposta:**

1. **Acurácia Avançada:** O Modelo Preditivo de Estoque da Mobly se destaca pela alta acurácia de suas previsões, resultado da aplicação de algoritmos de aprendizado de máquina de última geração. Isso confere à Mobly uma vantagem competitiva ao garantir que suas decisões se baseiem em informações confiáveis e atualizadas.
2. **Adaptação em Tempo Real:** Ao contrário de soluções estáticas, o modelo é capaz de se adaptar em tempo real às mudanças nas condições de mercado e demanda, garantindo que as previsões permaneçam relevantes e úteis mesmo diante de cenários dinâmicos.
3. **Foco no Valor Agregado:** A proposta se destaca por permitir que os profissionais se concentrem em atividades estratégicas e de alto valor, em vez de dedicar tempo excessivo ao gerenciamento manual de estoque. Isso resulta em uma equipe mais proativa e voltada para a inovação.
4. **Documentação Detalhada de Uso:** Nossa proposta inclui uma documentação completa e detalhada de uso do produto, fornecendo todas as informações necessárias para uma implantação bem-sucedida e um aproveitamento máximo de suas funcionalidades.

&emsp;Em conclusão, a proposta de implementação do Modelo Preditivo de Estoque na Mobly apresenta um potencial promissor, uma série de benefícios tangíveis e se destaca pela sua acurácia avançada e capacidade de adaptação em tempo real. Ao adotar essa solução, a Mobly estará equipada para otimizar seus processos de supply chain, melhorar sua eficiência operacional e tomar decisões mais informadas.

### 2.3 Proposta de solução

&emsp;A proposta de solução para os problemas enfrentados pela Mobly é o desenvolvimento de um modelo preditivo que permita prever a demanda diária de cada SKU, buscando uma acurácia de 70%, e também fazer a previsão de vendas por SKU por semana com uma acurácia de 90%.

&emsp;Um modelo preditivo é uma função matemática capaz de identificar padrões em uma série de dados coletados antecipadamente. Sendo assim, para realizar as análises preditivas, são utilizadas técnicas de Machine Learning, inteligência artificial e ferramentas estatísticas [[4]](#c10). Essas abordagens possibilitam estimar a probabilidade e a precisão de determinadas ocorrências.

&emsp;Além disso, um modelo de predição serve para identificar e reconhecer padrões dentro de uma quantidade de amostra de dados para realizar sua análise. O funcionamento desse modelo se baseia em três etapas: coleta de dados, processamento de dados e validação das respostas.

&emsp;Com base nessa descrição, o uso de um modelo preditivo se torna benéfico para a Mobly, pois ele proporcionará um aumento na precisão dos dados para reconhecer quais produtos serão vendidos rapidamente no estoque e quais devem ser repostos. Além disso, o modelo permitirá agilidade nas tomadas de decisão da empresa em relação a novas compras e ao gerenciamento do estoque para atender à demanda de forma mais eficiente. </br>
&emsp;Ademais, a  implementação do modelo preditivo contribuirá significativamente para aprimorar a gestão de estoque da Mobly, reduzindo custos operacionais e melhorando a disponibilidade dos produtos para os clientes. Com previsões mais precisas, a empresa poderá otimizar suas operações e se tornar mais competitiva no mercado.

## <a name="c3"></a>3. Metodologia

&emsp;A metodologia CRISP-DM (Cross-Industry Standard Process for Data Mining) é um processo estruturado e iterativo amplamente utilizado para guiar projetos de mineração de dados e análise de dados. Ela abrange desde a compreensão do problema até a implantação de soluções, garantindo uma abordagem sistemática para transformar dados brutos em informações úteis e insights acionáveis. A metodologia CRISP-DM é composta por seis etapas interconectadas, que juntas fornecem um roteiro abrangente para a realização de projetos de mineração de dados [[5]](#c11).

1. **Compreensão do Negócio (Business Understanding):** Nesta etapa, o profissional busca entender os objetivos e requisitos do projeto. Isso envolve identificar o problema que precisa ser resolvido, as metas de negócios e as necessidades das partes interessadas. O foco está em definir claramente o escopo do projeto e estabelecer critérios de sucesso mensuráveis [[5]](#c11).
3. **Compreensão dos Dados (Data Understanding):** Nesta fase, a atenção se volta para a coleta e avaliação dos dados disponíveis. Isso inclui explorar e analisar a qualidade dos dados, identificar lacunas e determinar se os dados atendem aos requisitos do projeto. A equipe também busca entender a estrutura dos dados, seus relacionamentos e quaisquer desafios técnicos envolvidos [[5]](#c11).
4. **Preparação dos Dados (Data Preparation):** Aqui, os dados são preparados para análise por meio de limpeza, transformação e formatação. Isso pode envolver a remoção de valores ausentes, a normalização de dados e a seleção de atributos relevantes. O objetivo é criar um conjunto de dados pronto para alimentar os algoritmos de análise [[5]](#c11).
5. **Modelagem (Modeling):** Nesta etapa, técnicas de mineração de dados e aprendizado de máquina são aplicadas ao conjunto de dados preparado. Diversos modelos são construídos e avaliados para determinar qual deles é mais adequado para resolver o problema em questão. Isso envolve a seleção de algoritmos, ajuste de parâmetros e validação cruzada [[5]](#c11).
6. **Avaliação (Evaluation):** Aqui,a equipe analisa métricas de desempenho, como precisão, recall, F1-score, entre outras, para determinar a qualidade dos resultados. Se necessário, os modelos são refinados e otimizados. É interessante destacar que nesta etapa também é feito uma análise se as métricas utilizadas e os resultados estão alinhados com o entendimento do negócio para que o modelo se apresente verdadeiramente eficaz para a solução que é buscada. Isso é um diferencial da metodologia CRISP-DM, pois ela requer essa reflexão se a avaliação feita é a melhor para o projeto em questão, tendo em vista o alinhamento com o negócio [[5]](#c11).
7. **Implantação (Deployment):** Na última etapa, os insights obtidos e os modelos desenvolvidos são implementados no ambiente de negócios. Isso pode envolver a criação de relatórios, painéis interativos ou integração direta com sistemas existentes. O objetivo é garantir que os resultados da análise sejam aproveitados para melhorar a tomada de decisões e processos de negócios [[5]](#c11).

&emsp;Cada uma dessas etapas é interdependente e pode ser iterativa, ou seja, é comum voltar a etapas anteriores para ajustar ou refinar os processos à medida que novas informações e insights são adquiridos. A metodologia CRISP-DM fornece uma estrutura sólida para orientar profissionais e equipes na condução bem-sucedida de projetos de mineração de dados, desde a compreensão inicial até a implementação prática de soluções baseadas em dados [[5]](#c11).

## <a name="c4"></a>4. Desenvolvimento e Resultados

### 4.1. Compreensão do Problema

#### 4.1.1. Contexto da indústria 

##### 4.1.1.1. Principais Players no Mercado de Móveis

&emsp;No mercado de móveis, diversos players desempenham um papel significativo na oferta de produtos e serviços. Entre os principais players, destacam-se empresas como Mobly, que é uma renomada varejista online de móveis e artigos de decoração. Além disso, segundo a entrevista kickoff (2023), outras empresas de destaque incluem:

**Lojas de Móveis Tradicionais:** Estabelecimentos físicos que oferecem uma ampla variedade de móveis e geralmente contam com showrooms para exibir seus produtos.

**Concorrentes Online:** Além da Mobly, outras empresas operam no mercado de móveis online, competindo em termos de catálogo, preço e experiência do cliente como, MadeiraMadeira, Tok Stok, Magazine Luiza, entre outros markets places que operam nesse mercado.

**Empresas de Design e Decoração:** Fornecem soluções de design de interiores e decoração, incluindo seleção de móveis adequados para diferentes estilos.

##### 4.1.1.2. Modelos de Negócio na Industria de Móveis

&emsp;Os modelos de negócio na indústria de móveis podem variar, abrangendo diferentes abordagens para atender às demandas dos consumidores [[6]](#c12). Alguns modelos de negócio comuns incluem:

**Varejo Online:** Empresas como a Mobly, adotam um modelo de negócios centrado no comércio eletrônico, oferecendo uma ampla gama de móveis para compra online, com entregas diretas aos clientes. Esse tipo de Empresa é mais difícil de se encontrar no mercado por precisar de uma parte logística grande envolvida, o que pode dar vantagem para a Mobly.

**Soluções de Design e Decoração:** Modelos de negócios que oferecem serviços de design de interiores, consultoria e decoração, muitas vezes incluindo a recomendação e venda de móveis. O que pode auxiliar em ganhos para a Mobly. Algumas tendências do mercado indicam que em algumas épocas sazonais como, Black Friday e Natal trazem mais compradores para a Mobly e para as outras empresas de venda de móveis. 

##### 4.1.1.3. Tendências e Impactos do Mercado de Móveis

&emsp;O mercado de móveis está sujeito a várias tendências e impactos que moldam sua evolução contínua [[7]](#c13). Algumas tendências e fatores impactantes incluem:

**Sustentabilidade:** O crescente foco na sustentabilidade leva as empresas a adotar materiais e processos mais ecológicos na fabricação de móveis, além de oferecer opções de produtos sustentáveis. Tal aspecto pode aumentar a taxa de aceitação da empresa no mercado, aumentando a sua reputação e trazendo uma melhor imagem para a empresa.

**Design Inteligente:** Móveis projetados para otimizar espaços menores, atender às necessidades de trabalho em casa e incorporar tecnologia estão ganhando popularidade. Assim como a Mobly criou recetemente o sofá que consegue ser levado em 4 caixas de papelão separadas e que trazem uma facilidade na locomoção e montagem do mesmo.

**Comércio Eletrônico em Ascensão:** O aumento das compras online impulsiona o crescimento das vendas de móveis pela internet, levando as empresas a aprimorar suas plataformas de e-commerce e logística. Sob esse cenário, a Mobly pode ter mais entrantes no mercado aumentando a concorrência e forçando que a mesma traga inovações ao mercado.

**Experiência do Cliente:** A busca por uma experiência do cliente excepcional, tanto online quanto offline, influencia os modelos de negócio e estratégias de marketing das empresas. Esse é um dos grandes diferenciais que uma empresa de móveis pode trazer, um ótima experiência no site e com preços a níveis acessíveis para os clientes.

**Personalização:** Os consumidores estão buscando móveis personalizados que se adaptem ao seu estilo e necessidades, impulsionando a criação de soluções de personalização.

**Tecnologia na Fabricação:** A incorporação da automação e da tecnologia na indústria de móveis está resultando em uma produção mais eficiente e personalizável. No entanto, esse avanço pode acarretar em um desafio. Por exemplo, à medida que os marketplaces evoluem, os parceiros da Mobly podem optar por vender seus produtos diretamente nesses espaços, o que levaria a um aumento no número de novos competidores nesse setor. Apesar disso, mesmo com a possibilidade de os parceiros contornarem a etapa intermediária e venderem diretamente aos consumidores, a Mobly destaca-se por sua capacidade de gerenciar toda a logística, algo que não pode ser assegurado ao vender por meio de marketplaces como o Mercado Livre.

&emsp;Essas tendências e impactos moldam a dinâmica competitiva da indústria de móveis, incentivando os principais players a se adaptarem e inovarem para atender às demandas em constante mudança dos consumidores.

##### 4.1.1.4. Principais Players na Indústria de Modelos Preditivos

&emsp;Na indústria de modelos preditivos, os atores centrais incluem organizações e empresas que desempenham um papel fundamental no desenvolvimento dessa tecnologia [[8]](#c14). Destacam-se entre esses atores o Google Colab, uma plataforma que democratiza o acesso a ferramentas de aprendizado de máquina, o Inteli, uma instituição de ensino que têm como objetivo desenvolver projetos tecnológicos preparando os alunos para o mercado, e a Mobly, uma parceira estratégica do Inteli que precisa do modelo preditivo para a otimização do estoque.

##### 4.1.1.5 Modelos de Negócio na Industria de Modelos Preditivos

&emsp;Os modelos de negócios na indústria de modelos preditivos refletem a ampla gama de aplicações dessa tecnologia. Enquanto o Inteli adota modelos preditivos em projetos para diversas empresas, a Mobly se destaca ao necessitar desse modelo para melhorar a gestão de estoque e para prever a demanda futura. Com uma previsão de demanda eficaz permite que a Mobly minimize influências e assegure uma disponibilidade adequada de produtos.

##### 4.1.1.6. Tendências e Impactos na Industria de Modelos Preditivos

&emsp;Tendências atuais no mercado de modelos preditivos apontam para sua crescente aplicação em diversos setores como, agricultura, saúde e manufatura [[4]](#c10). A colaboração entre Inteli e Mobly pode capitalizar essas tendências, a medida que o uso dos modelos preditivos feitos pelo Inteli aprimoram a logística de estoque da Mobly.

##### 4.1.1.7. 5 Forças Porter

&emsp;Para melhor entendimento do mercado em que o parceiro ( Mobly ) está inserido é necessário fazer uso de uma análise de mercado denominado as 5 Forças Porter. As 5 Forças de Porter são um modelo desenvolvido por Michael E. Porter para análise do ambiente competitivo de uma empresa ou indústria [[9]](#c15). Essas forças ajudam a identificar fatores que afetam a rentabilidade e a atratividade de um setor, possibilitando a formulação de estratégias para enfrentar a concorrência e alcançar vantagem competitiva. Abaixo, está exibida a análise das 5 Forças Porter da empresa Mobly:

1. Rivalidade entre os concorrentes:
&emsp;A Mobly opera em um setor altamente competitivo, onde diversas empresas competem por participação de mercado. Além dos varejistas especializados em móveis e decoração, como a Etna e a MadeiraMadeira, a empresa também enfrenta concorrência de gigantes do e-commerce, como Amazon e Mercado Livre, que expandiram suas categorias de produtos para incluir móveis e decoração. Essa rivalidade intensa pode resultar em pressões nos preços e margens, bem como na necessidade contínua de diferenciação através de ofertas únicas, experiência do cliente e inovação. Entretanto Mobly é a pioneira na venda de móveis online no Brasil e oferece preços acessíveis, o que pode gerar uma vantagem competitiva significativa em relação a outras empresas do setor. No entanto, a abertura de lojas físicas em São Paulo e em outros Locais do Brasil pode intensificar a competição com outras lojas de móveis tradicionais na região.
2. Poder de negociação dos fornecedores:
&emsp;A Mobly adota um modelo de beneficiamento, comprando matéria-prima e terceirizando a fabricação com fornecedores parceiros. Essa estratégia oferece controle sobre ambos os fornecedores de matéria-prima e mão-de-obra. A escala das operações da Mobly fortalece seu poder de negociação, permitindo-lhe estabelecer termos vantajosos. No entanto, a dependência de fornecedores externos também pode trazer riscos, e a exclusividade de produtos por parte dos fornecedores pode afetar as negociações. Equilibrar o controle e a diferenciação de produtos é fundamental para o sucesso.
3. Poder de negociação dos compradores:
&emsp;Os clientes têm poder de negociação devido à natureza transparente do mercado online. Eles podem comparar preços e avaliações de produtos com facilidade, o que os torna mais propensos a buscar ofertas competitivas. No entanto, a experiência personalizada e a oferta de preços acessíveis podem tornar os clientes mais satisfeitos e menos sensíveis a preços, reduzindo o poder de barganha dos compradores. Porém, apesar dos preços acessíveis que a Mobly disponibiliza há outros fatores que fazem com que os clientes sejam sensíveis a preços, como qualidade do atendimento, facilidade na hora da devolução de algum produto, velocidade da entrega, e disponibilidade de opções de pagamento. Tais fatores podem afetar a sensibilidade dos clientes aos preços e aumentando o seu poder de negociação.
4. Ameaça de novos entrantes:
&emsp;A experiência diferenciada no site, os preços acessíveis e a abertura de lojas físicas podem criar barreiras para novas empresas que desejem entrar no mercado de venda de móveis online. Apesar da experiência personalizada no site e nas lojas físicas, é válido pensar que há chance de novos entrantes no mercado, e pode se tornar mais forte o risco principalmente considerando o crescimento constante do e-commerce e a acessibilidade à tecnologia.
5. Ameaça de produtos substitutos:
&emsp;A Mobly enfrenta a ameaça de produtos substitutos tanto dentro do setor de móveis e decoração quanto fora dele. Lojas físicas, compras de segunda mão e até mesmo a opção de não comprar representam alternativas para os consumidores. Para minimizar essa ameaça, a Mobly pode focar na promoção dos benefícios exclusivos do comércio eletrônico, como conveniência, variedade de produtos, facilidade de comparação de preços e a capacidade de visualização virtual de produtos em espaços reais.

#### 4.1.2. Análise SWOT 

&emsp;A matriz SWOT é uma ferramenta utilizada para avaliar o cenário de uma empresa e auxiliar na tomada de decisões que podem impactar positiva ou negativamente a companhia. Nesse sentido, as letras dessa matriz representam:
+ S (Forças - Strengths): São características internas e recursos que conferem vantagem à empresa e que estão sob seu controle. </br>
+ W (Fraquezas - Weaknesses): São fatores internos que podem prejudicar o desenvolvimento da organização. </br>
+ O (Oportunidades - Opportunities): Representam fatores externos sobre os quais a empresa não possui controle direto que pode ser algo benéfico ou maléfico. Como exemplo temos: crescimento econômico, alta demanda por um produto e novas tendências. </br>
+ T (Ameaças - Threats): São fatores externos que podem potencialmente causar prejuízos à empresa, e ela também não tem controle sobre eles. Exemplos incluem mudanças regulatórias, instabilidade econômica ou avanços tecnológicos. </br>
Em suma, ao realizar uma análise SWOT, a organização pode identificar suas áreas fortes e aproveitar as oportunidades. Ao mesmo tempo, deve abordar suas fraquezas e enfrentar as ameaças para reduzir riscos e melhorar sua posição competitiva no mercado [[10]](#16). </br>

#### **Análise SWOT da Mobly com o método PASTEL:**

![forças](https://github.com/2023M3T9-Inteli/grupo4/assets/124094681/40fbcc72-ee7b-4cb1-af65-271e9aa8960c)

![fraquezas](https://github.com/2023M3T9-Inteli/grupo4/assets/124094681/35be5b67-dd2a-40c4-82fa-022b6aac3178)

![oportunidades](https://github.com/2023M3T9-Inteli/grupo4/assets/124094681/20558ef9-dca9-4459-89c0-91824e3d9500)

![ameaças](https://github.com/2023M3T9-Inteli/grupo4/assets/124094681/ad06ebad-345c-4634-b898-aa51eb94197d)

##### **Insights Estratégicos:**
&emsp;Com base na análise SWOT incorporando o método PASTEL, a Mobly pode considerar as seguintes estratégias:

 - Expansão Global Controlada: Aproveitar a oportunidade de expansão internacional com uma abordagem cautelosa, começando por mercados com alta demanda por móveis.

 - Ênfase na Sustentabilidade: Desenvolver linhas de produtos sustentáveis e comunicar efetivamente suas práticas ambientalmente amigáveis.

 - Melhoria da Qualidade: Investir em controle de qualidade para melhorar a satisfação do cliente e reduzir críticas negativas.

 - Inovação Tecnológica: Adotar tecnologias avançadas para melhorar a experiência do cliente, como ferramentas de realidade virtual para visualização de produtos.

 - Monitoramento Regulatório: Acompanhar de perto as mudanças nas regulamentações de comércio eletrônico e garantir a conformidade.

&emsp;A SWOT serve principalmete para mapear o interno da empresa ( fatos que são controláveis pela mesma ) e o ambiente externo ( onde a empresa não tem controle sobre os fatos ). Portanto relacionar os campos de Forças, Fraquezas, Oportunidade e Ameças traz alguns planos de ação que a empresa pode executar como, "a empresa pode utilizar suas forças para neutralizar as ameaças", "a empresa pode utilizar suas forças para aproveitar oportunidades", "quais fraquezas que a empresa deve liquidar para aproveitar oportunidades que estão entrando no mercado". Como no exemplo acima, correlacionar os campos da Análise SWOT podem trazer insights muito bons para tomar decisões mais seguras, trazem mais conhecimento sobre a empresa e o mercado e a análise também te ajuda a antecipar movimentos que podem afetar seu negócio. Sob esta ótica, abaixo estão alguns insights que a Matriz Swot fornece : 

- Insights Estratégicos:
&emsp;Com base na análise SWOT incorporando o método PASTEL, a Mobly pode considerar as seguintes estratégias:

 1. Expansão Global Controlada: Aproveitar a oportunidade de expansão internacional com uma abordagem cautelosa, começando por mercados com alta demanda por móveis.

 2. Ênfase na Sustentabilidade: Desenvolver linhas de produtos sustentáveis e comunicar efetivamente suas práticas ambientalmente amigáveis. O que seria eliminar uma fraqueza para acompanhar os movimentos globais de sustentabilidade.s

 3. Melhoria da Qualidade: Investir em controle de qualidade para melhorar a satisfação do cliente e reduzir críticas negativas.

 4. Inovação Tecnológica: Adotar tecnologias avançadas para melhorar a experiência do cliente, como ferramentas de realidade virtual para visualização de produtos.

 5. Monitoramento Regulatório: Acompanhar de perto as mudanças nas regulamentações de comércio eletrônico e garantir a conformidade.

&emsp;Esses insights estratégicos podem ajudar a Mobly a enfrentar os desafios do mercado de móveis e comércio eletrônico, aproveitando suas forças e as oportunidades oferecidas pelo ambiente macroambiental, ao mesmo tempo que aborda suas fraquezas e se prepara para possíveis ameaças.

**Legenda:**
**Strengths**
+ Experiência omnichannel: integra lojas físicas, virtuais e compradores. Assim, tem como finalidade não fazer com que o consumidor veja a diferença entre o mundo on-line e off-line.
+ Venda em multiplataformas: inclui vendas em lojas físicas, realizar marketplace in( vender o produtos de terceiros) e marketplace out(fazer com que terceiros vendam seus produtos). Além de possibilitar a compra tanto de modo mobile e desktop.
+ Ampla oferta de produtos: ocorre a venda de vários produtos diferentes e peças avulsas, como somente gavetas para determinadas mesas.
+ Serviço próprio de logística: a Mobly realiza todo o processo de venda e pós venda para seu cliente.
+ Estratégia de marketing: realização de propagandas em diversas redes, relatando o autovalor de seus produtos.
+ Atendimento ao cliente eficiente: A Mobly no Reclame Aqui normalmente responde todos os seus clientes que encontram algum empecilho na compra de seus produtos.
+ Ambientes decorados: apresenta um ambiente com potenciais decorações de quartos, cozinha, sala e etc. que os concorrentes não possuem, como o caso da Magazine Luiza e Casas Bahia.
+ Atendem diversos clientes: há atendimento de diversas classes de consumidores feita pela Mobly.
+ Oferece serviço de montagem própria: quando há a compra de algum produto, a Mobly realiza o trabalho de montagem do produto.

**Weaknesses**
+ Demora no serviço de entregas: realiza entregas demoradas de comparada aos concorrentes que disponibilizam uma melhor agilidade no envio dos produtos. 
+ Alto índice de clientes que, após passarem por um problema, não voltariam a comprar com a empresa: segundo o Reclame Aqui muitos consumidores após encontrarem algum problema não voltariam a comprar outro produto dessa empresa, sendo isso cerca de 33% na data: 08/08/2023.
+ Optar por não fazer parte de clube de descontos: Não possui algum clube específico para proporcionar promoções ou produtos exclusivos diretamente para seu público assinante.
+ Pouca visibilidade em redes sociais: não possui uma gama forte de consumidores que procuram a Mobly nas redes sociais, pois no dia 08/08/2023 a Tok&Stok e MadeiraMadeira possuem 3,1 milhões e 2,5 milhões de seguidores respectivamente, enquanto a Mobly 1,3 milhões de seguidores. Ademais, não possui um sistema de vendas por WhatsApp que facilite a compra do consumidor como a MadeiraMadeira.
+ Falha na gestão do estoque: a Mobly não tem um sistema que permita saber quais produtos sairiam rapidamente e os que ficaram estagnados no estoque. Assim, a ocupação a longo prazo desses produtos geraria mais gastos do que ganho, pois ela não poderia colocar outra mercadoria que geraria mais lucro pela falta de espaço.

**Opportunities**
+ Flexibilização da extração de matéria-prima:  com  a flexibilização de extração de matéria-primas possibilita que a Mobly tenha oportunidade de adquirir produtos mais facilmente e com isso um menor preço.
+ Alta demanda de consumo causada por crises: se houver uma crise em que a população não está preparada e seu ambiente de vivência(casa, apartamento e etc.) não estiver preparado, a Mobly pode investir no estoque de produtos que são mais procurados para colocar em seu estoque e vender posteriormente. Isso ocorreu na pandemia da Covid-19, em que houve um grande exponencial nas vendas.
+ Surgimento de tecnologia para facilitar a gestão de estoque: alguma pessoa desenvolvesse um robô/algoritmo que facilite a manutenção do estoque para a Mobly não ter problemas relacionados com espaço.
+ Diminuição de taxas alfandegárias: se houver a diminuição de taxas alfandegárias, a Mobly teria a possibilidade de aproveitar para comprar produtos importados com um menor custo e vender nacionalmente, assim gerando uma diversificação em seus produtos.
+ Melhora no poder de compra do consumidor: se houver uma melhora no poder de compra da população igualmente fará com que ela gaste mais. Assim, seria uma ótima oportunidade para a Mobly promover novas vendas.

**Threats**
+ Poucos produtos possuem avaliação no site: havendo poucos produtos com uma boa avaliação no website possivelmente leve aos compradores a não finalizarem a compra. Com isso, buscando outro site que tenha melhores recomendações para finalizarem seu anseio.
+ Mudança nas leis de extração de matéria-prima: havendo mudanças na extração da matéria prima ocasiona na perda de produtos da Mobly, pois os preços desses produtos iriam aumentar e a população não compraria. Dessa maneira, deixando no estoque.
+ Surgimento de empresas de móveis com maior investimento em tecnologia: o caso de empresas investirem em tecnologias com maior agilidade na gestão do estoque e em formas online de entregas acarretaria que a Mobly ficaria ultrapassada e assim perdendo consumidores e investidores.
+ Fortalecimento de empresas de marketplace no ramo de móveis: ocorrência no fortalecimento de empresas de marketplace no ramo de móveis, como Amazon e Magazine Luiza por exemplo prejudicaria a Mobly, pois com o marketing eficiente dessas duas companhias faria uma nova distribuição dos consumidores e assim a Mobly perdendo mercado.
+ Concorrentes utilizando tecnologia de realidade aumentada na representação dos seus produtos: se concorrentes começarem a investir em realidade aumentada as pessoas estariam mais imersas nos ambientes de decorados e assim a Mobly perdendo público por não proporcionar essa experiência



#### 4.1.3. Planejamento Geral da Solução

&emsp;A Mobly, visando aprimorar sua gestão de estoque e planejamento de compras, iniciou um projeto que utiliza seus históricos de vendas dos últimos 5 anos como fonte de dados. Esses registros de vendas abrangem informações como datas de transações, identificação específica de produtos (SKU) e as quantidades vendidas em cada transação 

&emsp;Nesse contexto, a nossa solução proposta é a construção de um modelo preditivo que faça uso desses dados históricos para prever a demanda futura de cada SKU em um horizonte de uma semana, para qualquer data. Este modelo, a ser executado diariamente, busca proporcionar previsões precisas sobre as quantidades de vendas para produtos individuais em intervalos de tempo específicos. 

&emsp;Portanto, a tarefa em questão se enquadra na categoria de regressão, onde o foco está na previsão de valores numéricos contínuos. No caso, a previsão da quantidade de vendas para cada SKU é um exemplo típico de regressão, pois visa estimar valores numéricos (quantidades vendidas) para um dado período. 

&emsp;A equipe de Supply Chain da Mobly será o principal setor beneficiado da solução desenvolvida. A partir das previsões geradas pelo modelo, poderão tomar decisões mais informadas sobre os produtos a serem adquiridos e suas quantidades, evitando tanto o excesso quanto a falta de estoque. Desse modo, os fornecedores também poderão se beneficiar das previsões para planejar a produção de itens que estejam fora de estoque na Mobly. 

&emsp;Dentre os benefícios esperados, a otimização do estoque se destaca, uma vez que previsões mais acuradas contribuem para um planejamento mais eficiente. Redução de custos, melhoria na experiência do cliente devido à disponibilidade adequada dos produtos, aumento nas vendas graças ao atendimento mais eficiente da demanda e aprimoramento das estratégias de planejamento da equipe de Supply Chain são outras vantagens notáveis. 

&emsp;O sucesso do projeto é avaliado com base em métricas como o Erro Quadrático Médio (RMSE) e o Coeficiente de Determinação (R²). Foram estabelecidas metas rigorosas para essas métricas, garantindo que o RMSE esteja dentro de limites aceitáveis e que o R² demonstre um ajuste adequado do modelo aos dados reais de vendas. Esses critérios de desempenho são essenciais para manter a qualidade das previsões da empresa.

#### 4.1.4. Value Proposition Canvas

&emsp;O _Value Preposition Canvas_ é um modelo criado para compreender melhor o modelo de negócio ao análisar tanto o lado do cliente quanto o lado da empresa. Ao fazer essa análise, busca-se compreender a dor do cliente, quais tarefas ele tem de realizar e o que o produto propõe ao interessado. Já do lado da empresa, observa-se o produto oferecido, as dores aliviadas e os criadores de ganho do produto, o que ele pode oferecer. Nesse sentido, elaboramos um Canvas com o intuito de análisar as necessidades do cliente da Mobly e como o produto ofertado, no caso o modelo preditivo, pode melhorar a experiência dos clientes da empresa.

*Figura 2 - Value Proposition Canvas* </br>
![Frame 1 (1)](https://github.com/2023M3T9-Inteli/grupo4/assets/84935638/55f7d1ba-8806-473a-a7a7-84a9994ff9ae) </br>
*Fonte: Elaborado pelos próprios autores*

**Justificativa**

*Value Proposition*

   * Criadores de ganho: O modelo preditivo traz diversos benefícios à empresa, sendo assim   os principais estão diretamente ligado ao estoque físico e ao caixa da empresa pelo modelo ter a capacidade de fazer uma seleção melhor de produtos que saírão. Com isso é possível evitar perdas de móveis devido a danificações por conta de excesso de tempo no estoque.  
   * Produtos e serviços: O principal produto oferecido é o modelo preditivo que busca aumentar a precisão de compras realizadas pelo serviço de logística, evitando causar rupturas do estoque.
   * Aliviam as dores: As dores aliviadas estão relacionadas principalmente ao financeiro, pois a proposta de valor traz um alívio financeiro evitando gastos excessivos com produtos de baixo giro.

*Customer Profile*

   * Ganhos: O consumidor é valorizado através do produto, pois poderá obter uma experiência mais satisfatória ao utilizar o site da mobly ao poder ter produtos disponíveis a pronta entrega.
   * Dores: O cliente busca ter uma experiência satisfatória ao realizar o processo de compra no site, porém com alguns produtos não estando disponíveis para pronta entrega, ele acaba por desistir de sua compra ou se descontentar. 
   * Tarefas do cliente: O cliente tem como objetivo principal poder utilizar do site ou loja física da mobly para poder realizar a compra do móvel desejado.

#### 4.1.5. Matriz de Riscos

&emsp;A matriz de riscos é um modelo criado para a avaliação de ocorrimentos que podem acontecer durante o desenvolvimento do projeto. Nela são feitas duas matrizes 3x3, sendo elas de risco e oportunidades, suas colunas representam o impacto que ele terá no projeto e suas linhas representam a probabilidade de algo acontecer. Sendo assim, poderá ter uma visão mais clara de eventos que poderam a vir acontecer no projeto  [[12]](#18).

*Figura 3 - Matriz de Risco* </br>
![Matriz de risco](https://github.com/2023M3T9-Inteli/grupo4/assets/124094681/ccc8e86f-9b77-4bb9-8a88-6009ef7bce61)[matriz de risco] </br>
*Fonte: Elaborado pelos próprios autores*

**Justificativa**
   
**Ameaças:**

* A aplicação encontrar dificuldades ao tentar modelar a Black Friday. -> A Black friday é uma data sazonal de grande importância para empresa, tendo suas        vendas impulsionadas por ela, tornando-se em parte um outliner mediante aos outros dados. Sendo assim, pode existir uma dificuldade do modelo ao realizar a previsão dessa data.      
* Perder a acurácia em previsões longas -> O algoritmo pode ter sua acurácia diminuída conforme o tempo, especialmente o quão mais longe estiver da data inicial. Sendo assim, a tendência é que sua acurácia vá diminuíndo gradativamente conforme a distância da previsão, porém alguns modelos perdem a acurácia de forma muito acelerada.
* Imprecisões nas previsões de recompras de produtos, causando um leve excesso ou falta no estoque -> Os modelos de previsão possuem uma margem de erro, a qual podem levar à leves erros na hora de realizarem recompras. Tal fato pode levar a uma pequena ruptura em um determinado item. 
* Existência de muitos dados nulos ou insuficientes para modelo -> Caso tenha-se muitos dados faltantes ou vazios, dificulta a realização do modelo, pois ele se tornará incapaz de identificar padrões.
* Baixa otimização no tempo de  resposta do modelo -> Existe o risco que o modelo exija um tempo de resposta maior do que o desejado.
* *Overfitting dos dados -> Alterar as informações para encaixar em um determinado modelo, porém se tornando ineficaz ao prever os próximos acontecimentos. Isso poderia encarretar em um problema caso acontesse em nosso modelo pois não permitiria alcançar a acurácia desejada.</li>
* Dificuldade ao compreender o uso do modelo preditivo. -> Caso o usuário não consiga compreender como utilizar o modelo preditivo de forma satisfatória, assim impedindo-o de tirar resultados proveitosos do mesmo. 
      
**Oportunidades:**
   
* Melhoria na reputação da empresa, pois melhora a avaliação da Mobly -> O modelo poderá permitir uma melhor recompra de produtos, ao prever futuras vendas e evitando possíveis rupturas. Sendo assim, o modelo evitiria futuros descontetamentos do cliente com a empresa ao realizar uma compra.
* Trazer um modelo que mantenha a acurácia dentro de um período proposto -> Caso o modelo mantenha sua acurácia dentro de um prazo de 90 dias se tornaria muito interessante a empresa, agregando imenso valor ao setor logístico. 
* Fácil adaptação dos usuários à nova ferramente -> Devido ao fato da equipe que utilizará o produto ser da área de tecnologia, existe uma oportunidade em ter uma fácil adesão e adaptação dos usuários a nova ferramenta.
* Possibilidade de uso do valor do dólar para aprimoramento do modelo. -> O uso da cotação do dólar contribuiria ao modelo, pois o mesmo está diretamente correlacionado com o preço de compra do produto, assim como o otimismo do consumidor.
* Melhora na experiência do cliente na hora da compra. -> O cliente poderá ter uma experiência de compra mais satisfatória devido ao fato de que acontecerá uma diminuição nas rupturas de sku, assim evitando uma demora para a entrega de um produto.
* Melhora na realização de recompra de produtos de acordo com a acurácia do modelo.
* O produto ter uma macro e uma micro análise dos acontecimentos que podem trazer mais ou menos demanda. -> Isso permitiria com que o modelo compreendesse fatores externos, em sua maioria econômicos e políticos, assim como internos para poder ter uma previsão mais precisa das saídas de skus. Porém sua implementação seria complexa e custosa, fazendo com que seja improvável de ser implementado.   
* Utilizar a ferramenta do google trends para melhorar acurácia do modelo. -> A ferramenta do google trends mostra quais tópicos estão em alto no momento, pode ajudar a compreender quais skus tem uma maior tendência a serem vendidos no momento. Todavia, sua implementação exige um grande esforço, a tornando improvável.
* Desenvolvimento de uma interface para o projeto. -> Permitiria uma melhor visualização e uso da IA, porém é de comum acordo que não seria algo necessário, fazendo com que seja uma oportunidade de baixa probabilidade e baixo impacto.

#### 4.1.6. Personas

&emsp;Uma "persona" é uma representação fictícia e detalhada de um cliente ideal, construída com base em dados reais e insights do público-alvo [[13]](#19). No contexto do nosso projeto de desenvolvimento de uma IA para o estoque da Mobly, as personas desempenham um papel crucial. Elas são essenciais para compreendermos as necessidades, comportamentos e desafios dos diferentes segmentos de clientes da Mobly, permitindo uma personalização mais precisa e uma abordagem estratégica na gestão de estoque. Ao construir personas sólidas, nossa IA terá a capacidade de otimizar a disponibilidade de produtos de acordo com as preferências específicas de cada persona, melhorando a experiência do cliente e a eficiência operacional.

*Figura 4: Persona Marina.* </br>
![template_persona](https://github.com/2023M3T9-Inteli/grupo4/assets/123904558/5f2758d9-0e1a-4eea-9dd5-1db97007e1f1) </br>
*Fonte: Elaborado pelos próprios autores*

**Nome:** Marina Ferreira
**Idade:** 32 anos
**Formação Acadêmica:** Bacharelado em Análise de Dados
**Experiência Profissional:** 4 anos na área de Business Inteligence e análise de dados.

**Descrição:**

&emsp;Marina Ferreira é uma analista de dados talentosa e dedicada na Mobly, uma das principais empresas de comércio eletrônico de móveis e decoração. Com um olhar afiado para detalhes e uma paixão por otimização de processos, ela desfruta da complexidade e dos desafios que a área de supply chain apresenta. 

**Habilidades e Responsabilidades:**

1. **Planejamento Estratégico:** Marina é especialista em desenvolver estratégias eficientes de Business Intelligence para assegurar a disponibilidade dos dados certos nos momentos e formatos adequados. Ela utiliza análises de dados, previsões de tendências e demanda de informações para embasar suas decisões.

2. **Gestão de Fontes de Dados:** Ela estabelece relacionamentos sólidos com fontes de dados e parceiros de integração, negociando acordos favoráveis e mantendo a conformidade com padrões de qualidade e segurança de dados.

3. **Otimização de Processos de Dados:** Marina é especialista em equilibrar os fluxos de dados, evitando excessos e lacunas. Ela faz uso de ferramentas de software avançadas para monitorar a integridade dos dados, antecipar necessidades futuras e evitar custos desnecessários.

4. **Monitoramento de Processos de Dados:** Sua responsabilidade engloba o acompanhamento e aprimoramento do fluxo de informações, desde a coleta até a entrega. Isso envolve o planejamento de processos, eficiência na transformação de dados e administração de repositórios.

5. **Resolução de Desafios:** Marina enfrenta desafios complexos na área de Business Intelligence com uma abordagem analítica. Identificando lacunas de dados, ineficiências e outros problemas, ela propõe soluções práticas para aprimorar os processos de gestão de informações.

6. **Análise de Dados:** Por meio de ferramentas analíticas, Marina interpreta métricas e indicadores-chave de desempenho para avaliar o sucesso das operações de Business Intelligence e implementar correções quando necessário.

7. **Colaboração:** Ela é uma excelente colaboradora, trabalhando em estreita colaboração com departamentos internos, como vendas, marketing, supply chain e finanças, para alinhar estratégias de Business Intelligence e alcançar os objetivos da empresa.

8. **Atualização Constante:** Mantendo-se informada sobre as últimas tendências e tecnologias em Business Intelligence, Marina participa de workshops, conferências e cursos para aprimorar continuamente suas habilidades na gestão de informações corporativas.


**Personalidade:**

&emsp;Marina é conhecida por sua ética de trabalho impecável, atenção aos detalhes e paixão por resolver desafios. Sua abordagem é proativa, resiliente e confiável, permitindo que ela lide com pressões e prazos apertados sem comprometer a qualidade. Sua comunicação eficaz e empatia a tornam uma colega de equipe excepcional.

&emsp;Resumindo, Marina Ferreira é uma analista de dados experiente e altamente qualificada, desempenhando um papel vital no sucesso operacional da Mobly ao garantir que os produtos alcancem os clientes de forma eficiente e eficaz.

**Como a Utilização do Modelo Preditivo Pode Sanar Dores na Rotina de Trabalho de Marina:**

1. **Análise de Dados Aprimorada:** Através do Modelo Preditivo de Estoque, algoritmos e dados históricos são empregados para antever a demanda futura por produtos. Isso permitirá que Marina tome decisões mais embasadas ao planejar as quantidades de itens em estoque, evitando tanto excesso quanto escassez.

2. **Otimização de Investimentos e Recursos:** Com base nas previsões do modelo, Marina pode determinar os momentos ideais para alocar recursos e investimentos. Isso reduzirá os custos associados a decisões mal informadas e maximizará o retorno sobre os investimentos, assegurando uma gestão mais eficaz dos recursos da empresa.

3. **Redução de Desperdícios Financeiros:** Evitando gastos desnecessários, Marina contribuirá para a diminuição dos custos operacionais e prevenirá desperdícios financeiros. O modelo proporcionará um equilíbrio entre eficiência financeira e otimização dos recursos da empresa.

4. **Adaptação Ágil às Mudanças de Mercado:** O Modelo Preditivo de Business Intelligence é ágil em se ajustar a variações nas condições de mercado e nas tendências de negócios. Isso permitirá que Marina e sua equipe reajam de maneira proativa a mudanças no mercado, evitando perdas de oportunidades de negócios devido a decisões desinformadas.

5. **Decisões Estratégicas Embasadas em Dados:** Com dados confiáveis fornecidos pelo modelo, Marina estará mais bem preparada para contribuir nas decisões estratégicas da empresa. Suas recomendações e insights embasados em informações precisas serão um diferencial na formulação de estratégias de longo prazo.

6. **Foco em Atividades Estratégicas e de Valor Agregado:** Com a automação das análises de dados, Marina terá mais tempo para se dedicar a atividades estratégicas de maior valor agregado, como colaborar com outros departamentos, analisar tendências de mercado e buscar constantemente melhorias nos processos de Business Intelligence.

#### 4.1.7. Jornada do Usuário

&emsp;Ao elaborarmos a Jornada do Usuário, adotamos uma abordagem que se concentra na compreensão completa desse quesito Nessa abordagem, o modelo preditivo que está sendo desenvolvido passou por um processo de implementação e aplicação em um cenário real. Ao fazer isso, criamos a oportunidade de realizar uma análise minuciosa das possíveis defasagens que o modelo poderia apresentar em um ambiente de uso prático e efetivo. Isso nos permitiu identificar de maneira mais precisa e abrangente os pontos onde o modelo pode precisar de ajustes ou melhorias para se alinhar de forma mais sólida e eficaz às nuances e complexidades do mundo real.

*Figura 5 - Jornada de Usuário* </br>
![Jornada do Usuario](https://github.com/2023M3T9-Inteli/grupo4/assets/123904558/68f226fb-e1b2-414d-9435-1f374dc3a9a9) </br>
*Fonte: Elaborado pelos próprios autores*

#### 4.1.8 Política de Privacidade

&emsp;Política de Privacidade
&emsp;A MOBLY COMÉRCIO VAREJISTA LTDA, pessoa jurídica de direito privado, com sede na Av. das Nações Unidas, n 16.737, Mezanino, Várzea de Baixo, Cidade de São Paulo, Estado de São Paulo, CEP: 04730-090, inscrita no CNPJ/MF sob o nº 14.055.516/0001-48 (“Lojista” ou “nós”) leva a sua privacidade a sério e zela pela segurança e proteção de dados de todos os seus clientes, parceiros, fornecedores e usuários (“Usuários” ou “você”) do site “berdms.lojavirtualnuvem.com.br” e qualquer outro site, Loja, aplicativo operado pelo Lojista (aqui designados, simplesmente, “Loja”).

&emsp;Esta Política de Privacidade (“Política de Privacidade”) destina-se a informá-lo sobre o modo como nós utilizamos e divulgamos informações coletadas em suas visitas à nossa Loja e em mensagens que trocamos com você (“Comunicações”).

&emsp;AO ACESSAR A LOJA, ENVIAR COMUNICAÇÕES OU FORNECER QUALQUER TIPO DE DADO PESSOAL, VOCÊ DECLARA ESTAR CIENTE E DE ACORDO COM ESTA POLÍTICA DE PRIVACIDADE, A QUAL DESCREVE AS FINALIDADES E FORMAS DE TRATAMENTO DE SEUS DADOS PESSOAIS QUE VOCÊ DISPONIBILIZAR NA LOJA.

&emsp;Esta Política de Privacidade fornece uma visão geral de nossas práticas de privacidade e das escolhas que você pode fazer, bem como direitos que você pode exercer em relação aos Dados Pessoais tratados por nós. Se você tiver alguma dúvida sobre o uso de Dados Pessoais, entre em contato com contato@mobly.com.br.

&emsp;Além disso, a Política de Privacidade não se aplica a quaisquer aplicativos, produtos, serviços, site ou recursos de mídia social de terceiros que possam ser oferecidos ou acessados por meio da Loja. O acesso a esses links fará com que você deixe a Loja e possa resultar na coleta ou compartilhamento de informações sobre você por terceiros. Nós não controlamos, endossamos ou fazemos quaisquer representações sobre esses sites de terceiros ou suas práticas de privacidade, que podem ser diferentes das nossas. Recomendamos que você revise a política de privacidade de qualquer site com o qual você interaja antes de permitir a coleta e o uso de seus Dados Pessoais.

&emsp;Caso você nos envie Dados Pessoais referentes a outras pessoas físicas, você declara ter a competência para fazê-lo e declara ter obtido o consentimento necessário para autorizar o uso de tais informações nos termos desta Política de Privacidade.

&emsp;Definições
&emsp;Para os fins desta Política de Privacidade:

&emsp;“Dados Pessoais” significa qualquer informação que, direta ou indiretamente, identifique ou possa identificar uma pessoa natural, como por exemplo, nome, CPF, data de nascimento, endereço IP, dentre outros;
&emsp;“Dados Pessoais Sensíveis” significa qualquer informação que revele, em relação a uma pessoa natural, origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico;
&emsp;“Tratamento de Dados Pessoais” significa qualquer operação efetuada no âmbito dos Dados Pessoais, por meio de meios automáticos ou não, tal como a recolha, gravação, organização, estruturação, armazenamento, adaptação ou alteração, recuperação, consulta, utilização, divulgação por transmissão, disseminação ou, alternativamente, disponibilização, harmonização ou associação, restrição, eliminação ou destruição. Também é considerado Tratamento de Dados Pessoais qualquer outra operação prevista nos termos da legislação aplicável;
&emsp;“Leis de Proteção de Dados” significa todas as disposições legais que regulem o Tratamento de Dados Pessoais, incluindo, porém sem se limitar, a Lei nº 13.709/18, Lei Geral de Proteção de Dados Pessoais (“LGPD”).
&emsp;Uso de Dados Pessoais
&emsp;Coletamos e usamos Dados Pessoais para gerenciar seu relacionamento conosco e melhor atendê-lo quando você estiver adquirindo produtos e/ou serviços na Loja, personalizando e melhorando sua experiência. Exemplos de como usamos os dados incluem:

&emsp;Viabilizar que você adquira produtos e/ou serviços na Loja;
&emsp;Para confirmar ou corrigir as informações que temos sobre você;
&emsp;Para enviar informações que acreditamos ser do seu interesse;
&emsp;Para personalizar sua experiência de uso da Loja;
&emsp;Para personalizar o envio de publicidades para você, baseada em seu interesse em nossa Loja; e
&emsp;Para entrarmos em contato por um número de telefone e/ou endereço de e-mail fornecido. Podemos entrar em contato com você pessoalmente, por mensagem de voz, através de equipamentos de discagem automática, por mensagens de texto (SMS), por e-mail, ou por qualquer outro meio de comunicação que seu dispositivo seja capaz de receber, nos termos da lei e para fins comerciais razoáveis.
&emsp;Além disso, os Dados Pessoais fornecidos também podem ser utilizados na forma que julgarmos necessária ou adequada: (a) nos termos das Leis de Proteção de Dados; (b) para atender exigências de processo judicial; (c) para cumprir decisão judicial, decisão regulatória ou decisão de autoridades competentes, incluindo autoridades fora do país de residência; (d) para proteger nossas operações; (e) para proteger direitos, privacidade, segurança nossos, seus ou de terceiros; (f) para detectar e prevenir fraude; (g) permitir-nos usar as ações disponíveis ou limitar danos que venhamos a sofrer; (h) de outros modos permitidos por lei.

&emsp;A NOSSA LOJA NÃO SE DESTINA A PESSOAS COM MENOS DE 18 (DEZOITO) ANOS E PEDIMOS QUE TAIS PESSOAS NÃO NOS FORNEÇAM QUALQUER DADO PESSOAL

&emsp;Não fornecimento de Dados Pessoais
&emsp;Você não é obrigado a compartilhar os Dados Pessoais que solicitamos, no entanto, se você optar por não os compartilhar, em alguns casos, não poderemos fornecer a você acesso completo à Loja, alguns recursos especializados ou ser capaz de prestar a assistência necessária ou, ainda, viabilizar a entrega do produto ou prestar o serviço contratado por você.

&emsp;Dados coletados
&emsp;O público em geral poderá navegar na Loja sem necessidade de qualquer cadastro e envio de Dados Pessoais. No entanto, algumas das funcionalidades da Loja poderão depender de cadastro e envio de Dados Pessoais como concluir a compra/contratação do serviço e/ou a viabilizar a entrega do produto/prestação do serviço por nós.

&emsp;No contato a Loja, nós podemos coletar:

&emsp;Dados de contato. Nome, sobrenome, número de telefone, cidade, Estado e endereço de e-mail; e
&emsp;Informações que você envia. Informações que você envia via formulário (dúvidas, reclamações, sugestões, críticas, elogios etc.).
&emsp;Na navegação geral na Loja, nós poderemos coletar:

&emsp;Dados de localização. Dados de geolocalização quando você acessa a Loja;
&emsp;Preferências. Informações sobre suas preferências e interesses em relação aos produtos/serviços (quando você nos diz o que eles são ou quando os deduzimos do que sabemos sobre você);
&emsp;Dados de navegação na Loja. Informações sobre suas visitas e atividades na Loja, incluindo o conteúdo (e quaisquer anúncios) com os quais você visualiza e interage, informações sobre o navegador e o dispositivo que você está usando, seu endereço IP, sua localização, o endereço do site a partir do qual você chegou. Algumas dessas informações são coletadas usando nossas Ferramentas de Coleta Automática de Dados, que incluem cookies, web beacons e links da web incorporados. Para saber mais, leia como nós usamos Ferramentas de Coleta Automática de Dados no item 7 abaixo;
&emsp;Dados anônimos ou agregados. Respostas anônimas para pesquisas ou informações anônimas e agregadas sobre como a Loja é usufruída. Durante nossas operações, em certos casos, aplicamos um processo de desidentificação ou pseudonimização aos seus dados para que seja razoavelmente improvável que você identifique você através do uso desses dados com a tecnologia disponível; e
&emsp;Outras informações que podemos coletar. Outras informações que não revelem especificamente a sua identidade ou que não são diretamente relacionadas a um indivíduo, tais como informações sobre navegador e dispositivo; dados de uso da Loja; e informações coletadas por meio de cookies, pixel tags e outras tecnologias.
&emsp;Ao menos que você informe em algum formulário livre preenchido por você, nós não coletamos Dados Pessoais Sensíveis.

&emsp;Compartilhamento de Dados Pessoais com terceiros
&emsp;Nós poderemos compartilhar seus Dados Pessoais:

&emsp;Com a(s) empresa(s) parceira(s) que você selecionar ou optar em enviar os seus dados, dúvidas, perguntas etc., bem como com provedores de serviços ou parceiros para gerenciar ou suportar certos aspectos de nossas operações comerciais em nosso nome. Esses provedores de serviços ou parceiros podem estar localizados nos Estados Unidos, na Argentina, no Brasil ou em outros locais globais, incluindo servidores para homologação e produção, e prestadores de serviços de hospedagem e armazenamento de dados, gerenciamento de fraudes, suporte ao cliente, vendas em nosso nome, atendimento de pedidos, personalização de conteúdo, atividades de publicidade e marketing (incluindo publicidade digital e personalizada) e serviços de TI, por exemplo;
&emsp;Com terceiros, com o objetivo de nos ajudar a gerenciar a Loja; e
&emsp;Com terceiros, caso ocorra qualquer reorganização, fusão, venda, joint venture, cessão, transmissão ou transferência de toda ou parte da nossa empresa, ativo ou capital (incluindo os relativos à falência ou processos semelhantes).
&emsp;Transferências internacionais de Dados
&emsp;Dados Pessoais e informações de outras naturezas coletadas por nós podem ser transferidos ou acessados por entidades pertencentes ao grupo corporativo das empresas parceiras em todo o mundo de acordo com esta Política de Privacidade.

&emsp;Forma de coleta automática de Dados Pessoais
Quando você visita a Loja, ela pode armazenar ou recuperar informações em seu navegador, seja na forma de cookies e de outras tecnologias semelhantes. Essas informações podem ser sobre você, suas preferências ou seu dispositivo e são usadas principalmente para que a Loja funcione como você espera. As informações geralmente não o identificam diretamente, mas podem oferecer uma experiência na internet mais personalizada.

&emsp;De acordo com esta Política de Privacidade, nós e nossos prestadores de serviços terceirizados podemos coletar seus Dados Pessoais de diversas formas, incluindo, entre outros:

&emsp;Por meio do navegador ou do dispositivo: Algumas informações são coletadas pela maior parte dos navegadores ou automaticamente por meio de dispositivos de acesso à internet, como o tipo de computador, resolução da tela, nome e versão do sistema operacional, modelo e fabricante do dispositivo, idioma, tipo e versão do navegador de Internet que está utilizando. Podemos utilizar essas informações para assegurar que a Loja funcione adequadamente.
&emsp;Uso de cookies: Os cookies permitem a coleta de informações tais como o tipo de navegador, o tempo dispendido na Loja, as páginas visitadas, as preferências de idioma, e outros dados de tráfego anônimos. Nós e nossos prestadores de serviços podemos utilizar essas informações para, dentre outros, personalizar sua experiência ao utilizar a Loja, assim como para direcionar publicidade para você, de acordo com os seus interesses. Também coletamos informações estatísticas sobre o uso da Loja para aprimoramento contínuo do nosso design e funcionalidade.
&emsp;Caso não deseje que suas informações sejam coletadas por meio de cookies, você pode configurar os cookies no menu "opções" ou "preferências" do seu browser. Nos links abaixo você encontra mais detalhes sobre como ajustar as preferências de cookies dos navegadores de internet mais populares:
&emsp;Google Chrome
&emsp;Mozilla Firefox
&emsp;Safari
&emsp;Internet Explorer
&emsp;Microsoft Edge
&emsp;Opera
&emsp;Caso deseje saber um pouco mais sobre os cookies de publicidade e remarketing, que servem para direcionarmos publicidade em função dos interesses de cada usuário e do número de visitas que realizou em nosso site e suas buscas na internet, acesse:
&emsp;Facebook
&emsp;Google
&emsp;Bing
&emsp;Uso de pixel tags e outras tecnologias similares: Pixel tags (também conhecidos como Web beacons e GIFs invisíveis) podem ser utilizados para rastrear ações de usuários da Loja (incluindo destinatários de e-mails), medir o sucesso das nossas campanhas de marketing e coletar dados estatísticos sobre o uso da Loja e taxas de resposta. Em caso de ter ativa a personalização de anúncios em ferramentas como Facebook, Google ou Bing, a informação pode ser usada para mostrar anúncios em seus serviços.No caso de você não desejar ser rastreado pode pedir para cada um dos serviços:
&emsp;Facebook
&emsp;Google
&emsp;Bing
&emsp;Podemos contratar empresas de publicidade comportamental, para obter relatórios sobre os anúncios da Loja em toda a internet. Para isso, essas empresas utilizam cookies, pixel tags e outras tecnologias para coletar informações sobre a sua utilização, ou sobre a utilização de outros usuários, da nossa Loja e de site de terceiros. Nós não somos responsáveis por pixel tags, cookies e outras tecnologias similares utilizadas por terceiros. Você pode configurar suas preferências no menu do seu browser. Esteja ciente de que se você mudar de computador ou navegador, ou usar vários computadores ou navegadores, você precisará repetir este processo para cada computador e cada navegador.
&emsp;Direitos do Usuário
&emsp;Você pode, a qualquer momento, requerer: (i) confirmação de que seus Dados Pessoais estão sendo tratados; (ii) acesso aos seus Dados Pessoais; (iii) correções a dados incompletos, inexatos ou desatualizados; (iv) anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade com o disposto em lei; (v) portabilidade de Dados Pessoais a outro prestador de serviços, contanto que isso não afete nossos segredos industriais e comerciais; (vi) eliminação de Dados Pessoais tratados com seu consentimento, na medida do permitido em lei; (vii) informações sobre as entidades às quais seus Dados Pessoais tenham sido compartilhados; (viii) informações sobre a possibilidade de não fornecer o consentimento e sobre as consequências da negativa; e (ix) revogação do consentimento. Os seus pedidos serão tratados com especial cuidado de forma a que possamos assegurar a eficácia dos seus direitos. Poderá lhe ser pedido que faça prova da sua identidade de modo a assegurar que a partilha dos Dados Pessoais é apenas feita com o seu titular.

&emsp;Você deverá ter em mente que, em certos casos (por exemplo, devido a requisitos legais), o seu pedido poderá não ser imediatamente satisfeito, além de que nós poderemos não conseguir atendê-lo por conta de cumprimento de obrigações legais.

&emsp;Segurança dos Dados Pessoais
Buscamos adotar as medidas técnicas e organizacionais previstas pelas Leis de Proteção de Dados adequadas para proteção dos Dados Pessoais na nossa organização. Infelizmente, nenhuma transmissão ou sistema de armazenamento de dados tem a garantia de serem 100% seguros. Caso tenha motivos para acreditar que sua interação conosco tenha deixado de ser segura (por exemplo, caso acredite que a segurança de qualquer uma de suas contas foi comprometida), favor nos notificar imediatamente.

&emsp;Links de hipertexto para outros sites e redes sociais
A Loja poderá, de tempos a tempos, conter links de hipertexto que redirecionará você para sites das redes dos nossos parceiros, anunciantes, fornecedores etc. Se você clicar em um desses links para qualquer um desses sites, lembramos que cada site possui as suas próprias práticas de privacidade e que não somos responsáveis por essas políticas. Consulte as referidas políticas antes de enviar quaisquer Dados Pessoais para esses sites.

&emsp;Não nos responsabilizamos pelas políticas e práticas de coleta, uso e divulgação (incluindo práticas de proteção de dados) de outras organizações, tais como Facebook, Apple, Google, Microsoft, ou de qualquer outro desenvolvedor de software ou provedor de aplicativo, Loja de mídia social, sistema operacional, prestador de serviços de internet sem fio ou fabricante de dispositivos, incluindo todos os Dados Pessoais que divulgar para outras organizações por meio dos aplicativos, relacionadas a tais aplicativos, ou publicadas em nossas páginas em mídias sociais. Nós recomendamos que você se informe sobre a política de privacidade de cada site visitado ou de cada prestador de serviço utilizado.

&emsp;Atualizações desta Política de Privacidade
Se modificarmos nossa Política de Privacidade, publicaremos o novo texto na Loja, com a data de revisão atualizada. Podemos alterar esta Política de Privacidade a qualquer momento. Caso haja alteração significativa nos termos dessa Política de Privacidade, podemos informá-lo por meio das informações de contato que tivermos em nosso banco de dados ou por meio de notificação em nossa Loja.

&emsp;Recordamos que nós temos como compromisso não tratar os seus Dados Pessoais de forma incompatível com os objetivos descritos acima, exceto se de outra forma requerido por lei ou ordem judicial.

&emsp;Sua utilização da Loja após as alterações significa que aceitou as Políticas de Privacidade revisadas. Caso, após a leitura da versão revisada, você não esteja de acordo com seus termos, favor encerrar o acesso à Loja.

&emsp;Pessoa responsável do tratamento dos Dados Pessoais
&emsp;Caso pretenda exercer qualquer um dos direitos previstos nesta Política de Privacidade e/ou nas Leis de Proteção de Dados, ou resolver quaisquer dúvidas relacionadas ao Tratamento de seus Dados Pessoais, favor contatar-nos através do e-mail contato@mobly.com.br.

### 4.2. Compreensão dos Dados

#### 4.2.1. Exploração de dados

&emsp;Nesse tópico aborda-se como foi feita e a importância da exploração dos dados do Modelo Preditivo para a Mobly. Assim, neste tópico, aborda-se uma faceta crucial da análise dessas informações, buscando compreender como a exploração de dados desempenha um papel fundamental na extração de insights significativos e na tomada de decisões para o projeto. Além disso, destaca-se a relevância dos mesmos como ferramentas valiosas que capturam pensamentos, raciocínios e contextos durante o processo de exploração de dados. Essa combinação entre análise exploratória e documentação reflexiva oferece uma base sólida para a compreensão profunda de conjuntos de dados complexos e a comunicação eficaz dos resultados obtidos.
Na área da análise de dados, a exploração de dados refere-se ao processo de investigar e examinar um conjunto de dados com o objetivo de descobrir padrões, tendências e informações relevantes. Essa etapa é fundamental para compreender a natureza dos dados antes de aplicar métodos mais avançados, como modelos preditivos.

&emsp;Ao explorar dados, sào realizados exames a respito das distribuições das variáveis com o objetivo de identificar possíveis relações entre os diferentes atributos, avaliar a presença de valores ausentes ou discrepantes, e visualizar os dados de várias maneiras. Essa exploração ajuda a revelar insights iniciais e a formular hipóteses sobre como os atributos estão relacionados.

&emsp;A importância da exploração de dados em um modelo preditivo é notável. Ela permite que os analistas entendam a qualidade e a confiabilidade dos dados disponíveis, identifiquem variáveis que podem ter influência significativa nas previsões e escolham as técnicas de modelagem mais adequadas. Além disso, a exploração de dados ajuda a evitar a introdução de viés nos modelos, ao identificar possíveis distorções ou desequilíbrios nos dados.

&emsp;Em resumo, a exploração de dados desempenha um papel crucial na construção de modelos preditivos precisos e confiáveis. Ela fornece o alicerce necessário para a seleção criteriosa de variáveis, o pré-processamento adequado dos dados e a escolha das abordagens analíticas mais apropriadas. Sem uma exploração sólida, os modelos correm o risco de serem mal informados, levando a previsões incorretas ou enviesadas.

&emsp;A apresentação do gráfico de comparação de receitas por SKU color no contexto da criação de uma IA para previsão de vendas é uma estratégia fundamental para uma compreensão mais aprofundada dos padrões de vendas passados e para aprimorar a precisão das previsões futuras. Essa correlação entre o "Revenue" - a receita um produto - e o "Sku Color" - a cor daquele produto -, tem como objetivo compreender melhor alguns pontos. É  importante ressaltar que nesse dados temos campos categóricos e numéricos, sendo a cor, por exemplo, um dado categórico, e o númeo de vendas, por outro lado, um dado numérico.

*Figura 6 - Comparação de Revenue por SKU Color em 2021* </br>
![newplot (9)](https://github.com/2023M3T9-Inteli/grupo4/assets/84935638/ac5859b2-d9e2-4b96-a8fd-2587a68f68e4) </br>
*Fonte: Elaborado pelos próprios autores*

&emsp;Esse gráfico apresenta diversas características que poderão ser aproveitadas pelo modelo, dentre elas estão:

1. Identificação de Tendências Históricas: Ao visualizar o gráfico, é possível identificar quais SKU colors têm historicamente gerado mais receitas ao longo do tempo. Isso pode revelar tendências de vendas sazonais, preferências dos consumidores ou outros padrões que podem afetar as previsões futuras. Um exemplo é a venda de SKUs na Black Friday, que por ser um evento onde há desconto e o móveis ficam mais baratos, é possível se enxergar com clareza que a quantidade de vendas aumenta muito. Portanto é uma época do ano que a demanda é maior, o que altera a quantidade de itens necessárias em estoque.

2. Foco em Itens Lucrativos: O gráfico pode destacar SKU colors que geram uma receita significativamente maior do que outras. Isso é crucial para a IA priorizar esses itens em suas previsões, uma vez que esses produtos têm um impacto mais substancial nos resultados financeiros.

3. Sazonalidade e Ciclos de Vendas: O gráfico pode revelar picos de vendas associados a determinadas SKU colors. Isso é particularmente útil para entender a sazonalidade dos produtos e ajustar as previsões de acordo, garantindo que a IA leve em consideração essas flutuações cíclicas.

4. Otimização de Estoque e Produção: Com base nas informações do gráfico, as decisões relacionadas ao gerenciamento de estoque e produção podem ser aprimoradas. Itens com vendas consistentes podem ser produzidos em maior quantidade, enquanto os de menor desempenho podem ter seus estoques reduzidos.

5. Personalização das Estratégias: A análise das receitas por SKU color ajuda a desenvolver estratégias de marketing e promoção mais eficazes. Itens populares podem receber mais investimento em promoção, enquanto produtos com desempenho mais fraco podem ser alvo de campanhas específicas. Tal 

&emsp;Em resumo, o gráfico de comparação de receitas por SKU color fornece insights valiosos para a IA de previsão de vendas, orientando a seleção de recursos, validando previsões, otimizando estratégias de estoque e produção e adaptando as abordagens de marketing. Ao entender a importância desses insights passados, a IA tem maior probabilidade de fazer previsões mais precisas e informadas, contribuindo para a tomada de decisões estratégicas e melhores resultados financeiros.

&emsp;O próximo gráfico estabelece uma correlação entre a quantidade de visitas ao site da Mobly e os produtos vendidos. Sob essta ótica, o gráfico é essencial para entender melhor como que os clientes tomam a decisao na hora da compra e a taxa de conversão de compras, ou seja, a assertividade que o produto tem para as vendas online. Este gráfico tem campos apenas numéricos.

*Figura 7 - Relações Entre os Itens Vendidos e a Visita Média Semanal* </br>
![image](https://github.com/2023M3T9-Inteli/grupo4/assets/123904558/bf7a9838-56c3-46f0-b11a-c8a00b426a16) </br>
*Fonte: Elaborado pelos próprios autores*

&emsp;Este gráfico estabelece uma relação entre a quantidade de itens vendidos e o número total de visualizações de produtos em um dia. Através do cálculo da razão entre essas duas variáveis e sua representação gráfica, é possível identificar padrões e tendências. Quanto maior a razão entre quantidade de itens vendidos e visualizações totais, menor é o número de visitas no site em relação às vendas. Dessa forma, é possível identificar duas principais características de relevância ao projeto:

1. Compreensão do comportamento do cliente: O gráfico revela se os clientes estão navegando por mais produtos antes de realizar uma compra ou se estão decidindo rapidamente.

2. Taxa de conversão de vendas: Ajuda a medir a eficácia das estratégias de conversão, otimizando a experiência do usuário.

&emsp;Portanto, o gráfico de Relação Entre Itens Vendidos e Visita Média Semanal gera insights sobre o giro do produto e o quão ele é assertivo, entendendo melhor a lógica de escoamento da empresa e assertividade que ela tem com seus produtos. Tal gráfico relacionado à outros gráficos, por exemplo, um gráfico de visitas diárias ao e-commerce, traz mais repertório para que a IA entenda a necessidade diária do estoque e a média de produtos que giram por dia no mesmo.

&emsp;O último gráfico representa a divisão do mês em 6 períodos para compreender a diferença de renda entre eles. O gráfico representa primcipalmente em que época do mês que a empresa têm mais giro de estoque. Por exemplo, no gráfico é interessante notar, que, nos períodos de final de mês, são feitas mais vendas do que nos períodos do início do mês, de acordo com o parceiro isso se da pelo fato de ser a época que está perto da virada da fatura dos cartões de crédito, o que é um gatilho para o cliente comprar mais móveis. Vale ressaltar que o gráfico representado a baixo tem apenas dados numéricos.

*Figura 8 - Receita ao Longo dos Meses* </br>
![gráfico 1](https://github.com/2023M3T9-Inteli/grupo4/assets/124094681/982f7c3d-5383-4933-84a5-23447aaa3947) </br>
*Fonte: Elaborado pelos próprios autores*

&emsp;Esse gráfico divide o mês em seis períodos para analisar as variações de renda ao longo do tempo. Cada período pode representar uma semana ou outra divisão temporal relevante para o negócio. Suas características mais relevantes são:

1. Identificação de padrões sazonais: Possibilita a identificação de flutuações regulares na renda ao longo do mês, como picos de vendas em determinados períodos.

2. Estratégias diferenciadas: Permite ajustar as estratégias de marketing, promoções e estoque de acordo com as variações de demanda em diferentes momentos do mês.

&emsp;Em resumo, o gráfico de Receita ao Longo dos Meses gera informações valiosas para o treinamento do modelo preditivo, já que aumenta a precisão de previsão de demanda dentro do mês, facilitando a compra de entoque e diminuindo riscos de falta ou de excedentes no mesmo.
Em suma, todos os gráficos que o grupo trouxe para análise, são de importânciaconsiderável para uma boa elaboração do modelo preditivo em desenvolvimento e, sendo assim, terão sua devida utilização em diversos momentos do projeto.

#### 4.2.2. Pré-processamento dos dados

&emsp;O pré-processamento de dados envolve atividades de preparação, organização e estruturação dos dados, visando melhorar sua qualidade, resolver problemas, como outliers, e garantir a adequação do conjunto de dados ao modelo preditivo. Algumas das etapas de pré-processamento incluem: Limpeza de dados, transformação de dados e codificação de variáveis categóricas, entre outras.

&emsp;Neste projeto, para a limpeza dos dados, iniciamos com um estudo de cada campo da planilha para identificar valores faltantes, os quais foram tratados como missing. Nesse contexto, optamos por removê-los, a fim de aumentar a precisão do modelo em relação aos valores necessários.

&emsp;Além disso, para lidar com outliers, todos os dados foram ajustados para uma mesma escala. Valores exponenciais foram normalizados usando logaritmo, o que resultou em uma distribuição linear, fazendo com que os dados assumam um comportamento mais adequado para a implementação em um modelo preditivo. 

&emsp;No entanto, a análise identificou a presença de outliers, que podem ser examinados em maior detalhe no "Notebook_principal", na seção denominada "Retirando Outliers". Devido ao grande número de outliers detectados nas colunas sku_weight, sku_lenght e supplier_delivery_time, optou-se por não apresentá-los em formato textual, no entanto, eles estão disponíveis para observação completa no notebook.

&emsp;Para abordar esses valores atípicos, optou-se pela estratégia de removê-los. Isso permitirá que o modelo seja construído em um contexto mais robusto e representativo, minimizando o impacto desses pontos extremos nos resultados.

&emsp;Para a transformação das colunas categóricas, optamos por usar a biblioteca LabelEncoder, que atribuiu valores únicos a cada categoria. Por fim, a normalização dos dados foi feita através do tratamento de valores exponenciais que possuem relevância significativa no modelo, com o objetivo de evitar problemas na visualização e nos cálculos, que podem ser impactados por informações não relevantes. 
#### 4.2.3. Hipóteses

&emsp;As hipóteses desempenham um papel crucial no aprimoramento da eficácia de um modelo de IA. Elas atuam como guias estratégicas para a seleção dos dados mais relevantes que serão fornecidos como entrada para o algoritmo. Ao definir hipóteses claras, é possível compreender quais características ou variáveis terão o maior impacto na previsão final, permitindo uma abordagem mais focada na coleta e preparação dos dados.

&emsp;Além disso, a elaboração de hipóteses sólidas contribui substancialmente para a etapa de pré-processamento de dados. Ao entender como os dados podem influenciar a previsão final, é mais fácil identificar possíveis outliers, erros ou lacunas nos dados, o que facilita a limpeza e o tratamento do banco de dados. Isso resulta em um conjunto de dados mais consistente e confiável, que por sua vez melhora a robustez do modelo de IA.

&emsp;A precisão do modelo também é grandemente beneficiada pelo estabelecimento de hipóteses bem fundamentadas. Ao direcionar os esforços para as características mais relevantes e impactantes, o modelo pode capturar padrões mais significativos nos dados, levando a previsões mais acuradas. Hipóteses que apontam diretamente para os fatores críticos proporcionam insights sobre quais recursos o modelo deve considerar com mais ênfase, aumentando a sua eficácia preditiva.

&emsp;A formulação de hipóteses concisas e direcionadas não apenas guia a construção do modelo preditivo, mas também desempenha um papel na satisfação do cliente com o resultado final. Ao alcançar previsões mais precisas e relevantes, o valor do produto de IA é amplificado, atendendo às expectativas e necessidades do cliente de maneira mais eficaz.

&emsp;Aqui estão três exemplos de hipóteses elaboradas, destacando como elas podem influenciar a precisão do modelo:

Hipótese 1: A Integração da Cor deve ser considerada como um parâmetro de Input para a IA

&emsp;Com base na análise das tendências de vendas e no feedback recebido no encontro de validação da 2ª Sprint (25/08/2023), podemos formular a seguinte hipótese: a cor dos produtos não deve ser considerada como um resultado final da IA, mas sim um fator de input que influencia as recomendações de compras para o estoque da Mobly. A hipótese sugere que ao integrar a cor como um dos parâmetros de entrada para o sistema de IA, a máquina será capaz de considerar a preferência do cliente por cores específicas ao determinar quais itens devem ser adquiridos para o estoque.

&emsp;Dentro dessa hipótese, espera-se que a IA leve em conta a cor dos produtos como um dos vários fatores, juntamente com histórico de vendas, sazonalidade, períodos do mês e outros dados relevantes, para gerar recomendações mais precisas e alinhadas com as preferências dos clientes. Isso permitiria que a Mobly mantivesse um estoque otimizado, oferecendo os produtos mais procurados nas cores preferidas pelos consumidores em momentos estratégicos. Utilizando esse gráfico é possível avaliar quais cores necessitam de maior quantidade no estoque que outras cores. Caso a pessoa de suply chain decida comprar a mesma quantidade de cor do produto, tal empregador verá que as cores pretas, brancas e cinzas tem maior giro e necessitam de maiores quantias no estoque, já as demais cores tem um poder de giro menor, o que acarreta em um acumulamento de uma determinada cor do produto dentro do estoque. Portanto, utilizando o modelo preditivo é possível entender quais cores tem mais giro que outras, preparando o estoque para esse tipo de situação.

Hipótese 2: Os meses de Novembro a Janeiro representam períodos de exceções sazonais

&emsp;Ao analisar as tendências de receita ao longo dos meses, constata-se que os períodos do mês têm uma influência considerável nas variações de vendas, corroborando com as informações fornecidas pelos representantes da Mobly. Durante um mês típico, a receita oscila notavelmente, variando entre 2 a 3 milhões de reais. No entanto, deve-se salientar que a abordagem estratégica centrada nos períodos do mês não é aplicável ao período que se estende do início de novembro ao meio de janeiro, uma vez que esses meses são caracterizados como outliers.

&emsp;A observação das flutuações de receita destaca a relevância de adaptar uma estratégia que leva em consideração as diferentes fases do mês. Contudo, os meses entre novembro e janeiro surgem como exceções, apresentando comportamentos distintos que escapam ao que é observado em outros meses. Os dados revelam uma tendência que difere significativamente em relação ao padrão geral dos períodos do mês. Portanto, a hipótese afirma que, embora uma estratégia baseada em períodos mensais seja valiosa, é crucial reconhecer que os meses atípicos, de novembro a janeiro, exigem uma abordagem diferenciada devido à influência de fatores sazonais ou eventos específicos.

&emsp;Entender as flutuações de receita ao longo dos meses é crucial para otimizar nosso modelo preditivo. A análise revela que os períodos mensais têm um impacto significativo nas variações de vendas, alinhando-se com informações da equipe Mobly. Embora a estratégia mensal seja valiosa na maioria dos meses, os meses de novembro a janeiro são exceções, exibindo padrões atípicos devido a fatores sazonais. Essa hipótese ressalta a importância de uma abordagem diferenciada para esses meses, equilibrando a precisão do modelo com a adaptação a cenários excepcionais.

Hipótese 3: Em média, a cada 30 itens visualizados no site, 1 é vendido

&emsp;Com base na análise do gráfico que compara a relação entre o número de itens vendidos e a média semanal de visitas ao site, surge a seguinte hipótese: em média, a cada 30 itens visualizados no site da Mobly, ocorre a venda de aproximadamente 1 item.

&emsp;A interpretação do gráfico evidencia uma conexão entre a quantidade de itens vendidos e a atividade de visualização por parte dos visitantes do site. Uma proporção notável se destaca, indicando que, em termos médios, a cada conjunto de 30 itens que são visualizados, aproximadamente 1 deles é efetivamente vendido.

&emsp;A compreensão dessa relação entre visualizações e vendas é de grande utilidade para aprimorar o modelo de previsão de estoque da Mobly. Essa informação proporciona um indicador mais robusto e detalhado do comportamento do cliente, permitindo que a IA leve em consideração não apenas as vendas passadas, mas também a atividade de visualização que antecede essas vendas.

&emsp;Em resumo, a formulação de hipóteses sólidas e estrategicamente orientadas desempenha um papel fundamental no aprimoramento do processo de construção de modelos de IA. Ao compreender como os dados podem influenciar as previsões finais, torna-se possível selecionar e preparar os dados de maneira mais eficaz, resultando em modelos mais precisos e confiáveis. Além disso, a adaptação a cenários excepcionais, como os meses atípicos identificados, demonstra a flexibilidade e a capacidade do modelo de abordar situações complexas do mundo real. Ao considerar esses elementos, garantimos que o produto final não apenas atenda às expectativas do cliente, mas também se destaque na entrega de previsões valiosas e contextualmente relevantes.

### 4.3. Preparação dos Dados e Modelagem


#### 4.3.1

&emsp;No campo da análise de dados e aprendizado de máquina, várias abordagens e algoritmos têm sido empregados para solucionar desafios complexos, como previsões de demanda em ambientes empresariais. Entre essas abordagens, as que receberam mais destaque são os modelos Random Forest, Ridge, PolynomialRegression e Gradient Boost.

&emsp;Sendo assim, o Random Forest é um algoritmo de aprendizado de máquina baseado em um conjunto de árvores de decisão individuais. Cada árvore é treinada com uma amostra dos dados e gera uma previsão, de tal forma que a previsão final é obtida através de uma combinação das previsões individuais das árvores. Essa abordagem de conjunto permite a redução do overfitting, além de lidar bem com dados complexos, características irrelevantes e ruído [[17]](#c23).

&emsp;Ademais, o Random Forest pode capturar relações não lineares e interações complexas entre variáveis, tornando-o uma escolha sólida para previsões de demanda em ambientes empresariais. Suas vantagens incluem alta precisão, robustez, capacidade de lidar com dados desbalanceados e ruído, e a possibilidade de capturar interações complexas entre fatores. No entanto, ele pode ser computacionalmente complexo e a interpretação do modelo resultante pode ser desafiadora [[17]](#c23).

&emsp;O Polynomial Regression é um algoritmo de regressão que modela a relação entre uma variável independente e uma variável dependente como um polinômio de grau n. Isso permite capturar relações não lineares entre as variáveis, tornando-o uma escolha sólida para previsões de demanda em ambientes empresariais. No entanto, é importante ajustar o grau do polinômio adequadamente para evitar overfitting [[26]](#c32).

&emsp;O Gradient Boost é um algoritmo de aprendizado de máquina que constrói um modelo de previsão a partir de árvores de decisão individuais em uma abordagem sequencial, onde cada árvore corrige os erros do modelo anterior. Isso o torna poderoso para capturar relações complexas entre variáveis e lidar com dados desbalanceados. No entanto, é importante ajustar os hiperparâmetros adequadamente para obter bons resultados [[23]](#c29).

&emsp;Dentre essas abordagens, o Gradient Boost foi escolhido devido à sua capacidade de lidar com a complexidade dos dados empresariais e capturar relações não lineares e interações complexas entre variáveis. Além disso, sua abordagem sequencial permite melhorar o desempenho do modelo ao longo do tempo. No entanto, é importante ajustar os hiperparâmetros adequadamente para obter resultados ótimos. Essa escolha foi feita porque o Gradient Boost se adapta bem aos desafios de previsão de demanda da Mobly, oferecendo a capacidade de capturar relações complexas e lidar com dados desbalanceados. Embora outras abordagens sejam viáveis, o Gradient Boost demonstrou ser uma escolha sólida para fornecer resultados precisos e confiáveis na gestão da demanda da empresa Mobly.

##### 4.3.2

&emsp;Métricas Preditivas são medidas quantitativas utilizadas para avaliar o desempenho de modelos de machine learning e de conjuntos de dados estatísticos que realizam previsões ou estimativas. A sua realização é dada após a modelagem, e permitem medir a eficiência de um modelo em termos de suas previsões. Ademais, algumas das métricas possíveis para modelos de regressão, como o que está sendo utilizado, são: Coeficiente de Determinação ($R^2$), Erro Médio Absoluto (MAE), Erro Quadrático Médio (MSE) e Raiz Quadrada do Erro Médio (REMQ).

&emsp;A primeira métrica usada foi o $R^2$, também conhecido como Coeficiente de Determinação, é uma métrica que representa a proporção da variabilidade dos dados capturada pelo modelo. Seus valores podem variar de 0 a 1 e são frequentemente expressos como uma porcentagem (de 0% a 100%). De tal maneira que, quanto maior o valor de $R^2$, melhor o modelo é em explicar as variações nos dados [[15]](#c21).

&emsp;Esta métrica é empregada para avaliar a adequação de um modelo de regressão, medindo a proporção da variância total dos dados explicada pela relação linear com as variáveis independentes. Em suma, ela oferece uma indicação da qualidade do ajuste do modelo aos dados observados [[16]](#22). Contudo, enquanto o $R^2$ serve como uma medida ampla da qualidade do modelo, ele não fornece informações detalhadas sobre o funcionamento do modelo para diferentes pontos de dados ou sobre sua adequação para uma análise específica.

&emsp;A fórmula do Coeficiente de Determinação é: $$1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}$$ </br>
$SS_{res}$ = soma dos quadrados dos erros. </br>
$SS_{tot}$ =  A soma total dos quadrados, que mede a variabilidade total dos valores observados em relação à média dos valores observados. É a soma das diferenças entre os valores observados e a média ($y - \hat{y}$) ao quadrado para todos os pontos de dados. </br>

&emsp;A segunda métrica a ser considerada é o Erro Médio Absoluto (EMA), o qual é amplamente usado para avaliar o desempenho de modelos de regressão e machine learning. Esta métrica quantifica a média das diferenças absolutas entre os valores previstos pelo modelo e os valores reais observados nos dados. Sendo assim, o EMA é uma medida direta de quão distantes as previsões do modelo se encontram dos valores reais.

&emsp;A fórmula para calcular o Erro Médio Absoluto é: $$\frac{1}{n} \sum_{i=1}^{n}|y_i - \hat{y}_i|$$ </br>
$n$ = número total de exemplos de dados. </br>
$y_i$ = número total de exemplos de dados. </br>
$\hat{y}_i$ = representa o valor previsto pelo modelo para o i-ésimo exemplo. </br>

&emsp;Dessa forma, o EMA é uma métrica intuitiva que calcula a média das diferenças absolutas, independentemente de serem positivas ou negativas. Quanto menor o valor do EMA, melhor o modelo se ajusta aos dados, indicando que suas previsões estão mais alinhadas com os valores reais. É relevante destacar que o EMA não penaliza erros grandes tão intensamente quanto algumas outras métricas, como o Erro Quadrático Médio (EQM). Assim, ele pode ser mais apropriado quando o objetivo é avaliar o desempenho do modelo de forma mais robusta diante de "outliers".

&emsp;Ademais, o Erro Quadrático Médio (EQM) é outra métrica amplamente adotada para avaliar modelos de regressão e previsão. Desse modo, assim como o EMA, o EQM quantifica a discrepância entre as previsões do modelo e os valores reais. É importante ressaltar que o EQM possui uma particularidade: penaliza erros maiores de forma mais intensa. Isso ocorre porque, ao contrário do EQM, que considera o valor absoluto da diferença,  o EQM eleva esta diferença ao quadrado antes de calcular a média.

&emsp;A fórmula para calcular o Erro Quadrático Médio é: $$\frac{1}{n} \sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$ 
$n$ = número total de exemplos de dados. </br>
$y_i$ = número total de exemplos de dados. </br>
$\hat{y}_i$ = representa o valor previsto pelo modelo para o i-ésimo exemplo. </br>

&emsp;Um EQM menor indica um ajuste mais preciso do modelo. Contudo, por elevar ao quadrado a diferença, essa métrica é mais sensível a outliers que o EMA [[15]](#c21).

&emsp;Por fim, o REMQ (Raiz do Erro Médio Quadrático) é uma métrica que segue o mesmo princípio do EMA, incluindo a ideia de penalização por diferenças significativas entre os valores previstos e os valores reais. No entanto, o REMQ adiciona um componente importante: a raiz quadrada na fórmula, que permite que as diferenças sejam tratadas na mesma escala que os dados originais. Isso resulta em uma métrica que fornece uma interpretação mais intuitiva dos erros, pois as unidades permanecem consistentes com os dados originais  [[15]](#c21). 

A fórmula do Raiz do Erro Médio Quadrático = $$\sqrt{\frac{1}{n} \sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$ </br>
$n$ = número total de exemplos de dados. </br>
$y_i$ = número total de exemplos de dados. </br>
$\hat{y}_i$ = representa o valor previsto pelo modelo para o i-ésimo exemplo. </br>

#### 4.3.3

&emsp;Na perspectiva da previsão de demanda na Mobly, a seleção do método de aprendizado de máquina assume um papel de considerável importância na busca por previsões exatas e confiáveis. Dentre as alternativas à disposição, o algoritmo Gradient Boost se apresenta como uma escolha sólida e fundamentada, devido às suas propriedades particulares e à sua capacidade de lidar com os desafios inerentes à previsão de demanda em um ambiente empresarial [[23]](#c29).

&emsp;O Gradient Boost é um método de aprendizado de máquina que constrói um modelo de previsão de forma sequencial, utilizando árvores de decisão individuais. Para uma compreensão simplificada, podemos imaginá-lo como a formação de uma equipe de especialistas em previsão, na qual cada especialista é representado por uma árvore de decisão. Cada especialista (ou árvore) concentra-se em corrigir os erros cometidos pelo especialista anterior, semelhante à ideia de uma equipe de trabalho aprimorando seu desempenho com o passar do tempo [[23]](#c29).

&emsp;Isso torna o Gradient Boost notável é sua habilidade para lidar com dados complexos e variáveis irrelevantes. Ele automaticamente avalia a importância das informações disponíveis para realizar as previsões, assemelhando-se à capacidade de uma equipe que compreende quais dados são mais cruciais para a tarefa em questão [[24]](#c30).

&emsp;Adicionalmente, o Gradient Boost demonstra uma notável resiliência em relação a dados ruidosos e é apto a trabalhar com conjuntos de dados desbalanceados, uma ocorrência frequente em cenários de previsão de demanda. Essa resiliência é de extrema relevância para garantir que o modelo forneça previsões precisas, mesmo em situações desafiadoras e sujeitas a flutuações imprevisíveis [[25]](#c31).

&emsp;Uma característica adicional de destaque do Gradient Boost reside na sua capacidade de capturar relações não lineares e interações complexas entre variáveis. Em ambientes empresariais, as relações entre os fatores que afetam a demanda podem ser intricadas e não lineares. O Gradient Boost é eficaz na modelagem dessas relações, resultando em previsões mais realistas e precisas [[25]](#c31).

&emsp;No contexto do projeto da Mobly, em que a previsão de demanda desempenha um papel crucial na gestão eficaz de recursos e estoque, a escolha do Gradient Boost é amplamente justificada. Sua abordagem sequencial, capacidade de enfrentar a complexidade dos dados, variáveis irrelevantes, ruídos e relações não lineares fazem dele uma opção de destaque. Além disso, ao melhorar progressivamente o modelo ao longo do processo de previsão, o Gradient Boost é capaz de fornecer previsões confiáveis e generalizáveis [[24]](#c30).

&emsp;Em resumo, considerando a complexidade dos dados, a presença de variáveis irrelevantes, ruído e a necessidade de lidar com relações não lineares, o Gradient Boost se destaca como a escolha ideal para o projeto de previsão de demanda na Mobly. Suas características únicas e sua adaptação aos dados empresariais garantem que seja a melhor opção para fornecer previsões precisas e embasadas, o que é essencial para a tomada de decisões informadas e estratégicas em um ambiente empresarial altamente competitivo.

### 4.4. Comparação de Modelos

&emsp;A comparação de modelos preditivos desempenha um papel crucial na análise de dados e no desenvolvimento de modelos de machine learning. Nesse contexto, no projeto da Mobly, várias métricas de avaliação foram utilizadas, incluindo o Coeficiente de Determinação (R²), o Erro Médio Absoluto (EMA), o Erro Quadrático Médio (EQM) e a Raiz Quadrada do Erro Médio (REQM). <br>
&emsp;Ao analisar as características dessas métricas, o REQM emergiu como a escolha mais adequada para avaliar o desempenho do modelo de Gradient Boosting. O REQM calcula a raiz quadrada da média dos quadrados das diferenças entre os valores reais e os valores previstos. Quanto menor o valor do REQM, melhor o desempenho do modelo, indicando previsões mais próximas dos valores reais. Além disso, o REQM retorna resultados na mesma unidade da variável alvo, facilitando a interpretação dos resultados e a compreensão de desvios em relação aos dados de estoque da Mobly. <br>
&emsp;É importante notar que o REQM é sensível a outliers, o que significa que ele penaliza erros maiores de forma mais significativa do que erros menores. No entanto, essa métrica é particularmente adequada para avaliar modelos de regressão, como no caso do projeto da Mobly, onde o objetivo é prever valores numéricos com precisão. Com isso, as demais métricas não foram amplamente utilizadas, pois, por exemplo, a R² retorna valores ao quadrado e não fornece informações detalhadas sobre as previsões de vendas por SKU, que é uma necessidade específica deste projeto, já que ela estabelece o grau de correlação. Já o EQM retorna resultados fora da escala que necessitamos, ou seja, está dando os valores de SKU ao quadrado. Além disso, o EQM é uma medida que quantifica a média dos quadrados dos erros entre as previsões de um modelo e os valores reais. Quanto menor o valor do EQM, melhor o desempenho do modelo, indicando que as previsões estão mais próximas dos valores reais. No entanto, essa métrica é sensível a outliers e não se torna uma boa métrica de validação. Então, com base nesses pontos tratados, demonstra-se que o REQM se torna a melhor métrica. <br>
&emsp;No projeto, foram implementados diferentes modelos preditivos, incluindo o Polynomial Regression, o Random Forest e o Gradient Boost. A Polynomial Regression, ou Regressão Polinomial em português, é um tipo de técnica de modelagem de dados utilizada no campo de aprendizado de máquina e estatísticas. Enquanto a regressão linear busca estabelecer uma relação linear simples entre uma variável de resposta (também chamada de variável dependente) e uma ou mais variáveis de entrada (variáveis independentes), a regressão polinomial permite modelar relações mais complexas e não lineares entre essas variáveis. <br>
&emsp;Essa técnica é chamada de "polinomial" porque ela se baseia na expansão de variáveis independentes em termos de polinômios de diferentes graus. Em outras palavras, a regressão polinomial ajusta um modelo que é uma combinação de termos polinomiais, como x, x², x³, e assim por diante, em vez de uma simples reta. <br>
A principal vantagem da regressão polinomial é sua capacidade de se adaptar a dados que não seguem uma relação linear simples, como curvas, ondulações ou padrões não lineares. Isso a torna útil em situações em que a relação entre as variáveis é mais complexa e a regressão linear não é adequada. <br>
&emsp;No entanto, é importante notar que a regressão polinomial também pode ser sensível ao overfitting, especialmente quando se usa polinômios de alto grau, o que pode levar a um modelo que se ajusta demais aos dados de treinamento e não generaliza bem para novos dados. Portanto, ao usar a regressão polinomial, é necessário encontrar um equilíbrio entre a complexidade do modelo (representada pelo grau do polinômio) e a capacidade de generalização. [[19]](#25) <br>
&emsp;Outro modelo utilizado foi O Random Forest que é uma técnica poderosa em análises de regressão, amplamente adotada em ciência de dados e aprendizado de máquina. Sua principal vantagem é a capacidade de lidar com dados complexos e ruidosos, resistindo a outliers e valores atípicos. Isso o torna ideal para situações do mundo real, onde os dados podem ser imperfeitos [[17]](#c23). <br>
&emsp;Além disso, o Random Forest é robusto contra o overfitting, um problema comum em modelagem. Ele constrói várias árvores de decisão independentes e combina suas previsões, o que ajuda a evitar ajustes excessivos aos dados de treinamento e melhora o desempenho em dados de teste. [[17]](#c23) <br>
&emsp;Outro ponto forte é a capacidade de avaliar a importância relativa de cada atributo na previsão, auxiliando na interpretação do modelo. Entretanto, ele não é muito adequado quando há relações complexas e não lineares nos dados [[17]](#c23).. <br>
&emsp;Já o Gradient Boost é uma técnica avançada de aprendizado de máquina que se destaca pela sua capacidade de produzir modelos de alta precisão em uma variedade de tarefas de previsão e classificação. Essa abordagem pertence à família de algoritmos de ensemble, que combinam várias árvores de decisão simples para criar um modelo mais poderoso e preciso [[18]](#c24). <br>
&emsp;A ideia central por trás do Gradient Boost é construir uma série de árvores de decisão fracas, que são árvores de decisão com baixa capacidade de modelagem, e depois combiná-las para formar um modelo forte. A cada etapa, o algoritmo ajusta a árvore de decisão para corrigir os erros cometidos pelas árvores anteriores. Esse processo é repetido várias vezes, e as previsões de todas as árvores são combinadas para produzir a previsão final [[18]](#c24).<br>
&emsp;Ao ajustar os parâmetros do Gradient Boost, o modelo busca encontrar a melhor combinação de árvores de decisão fracas, cada uma contribuindo para a melhoria das previsões. Essa abordagem é particularmente eficaz em casos em que as relações entre as variáveis independentes e a variável dependente são complexas e não lineares. O Gradient Boost se mostrou o melhor modelo para ser implementado nesses tipos de dados, permitindo previsões precisas da quantidade de móveis em estoque. <br>
&emsp;Além disso, após a escolha do Gradient Boost, foi realizado o ajuste de hiperparâmetros, uma técnica fundamental em aprendizado de máquina e ciência de dados. O ajuste de hiperparâmetros envolve a seleção cuidadosa de valores para parâmetros importantes do modelo, a fim de otimizar seu desempenho. <br>
&emsp;Dessa maneira, para encontrar a melhor combinação de hiperparâmetros, utilizou-se o Random Search, uma abordagem eficiente quando o espaço de hiperparâmetros é extenso. Isso permitiu explorar uma ampla gama de valores de hiperparâmetros de forma eficiente, garantindo resultados precisos e um custo computacional gerenciável. <br>
&emsp;Nessa perspectiva, os hiperparâmetros escolhidos foram:

- n_estimators: Este hiperparâmetro define o número de árvores de decisão (ou estimadores) que serão criadas no processo de Gradient Boosting. Cada árvore é treinada sequencialmente para corrigir os erros das árvores anteriores. Um valor maior de n_estimators geralmente resulta em um modelo mais robusto, mas também aumenta o tempo de treinamento.

- learning_rate: O learning rate (taxa de aprendizado) control

a a contribuição de cada árvore no ensemble. Um valor menor, como 0.01, significa que cada árvore contribui com uma pequena parte para a previsão final, tornando o modelo mais robusto, mas potencialmente exigindo um número maior de árvores para alcançar alta precisão. Valores maiores, como 0.5, fazem com que cada árvore tenha um impacto maior, tornando o modelo mais sensível aos dados, mas também mais propenso ao overfitting.

- max_depth: Este hiperparâmetro define a profundidade máxima de cada árvore de decisão no ensemble. Árvores mais profundas podem capturar relações mais complexas nos dados, mas também são mais propensas a overfitting. Definir um valor razoável ajuda a controlar a complexidade do modelo.

- min_samples_split: O min_samples_split determina o número mínimo de amostras necessárias para dividir um nó interno da árvore. Isso ajuda a evitar divisões que seriam muito específicas para o conjunto de treinamento, reduzindo o risco de overfitting.

- min_samples_leaf: O min_samples_leaf define o número mínimo de amostras necessário para formar uma folha da árvore. Isso ajuda a controlar o tamanho mínimo das folhas e evita divisões muito específicas, contribuindo para evitar o overfitting.

- Bootstrap: Com opções True e False, esse hiperparâmetro controla se a amostragem de dados é feita com substituição (bootstrapping). A inclusão dessas opções permitiu ao modelo explorar diferentes abordagens de amostragem, dependendo das características dos dados.

&emsp;Nessa perspectiva, o modelo Gradient Boost foi otimizado com o Random Search, pois ele é especialmente valioso quando se lida com um espaço de hiperparâmetros extenso, onde uma busca exaustiva se torna impraticável em termos de tempo e recursos computacionais. O Random Search permite uma exploração eficiente de uma ampla gama de valores de hiperparâmetros, embora não garanta a exploração de todas as combinações possíveis [[20]](#c26). Por outro lado, o Grid Search se torna menos viável, uma vez que é mais apropriado quando se tem uma compreensão clara dos valores ideais para os hiperparâmetros e deseja-se avaliar todas as combinações sistematicamente. Geralmente, o Grid Search é mais útil quando o espaço de hiperparâmetros é relativamente pequeno, pois pode ser computacionalmente custoso de outra forma. Portanto, dado o amplo espaço de hiperparâmetros neste projeto de Gradient Boosting, o Random Search emergiu como a escolha mais eficaz em termos de otimização. <br>
&emsp;Em resumo, o modelo Gradient Boost se destacou como a escolha mais adequada para resolver o problema de previsão de estoque da Mobly. Sua capacidade de lidar com relações complexas e não lineares entre variáveis e o ajuste cuidadoso de hiperparâmetros com o Random Search contribuíram para resultados precisos e eficientes. <br>

### 4.5. Avaliação

&emsp;Na seção 4.1 do projeto, o objetivo principal é estabelecer uma solução final para o modelo preditivo em questão, tendo em mente o entendimento do negócio e a conformidade com os requisitos e definições estabelecidos. A escolha da solução final foi um processo meticuloso e fundamentado, cujas razões serão explicadas a seguir.

&emsp;Sob essa ótica, a Mobly enfrentava um desafio crítico relacionado ao giro do estoque. Tal problema decorria da falta de uma ferramenta capaz de prever a demanda semanal e diária de SKUs (produtos) que seriam vendidos. Durante a entrevista de kickoff em 2023, os representantes da Mobly apresentaram os problemas atualmente enfrentados pela falta de um modelo preditivo funcional. Dentre eles, o principal é o tempo decorrido desde o planejamento da compra até o reabastecimento do estoque. Esse processo envolvia a utilização de parâmetros históricos para a medição de vendas dos últimos 30 a 60 dias, contato com os fornecedores e diversas reuniões para a tomada dessas decisões, entre outras etapas.

&emsp;A introdução do Modelo Preditivo de Estoque na Mobly representa uma abordagem inovadora e altamente eficaz para aprimorar as operações de supply chain e otimizar a gestão de inventário. Este sistema tem o potencial de revigorar a forma como a Mobly gerencia seu estoque, trazendo consigo uma série de benefícios substanciais e se destacando de outras soluções disponíveis no mercado.

#### **Potenciais da Proposta:**

**Precisão de Previsão:** O Modelo Preditivo de Estoque utiliza algoritmos avançados para prever com alta precisão as demandas futuras por produtos. Isso proporciona uma visão holística das necessidades de estoque, permitindo à Mobly tomar decisões embasadas e eficientes.

**Adaptação Dinâmica:** O modelo é capaz de se adaptar rapidamente às variações de demanda. Essa flexibilidade garante que as previsões permaneçam atualizadas e relevantes em um ambiente de negócios em constante evolução.

**Otimização de Recursos:** Ao evitar excesso ou ruptura de estoque, o modelo contribui para a otimização dos recursos financeiros da Mobly. Isso se traduz em redução de custos operacionais, evitando gastos desnecessários com armazenamento ou perdas de vendas.

#### **Benefícios da Proposta:**

**Eficiência Operacional:** Com o Modelo Preditivo de Estoque, a Mobly pode automatizar e aprimorar significativamente os processos de planejamento e recompra de estoque. Isso libera recursos e tempo para atividades estratégicas, impulsionando a eficiência geral das operações.

**Tomada de Decisões Informadas:** A base de dados confiável e análises precisas fornecidas pelo modelo capacitam os profissionais de supply chain a tomar decisões informadas e estratégicas. Isso resulta em um planejamento mais eficaz e assertivo.

**Minimização de Riscos:** A previsão precisa de demanda e recompra oportuna reduz os riscos associados a excesso ou escassez de estoque. Isso permite à Mobly responder de maneira ágil às flutuações do mercado, minimizando perdas e maximizando oportunidades.

&emsp;Em conclusão, a proposta de implementação do Modelo Preditivo de Estoque na Mobly apresenta um potencial promissor e uma série de benefícios tangíveis. Ao adotar essa solução, a Mobly estará equipada para otimizar seus processos de supply chain, melhorar sua eficiência operacional e tomar decisões mais informadas, alinhando-se perfeitamente com as necessidades específicas do mercado de varejo e suas operações de logística. A escolha desta solução representa um marco crucial no avanço dos esforços da Mobly para atingir o sucesso e a liderança em seu setor.

#### **Plano de Contingência para Falhas nas Previsões do Modelo:**

&emsp;É fundamental reconhecer que nenhum modelo preditivo é infalível, e a Mobly precisa estar preparada para lidar com situações em que o Modelo Preditivo de Estoque não atende às expectativas. Para isso, foi desenvolvido um sólido plano de contingência que visa mitigar os impactos negativos das falhas nas previsões. 

&emsp;Monitoramento Contínuo: Implementaremos um sistema de monitoramento constante das previsões do modelo. Isso envolve a análise regular da precisão das previsões em comparação com os dados reais de vendas e estoque. Caso seja identificada uma tendência persistente de falhas, as alarmes serão acionados.

&emsp;Avaliação das Causas das Falhas: É crucial entender as razões por trás das falhas do modelo. Realizaremos uma análise aprofundada para identificar se as falhas estão relacionadas a mudanças inesperadas nas tendências de mercado, sazonalidade, eventos especiais, erros nos dados de entrada ou outras variáveis não consideradas pelo modelo [[21]](#c27).

&emsp;Revisão e Aprimoramento do Modelo: Com base na análise das causas das falhas, trabalharemos na revisão e aprimoramento do Modelo Preditivo de Estoque. Isso pode envolver a incorporação de novos dados, ajuste dos parâmetros do modelo, ou até mesmo a adoção de algoritmos de aprendizado de máquina mais avançados, se necessário [[21]](#c27).

&emsp;Uso de Métodos de Suavização: Para casos em que as falhas sejam devido a flutuações temporárias e volatilidade extrema, consideraremos a implementação de métodos de suavização para tornar as previsões mais estáveis. Isso ajudará a evitar decisões drásticas baseadas em flutuações de curto prazo.

&emsp;Estoque de Segurança: Mantendo um estoque de segurança adequado para produtos de alta demanda e críticos, a Mobly estará preparada para atender à demanda mesmo em situações de falha do modelo. Isso pode ajudar a minimizar as perdas decorrentes de rupturas de estoque.

&emsp;Comunicação com Fornecedores: Em casos de falhas que afetem diretamente o reabastecimento, manteremos uma comunicação próxima com os fornecedores. Seremos transparentes sobre as dificuldades enfrentadas e buscaremos soluções alternativas para garantir o abastecimento adequado [[22]](#c28).

&emsp;Plano de Ação para Clientes: Para casos em que as falhas do modelo possam impactar as entregas ou disponibilidade de produtos para os clientes, estabeleceremos um plano de ação para minimizar o impacto. Isso incluirá comunicações proativas com os clientes, oferecendo alternativas quando possível.

&emsp;Treinamento da Equipe: A equipe responsável pelo gerenciamento do estoque e supply chain será treinada para tomar decisões informadas em situações de falha do modelo. Isso inclui o uso de dados históricos e conhecimento do mercado para tomar decisões estratégicas [[21]](#c27).

&emsp;Avaliação Contínua e Aprendizado: A Mobly manterá uma abordagem de aprendizado contínuo, avaliando a eficácia do plano de contingência e aplicando lições aprendidas para melhorar a resiliência do modelo preditivo e as operações gerais.

&emsp;Em resumo, este plano de contingência foi desenvolvido com o objetivo de permitir que a Mobly lide de maneira eficaz com falhas nas previsões do Modelo Preditivo de Estoque. Ao monitorar, avaliar, ajustar e tomar medidas adequadas, a Mobly estará bem preparada para enfrentar desafios imprevistos e garantir a continuidade de suas operações de supply chain de maneira eficiente e eficaz.

#### **Explorando as Hipóteses e sua Relevância para o Modelo:**

&emsp;As hipóteses desempenham um papel crucial no aprimoramento da eficácia de um modelo de IA, orientando a seleção de dados relevantes e influenciando a estratégia de previsão. Ao definir hipóteses claras e sólidas, é possível compreender quais características ou variáveis terão o maior impacto na previsão final, o que, por sua vez, permite uma abordagem mais focada na coleta e preparação dos dados.

**Contribuição das Hipóteses para o Pré-processamento de Dados:**

&emsp;A elaboração de hipóteses sólidas contribui substancialmente para a etapa de pré-processamento de dados. Com uma compreensão clara de como os dados podem influenciar a previsão final, é mais fácil identificar possíveis outliers, erros ou lacunas nos dados. Isso resulta em um conjunto de dados mais consistente e confiável, melhorando a robustez do modelo de IA.

**Aprimoramento da Precisão do Modelo:**

&emsp;A precisão do modelo também se beneficia significativamente do estabelecimento de hipóteses bem fundamentadas. Ao direcionar os esforços para as características mais relevantes e impactantes, o modelo pode capturar padrões mais significativos nos dados, levando a previsões mais acuradas. Hipóteses que apontam diretamente para os fatores críticos proporcionam insights sobre quais recursos o modelo deve considerar com mais ênfase, aumentando a sua eficácia preditiva.

**Satisfação do Cliente e Valor do Produto:**

&emsp;A formulação de hipóteses concisas e direcionadas desempenha um papel crucial na satisfação do cliente com o resultado final. Ao alcançar previsões mais precisas e relevantes, o valor do produto de IA é amplificado, atendendo às expectativas e necessidades do cliente de maneira mais eficaz.

&emsp;Aqui estão três exemplos de hipóteses elaboradas, destacando como elas podem influenciar a precisão do modelo:

**Hipótese 1: Integração da Cor como Parâmetro de Input:**

&emsp;Com base na análise das tendências de vendas e no feedback recebido no encontro de validação da 2ª Sprint (25/08/2023), formulamos a seguinte hipótese: a cor dos produtos deve ser considerada como um parâmetro de input que influencia as recomendações de compras para o estoque da Mobly. A integração da cor como um dos parâmetros de entrada permite que o modelo leve em conta a preferência do cliente por cores específicas ao determinar quais itens devem ser adquiridos para o estoque.

&emsp;Dentro dessa hipótese, espera-se que modelo de machine learning leve em conta a cor dos produtos como um dos vários fatores, juntamente com histórico de vendas, sazonalidade, períodos do mês e outros dados relevantes, para gerar recomendações mais precisas e alinhadas com as preferências dos clientes.

**Hipótese 2: Exceções Sazonais nos Meses de Novembro a Janeiro:**

&emsp;Ao analisar as tendências de receita ao longo dos meses, constata-se que os períodos do mês têm uma influência considerável nas variações de vendas. No entanto, a hipótese destaca que os meses entre novembro e janeiro representam exceções sazonais, exibindo comportamentos distintos devido a fatores sazonais ou eventos específicos. Isso requer uma abordagem diferenciada para esses meses, reconhecendo que a estratégia baseada em períodos mensais pode não ser aplicável.

**Hipótese 3: Relação entre Visualizações e Vendas:**

&emsp;Com base na análise do gráfico que compara o número de itens visualizados no site e o número de itens vendidos, formulamos a hipótese de que, em média, a cada 30 itens visualizados no site da Mobly, ocorre a venda de aproximadamente 1 item. Essa relação entre visualizações e vendas é crucial para otimizar o modelo de previsão de estoque, permitindo que a IA leve em consideração não apenas as vendas passadas, mas também a atividade de visualização que antecede essas vendas.

&emsp;Em resumo, as hipóteses desempenham um papel central na construção de um modelo preditivo eficaz. Elas guiam a seleção de dados, influenciam o pré-processamento, aprimoram a precisão do modelo e contribuem para a satisfação do cliente. Ao adotar uma abordagem orientada por hipóteses, a Mobly está em posição de maximizar o valor de seu produto de IA, atendendo às necessidades do mercado de forma mais eficaz e precisa.

## <a name="c5"></a>5. Conclusões e Recomendações

&emsp;O projeto teve como principal objetivo facilitar a tomada de decisão no setor de gerenciamento de estoque, visando prever com precisão em quantos móveis serão vendidos em um espaço de tempo determinado pelo usuário, evitando assim a compra de itens que poderiam ficar parados no estoque. Para alcançar esse objetivo, a equipe de desenvolvimento utilizou um conjunto de dados fornecido pela Mobly, que continha informações detalhadas sobre mais de 800.000 móveis 
e suas respectivas vendas durante o período de 2020 a 2023. Além disso, dados econômicos, como o valor do dólar, taxa Selic na data de venda do produto, e taxa de desemprego, foram incorporados ao conjunto de dados.

&emsp;A técnica escolhida para a construção do modelo preditivo foi o algoritmo Gradient Boost, otimizado com o algoritmo de otimização Random Search. Para avaliar a eficácia do modelo, foram utilizadas métricas como Erro Quadrado Médio, Erro Médio Absoluto, Raiz do Erro Quadrado Médio e Coeficiente de Determinação. Os resultados obtidos demonstraram que o modelo possui boa precisão, com um Erro Quadrado Médio (MSE) de 283.7543054735171, um Erro Médio Absoluto (MAE) de 6.785278207488016, um Root Mean Squared Error (RMSE) de 16.8450083251246 e um Coeficiente de Determinação (R²) de 0.7100179868385621.

&emsp;As variáveis mais relevantes para as previsões do modelo incluem 'sku', 'unit_price', 'sku_height', 'sku_width', 'sku_length', 'sku_weight', 'winning_price', 'stock_qty', 'log_avg_website_visits_last_week', 'diferencia_concorrencia', 'semana_do_ano','selic' e 'taxa-desemprego'. Com essas informações, é possível prever com maior precisão por quanto tempo um produto em potencial ficará em estoque, permitindo uma tomada de decisão mais embasada.

&emsp;No entanto, é importante observar que a integridade dos dados é crucial para a precisão do modelo. Recomenda-se que o banco de dados seja constantemente atualizado e complementado com itens diversos, a fim de evitar enviesamentos nas previsões.

&emsp;Para otimizar o uso do modelo, recomenda-se a adequação do ambiente de desenvolvimento às práticas da Mobly, incluindo a divisão do código em vários notebooks ou a filtragem das células mais relevantes. Além disso, a criação de uma interface de usuário (UI) pode aprimorar a experiência do usuário final, tornando o acesso e a interpretação das previsões mais acessíveis.

&emsp; Além disso, é recomendado que caso seja utilizado o modelo de input e output criado pelos alunos, é necessário a adaptação de dois fatores. Sendo o primeiro, o tempo que pode ser previsto, que atualmente é uma única semana. Ademais, tem-se de criar um método para decodifar o sku para o seu código natural.

&emsp;Em resumo, o modelo preditivo de regressão Gradient Boost desenvolvido neste projeto oferece uma ferramenta valiosa para o setor de gerenciamento de estoque da Mobly, possibilitando decisões mais informadas e estratégicas em relação ao estoque de produtos. É fundamental manter a qualidade e a atualização dos dados para garantir a eficácia contínua do modelo e considerar a implementação de melhorias na interface do usuário para uma utilização mais eficiente.

## <a name="c6"></a>6. Referências

<a name="c7"></a> [1] MOBLY. Quem Somos. Disponível em: <https://investors.mobly.com.br/quem-somos/>. Acesso em: 5 ago. 2023. </br>
<a name="c8"></a> [2] MOBLY. Aplicativo Mobly. Disponível em: <https://www.mobly.com.br/aplicativo-mobly/>. Acesso em: 5 ago. 2023. </br>
<a name="c9"></a> [3] VENDA NA AMAZON. O que é SKU do produto e qual a importância de utilizar esse código? Disponível em: <https://venda.amazon.com.br/sellerblog/o-que-e-sku-do-produto-e-qual-a-importancia-de-utilizar-esse-codigo>. Acesso em: 5 ago. 2023. </br>
<a name="c10"></a> [4] BLOG CLEAR SALE. Modelo Preditivo: Saiba como aplicá-lo. Disponível em: <https://blogbr.clear.sale/modelo-preditivo-saiba-como-aplica-lo#:~:text=Um%20modelo%20preditivo%20é%2C%20de,matemática%2C%20com%20probabilidade%20e%20estatística>. Acesso em: 26 set. 2023. </br>
<a name="c11"></a> [5] VOITTO. Metodologia CRISP-DM: Descubra o que é a metodologia CRISP DM. Disponível em: <https://www.voitto.com.br/blog/artigo/crisp-dm>. Acesso em: 18 set. 2023. </br>
<a name="c12"></a> [6] INSTITUTO MUDITA. 12 Tipos de Modelos de Negócios. Disponível em: <https://www.institutomudita.com/blogmudi/12-tipos-de-modelos-de-negocios>. Acesso em: 26 set. 2023. </br>
<a name="c13"></a> [7] MANNESOFT MAIS LOJAS. Os Desafios e Oportunidades do Mercado de Móveis Pós-Pandemia. Disponível em: <https://www.mannesoftmaislojas.com.br/blog/os-desafios-e-oportunidades-do-mercado-de-moveis-pos-pandemia>. Acesso em: 26 set. 2023. </br>
<a name="c14"></a> [8] BLOG CLEAR SALE. Modelo Preditivo: o que é, para que serve e como aplicá-lo? Disponível em: <https://blogbr.clear.sale/modelo-preditivo-saiba-como-aplica-lo>. Acesso em: 8 ago. 2023. </br>
<a name ="c15"></a> [9] ROCK CONTENT. As 5 Forças de Porter: quais são elas e como entender o conjunto de fatores que influenciam no sucesso do seu negócio? Disponível em: <https://rockcontent.com/br/blog/5-forcas-de-porter/>. Acesso em: 6 ago. 2023. </br>
<a name ="c16"></a> [10] UFABC JR. Análise SWOT: o que é + 4 passos de como fazer do zero! Disponível em: <https://ufabcjr.com.br/metodologia-agil-analise-swot-2/?gclid=Cj0KCQjw2qKmBhCfARIsAFy8buIPIdcMWe_pyFdAqJ1e79rWXvp0rVsA3Ek4eb4MahhFY5zcLXNlBYwaAnrrEALw_wcB>. Acesso em: 1 ago. 2023. </br>
<a name ="c17"></a> [11] TAPI. Disponível em: <https://drive.google.com/file/d/1VGnbT8ICFWSSEOQ3tPEKNjyP223SkvtP/view>. Acesso em: 3 ago. 2023. </br>
<a name="c18"></a> [12] COMO FAZER MATRIZ DE ANÁLISE DE RISCOS. Disponível em: <https://www.youtube.com/watch?v=hxPjCp_hBg0>. Acesso em: 8 ago. 2023. </br>
<a name="c19"></a> [13] PERSONA: o que é, como definir e por que criar uma para sua empresa [+ exemplos práticos e um gerador]. Disponível em: <https://resultadosdigitais.com.br/marketing/persona-o-que-e/>. Acesso em: 23 ago. 2023. </br>
<a name="c20"></a> [14] ACURÁCIA: entenda o que é qual a sua relevância no ambiente corporativo. Disponível em: <https://uplexis.com.br/blog/artigos/acuracia-entenda-o-que-e/>. Acesso em: 28 ago. 2023. </br>
<a name="c21"></a> [15] DE, C. Prevendo Números: Entendendo as métricas R2, MAE, MAPE, MSE e RMSE. Medium | Data Hackers, Dec, 2021. Disponível em: <https://medium.com/data-hackers/prevendo-n%C3%BAmeros-entendendo-m%C3%A9tricas-de-regress%C3%A3o-35545e011e70>. Acesso em: 28 ago. 2023. </br>
<a name="c22"></a> [16] Entenda o que é o coeficiente de determinação na regressão linear – Psicometria Online. Disponível em: <https://psicometriaonline.com.br/entenda-o-que-e-o-coeficiente-de-determinacao-na-regressao-linear/#:~:text=O%20coeficiente%20de%20determina%C3%A7%C3%A3o%20%C3%A9,varia%20de%200%20a%201>. Acesso em: 28 ago. 2023. </br>
<a name="c23"></a>[17] CÍNTHIA PESSANHA. Random Forest: como funciona um dos algoritmos mais populares de ML. Disponível em: <https://medium.com/cinthiabpessanha/random-forest-como-funciona-um-dos-algoritmos-mais-populares-de-ml-cc1b8a58b3b4>. Acesso em: 4 out. 2023.
<a name="c24"></a>[18] SILVA, J. Uma breve introdução ao algoritmo de Machine Learning Gradient Boosting utilizando a biblioteca Scikit-Learn. Disponível em: <https://medium.com/equals-lab/uma-breve-introdu%C3%A7%C3%A3o-ao-algoritmo-de-machine-learning-gradient-boosting-utilizando-a-biblioteca-311285783099>. Acesso em: 5 out. 2023.
<a name="c25"></a>[19] ABHIGYAN. Understanding Polynomial Regression!!! - Analytics Vidhya - Medium. Disponível em: <https://medium.com/analytics-vidhya/understanding-polynomial-regression-5ac25b970e18>. Acesso em: 5 out. 2023.
<a name="c26"></a>[20] STALFORT, J. Hyperparameter tuning using Grid Search and Random Search: A Conceptual Guide. Disponível em: <https://medium.com/@jackstalfort/hyperparameter-tuning-using-grid-search-and-random-search-f8750a464b35>. Acesso em: 5 out. 2023.
<a name="c27"></a>[21] Plano de Contigência de TI: aprenda a elaborar e colocá-lo em prática! Disponível em: <https://ascenty.com/blog/artigos/plano-de-contingencia-de-ti/#:~:text=O%20plano%20de%20contingência%20de,da%20atuação%20de%20um%20negócio.>. Acesso em: 02/10/2023
<a name="c28"></a>[22] Plano de contingência e estrutura tecnológica. Disponível em : <https://unibrbotucatu.com.br/wp-content/uploads/2019/12/Plano-de-Contingência-InfraTecnol.pdf>. Acesso em 02/10/2023
<a name="c29"></a>[23] EQUALS Lab. Uma breve introdução ao algoritmo de machine learning Gradient Boosting utilizando a biblioteca scikit-learn. Medium, 2019. Disponível em: <https://medium.com/equals-lab/uma-breve-introdu%C3%A7%C3%A3o-ao-algoritmo-de-machine-learning-gradient-boosting-utilizando-a-biblioteca-311285783099.> Acesso em: 5 de outubro de 2023.
<a name="c30"></a>[24] All You Need to Know About Gradient Boosting Algorithm - Part 1: Regression. Towards Data Science, 2023. Disponível em: <https://towardsdatascience.com/all-you-need-to-know-about-gradient-boosting-algorithm-part-1-regression-2520a34a502.> Acesso em: 5 de outubro de 2023.
<a name="c31"></a>[25] Gradient Boosting Algorithm: A Complete Guide for Beginners. Analytics Vidhya, 2021. Disponível em: <https://www.analyticsvidhya.com/blog/2021/09/gradient-boosting-algorithm-a-complete-guide-for-beginners/>. Acesso em: 5 de outubro de 2023.
<a name="c32"></a>[26]All You Need to Know About Polynomial Regression. Analytics Vidhya, 2021. Disponível em: <https://www.analyticsvidhya.com/blog/2021/07/all-you-need-to-know-about-polynomial-regression/#:~:text=Polynomial%20regression%20is%20a%20form,convert%20it%20into%20Polynomial%20regression>. Acesso em: 5 de outubro de 2023.


## <a name="attachments"></a>Anexos
```
Utilize esta seção para anexar materiais como manuais de usuário, 
documentos complementares que ficaram grandes e não couberam no 
corpo do texto etc.

Remova este bloco ao final
```
