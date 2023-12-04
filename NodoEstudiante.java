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
public class NodoEstudiante {
    Estudiante datos;
    NodoEstudiante sig;

    public NodoEstudiante(Estudiante est) {
        this(est, null);
    }
    
    public NodoEstudiante(Estudiante est, NodoEstudiante nodo) {
        datos = est;
        sig = nodo;
    }
    
    Estudiante obtenerEstudiante(){
        return datos;        
    }
    
    NodoEstudiante obtenerSigiente(){
        return sig;
    }
}
