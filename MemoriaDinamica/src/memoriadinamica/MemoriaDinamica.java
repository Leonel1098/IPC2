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
public class MemoriaDinamica {
    static ListaSimple lista = new ListaSimple("Lista Simple");
    static ListaDoble lista2 = new ListaDoble("Lista Doble");
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Estudiante est3 = new Estudiante(1, "Jose", 15, "jose@example.com");
        Estudiante est5 = new Estudiante(2, "Maria", 16, "maria@example.com");
        Estudiante est2 = new Estudiante(3, "Eddy", 19, "eddy@example.com");
        Estudiante est7 = new Estudiante(4, "Marta", 10, "marta@example.com");
        Estudiante est1 = new Estudiante(5, "Fernando", 5, "fernando@example.com");
        Estudiante est6 = new Estudiante(6, "Emily", 21, "emily@example.com");
        Estudiante est4 = new Estudiante(7, "Juan", 13, "juan@example.com");
        
        lista.insertarAlFinal(est1);
        lista.insertarAlFinal(est2);
        lista.insertarAlFinal(est3);
        lista.insertarAlFinal(est4);
        lista.insertarAlFinal(est5);
        lista.insertarAlFinal(est6);
        lista.insertarAlFinal(est7);
        
        //lista.imprimir();
        
        //burbujaCarne();
        //burbujaCarneApuntadores();
        //burbujaEdad();
        //seleccionCarne();
        //seleccionEdad();
        
        
        //lista.imprimir();
        
        lista2.insertarAlFinal(est1);
        lista2.insertarAlFinal(est2);
        lista2.insertarAlFinal(est3);
        lista2.insertarAlFinal(est4);
        lista2.insertarAlFinal(est5);
        lista2.insertarAlFinal(est6);
        lista2.insertarAlFinal(est7);
        
        lista2.imprimir();
        
        //insercionCarne();
        //insercionEdad();
        //quicksortCarne(lista2.primerNodo(), lista2.ultimoNodo());
        //quicksortEdad(lista2.primerNodo(), lista2.ultimoNodo());
        
        //lista2.imprimir();
        
