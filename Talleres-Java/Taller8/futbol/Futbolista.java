package futbol;

public abstract class Futbolista implements Comparable{
	private String nombre;
	private int edad;
	private String posicion;
	
	protected Futbolista(String nombre, int edad, String posicion) {
		this.nombre = nombre;
		this.edad = edad;
		this.posicion = posicion;
	}
	
	protected Futbolista() {
		this.nombre = "Maradona";
		this.edad = 30;
		this.posicion = "delantero";
	}
	
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public String getPosicion() {
		return posicion;
	}

	public void setPosicion(String posicion) {
		this.posicion = posicion;
	}

	public String toString() {
		return "El futbolista " +nombre+
				" tiene " +edad+
				", y juega de " +posicion;
	}
	
	public boolean equals(Futbolista f) {
		return (this == f);
	}
	
	public abstract boolean jugarConLasManos();
	
	public abstract int compareTo(Object X);
}