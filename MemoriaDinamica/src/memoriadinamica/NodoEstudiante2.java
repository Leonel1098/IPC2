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
public class NodoEstudiante2 {
    Estudiante datos;
    NodoEstudiante2 ant;
    NodoEstudiante2 sig;

    public NodoEstudiante2(Estudiante est) {
        this(est, null, null);
    }
    
    public NodoEstudiante2(Estudiante est, NodoEstudiante2 nodo1, NodoEstudiante2 nodo2) {
        datos = est;
        ant = nodo1;
        sig = nodo2;
    }
    
    Estudiante obtenerEstudiante(){
        return datos;        
    }
    
    NodoEstudiante2 obtenerAnterior(){
        return ant;
    }
    
    NodoEstudiante2 obtenerSigiente(){
        return sig;
    }
}
