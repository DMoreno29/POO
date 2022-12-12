package vehiculos;

public class Automovil extends Vehiculo{
	private static int cantidadAutomoviles;
	private int puestos;
	
	public Automovil(String placa, String nombre, double precio, 
			double peso, Fabricante fabricante, int puestos) {
		super(placa, 4, 100, nombre, precio, peso, "FWD", fabricante);
		this.puestos = puestos;
		cantidadAutomoviles++;
	}
	public Automovil() {
		cantidadAutomoviles++;
	}
	
	public int getPuestos() {
		return puestos;
	}
	public void setPuestos(int puestos) {
		this.puestos = puestos;
	}
	public static int cantidadAutomoviles() {
		return cantidadAutomoviles;
	}
}
