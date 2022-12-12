package comunicacion;
public class Alfabeto extends Pictograma{
	private static String letras[];
	private String interpretacion;
	
	public static String[] getLetras() {
		return letras;
	}
	public static void setLetras(String[] letras) {
		Alfabeto.letras = letras;
	}
	public String getInterpretacion() {
		return interpretacion;
	}
	public void setInterpretacion(String interpretacion) {
		this.interpretacion = interpretacion;
	}
	
	public Alfabeto(String origen, String[] alfabeto, String interpretacion) {
		super(origen);
		Alfabeto.letras = alfabeto;
		this.interpretacion = interpretacion;
		
	}
	
	public int cantidadLetras() {
		return getLetras().length;
	}
	
	
	public String interpretacion() {
		return getInterpretacion();
	}
	
	
	public String toString() {
		String salida = null;
		for(String word: letras)
		{
			salida += ", " + word;
		}
		return salida.substring(6);
	}
}
