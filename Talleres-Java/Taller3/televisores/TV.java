package taller3.televisores;

public class TV {
	private Marca marca;
	private int canal = 1;
	 private int precio = 500;
	private boolean estado;
	private int volumen = 1;
	private Control control;
	static int numTV = 0;
	
	public TV(Marca marca, boolean estado){
		this.marca = marca;
		this.estado = estado;
		numTV++;
	}
	
	public Marca getMarca() {
		return this.marca;
	}
	public Control getControl() {
		return this.control;
	}
	public int getPrecio() {
		return this.precio;
	}
	public int getVolumen() {
		return this.volumen;
	}
	public int getCanal() {
		return this.canal;
	}
	
	public void setMarca(Marca marca) {
		this.marca = marca;
	}
	public void setControl(Control control) {
		this.control = control;
	}
	public void setPrecio(int precio) {
		this.precio = precio;
	}
	public void setVolumen(int volumen) {
		if(volumen >= 0 && volumen <= 7 && this.estado == true) {
			this.volumen = volumen;
		}
	}
	public void setCanal(int canal) {
		if(canal >= 1 && canal <= 120 && this.estado == true) {
			this.canal = canal;
		}
	}
	
	public void turnOn() {
		this.estado = true;
	}
	public void turnOff() {
		this.estado = false;
	}
	
	public boolean getEstado() {
		return this.estado;
	}
	
	public void canalUp() {
		if(this.estado == true && this.canal <= 119) {
			this.canal++;
		}
	}
	public void canalDown() {
		if( this.estado == true && this.canal >= 2) {
			this.canal--;
		}
	}
	public void volumenUp() {
		if( this.estado == true && this.volumen <= 6) {
			this.volumen++;
		}
	}
	public void volumenDown() {
		if( this.estado == true && this.volumen >= 1) {
			this.volumen--;
		}
	}
	
	public static void setNumTV(int eVal) {
		numTV = eVal;
	}
	public static int getNumTV() {
		return numTV;
	}
}
