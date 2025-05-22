//Guarda peças pequenas e ajuda a guardar peças grandes

!start.

+!start : true 
    <- 
    .print("Posso guardar peças pequenas e ajudar a guardar peças grandes.").


+!peca(Tamanho) : Tamanho = pequena
    <-
    .print("Percebi uma peça", Tamanho, "e devo guarda-la");
    guardarPeca(Tamanho).
    

+!ajudaGuardar[source(Agente)] : true
    <-
    .print(Agente, "está pedindo ajuda para guardar um apeça... e vou ajuda-lo.");
    ajudarGuardarPeca(Tamanho)