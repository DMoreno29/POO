package vehiculos;

public class Camioneta extends Vehiculo{
	private static int cantidadCamionetas;
	private boolean volco;
	
	public Camioneta(String placa, int puertas, String nombre, double precio, double peso,
			Fabricante fabricante, boolean volco) {
		super(placa, puertas, 90, nombre, precio, peso, "4X4", fabricante);
		this.volco = volco;
		cantidadCamionetas++;
	}
	public Camioneta() {
		cantidadCamionetas++;
	}
	
	public boolean isVolco() {
		return volco;
	}
	public void setVolco(boolean volco) {
		this.volco = volco;
	}
	public static int cantidadCamionetas() {
		return cantidadCamionetas;
	}

}
