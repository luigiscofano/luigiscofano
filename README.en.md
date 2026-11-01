# Luigi Scofano de Araujo

**Computer Engineering at Poli-USP · Software development · Artificial intelligence · Data**

I build applications and experiments to understand how computing solves problems: interpreting images and documents, organizing data, simulating circuits, and creating games.

[Português](README.md) · [LinkedIn](https://br.linkedin.com/in/luigi-scofano-de-araujo-233102261/en) · [Email](mailto:luigiscofano.dev@gmail.com) · [All repositories](https://github.com/luigiscofano?tab=repositories)

[About me](#about-me) · [Featured projects](#featured-projects) · [Hardware and systems](#digital-systems-and-computer-architecture) · [Algorithms and Java](#algorithms-and-object-oriented-programming) · [Getting started](#how-to-explore-and-run-the-projects) · [Skills](#skills) · [Experience](#professional-experience)

## About me

I am a **Computer Engineering undergraduate at the University of São Paulo's Polytechnic School**, interested in software development, artificial intelligence, and data science. My background combines academic research, business data analysis, programming projects, and teaching.

I enjoy understanding how tools work: how a model interprets an image, how information can be recovered from a historical document, or how data can answer a business question. I aim to turn that understanding into readable code, documentation, and experiences others can explore.

- **Research:** NLP and OCR for Old Tupi at IME-USP, supervised by Prof. Marcelo Finger; a 3D virtual museum at LASSu-USP.
- **Experience:** dashboards and data analysis at Núclea, technology applied to FX at BTG Pactual, and prototypes supporting commercial work at TRIA Commodities.
- **Currently learning:** Python, machine learning, and generative AI through an IBM learning program.
- **Beyond code:** I teach Brazilian jiu-jitsu and previously helped manage the sport at Poli-USP's athletics association.

### Where to start

| If you want to explore… | Start with |
| --- | --- |
| A visual application using a webcam and gestures | [GestureLab](https://github.com/luigiscofano/gesturelab) |
| Language research, OCR, and data quality | [Old Tupi research](https://github.com/luigiscofano/ic-pln-tupi-antigo) |
| Mathematical experiments, plots, and notebooks | [Numerical Methods](https://github.com/luigiscofano/usp-metodos-numericos) |
| A C game with a separate rules engine and interface | [Tetris in C](https://github.com/luigiscofano/tetris-c) |
| Circuits, sensors, communication, and FPGA games | [Digital Laboratory I and II](https://github.com/luigiscofano/usp-labdig) |
| Processors, instructions, and low-level execution | [Digital Systems](https://github.com/luigiscofano/usp-pcs3225-sistemas-digitais) and [MVN Assembly](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao) |
| Algorithms, object-oriented programming, and Java foundations | [MAC0122](https://github.com/luigiscofano/usp-mac0122-algoritmos), [MAC0321](https://github.com/luigiscofano/usp-mac0321-poo), and [Pokédex](https://github.com/luigiscofano/Pokedex) |

## Featured projects

### GestureLab · Hands, gestures, air writing, and poses

**[Repository](https://github.com/luigiscofano/gesturelab)** · Python · OpenCV · MediaPipe · NumPy

A computer vision laboratory that turns a webcam into a visual interface. Detected hand or body landmarks drive overlays, gesture labels, persistent strokes, and geometric pose comparisons. Its **four modes run independently**, selected through the command line:

| Mode | Available behavior |
| --- | --- |
| `hands` | Displays 21 landmarks per hand, connections, handedness, and optional landmark indices. |
| `gestures` | Shows gestures from seven predefined classes, with a configurable display threshold. |
| `airwrite` | Uses the index finger as a pen, with smoothing, pause, undo, PNG export, and JSON trajectories. |
| `posematch` | Compares a body pose against a local catalog using geometric normalization, ranking, and threshold-based rejection. |

**My work:** model integration, CLI, capture and visualization, temporal pen state, export, geometric comparison, a reproducible catalog, and tests. The initial PoseMatch catalog contains 12 original illustrations; visual detection uses pretrained MediaPipe models.

**Current status:** desktop application, webcam input, still-image processing in compatible modes, documentation, and CI. Air writing produces drawings and trajectories; recognizing letters and words remains a proposed extension. Pose matching uses the local catalog.

[Installation](https://github.com/luigiscofano/gesturelab/blob/main/docs/INSTALACAO.md) · [Usage](https://github.com/luigiscofano/gesturelab/blob/main/docs/USO.md) · [Architecture](https://github.com/luigiscofano/gesturelab/blob/main/docs/ARQUITETURA.md) · [Validation](https://github.com/luigiscofano/gesturelab/blob/main/docs/VALIDACAO.md)

### Old Tupi research · OCR and linguistic data

**[Repository](https://github.com/luigiscofano/ic-pln-tupi-antigo)** · Python · NLP · OCR · Unicode · Jupyter

Undergraduate research at **IME-USP**, supervised by **Prof. Dr. Marcelo Finger**, on extracting and structuring data for an electronic Old Tupi dictionary. The central challenge is turning lexicographic sources into usable records while preserving spellings, diacritics, source locations, and review decisions.

The repository includes TSV import, original-field preservation, Unicode NFC normalization, auditing, and CSV/JSONL export. It also provides character and word error metrics, an optional Tesseract adapter, a demonstration notebook, a recovered Colab notebook, and methodology documentation.

**My work:** digitization, lexicographic structuring, error analysis, Unicode handling, and traceable review. Portfolio tools expose data provenance and the checks performed. The research also explored language models for organizing and reviewing information.

**Current status:** executable tools and a demonstration with three fictional records. The complete validated corpus is not distributed; functional demonstrations and recovered rules do not establish independent linguistic validation.

**Academic collaboration:** the related [Tupi–Portuguese Dictionary](https://caleberezende.github.io/tradutorestupi/) is maintained by **Calebe Rezende**, with credit and context recorded in the research documentation.

[Methodology](https://github.com/luigiscofano/ic-pln-tupi-antigo/blob/main/docs/METODOLOGIA.md) · [Provenance](https://github.com/luigiscofano/ic-pln-tupi-antigo/blob/main/docs/PROCEDENCIA.md) · [Demonstration](https://github.com/luigiscofano/ic-pln-tupi-antigo/blob/main/notebooks/README.md) · [Validation](https://github.com/luigiscofano/ic-pln-tupi-antigo/blob/main/docs/VALIDACAO.md)

### Numerical Methods · Reproducible mathematical experiments

**[Repository](https://github.com/luigiscofano/usp-metodos-numericos)** · Python · NumPy · SciPy · Matplotlib · Jupyter

Seven notebooks connect mathematical formulations to implementation and analysis. Experiments investigate precision, error, convergence, stability, and computational cost through plots and comparison references.

| Notebook | Main topics |
| --- | --- |
| 1 · Python introduction | Arrays, functions, masks, vectorization, and error handling. |
| 2 · Roots and fractals | Real and complex Newton methods, multiple roots, and basins of attraction. |
| 3 · Floating point and linear systems | Cancellation, Gaussian elimination, pivoting, PLU, and conditioning. |
| 4 · DFT and FFT | Transforms, reconstruction, spectra, aliasing, and algorithmic cost. |
| 5 · Interpolation | Newton, barycentric form, Chebyshev nodes, Runge's phenomenon, and splines. |
| 6 · ODEs and Chua's circuit | Euler, Heun, RK4, stability, pendulum, and nonlinear dynamics. |
| 7 · Synthetic GPS | Pseudoranges, Gauss–Newton, ECEF coordinates, and geometry effects. |

**My work in this edition:** an educational library with six method families, revised notebooks, experiments, figures, tests, and automated HTML export. Recovered course materials remain in a separate archive with teaching-material credits preserved.

**Current status:** notebooks, library, and automated execution in fresh kernels. GPS uses synthetic data; limitations such as radix-2 FFT and fixed-step ODE methods are documented.

[Notebook catalog](https://github.com/luigiscofano/usp-metodos-numericos/blob/main/notebooks/README.md) · [Library](https://github.com/luigiscofano/usp-metodos-numericos/blob/main/numericos/README.md) · [Mathematical guide](https://github.com/luigiscofano/usp-metodos-numericos/blob/main/docs/METODOS.md) · [Validation](https://github.com/luigiscofano/usp-metodos-numericos/blob/main/docs/VALIDACAO.md)

### Tetris in C · Rules, terminal, and replay

**[Repository](https://github.com/luigiscofano/tetris-c)** · C11 · Make · Python verification tools

A falling-block game on a 10×20 board, with seven pieces, next-piece display, movement, rotation, collision handling, line clearing, scoring, levels, pause, and restart. The terminal handles interaction while a separate engine implements the rules.

**My work:** matrix modeling, geometric transformations, line compaction, seven-bag randomization, and separation of rules from platform code. A seed and command file reproduce the same game for debugging and comparisons. This is a new portfolio implementation related to university coursework, with its provenance documented.

**Current status:** interactive play, deterministic replay, engine and CLI tests, POSIX terminal checks, and a preview generated from a replay. Rotation uses simple horizontal attempts; hold, ghost pieces, and SRS are outside this version.

[Installation](https://github.com/luigiscofano/tetris-c/blob/main/docs/INSTALACAO.md) · [Rules](https://github.com/luigiscofano/tetris-c/blob/main/docs/REGRAS.md) · [Architecture](https://github.com/luigiscofano/tetris-c/blob/main/docs/ARQUITETURA.md) · [Replays](https://github.com/luigiscofano/tetris-c/blob/main/examples/README.md)

## Digital systems and computer architecture

### Digital Laboratory I and II · Circuits, sensors, and games

**[Repository](https://github.com/luigiscofano/usp-labdig)** · Verilog · Icarus Verilog · FPGA/Quartus · Processing

Poli-USP coursework organized into **11 experiments and two integrated projects**, with source code, reports, documentation, and simulations. Targets have their own dependencies and can be studied separately.

- **LabDig I:** counters, comparators, finite-state machines, physical inputs, and sequence/memory games.
- **LabDig II:** PWM servo control, UART, the HC-SR04 ultrasonic sensor, digital distance measurement, and sonar.
- **Math Genius:** arithmetic challenges stored in ROM, with difficulty selection, answers, and feedback coordinated by control and datapath logic.
- **Guardião do Paredão:** a move-and-stop game combining position measurements, servo control, signaling, and serial communication. Its Processing interface displays the round, keeps history, exports CSV, and provides a simulation mode without a board.

**Contribution and learning:** group coursework, archive organization, corrections, and supporting tools; FSM modeling, control/datapath separation, protocols, and sensor/actuator integration. Documentation covers 210 recovered Verilog sources and 31 revised reports, distinguishing historical variants from selected targets.

**Current status:** compilation of 13 targets and simulation scenarios with assertions. Synthesis, timing, pin assignments, and physical acceptance of this edition's revisions remain hardware steps; complete game coverage is still pending for Math Genius and the memory games.

[Start here](https://github.com/luigiscofano/usp-labdig/blob/main/docs/COMECE_AQUI.md) · [Math Genius](https://github.com/luigiscofano/usp-labdig/blob/main/projetos/math-genius/README.md) · [Guardião](https://github.com/luigiscofano/usp-labdig/blob/main/projetos/guardiao-do-paredao/README.md) · [Documents](https://github.com/luigiscofano/usp-labdig/blob/main/docs/DOCUMENTOS.md)

### PCS3225 · Double-Dabble, calculator, and RISC-V

**[Repository](https://github.com/luigiscofano/usp-pcs3225-sistemas-digitais)** · SystemVerilog · Icarus Verilog · GTKWave

Three independent Digital Systems II projects make the path from algorithm to registers, control signals, and execution observable.

| Project | Available implementation |
| --- | --- |
| Double-Dabble | Binary-to-BCD conversion, a state machine, and `start`/`done` handshake, tested with 8- and 18-bit inputs. |
| Programmable calculator | A 32-bit datapath, 16 registers, ROM, and a custom educational ISA with arithmetic and logic operations. |
| RISC-V core | A 14-instruction subset, immediate decoding, register file, aligned accesses, and illegal-instruction/misalignment signaling. |

**Contribution and learning:** number conversion, sequential control, ALUs, instruction formats, and testbenches. VCD files and figures expose actual simulated signals, including the conversion of 42 to BCD.

**Current status:** RTL, test programs, and waveforms. The core implements an educational RISC-V subset; this edition does not include FPGA validation.

[RTL modules](https://github.com/luigiscofano/usp-pcs3225-sistemas-digitais/blob/main/rtl/README.md) · [Architecture and ISA](https://github.com/luigiscofano/usp-pcs3225-sistemas-digitais/blob/main/docs/ARQUITETURA.md) · [Waveforms](https://github.com/luigiscofano/usp-pcs3225-sistemas-digitais/blob/main/assets/README.md)

### PCS3616 · MVN Assembly, stack, and RPN calculator

**[Repository](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao)** · MVN Assembly · Python

A postfix calculator running on an educational von Neumann machine. The expression `12 3 +` produces 15 through assembled and executed code. The pipeline combines a two-pass assembler, virtual machine, byte reader, bounded stack, and operator scanner.

**Contribution and learning:** word/byte representation, endianness, subroutine calls, stacks, assembly, and error handling. The `--trace` mode follows instructions; division by zero, missing operands, and stack overflow have explicit status codes.

**Current status:** CLI, tests, and tracing. Arithmetic wraps at 16 bits and the stack holds 127 words. The runtime implements the documented educational subset with bounded input and execution.

[Assembly](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/blob/main/asm/README.md) · [Assembler and machine](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/blob/main/mvn/README.md) · [Memory map and ABI](https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao/blob/main/docs/ARQUITETURA.md)

## Algorithms and object-oriented programming

### MAC0122 · Algorithms, invariants, and tests

**[Repository](https://github.com/luigiscofano/usp-mac0122-algoritmos)** · Java · C11 · Python verification tools

Four independent studies with examples, contracts, complexity analysis, and tests:

- **Gene search:** finds start/stop sequences in the same reading frame while retaining overlapping occurrences.
- **Interval union:** sorts and merges closed intervals, computes total length, and can generate an SVG.
- **Pair counting in A+A:** uses two pointers on a sorted array, accounting for multiplicities and distinct indices.
- **Collatz in C:** records steps, peak values, and termination status, with overflow protection and an execution budget.

**Learning and status:** correctness through invariants, cost analysis, edge cases, and comparison against simple references. Java programs and the C extension have verification tools; the recovered Collatz report is kept separately from this edition's implementations.

[Code and contracts](https://github.com/luigiscofano/usp-mac0122-algoritmos/blob/main/src/README.md) · [Topic guides](https://github.com/luigiscofano/usp-mac0122-algoritmos/blob/main/docs/topicos/README.md) · [Examples](https://github.com/luigiscofano/usp-mac0122-algoritmos/blob/main/examples/README.md)

### MAC0321 · Events, states, CSV, and multisets

**[Repository](https://github.com/luigiscofano/usp-mac0321-poo)** · Java · Object-oriented programming · State pattern

Studies of responsibilities, time, and persistence. Modules serve separate purposes: a priority-queue event scheduler with deterministic tie-breaking; a patient/doctor/drug simulation with fictional rules; financial entries whose states depend on an explicit clock; CSV persistence with escaped fields; and a frequency-based multiset.

**Learning:** object composition, contracts, testable states, decimal values, file handling, and collection semantics. The simulation is a software exercise with no clinical validity.

**Current status:** modules, terminal demonstration, and tests. The historical Lista 08 archive has its own dependencies and remains outside the new test suite.

[Documentation](https://github.com/luigiscofano/usp-mac0321-poo/blob/main/docs/README.md) · [Archive](https://github.com/luigiscofano/usp-mac0321-poo/blob/main/acervo/README.md) · [Validation](https://github.com/luigiscofano/usp-mac0321-poo/blob/main/docs/VALIDACAO.md)

### Pokédex in Java · Introductory object models

**[Repository](https://github.com/luigiscofano/Pokedex)** · Java · Classes · Enums · Collections

A small entity-modeling demonstration: Pokémon with species, types, trainer, and health; overloaded constructors, copying, damage, and an `ArrayList`. The program creates four characters and prints results in the terminal.

**Learning and status:** basic encapsulation, enums, generics, and `toString` in an application without external dependencies. Data lives in memory. Damage/health validation, persistence, and automated tests are possible extensions; current limits are described in the README.

[Code map](https://github.com/luigiscofano/Pokedex/blob/main/src/README.md) · [Entry point](https://github.com/luigiscofano/Pokedex/blob/main/src/Main.java)

### MAC0321 · Lista 08, Swing, and design patterns

**[Repository](https://github.com/luigiscofano/MAC0321-Lista08)** · Java · Swing · JUnit · Adapter

Coursework **coauthored with Hugo Spadete Arrivabene**. Independent exercises cover a Swing factorial interface, controller tests, collection wrappers, an adapter for unique-value iteration, and a string-concatenation comparison.

**Learning and status:** interface/logic separation, exceptions, tests, generics, and composition-based adaptation. The 13 historical source files and per-exercise guides are available. The interface requires a graphical environment and acceptance tests may require interaction. Factorial uses `long` and can overflow above 20!.

[Exercise index](https://github.com/luigiscofano/MAC0321-Lista08/blob/master/src/README.md)

## How to explore and run the projects

Each repository explains **its problem, modules, setup, first execution, expected output, and current status**. The [complete project index](docs/PROJETOS.md), in Portuguese, collects entry points and verification links for all public projects. Most detailed project guides are also in Portuguese.

| Family | Typical preparation | First step |
| --- | --- | --- |
| GestureLab | Python 3.12, virtual environment, dependencies, models, camera/graphical environment | Start `hands`, then try the other modes. |
| Old Tupi and Numerical Methods | Python 3.12, dependencies, and a notebook kernel | Run the TSV demo or execute/export notebooks. |
| Tetris | C11 compiler, GNU Make, and ANSI terminal | Run `make demo` for a replay, then play interactively. |
| Algorithms and OOP | JDK 17+; Python 3.12 for the newer verification scripts | Compile/test and run the chosen demonstration. |
| Digital circuits | Icarus Verilog, Python, and optional GTKWave | Simulate a target and inspect its signals. |
| MVN Assembly | Python 3.12 and its standard library | Assemble an RPN expression and inspect its trace. |

**A complete starting example without a webcam, board, or external Python dependencies:** with Git and Python 3.12 installed, run:

```sh
git clone https://github.com/luigiscofano/usp-pcs3616-sistemas-programacao.git
cd usp-pcs3616-sistemas-programacao
python scripts/executar.py "12 3 +" --trace
python -m unittest discover -s tests -v
```

The expression should return `status: 0` and `resultado: 15`; its trace is saved to `build/trace.json`. Use `python3` if that is your system's command. Other projects have their own setup requirements in their READMEs.

## Skills

| Area | Tools and concepts | Portfolio or professional application |
| --- | --- | --- |
| **Software development** | Python, Java, C; JavaScript and TypeScript for web projects | Local applications, CLIs, libraries, domain models, and interfaces. |
| **Computer vision** | OpenCV, MediaPipe, NumPy, coordinates, temporal state | GestureLab: pretrained models, gesture-controlled pen, and pose comparison. |
| **NLP and documents** | OCR, Unicode, lexicographic data, text evaluation, and LLM research | Old Tupi: extraction, source preservation, auditing, and review. |
| **Scientific computing** | NumPy, SciPy, Matplotlib, Jupyter | Numerical implementations, plots, convergence, and reproducible experiments. |
| **Data and BI** | SQL/MySQL, Excel, Power BI, Power Query, DAX | Data preparation, modeling, metrics, and dashboards. |
| **Hardware and architecture** | Verilog, SystemVerilog, FSMs, datapaths, UART, PWM, RISC-V, MVN Assembly | Circuits, communication, simulation, and instruction execution. |
| **Web and computer graphics** | Three.js, TypeScript, Vite | Virtual museum, 3D navigation, and educational browser experiences. |
| **Quality and collaboration** | Git, GitHub, testing, pytest, unittest, JUnit, Ruff, GitHub Actions | Project-specific verification, documentation, and change history. |
| **Foundations** | Algorithms, data structures, OOP, operating systems, networks | Computer Engineering coursework and applied studies. |

**Developing further:** machine learning, generative AI, and data engineering.

## Research and development

Alongside [Old Tupi research](#old-tupi-research--ocr-and-linguistic-data), I work on initiatives connecting technology, education, and interaction.

### Virtual museum · LASSu-USP

I contribute to an **interactive museum about the history of computing**, with a browser-based 3D environment. The project uses **Three.js, TypeScript, and Vite** and involves navigation, object interaction, and educational content.

**Topics:** web development, computer graphics, 3D environments, and learning.

### Intuição · Logic games and learning

I am developing a puzzle platform with accessible rules, progressive difficulty, and room for experimentation. My work covers mechanics, level design, hints, and user experience.

The design principle is to increase difficulty through the **decisions and relationships players need to discover**, encouraging logical reasoning and independent learning.

**Topics:** game logic, interfaces, level design, and educational objectives. **In development.**

## Professional experience

**Núclea · HR data and reporting**  
I worked with Compensation and Benefits datasets, Power BI dashboards, and analyses using Excel and MySQL. I organized indicators covering headcount, hiring, departures, compensation, and performance, automated data consolidation, and used Git for version control.

**BTG Pactual · Foreign Exchange (FX)**  
I participated in the Summer Job program, supporting market analysis and quantitative models for the international FX team. I also worked on front-end interfaces for the team.

**TRIA Commodities · Commercial work, data, and automation**  
I work in the commercial area and develop prototypes to support prospecting and opportunity tracking. This includes cross-referencing CCEE information with HubSpot, deduplication, and filters for lead analysis.

These experiences strengthen my interest in solutions that connect business needs, data, and technical implementation.

## Education and learning

- **Computer Engineering — University of São Paulo, Polytechnic School:** degree in progress; expected graduation in 2027.
- **CS50 — Harvard / edX:** introductory computer science course completed.
- **Artificial intelligence learning program — IBM / edX:** in progress, covering Python, machine learning, and generative AI.
- **Undergraduate research:** NLP at IME-USP and a virtual museum at LASSu-USP.

<details>
<summary><strong>Teaching, leadership, languages, and other achievements</strong></summary>

### Teaching and leadership

I teach Brazilian jiu-jitsu and self-defense, with activities connected to **Gracie University** and **USP**. Teaching reinforces my commitment to clear explanations, progressive challenges, practice, and feedback.

As jiu-jitsu director at **Poli-USP's athletics association**, I helped organize training, manage resources, coordinate events, and work with students. I also served as a student representative and volunteered as a mathematics and Portuguese teacher at **ACEP**.

### Languages

- **Portuguese:** native.
- **English:** advanced — Cambridge C1 Advanced.
- **Spanish and French:** intermediate.

### Science and mathematics competitions

- **Brazilian National Science Olympiad:** gold in 2020 and 2021.
- **Canguru de Matemática Brasil:** gold in 2021 and silver in 2020.
- **Rio de Janeiro Chemistry Olympiad:** silver in 2020.

</details>

## Organization, authorship, and validation

The portfolio combines applications, educational implementations, research, and coursework archives. Each repository identifies work developed in the current edition, recovered sources, teaching materials, and collaborators' contributions. Group projects, libraries, and models retain their credits and usage terms.

Validation guides explain the scope of each piece of evidence: software tests, circuit simulation, synthetic experiments, and evaluation on real equipment answer different questions. READMEs distinguish available functionality and next steps; history and workflows make progress traceable.

This repository is the profile presentation rendered directly by GitHub. For a local copy, clone `https://github.com/luigiscofano/luigiscofano.git` and open `README.en.md` in a Markdown viewer. The page requires no installation or build.

[Complete project index](docs/PROJETOS.md) · [Documentation standard](docs/PADRAO_README.md) · [Português](README.md)

## Contact

I welcome conversations about projects, research, and opportunities in **software development, artificial intelligence, and data**, especially when there is a concrete problem to investigate and a solution to build.

**[LinkedIn](https://br.linkedin.com/in/luigi-scofano-de-araujo-233102261/en)** · **[luigiscofano.dev@gmail.com](mailto:luigiscofano.dev@gmail.com)**
