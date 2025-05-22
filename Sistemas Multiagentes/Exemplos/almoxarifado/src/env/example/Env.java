package example;

import jason.asSyntax.*;
import jason.environment.*;
import jason.asSyntax.parser.*;

import java.text.ParseException;
import java.util.Random;
import java.util.logging.*;

public class Env extends Environment {

    private Logger logger = Logger.getLogger("almoxarifado."+Env.class.getName());
    int quantidadePecas;

    public String sortearPeca(){
        Random gerador = new Random();
        int numero = gerador.nextInt(3);
        if(numero == 0){
            return "peca(pequena)";
        } else if (numero == 1){
            return "peca(media)";
        } else if (numero == 2){
            return "peca(grande)";
        }
    }
   
    @Override
    public void init(String[] args) {
        super.init(args);
        quantidadePecas = Integer.parseInt(args[0]);
        try {
            addPercept(ASSyntax.parseLiteral("quantidadePecas("+quantidadePecas+")"));
            addPercept(ASSyntax.parseLiteral(sortearPeca()));
        } catch (ParseException e) {
            e.printStackTrace();
        }
    }

    @Override
    public boolean executeAction(String agName, Structure action) {
        if (action.getFunctor().equals("guardarPeca")) { 
             logger.info(agName + "esta guardando uma peca..." + action.getTerm(0).toString());
             try {
                removePercept(ASSyntax.parseLiteral("peca("+action.getTerm(0).toString()+")"));
                removePercept(ASSyntax.parseLiteral("quantidadePecas("+quantidadePecas+")"));
                quantidadePecas--;
                addPercept(ASSyntax.parseLiteral("quantidadePecas("+quantidadePecas+")"));
                logger.info("-------------------------" + quantidadePecas + "-----------------------");
             } catch(ParseException e){
                e.printStackTrace();
             }
        } else if(action.getFunctor().equals("ajudarGuardarPeca")){
             logger.info(agName + "esta ajudando a guardar uma peca..." + action.getTerm(0).toString());
        }

        if(quantidadePecas > 0){
            try {
                Thread.sleep(5000);
                addPercept(ASSyntax.parseLiteral(sortearPeca()));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        return true; 
    }

    @Override
    public void stop() {
        super.stop();
    }
}
