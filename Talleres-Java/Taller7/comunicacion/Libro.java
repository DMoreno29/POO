package comunicacion;

public class Libro extends Escrito{
	private String co_autor;
	private String editorial;
	private String edicion;
	private String interpretacion;
	
	public Libro(String origen, String titulo, String autor, int paginas,
			String co_autor, String editorial, String edicion, String interpretacion) {
		super(origen, titulo, autor, paginas);
		this.co_autor = co_autor;
		this.edicion = edicion;
		this.editorial = editorial;
		this.interpretacion = interpretacion;
	}
	
	
	public String getCo_autor() {
		return co_autor;
	}


	public void setCo_autor(String co_autor) {
		this.co_autor = co_autor;
	}


	public String getEditorial() {
		return editorial;
	}


	public void setEditorial(String editorial) {
		this.editorial = editorial;
	}


	public String getEdicion() {
		return edicion;
	}


	public void setEdicion(String edicion) {
		this.edicion = edicion;
	}


	public String getInterpretacion() {
		return interpretacion;
	}


	public void setInterpretacion(String interpretacion) {
		this.interpretacion = interpretacion;
	}


	
	public int palabrasTotales(int parametro) {
		return (getPaginas()*2)*parametro;
	}
	
	public String interpretacion() {
		return getInterpretacion();
	}
	
	public String toString() {
		return super.getOrigen() + "\n"
				+ super.getTitulo() + "\n"
				+ super.getAutor() + "\n"
				+ super.getPaginas() + "\n"
				+ getCo_autor() + "\n"
				+ getEditorial() + "\n"
				+ getEdicion();
						
	}
}
