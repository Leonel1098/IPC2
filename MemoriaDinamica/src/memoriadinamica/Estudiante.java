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
public class Estudiante {
    private int carne;
    private String nombre;
    private int edad;
    private String correo;
    
    public Estudiante (int carne, String nombre, int edad, String correo){
        this.carne = carne;
        this.nombre = nombre;
        this.edad = edad;
        this.correo = correo;
    }

    public int getCarne(){
        return carne;
    }

    public int getEdad(){
        return edad;
    }
    
    @Override
    public String toString(){
        return "Carné: " + carne + ", Nombre: " + nombre + ", Edad: " + edad + ", Correo: " + correo + "\n";
    }
}
