package br.ufsc.cache;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.StreamCorruptedException;
import java.util.LinkedList;
import java.util.List;
import Database.Person;
import android.content.Context;



public class AllowedPersonsCache {
	
	private static final String allowed_persons_cache = "allowed-persons-cache.data";
	
    static public void save(Database.Person[] allowed,
		                    Context context) throws IOException {
    	
        FileOutputStream cache_file = null;
		ObjectOutputStream persons_output_stream = null;
		
	
		cache_file = context.openFileOutput(allowed_persons_cache, Context.MODE_MULTI_PROCESS | 
		        		                                           Context.MODE_WORLD_READABLE |
		        		                                           Context.MODE_WORLD_WRITEABLE);
		persons_output_stream = new ObjectOutputStream(cache_file);
				    
								
		for (int i = 0; i < allowed.length; i++) {
		  	persons_output_stream.writeObject(allowed[i]);	
		}
    
		persons_output_stream.close();
		cache_file.close();
    }
    
    static public void flush (Context context){
    	context.deleteFile(allowed_persons_cache);
    }
    
    static public List<Person> load(Context context) throws StreamCorruptedException, IOException, ClassNotFoundException {
    	
    	List<Database.Person> allowed_person = new LinkedList<Database.Person>();
    	FileInputStream cache_file = null;
    	ObjectInputStream persons_input_stream = null;
    	
    	try {
    	    cache_file = context.openFileInput(allowed_persons_cache);
    	} catch (FileNotFoundException e) {
    		return new LinkedList<Database.Person>();
    	}
    	
    	persons_input_stream = new ObjectInputStream(cache_file);
    	
    	try {    	
    	    while (true) {
    	    	/*YES WHILE TRUE, THANK YOU JAVA ;-) */
    	        allowed_person.add((Database.Person) persons_input_stream.readObject());
    	    }
    	    
    	} catch (EOFException e) {
    		/* i just HATE java, can you believe that i must read until an exception is throw? OMG!!!
    		   http://www.javadb.com/reading-objects-from-file-using-objectinputstream */
    	} 
    	    	
    	persons_input_stream.close();
    	cache_file.close();
    	
    	return allowed_person;
    }
    		
}
