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
public class ListaSimple {

    private NodoEstudiante primerNodo;
    private NodoEstudiante ultimoNodo;
    private String nombre;
    private int longitud;

    public ListaSimple() {
        this("lista");
    }

    public ListaSimple(String nombreLista) {
        nombre = nombreLista;
        primerNodo = ultimoNodo = null;
        longitud = 0;
    }

    public void insertarAlFrente(Estudiante est) {
        if (estaVacia()) {
            primerNodo = ultimoNodo = new NodoEstudiante(est);
        } else {
            primerNodo = new NodoEstudiante(est, primerNodo);
        }

        longitud++;
    }

    public void insertarAlFinal(Estudiante est) {
        if (estaVacia()) {
            primerNodo = ultimoNodo = new NodoEstudiante(est);
        } else {
            ultimoNodo = ultimoNodo.sig = new NodoEstudiante(est);
        }

        longitud++;
    }

    public Estudiante EliminarDelFrente() throws ExcepcionListaVacia {
        if (estaVacia()) {
            throw new ExcepcionListaVacia(nombre);
        }

        Estudiante est = primerNodo.datos;

        if (primerNodo == ultimoNodo) {
            primerNodo = ultimoNodo = null;
        } else {
            primerNodo = primerNodo.sig;
        }

        longitud--;
        return est;
    }

    public Estudiante EliminarDelFinal() throws ExcepcionListaVacia {
        if (estaVacia()) {
            throw new ExcepcionListaVacia(nombre);
        }

        Estudiante est = ultimoNodo.datos;

        if (primerNodo == ultimoNodo) {
            primerNodo = ultimoNodo = null;
        } else {
            NodoEstudiante actual = primerNodo;

            while (actual.sig != ultimoNodo) {
                actual = actual.sig;
            }

            ultimoNodo = actual;
            actual.sig = null;
        }

        longitud--;
        return est;
    }

    public boolean estaVacia() {
        return primerNodo == null;
    }

    public int longitudLista() {
        return longitud;
    }

    public NodoEstudiante primerNodo() {
        return primerNodo;
    }
    
    public void setprimerNodo(NodoEstudiante nodo) {
        primerNodo = nodo;
    }

    public NodoEstudiante ultimoNodo() {
        return ultimoNodo;
    }
    
    public void setultimoNodo(NodoEstudiante nodo) {
        ultimoNodo = nodo;
    }

    public void imprimir() {
        if (estaVacia()) {
            System.out.printf("%s vacia\n", nombre);
            return;
        }

        System.out.printf("La %s es:\n", nombre);
        NodoEstudiante actual = primerNodo;

        while (actual != null) {
            System.out.printf("%s ", actual.datos);
            actual = actual.sig;
        }

        System.out.println("\n");
    }
}
