# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> 💡 **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.

---

### 👤 Identificação do Candidato

- **Nome completo:** Weslley Fernandes Souza
- **GitHub:** https://github.com/thewesdev

---

## 1️⃣ Visão Geral da Solução

Meu projeto é um timer pomodoro com tempo de 25 minutos, mas sem a parte do descanço de 5 minutos.

quando o circuito é energizado um circulo é desenhado, o timer, logo em seguida, é esperado um clique dentro do circulo, se o clique for registrado, o timer começara a contar, o tempo corre sendo decrementado em baixo do circulo, e o circulo é preenchido com uma linha a cada 1 segundo.

o usuário pode iniciar o timer clicando nele quando o timer não estiver correndo, se o timer já tiver sido iniciado e o usuário clicar, o timer será pausado, em caso de já estar pausado, o timer despausará.

---

## 2️⃣ Arquitetura do Sistema Embarcado

primeiramente, antes do loop, eu inicio algumas variáveis uteis, como as mais importantes sendo o display e o touch, que são de 2 arquivos que eu peguei de outro repositorio, clicando [aqui](https://github.com/hlf20010508/micropython-ili9341-ft6206) você encontrará o repositório em questão.

quando o loop começa, eu verifico se a tela já foi desenhada, se não tiver sido, ele desenha a tela, um circulo vazio e um texto escrito "25:00" logo abaixo.

depois eu verifico o touch, se o usuário tiver clicado, mas o timer não tiver sido iniciado, o timer é iniciado, se o timer já estivesse iniciado, ele será pausado, e se já tiver iniciado e estiver pausado, ele será despausado.

logo em seguida eu verifico se o timer está iniciado e não pausado, se já tiver corrido 1 segundo, ou em caso de atraso, mais de 1 segundo, eu decremento o tempo que está para ser descontado e desenho uma nova linha no circulo, para preenche-lo, e o tempo na tela é atualizado.

se o timer for menor ou igual a zero, a tela é apagada, e todos os booleanos setados antes do loop tem seus valores definidos como false, assim como foram setados, o que fará com que o comportamente esperado seja de que o circuito tivesse acabado de ser energizado.

---

## 3️⃣ Componentes Utilizados na Simulação

foi usado um circuito esp32 devkit c v4, um protoboard e um ili9341 cap touch.

o ili9341 é o display usado, com pinos usados para o desenho no display e outros pinos para o touch, para desenho se usa pinos referentes a interface spi, e para o touch a interface i2c.

---

## 4️⃣ Decisões Técnicas Relevantes

o código foi organizado em um loop principal responsável por controlar a interface, leitura de toque e atualização do temporizador.

a renderização inicial é feita apenas uma vez para evitar processamento desnecessário.

eu utilizei variáveis de estado (has_timer_started, has_timer_paused, has_screen_drawned) para controlar o fluxo do sistema, permitindo iniciar, pausar e reiniciar o timer de forma simples e a variável last_touch evita múltiplos acionamentos causados pelo toque contínuo.

a temporização foi implementada com time.ticks_ms() e time.ticks_diff(), garantindo que o timer funcione independentemente da velocidade do loop.

para melhorar o desempenho, apenas partes específicas da tela são atualizadas, evitando redesenho a todo momento.

---

## 5️⃣ Resultados Obtidos

O comportamento final não foi possível de ser testado, pois o wokwi não simula o touch corretamente ou a lib que eu usei tem algum erro, o clique no display é contado, isso eu tenho certeza, pois quando clico, a simulação fica mais lenta, mas a lib não registra o click, eu usei prints na simulação para testar se algum parametro da lib era modificado, mas não acontecia nada, eu acredito que o wokwi não simule o touch infelizmente.  

---

## 6️⃣ Comentários Adicionais (Opcional)

uma limitação clara é o wokwi, ele aparentemente não simulou direito o touch.

---

> ✅ Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****
