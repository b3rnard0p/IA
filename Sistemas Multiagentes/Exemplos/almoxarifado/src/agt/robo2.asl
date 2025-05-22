//Guarda peças médias

!start.


+!start : true 
    <- 
    .print("Guardo peças médias e com a ajuda do robo1 guardo peças grandes.").


+!peca(Tamanho) : Tamanho = grande
    <-
    .print("Percebi uma peça", Tamanho, "e vou precisar da ajuda do robo1 para gurada-la.");
    .send(robo1,achieve,ajudaGuardar(Tamanho));
    guardarPeca(Tamanho).


+!peca(Tamanho) : Tamanho = media
    <-
    .print("Percebi uma peça", Tamanho, "e devo guarda-la");
    .wait(1000);
    guardarPeca(Tamanho).