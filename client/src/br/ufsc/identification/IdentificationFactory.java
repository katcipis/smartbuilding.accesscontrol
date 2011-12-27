package br.ufsc.identification;

public class IdentificationFactory {

	public static Identification fromDatabaseId(Database.Identification db_id) {
		// this solution is bad, but avoiding this on java is awfull =/
		// http://stackoverflow.com/questions/934509/java-equivalent-of-function-mapping-in-python
		// Good example of bad design pattern based on the lack of useful facilities on a language.
		
		if (db_id.type == Database.IDType.RFID) {
			return new RFID(db_id);
		}
		
		return new NullIdentification();
	}

}
