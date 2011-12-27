package br.ufsc.cache;

import java.io.IOException;

import android.content.Context;
import Database.Person;
import Ice.Current;

public class CacheCoeherenceServerI extends Database._CacheCoeherenceServerDisp {

	/**
	 * 
	 */
	private static final long serialVersionUID = 412516134377653172L;
	private Context context;

	public CacheCoeherenceServerI(Context context) {
		this.context = context;
	}

	public void update(Person[] persons, Current __current) {
		try {
			AllowedPersonsCache.save(persons, context);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
}