        //Estudiante est = busquedaLineal(2);
        insercionCarne();
        lista2.imprimir();
        Estudiante est = busquedaBinaria(5);
        System.out.println(est);
    }
    
    public static void burbujaCarne(){
        for (int i=1; i<lista.longitudLista(); i++){
            NodoEstudiante actual = lista.primerNodo();
            for (int j=0; j<lista.longitudLista()-1; j++){
                if(actual.datos.getCarne()>actual.sig.datos.getCarne()){
                    Estudiante tmp = actual.datos;
                    actual.datos = actual.sig.datos;
                    actual.sig.datos = tmp;
                }
                
                actual = actual.sig;
            }
        }
    }
    
    public static void burbujaCarneApuntadores(){
        for (int i=1; i<lista.longitudLista(); i++){
            NodoEstudiante anterior = null;
            NodoEstudiante actual = lista.primerNodo();
            for (int j=0; j<lista.longitudLista()-1; j++){
                if (actual.datos.getCarne()>actual.sig.datos.getCarne()){
                    NodoEstudiante t0 = null;
                    
                    if (actual!=lista.primerNodo())
                        t0 = anterior;
                    NodoEstudiante t1 = actual;
                    NodoEstudiante t2 = actual.sig;
                    NodoEstudiante t3 = actual.sig.sig;
                    
                    if (t0!=null)
                        t0.sig = t2;                    
                    t1.sig = t3;
                    t2.sig = t1;
                    
                    if (actual==lista.primerNodo())
                        lista.setprimerNodo(t2);
                    
                    actual = t2;                    
                    
                    if (i==1 && j==lista.longitudLista()-1)
                        lista.setultimoNodo(actual.sig);
                }
                anterior = actual;
                actual = actual.sig;
            }
        }
    }
    
    public static void burbujaEdad(){
        for (int i=1; i<lista.longitudLista(); i++){
            NodoEstudiante actual = lista.primerNodo();
            for (int j=0; j<lista.longitudLista()-1; j++){
                if(actual.datos.getEdad()>actual.sig.datos.getEdad()){
                    Estudiante tmp = actual.datos;
                    actual.datos = actual.sig.datos;
                    actual.sig.datos = tmp;
                }
                
                actual = actual.sig;
            }
        }
    }
    
    public static void seleccionCarne(){
        NodoEstudiante masPequenio = lista.primerNodo();
        NodoEstudiante tmp = masPequenio;
        
        for (int i=0; i<lista.longitudLista()-1; i++){
            NodoEstudiante actual = tmp.sig;
            for (int j=i+1; j<lista.longitudLista(); j++){
                if (actual.datos.getCarne()<masPequenio.datos.getCarne())
                    masPequenio = actual;
                actual = actual.sig;
            }            
           intercambiar(tmp, masPequenio);
           tmp = tmp.sig;
           masPequenio = tmp;
        }
    }
    
    public static void seleccionEdad(){
        NodoEstudiante masPequenio = lista.primerNodo();
        NodoEstudiante tmp = masPequenio;
        
        for (int i=0; i<lista.longitudLista()-1; i++){
            NodoEstudiante actual = tmp.sig;
            for (int j=i+1; j<lista.longitudLista(); j++){
                if (actual.datos.getEdad()<masPequenio.datos.getEdad())
                    masPequenio = actual;
                actual = actual.sig;
            }            
           intercambiar(tmp, masPequenio);
           tmp = tmp.sig;
           masPequenio = tmp;
        }
    }
    
    public static void intercambiar(NodoEstudiante primero, NodoEstudiante segundo){
        Estudiante tmp = primero.datos;
        primero.datos = segundo.datos;
        segundo.datos = tmp;
    }
    
    public static void insercionCarne(){
        Estudiante insercion;
        NodoEstudiante2 actual = lista2.primerNodo().sig;
        
        for (int i=1; i<lista2.longitudLista(); i++){
            insercion = actual.datos;
            
            NodoEstudiante2 moverElemento = actual;
            
            while (moverElemento!=null && moverElemento.ant.datos.getCarne()>insercion.getCarne()){
                moverElemento.datos = moverElemento.ant.datos;
                moverElemento = moverElemento.ant;
                if (moverElemento.ant == null)
                    break;
            }
            
            moverElemento.datos = insercion;
            actual = actual.sig;
        }
    }
    
    public static void insercionEdad(){
        Estudiante insercion;
        NodoEstudiante2 actual = lista2.primerNodo().sig;
        
        for (int i=1; i<lista2.longitudLista(); i++){
            insercion = actual.datos;
            
            NodoEstudiante2 moverElemento = actual;
            
            while (moverElemento!=null && moverElemento.ant.datos.getEdad()>insercion.getEdad()){
                moverElemento.datos = moverElemento.ant.datos;
                moverElemento = moverElemento.ant;
                if (moverElemento.ant == null)
                    break;
            }
            
            moverElemento.datos = insercion;
            actual = actual.sig;
        }
    }
    
    public static void quicksortCarne(NodoEstudiante2 nodoizq, NodoEstudiante2 nododer){
        Estudiante pivote = nodoizq.datos;
        int i=-1, j=-1, izq, der;
        NodoEstudiante2 nodoi = nodoizq;
        NodoEstudiante2 nodoj = nododer;
        Estudiante aux;
        
        NodoEstudiante2 actual = lista2.primerNodo();
        while(actual!=null){
            i++;
            if(actual==nodoizq) break;
            actual = actual.sig;
        }
        
        actual = lista2.primerNodo();
        while(actual!=null){
            j++;
            if(actual==nododer) break;
            actual = actual.sig;
        }
        izq = i;
        der = j;
        
        while(i<j){
            while(nodoi.datos.getCarne()<=pivote.getCarne() && i<j){
                i++;
                nodoi = nodoi.sig;
            }
            while(nodoj.datos.getCarne()>pivote.getCarne()){
                j--;
                nodoj = nodoj.ant;
            }
            if (i<j){
                aux = nodoi.datos;
                nodoi.datos = nodoj.datos;
                nodoj.datos = aux;
            }
        }
        
        nodoizq.datos = nodoj.datos;
        nodoj.datos = pivote;
        
        if(izq<j-1)
            quicksortCarne(nodoizq, nodoj.ant);
        if(j+1<der)
            quicksortCarne(nodoj.sig, nododer);
    }
    
    public static void quicksortEdad(NodoEstudiante2 nodoizq, NodoEstudiante2 nododer){
        Estudiante pivote = nodoizq.datos;
        int i=-1, j=-1, izq, der;
        NodoEstudiante2 nodoi = nodoizq;
        NodoEstudiante2 nodoj = nododer;
        Estudiante aux;
        
        NodoEstudiante2 actual = lista2.primerNodo();
        while(actual!=null){
            i++;
            if(actual==nodoizq) break;
            actual = actual.sig;
        }
        
        actual = lista2.primerNodo();
        while(actual!=null){
            j++;
            if(actual==nododer) break;
            actual = actual.sig;
        }
        izq = i;
        der = j;
        
        while(i<j){
            while(nodoi.datos.getEdad()<=pivote.getEdad() && i<j){
                i++;
                nodoi = nodoi.sig;
            }
            while(nodoj.datos.getEdad()>pivote.getEdad()){
                j--;
                nodoj = nodoj.ant;
            }
            if (i<j){
                aux = nodoi.datos;
                nodoi.datos = nodoj.datos;
                nodoj.datos = aux;
            }
        }
        
        nodoizq.datos = nodoj.datos;
        nodoj.datos = pivote;
        
        if(izq<j-1)
            quicksortEdad(nodoizq, nodoj.ant);
        if(j+1<der)
            quicksortEdad(nodoj.sig, nododer);
    }
    
    public static Estudiante busquedaLineal(int carne){
        NodoEstudiante actual = lista.primerNodo();
        
        while (actual!=null){
            if (actual.datos.getCarne()==carne){
                System.out.println(actual.datos.toString());
                return actual.datos;
            }
            actual = actual.sig; 
       }
        
       return null;
    }
    
    public static Estudiante busquedaBinaria(int carne){
        NodoEstudiante2 inferior = lista2.primerNodo();
        NodoEstudiante2 superior = lista2.ultimoNodo();
        int i = 0, s = lista2.longitudLista()-1;
        int m = lista2.longitudLista()/2;
        NodoEstudiante2 medio = inferior;
        NodoEstudiante2 ubicacion = null;
        
        for (int j=0; j<m;j++) medio = medio.sig;
        
        do{
            if (carne==medio.datos.getCarne())
                ubicacion = medio;
            else if (carne<medio.datos.getCarne()){
                superior = medio.ant;
                s = m - 1;
            }else{
                inferior = medio.sig;
                i = m + 1;
            }
            
            m = (i + s + 1)/2;
            medio = lista2.primerNodo();
            for (int j=0; j<m;j++) medio = medio.sig;
        } while ((i<=s) && (ubicacion==null));
        
        System.out.println(ubicacion);
        return ubicacion.datos;
    }
}
