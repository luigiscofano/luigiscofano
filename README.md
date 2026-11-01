# Luigi Scofano de Araujo

**Engenharia de Computação na Poli-USP · Desenvolvimento de software · Inteligência artificial · Dados**

Construo aplicações e experimentos para entender como a computação resolve problemas: da interpretação de imagens e documentos à organização de dados, simulação de circuitos e criação de jogos.

[LinkedIn](https://br.linkedin.com/in/luigi-scofano-de-araujo-233102261/en) · [E-mail](mailto:luigiscofano.dev@gmail.com) · [English version](README.en.md) · [Todos os repositórios](https://github.com/luigiscofano?tab=repositories)

[Sobre mim](#sobre-mim) · [Destaques](#projetos-em-destaque) · [Hardware e sistemas](#sistemas-digitais-e-arquitetura) · [Algoritmos e Java](#algoritmos-e-orientação-a-objetos) · [Como executar](#como-explorar-e-executar) · [Competências](#competências) · [Trajetória](#trajetória-profissional)

## Sobre mim

Sou graduando em **Engenharia de Computação na Escola Politécnica da Universidade de São Paulo**, com interesse em desenvolvimento de software, inteligência artificial e ciência de dados. Minha trajetória reúne pesquisa acadêmica, análise de dados em empresas, projetos de programação e ensino.

Gosto de entender o mecanismo por trás das ferramentas: como um modelo interpreta uma imagem, como recuperar informação de um documento histórico ou como organizar dados para responder a uma pergunta de negócio. Procuro traduzir esse aprendizado em código claro, documentação e experiências que outras pessoas consigam explorar.

- **Pesquisa:** PLN e OCR aplicados ao Tupi Antigo no IME-USP, sob orientação do Prof. Marcelo Finger; museu virtual 3D no LASSu-USP.
- **Experiência:** dashboards e análise de dados na Núclea, tecnologia aplicada a FX no BTG Pactual e protótipos de apoio comercial na TRIA Commodities.
- **Aprendizado atual:** Python, machine learning e IA generativa, com formação IBM em andamento.
- **Além do código:** sou professor de jiu-jítsu e já atuei na gestão da modalidade na Atlética da Poli-USP.

### Por onde começar

| Se você quer conhecer… | Comece por |
| --- | --- |
| Uma aplicação visual com webcam e interação por gestos | [GestureLab](https://github.com/luigiscofano/gesturelab) |
| Pesquisa em linguagem, OCR e qualidade de dados | [IC · Tupi Antigo](https://github.com/luigiscofano/ic-pln-tupi-antigo) |
| Experimentos matemáticos com código, gráficos e notebooks | [Métodos Numéricos](https://github.com/luigiscofano/usp-metodos-numericos) |
| Um jogo em C com motor separado da interface | [Tetris em C](https://github.com/luigiscofano/tetris-c) |
| Circuitos, sensores, comunicação e jogos em FPGA | [Laboratório Digital I e II](https://github.com/luigiscofano/usp-labdig) |
| Processadores, instruções e execução em baixo nível | [Sistemas Digitais](https://github.com/luigiscofano/usp-pcs3225-sistemas-digitais) e [Assembly MVN](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao) |
| Algoritmos, orientação a objetos e fundamentos de Java | [MAC0122](https://github.com/luigiscofano/usp-mac0122-algoritmos), [MAC0321](https://github.com/luigiscofano/usp-mac0321-poo) e [Pokédex](https://github.com/luigiscofano/Pokedex) |

## Projetos em destaque

### GestureLab · Mãos, gestos, escrita no ar e poses

**[Abrir repositório](https://github.com/luigiscofano/gesturelab)** · Python · OpenCV · MediaPipe · NumPy

Laboratório de visão computacional que transforma a webcam em uma interface visual. O programa localiza pontos das mãos ou do corpo e usa essas coordenadas para desenhar conexões, reconhecer gestos, produzir traços e comparar poses. Os **quatro modos são independentes**, selecionados pela linha de comando:

| Modo | O que já faz |
| --- | --- |
| `hands` | Mostra 21 pontos por mão, conexões e indicação de lado, com opção de exibir os índices. |
| `gestures` | Exibe gestos de sete classes predefinidas, com limiar configurável para apresentação do resultado. |
| `airwrite` | Usa o indicador como caneta, com suavização, pausa, desfazer e exportação do desenho em PNG e das trajetórias em JSON. |
| `posematch` | Compara uma pose corporal com um catálogo local, usando normalização geométrica, ranking e rejeição por limiar. |

**Meu trabalho:** integração dos modelos, CLI, captura e visualização, controle temporal da caneta, exportação, comparação geométrica, catálogo reproduzível e testes. O catálogo inicial do PoseMatch contém 12 ilustrações originais; o detector visual utiliza modelos pré-treinados do MediaPipe.

**Estado atual:** aplicação de desktop com webcam e processamento de fotos nos modos compatíveis, documentação e CI. A escrita produz desenhos e trajetórias; reconhecimento de letras e palavras permanece como evolução. A busca de poses usa o catálogo local.

[Instalação](https://github.com/luigiscofano/gesturelab/blob/main/docs/INSTALACAO.md) · [Uso e controles](https://github.com/luigiscofano/gesturelab/blob/main/docs/USO.md) · [Arquitetura](https://github.com/luigiscofano/gesturelab/blob/main/docs/ARQUITETURA.md) · [Validação](https://github.com/luigiscofano/gesturelab/blob/main/docs/VALIDACAO.md)

### IC · Tupi Antigo, OCR e dados linguísticos

**[Abrir repositório](https://github.com/luigiscofano/ic-pln-tupi-antigo)** · Python · PLN · OCR · Unicode · Jupyter

Pesquisa de iniciação científica no **IME-USP**, orientada pelo **Prof. Dr. Marcelo Finger**, sobre extração e estruturação de dados para um dicionário eletrônico de Tupi Antigo. O problema central é transformar fontes lexicográficas em registros utilizáveis preservando grafias, diacríticos, localização na fonte e decisões de revisão.

O repositório reúne um pipeline de importação TSV, preservação dos campos originais, normalização Unicode NFC, auditoria e exportação CSV/JSONL. Também inclui métricas de erro de caracteres e palavras, adaptador opcional para Tesseract, notebook demonstrativo, Colab recuperado e documentação científica.

**Meu trabalho:** digitalização e estruturação lexicográfica, análise de erros, tratamento de Unicode e revisão rastreável. As ferramentas da edição de portfólio tornam explícitas a procedência dos dados e as verificações realizadas. Na pesquisa, também explorei o uso de modelos de linguagem na organização e revisão da informação.

**Estado atual:** ferramentas executáveis e demonstração com três registros fictícios. O corpus integral validado não é distribuído; a demonstração funcional e as regras recuperadas não equivalem a validação linguística independente.

**Parceria acadêmica:** o projeto relacionado [Dicionário Tupi-Português](https://caleberezende.github.io/tradutorestupi/) é de **Calebe Rezende**, com os devidos créditos e contexto registrados na documentação da IC.

[Metodologia](https://github.com/luigiscofano/ic-pln-tupi-antigo/blob/main/docs/METODOLOGIA.md) · [Procedência](https://github.com/luigiscofano/ic-pln-tupi-antigo/blob/main/docs/PROCEDENCIA.md) · [Demonstração](https://github.com/luigiscofano/ic-pln-tupi-antigo/blob/main/notebooks/README.md) · [Validação](https://github.com/luigiscofano/ic-pln-tupi-antigo/blob/main/docs/VALIDACAO.md)

### Métodos Numéricos · Matemática em experimentos reproduzíveis

**[Abrir repositório](https://github.com/luigiscofano/usp-metodos-numericos)** · Python · NumPy · SciPy · Matplotlib · Jupyter

Sete roteiros que conectam a formulação matemática à implementação e à análise de resultados. O objetivo é investigar precisão, erro, convergência, estabilidade e custo computacional, com gráficos e referências de comparação.

| Roteiro | Principais temas |
| --- | --- |
| 1 · Introdução a Python | Arrays, funções, máscaras, vetorização e tratamento de erros. |
| 2 · Zeros e fractais | Newton real e complexo, raízes múltiplas e bacias de atração. |
| 3 · Ponto flutuante e sistemas lineares | Cancelamento, eliminação de Gauss, pivotamento, PLU e condicionamento. |
| 4 · DFT e FFT | Transformadas, reconstrução, espectros, aliasing e custo dos algoritmos. |
| 5 · Interpolação | Newton, forma baricêntrica, nós de Chebyshev, fenômeno de Runge e splines. |
| 6 · EDO e circuito de Chua | Euler, Heun, RK4, estabilidade, pêndulo e dinâmica não linear. |
| 7 · GPS sintético | Pseudodistâncias, Gauss–Newton, coordenadas ECEF e efeito da geometria. |

**Meu trabalho nesta edição:** biblioteca didática organizada em seis famílias de métodos, roteiros reelaborados, experimentos, figuras, testes e exportação automática para HTML. O acervo recuperado fica separado e preserva os créditos do material docente.

**Estado atual:** notebooks, biblioteca e execução automatizada em kernel novo. O GPS utiliza dados sintéticos; os métodos têm limites documentados, como FFT radix-2 e EDO de passo fixo.

[Catálogo dos notebooks](https://github.com/luigiscofano/usp-metodos-numericos/blob/main/notebooks/README.md) · [Biblioteca](https://github.com/luigiscofano/usp-metodos-numericos/blob/main/numericos/README.md) · [Guia matemático](https://github.com/luigiscofano/usp-metodos-numericos/blob/main/docs/METODOS.md) · [Validação](https://github.com/luigiscofano/usp-metodos-numericos/blob/main/docs/VALIDACAO.md)

### Tetris em C · Regras, terminal e replay

**[Abrir repositório](https://github.com/luigiscofano/tetris-c)** · C11 · Make · Python para verificação

Jogo de blocos em um tabuleiro 10×20, com sete peças, próxima peça, movimentação, rotação, colisões, remoção de linhas, pontuação, níveis, pausa e reinício. O terminal oferece a interação; o motor concentra as regras e pode ser exercitado separadamente.

**Meu trabalho:** modelagem por matrizes, transformações geométricas, compactação de linhas, sorteio em sacos de sete e separação entre regras e plataforma. Uma seed e um arquivo de comandos permitem reproduzir a mesma partida, investigar falhas e comparar resultados. A implementação atual é uma nova edição de portfólio relacionada ao trabalho da graduação, com essa procedência documentada.

**Estado atual:** jogo interativo, replay determinístico, testes do motor e da CLI, verificações do terminal POSIX e preview gerado a partir de uma partida. A rotação usa tentativas horizontais simples; recursos como hold, ghost e SRS ficam fora desta versão.

[Instalação](https://github.com/luigiscofano/tetris-c/blob/main/docs/INSTALACAO.md) · [Regras](https://github.com/luigiscofano/tetris-c/blob/main/docs/REGRAS.md) · [Arquitetura](https://github.com/luigiscofano/tetris-c/blob/main/docs/ARQUITETURA.md) · [Replays](https://github.com/luigiscofano/tetris-c/blob/main/examples/README.md)

## Sistemas digitais e arquitetura

### Laboratório Digital I e II · Circuitos, sensores e jogos

**[Abrir repositório](https://github.com/luigiscofano/usp-labdig)** · Verilog · Icarus Verilog · FPGA/Quartus · Processing

Acervo da Poli-USP organizado em **11 experiências e dois projetos integradores**, com fontes, relatórios, documentação e simulações. Cada alvo tem suas próprias dependências e pode ser estudado separadamente.

- **LabDig I:** contadores, comparadores, máquinas de estados, entradas físicas e jogos de sequência e memória.
- **LabDig II:** servo por PWM, UART, sensor ultrassônico HC-SR04, trena digital e sonar.
- **Math Genius:** jogo de desafios aritméticos, com operações em ROM, seleção de dificuldade, resposta e feedback coordenados por controle e fluxo de dados.
- **Guardião do Paredão:** jogo de avançar e parar que integra medição de posição, servo, sinalização e comunicação serial. A interface Processing mostra a rodada, guarda histórico, exporta CSV e possui modo de simulação sem placa.

**Contribuição e aprendizado:** trabalhos em grupo, organização do acervo, correções e ferramentas de apoio; modelagem de FSM, unidade de controle, fluxo de dados, protocolos e integração de sensores/atuadores. A documentação reúne 210 fontes Verilog recuperados e 31 relatórios revisados, distinguindo versões históricas e alvos selecionados.

**Estado atual:** compilação dos 13 alvos e cenários de simulação com asserções. Síntese, timing, pinagem e aceitação física das revisões desta edição permanecem como etapas de bancada; Math Genius e jogos de memória têm cobertura parcial de partidas.

[Comece aqui](https://github.com/luigiscofano/usp-labdig/blob/main/docs/COMECE_AQUI.md) · [Math Genius](https://github.com/luigiscofano/usp-labdig/blob/main/projetos/math-genius/README.md) · [Guardião](https://github.com/luigiscofano/usp-labdig/blob/main/projetos/guardiao-do-paredao/README.md) · [Documentos](https://github.com/luigiscofano/usp-labdig/blob/main/docs/DOCUMENTOS.md)

### PCS3225 · Double-Dabble, calculadora e RISC-V

**[Abrir repositório](https://github.com/luigiscofano/usp-pcs3225-sistemas-digitais)** · SystemVerilog · Icarus Verilog · GTKWave

Três projetos independentes de Sistemas Digitais II que tornam observável o caminho entre algoritmo, registradores, controle e execução:

| Projeto | Implementação disponível |
| --- | --- |
| Double-Dabble | Conversão binário–BCD, máquina de estados e handshake `start`/`done`, com testes para entradas de 8 e 18 bits. |
| Calculadora programável | Datapath de 32 bits, 16 registradores, ROM e ISA didática própria com operações aritméticas e lógicas. |
| Núcleo RISC-V | Subconjunto de 14 instruções, imediatos, banco de registradores, acessos alinhados e sinalização de instruções ilegais ou desalinhamento. |

**Contribuição e aprendizado:** conversão numérica, controle sequencial, ULA, formatos de instrução e testbenches. Os arquivos VCD e as figuras permitem acompanhar sinais reais da simulação, como a conversão de 42 para BCD.

**Estado atual:** RTL, programas de teste e formas de onda. O núcleo implementa um subconjunto didático de RISC-V; esta edição não inclui validação em FPGA.

[Módulos RTL](https://github.com/luigiscofano/usp-pcs3225-sistemas-digitais/blob/main/rtl/README.md) · [Arquitetura e ISA](https://github.com/luigiscofano/usp-pcs3225-sistemas-digitais/blob/main/docs/ARQUITETURA.md) · [Formas de onda](https://github.com/luigiscofano/usp-pcs3225-sistemas-digitais/blob/main/assets/README.md)

### PCS3616 · Assembly MVN, pilha e calculadora RPN

**[Abrir repositório](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao)** · Assembly MVN · Python

Calculadora de notação pós-fixa executada por um ambiente didático de Máquina de Von Neumann. A expressão `12 3 +` produz 15 a partir do Assembly montado e executado. O percurso integra montador de duas passagens, máquina virtual, leitor de bytes, pilha limitada e scanner de operadores.

**Contribuição e aprendizado:** representação de palavras e bytes, endianidade, chamadas de subrotina, pilha, montagem e tratamento de erros. O modo `--trace` permite seguir as instruções; casos de divisão por zero, operandos ausentes e estouro da pilha possuem status definidos.

**Estado atual:** CLI, testes e rastreamento. A aritmética é modular de 16 bits e a pilha comporta 127 palavras. O executor implementa o subconjunto didático documentado, com limites de entrada e de execução.

[Assembly](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/blob/main/asm/README.md) · [Montador e máquina](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/blob/main/mvn/README.md) · [Mapa de memória e ABI](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/blob/main/docs/ARQUITETURA.md)

## Algoritmos e orientação a objetos

### MAC0122 · Algoritmos, invariantes e testes

**[Abrir repositório](https://github.com/luigiscofano/usp-mac0122-algoritmos)** · Java · C11 · Python para verificação

Quatro estudos independentes, com exemplos, contratos, análise de complexidade e testes:

- **Busca de genes:** identifica inícios e términos no mesmo quadro de leitura, preservando ocorrências sobrepostas.
- **União de intervalos:** ordena e combina intervalos fechados, calcula o comprimento da união e pode gerar uma representação SVG.
- **Contagem de pares em A+A:** usa dois ponteiros em um vetor ordenado, considerando multiplicidades e índices distintos.
- **Collatz em C:** registra passos, pico e estado de término, com proteção contra overflow e orçamento de execução.

**Aprendizado:** justificar corretude por invariantes, analisar custo, tratar casos de fronteira e comparar algoritmos com referências simples. Os programas Java e a extensão C estão disponíveis com verificadores; o relatório histórico de Collatz fica separado das implementações desta edição.

[Código e contratos](https://github.com/luigiscofano/usp-mac0122-algoritmos/blob/main/src/README.md) · [Guias por assunto](https://github.com/luigiscofano/usp-mac0122-algoritmos/blob/main/docs/topicos/README.md) · [Exemplos](https://github.com/luigiscofano/usp-mac0122-algoritmos/blob/main/examples/README.md)

### MAC0321 · Eventos, estados, CSV e multiconjuntos

**[Abrir repositório](https://github.com/luigiscofano/usp-mac0321-poo)** · Java · Orientação a objetos · Padrão State

Estudos de responsabilidades, passagem do tempo e persistência. Os módulos têm propósitos próprios: agenda de eventos com fila de prioridade e desempate determinístico; simulação de paciente, médico e droga com regras fictícias; lançamentos com estados calculados a partir de um relógio explícito; persistência CSV com campos escapados; multiconjunto baseado em frequências.

**Aprendizado:** composição de objetos, contratos, estados testáveis, valores decimais, leitura/escrita de arquivos e semântica de coleções. A simulação é um exercício de software; as regras não possuem validade clínica.

**Estado atual:** módulos, demonstração no terminal e suíte de testes. O acervo da Lista 08 tem dependências próprias e permanece separado da suíte nova.

[Documentação](https://github.com/luigiscofano/usp-mac0321-poo/blob/main/docs/README.md) · [Acervo](https://github.com/luigiscofano/usp-mac0321-poo/blob/main/acervo/README.md) · [Validação](https://github.com/luigiscofano/usp-mac0321-poo/blob/main/docs/VALIDACAO.md)

### Pokédex em Java · Primeiros modelos orientados a objetos

**[Abrir repositório](https://github.com/luigiscofano/Pokedex)** · Java · Classes · Enumerações · Coleções

Demonstração pequena para estudar modelagem de entidades: Pokémon com espécie, tipos, treinador e vida, construtores sobrecarregados, cópia, dano e armazenamento em `ArrayList`. O programa cria quatro personagens e imprime os resultados no terminal.

**Aprendizado e estado atual:** encapsulamento básico, enumerações, generics e `toString`, em uma aplicação sem dependências externas. Os dados ficam em memória. Validação de dano/vida, persistência e suíte automatizada são evoluções possíveis; os limites atuais estão descritos no README.

[Mapa do código](https://github.com/luigiscofano/Pokedex/blob/main/src/README.md) · [Programa principal](https://github.com/luigiscofano/Pokedex/blob/main/src/Main.java)

### MAC0321 · Lista 08, Swing e padrões de projeto

**[Abrir repositório](https://github.com/luigiscofano/MAC0321-Lista08)** · Java · Swing · JUnit · Adapter

Trabalho acadêmico em **coautoria com Hugo Spadete Arrivabene**. Reúne exercícios independentes de fatorial com interface Swing, testes do controlador, wrappers de coleções, adaptação para iteração de valores únicos e comparação de concatenação de strings.

**Aprendizado e estado atual:** separação de interface e lógica, exceções, testes, generics e adaptação por composição. Os 13 fontes históricos e os guias por exercício estão disponíveis. A interface exige ambiente gráfico; testes de aceitação podem pedir interação. O fatorial usa `long` e pode exceder sua capacidade acima de 20!.

[Índice dos exercícios](https://github.com/luigiscofano/MAC0321-Lista08/blob/master/src/README.md)

## Como explorar e executar

Cada repositório explica **o problema, os módulos, a instalação, uma primeira execução, os resultados esperados e o estado atual**. O [índice completo](docs/PROJETOS.md) reúne os pontos de entrada de todos os projetos públicos e os links de verificação.

| Família | Preparação típica | Primeiro caminho |
| --- | --- | --- |
| GestureLab | Python 3.12, ambiente virtual, dependências, modelos e câmera/ambiente gráfico | Iniciar `hands`; depois experimentar os outros modos. |
| Tupi Antigo e Métodos Numéricos | Python 3.12, dependências e kernel para notebooks | Rodar a demonstração TSV ou executar/exportar os roteiros. |
| Tetris | Compilador C11, GNU Make e terminal ANSI | `make demo` para replay; modo interativo para jogar. |
| Algoritmos e POO | JDK 17+; Python 3.12 nos verificadores das edições novas | Compilar/testar e executar a demonstração escolhida. |
| Circuitos digitais | Icarus Verilog, Python e GTKWave opcional | Simular um alvo e acompanhar os sinais. |
| Assembly MVN | Python 3.12 e biblioteca padrão | Montar uma expressão RPN e inspecionar o trace. |

**Exemplo completo para começar sem webcam, placa ou dependências Python externas:** com Git e Python 3.12 instalados, execute no terminal:

```sh
git clone https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao.git
cd usp-pcs3616-sistemas-programacao
python scripts/executar.py "12 3 +" --trace
python -m unittest discover -s tests -v
```

A expressão deve devolver `status: 0` e `resultado: 15`; o rastreamento fica em `build/trace.json`. Se o seu sistema usa `python3`, substitua o nome do comando. Os demais projetos têm requisitos próprios, detalhados em seus READMEs.

## Competências

| Área | Ferramentas e conhecimentos | Aplicação no portfólio ou na trajetória |
| --- | --- | --- |
| **Desenvolvimento de software** | Python, Java, C; JavaScript e TypeScript em projetos web | Aplicações locais, CLI, bibliotecas, modelagem de domínio e interfaces. |
| **Visão computacional** | OpenCV, MediaPipe, NumPy, coordenadas e estado temporal | GestureLab: modelos pré-treinados, caneta por gestos e comparação de poses. |
| **PLN e documentos** | OCR, Unicode, dados lexicográficos, avaliação textual e estudo de LLMs | IC de Tupi Antigo: extração, preservação da fonte, auditoria e revisão. |
| **Computação científica** | NumPy, SciPy, Matplotlib e Jupyter | Implementação de métodos, gráficos, convergência e experimentos reproduzíveis. |
| **Dados e BI** | SQL/MySQL, Excel, Power BI, Power Query e DAX | Preparação de bases, modelagem, indicadores e dashboards. |
| **Hardware e arquitetura** | Verilog, SystemVerilog, FSM, datapath, UART, PWM, RISC-V e Assembly MVN | Circuitos, comunicação, simuladores e execução de instruções. |
| **Web e computação gráfica** | Three.js, TypeScript e Vite | Museu virtual, navegação 3D e experiências educativas no navegador. |
| **Qualidade e colaboração** | Git, GitHub, testes, pytest, unittest, JUnit, Ruff e GitHub Actions | Verificações adequadas a cada projeto, documentação e histórico de mudanças. |
| **Fundamentos** | Algoritmos, estruturas de dados, orientação a objetos, sistemas operacionais e redes | Formação em Engenharia de Computação e estudos aplicados. |

**Em aprofundamento:** machine learning, IA generativa e engenharia de dados.

## Pesquisa e desenvolvimento

Além da [pesquisa em Tupi Antigo](#ic--tupi-antigo-ocr-e-dados-linguísticos), trabalho em iniciativas que aproximam tecnologia, educação e interação.

### Museu virtual · LASSu-USP

Contribuo para um **museu interativo sobre a história da computação**, com ambiente 3D acessível pelo navegador. O trabalho utiliza **Three.js, TypeScript e Vite** e envolve navegação, interação com objetos e apresentação de conteúdo educativo.

**Temas:** desenvolvimento web, computação gráfica, ambientes 3D e aprendizagem.

### Intuição · Jogos de lógica e aprendizagem

Desenvolvo uma plataforma de puzzles com regras acessíveis, dificuldade progressiva e espaço para experimentar. Meu trabalho envolve as mecânicas, a construção de fases, as dicas e a experiência de uso.

O princípio de design é fazer a dificuldade crescer pelas **decisões e relações que o jogador precisa descobrir**, valorizando raciocínio lógico e autonomia.

**Temas:** lógica de jogos, interfaces, design de níveis e objetivos pedagógicos. **Em desenvolvimento.**

## Trajetória profissional

**Núclea · Dados e indicadores de RH**  
Trabalhei com bases de Remuneração e Benefícios, dashboards em Power BI e análises com Excel e MySQL. Estruturei indicadores de quadro de pessoal, contratações, desligamentos, remuneração e desempenho, além de automatizar a consolidação de informações e utilizar Git no versionamento.

**BTG Pactual · Foreign Exchange (FX)**  
Participei do programa Summer Job, apoiando análises de mercado e modelos quantitativos para a equipe de câmbio internacional. Também trabalhei no desenvolvimento de interfaces front-end para a equipe.

**TRIA Commodities · Comercial, dados e automação**  
Atuo na área comercial e desenvolvo protótipos para apoiar a prospecção e a organização de oportunidades. O trabalho inclui cruzamento de informações da CCEE com o HubSpot, deduplicação e filtros para apoiar a análise de leads.

Essas experiências reforçam meu interesse por soluções que conectem necessidades de negócio, dados e implementação técnica.

## Formação e aprendizado

- **Engenharia de Computação — Escola Politécnica da USP:** graduação em andamento, com conclusão prevista para 2027.
- **CS50 — Harvard / edX:** curso de introdução à computação concluído.
- **Formação em inteligência artificial — IBM / edX:** em andamento, com estudos de Python, machine learning e IA generativa.
- **Iniciação científica:** PLN no IME-USP e museu virtual no LASSu-USP.

<details>
<summary><strong>Ensino, liderança, idiomas e outras conquistas</strong></summary>

### Ensino e liderança

Sou professor de jiu-jítsu e defesa pessoal, com atuação ligada à **Gracie University** e à **USP**. Ensinar reforça meu compromisso com explicações claras, progressão de dificuldade, prática e feedback.

Na **Atlética da Poli-USP**, fui diretor de jiu-jítsu, com responsabilidades de organização de treinos, gestão de recursos, eventos e relacionamento com alunos. Também atuei como representante discente e como professor voluntário de matemática e português na **ACEP**.

### Idiomas

- **Português:** nativo.
- **Inglês:** avançado — Cambridge C1 Advanced.
- **Espanhol e francês:** intermediários.

### Olimpíadas científicas

- **Olimpíada Nacional de Ciências:** ouro em 2020 e 2021.
- **Canguru de Matemática Brasil:** ouro em 2021 e prata em 2020.
- **Olimpíada de Química do Rio de Janeiro:** prata em 2020.

</details>

## Organização, autoria e validação

O portfólio reúne aplicações, implementações de estudo, pesquisa e acervo acadêmico. Cada repositório identifica o que foi desenvolvido nesta edição, o que foi recuperado, os materiais docentes e as contribuições de outras pessoas. Trabalhos em grupo, bibliotecas e modelos mantêm seus créditos e condições de uso.

Os guias de validação explicam o alcance de cada evidência: testes de software, simulação de circuitos, experimentos sintéticos e avaliação em equipamento real respondem a perguntas diferentes. Os READMEs indicam as funcionalidades disponíveis e os próximos passos; o histórico e os workflows permitem acompanhar a evolução.

Este repositório é a apresentação do perfil, renderizada diretamente pelo GitHub. Para ler uma cópia local, clone `https://github.com/luigiscofano/luigiscofano.git` e abra `README.md` em um editor com prévia Markdown. A página não exige instalação ou build.

[Índice completo dos projetos](docs/PROJETOS.md) · [Padrão de documentação](docs/PADRAO_README.md) · [Versão em inglês](README.en.md)

## Contato

Tenho interesse em projetos, pesquisa e oportunidades em **desenvolvimento de software, inteligência artificial e dados**, especialmente quando há um problema concreto para investigar e uma solução para construir.

**[LinkedIn](https://br.linkedin.com/in/luigi-scofano-de-araujo-233102261/en)** · **[luigiscofano.dev@gmail.com](mailto:luigiscofano.dev@gmail.com)**
