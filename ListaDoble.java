/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package memoriadinamica;

/**
 *
 * @author zinco
 */
public class ListaDoble {
    private NodoEstudiante2 primerNodo;
    private NodoEstudiante2 ultimoNodo;
    private String nombre;
    private int longitud;
    
    public ListaDoble(){
        this("lista");
    }
    
    public ListaDoble(String nombreLista){
        nombre = nombreLista;
        primerNodo = ultimoNodo = null;
        longitud = 0;
    }
    
    public void insertarAlFrente(Estudiante est){
        if(estaVacia())
            primerNodo = ultimoNodo = new NodoEstudiante2(est);
        else
            primerNodo = primerNodo.ant = new NodoEstudiante2(est, null, primerNodo);
        
        longitud++;
    }
    
    public void insertarAlFinal(Estudiante est){
        if(estaVacia())
            primerNodo = ultimoNodo = new NodoEstudiante2(est);
        else
            ultimoNodo = ultimoNodo.sig = new NodoEstudiante2(est, ultimoNodo, null);
        
        longitud++;
    }
    
    public Estudiante EliminarDelFrente() throws ExcepcionListaVacia{
        if(estaVacia())
            throw new ExcepcionListaVacia(nombre);
        
        Estudiante est = primerNodo.datos;
        
        if(primerNodo == ultimoNodo)
            primerNodo = ultimoNodo = null;
        else{
            primerNodo = primerNodo.sig;
            primerNodo.ant = null;
        }            
        
        longitud--;
        return est;
    }
    
    public Estudiante EliminarDelFinal() throws ExcepcionListaVacia{
        if(estaVacia())
            throw new ExcepcionListaVacia(nombre);
        
        Estudiante est = ultimoNodo.datos;
        
        if(primerNodo == ultimoNodo)
            primerNodo = ultimoNodo = null;
        else{
            //NodoEstudiante2 actual = primerNodo;
            
            /*while(actual.sig != ultimoNodo)
                actual = actual.sig;
            
            ultimoNodo = actual;*/
            
            ultimoNodo = ultimoNodo.ant;
            ultimoNodo.sig = null;
        }
        
        longitud--;
        return est;
    }
    
    public boolean estaVacia(){
        return primerNodo == null;
    }
    
    public int longitudLista(){
        return longitud;
    }
    
    public NodoEstudiante2 primerNodo(){
        return primerNodo;
    }

    NodoEstudiante2 ultimoNodo() {
        return ultimoNodo;
    }
    
    public void imprimir(){
        if(estaVacia()){
            System.out.printf("%s vacia\n", nombre);
            return;
        }
        
        System.out.printf("La %s es:\n", nombre);
        NodoEstudiante2 actual = primerNodo;
        
        while(actual != null){
            System.out.printf("%s ", actual.datos);
            actual = actual.sig;
        }
        
        System.out.println("\n");
    }
}
