Simulador de Escalonamento de Processos

Este projeto é um simulador gráfico de escalonamento de processos, apresentado de forma lúdica como uma corrida de execução. Cada processo é representado por uma capa de álbum da banda Of Monsters and Men. O usuário pode escolher entre duas políticas de escalonamento: FIFO (First In, First Out) e Round Robin.

Uso de Inteligência Artificial

O sistema incorpora elementos de inteligência artificial para tornar a simulação dinâmica e interativa:

Progresso dos processos: As barras de progresso avançam de forma não determinística com valores simulados.
Tomada de decisão automatizada: Com base na política de escalonamento escolhida, o sistema determina o processo vencedor (aquele que finaliza primeiro).
Interface otimizada: O código foi aprimorado com o auxílio de IA, garantindo uma experiência visual e funcional intuitiva.
Funcionalidades

Interface gráfica com imagem de fundo e elementos interativos
Seleção entre as políticas de escalonamento FIFO e Round Robin
Entrada de quantum para a política Round Robin
Barras de progresso que simulam a execução dos processos
Indicação visual do processo vencedor ao final da corrida
Botão para limpar corridas anteriores antes de iniciar uma nova
Requisitos

Python 3
Bibliotecas:
tkinter (inclusa por padrão no Python)
Pillow (para manipulação de imagens)
Instalação do Pillow
pip install pillow
Como Usar

Certifique-se de que as imagens king.png, dirty.png, mountain.png e dirtypaws.png estejam na mesma pasta do código.
Execute o script Python:
python nome_do_arquivo.py
Escolha entre FIFO ou Round Robin e, se necessário, defina o quantum.
Clique em Iniciar Corrida para visualizar a execução dos processos.
Para iniciar uma nova corrida, clique em Limpar Corrida.
Estrutura do Código

O programa possui três funções principais:

iniciar_interface(): Cria e exibe a interface gráfica.
iniciar_corrida(): Simula a execução dos processos, atualizando as barras de progresso.
limpar_corrida(): Remove os elementos da corrida anterior para permitir uma nova simulação.
