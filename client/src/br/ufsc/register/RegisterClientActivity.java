package br.ufsc.register;

import java.io.IOException;
import java.io.StreamCorruptedException;
import java.util.List;

import br.ufsc.cache.AllowedPersonsCache;
import Database.Person;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class RegisterClientActivity extends Activity {
	
    private static boolean cacheServiceIsRunning = false;
    private static boolean rfidAcquirerServiceIsRunning = false;

	/** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        startRFIDAcquirerService();
        addRegisterCallback();
        addFlushCacheCallback();
        addFlushLogCallback();
        addLoadCacheCallback();
    }

	private void startRFIDAcquirerService() {
		if (rfidAcquirerServiceIsRunning) {
			return;
		}
	
      	logMessage("Starting RFID acquirer service");
      	rfidAcquirerServiceIsRunning = true;
		startService(new Intent("br.ufsc.identification.RFIDAcquirerService"));
    }

	private void addFlushLogCallback() {
		final Button button = (Button) findViewById(R.id.flush_log);
        
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {                
            	EditText log = (EditText) findViewById(R.id.log);
            	log.setText("");
            }
        });
		
	}

	private void addLoadCacheCallback() {
		final Button button = (Button) findViewById(R.id.load_cache);
        
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {                
                showAllowedPersons();
            }
        });
		
	}

	private void addFlushCacheCallback() {
		final Button button = (Button) findViewById(R.id.flush_cache);
        final RegisterClientActivity registerActivity = this;
        
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {                
                try {
                    AllowedPersonsCache.flush(registerActivity);
                } catch (Exception e) {
                	logMessage(e.getMessage());
                	return;
                }
                
                logMessage ("flushed cache");
            }
        });
		
	}

	private void addRegisterCallback() {
		final Button button = (Button) findViewById(R.id.register);
        final RegisterClientActivity registerActivity = this;
        
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
            	RegisterClientThread register;
                EditText serverIP, serverPort, room;
                
                try {
                    serverIP = (EditText)findViewById(R.id.server_ip);
                    serverPort = (EditText)findViewById(R.id.server_port);
                    room = (EditText)findViewById(R.id.room);
                
                    register = new RegisterClientThread(serverIP.getText().toString(), 
                		                                serverPort.getText().toString(),
                		                                room.getText().toString(),
                		                                registerActivity);
                } catch (Exception e) {
                	registerActivity.logMessage(e.getMessage());
                	return;
                }
                
                register.start();
            }
        });
        
	}
    
    public void logMessage(final String message){
    	//This may not be called from the ui thread
    	this.runOnUiThread(new Runnable(){
    		
    		public void run(){
    			
    			EditText log = (EditText) findViewById(R.id.log);
    			log.append(message + "\n");
    		}
    	});
    }
    
    public void showAllowedPersons(){
    	
    	final Context context = this;
    	
    	this.runOnUiThread(new Runnable(){
    		
    		public void run(){
					List<Person> allowed = null;
					
					try {
						allowed = AllowedPersonsCache.load(context);
					} catch (StreamCorruptedException e) {
						logMessage("StreamCorruptedException: " + e.toString());
						return;
					} catch (IOException e) {
						logMessage("IOException: " + e.toString());
						return;
					} catch (ClassNotFoundException e) {
						logMessage("ClassNotFoundException: " + e.toString());
						return;
					}
					
                    EditText list = (EditText) findViewById(R.id.allowed_persons);
					list.setText("");
	    			
					if (allowed.size() == 0) {
						logMessage("No allowed people");
						return;
					}
								
    			    for (Database.Person person : allowed) {
    				    String person_data = "Name: " + person.name + " Ids: ";
    				
    			     	for (Database.Identification id : person.ids) {
    				    	person_data += "id-type[" + id.type + "] ";
    					    person_data += "id-data[" + id.data + "]";
    				    }
    				
    				    person_data += "\n";
    				    list.append(person_data);
    			    }
    			    
    			    logMessage("cache loaded");
				
    		}
    		
    	});
    }
    
    public void saveAllowedPersons(Database.Person[] allowed){
    	
    	//This may not be called from the ui thread
    	final Database.Person[] allowed_copy = allowed.clone();
    	final Context context = this;
    	
    	this.runOnUiThread(new Runnable(){
    		
    		public void run(){
    			
			    try {
					AllowedPersonsCache.save(allowed_copy, context);
				} catch (IOException e) {
					logMessage("IOException: " + e.toString());
				}
    		}
    		
    	});
    }

	public void startCacheService() {		
        this.runOnUiThread(new Runnable(){
    		
    	    public void run(){
    	    	if (cacheServiceIsRunning) {
    	    		return;
    	    	}
    	    	logMessage("Starting cache coeherence service");
    	    	cacheServiceIsRunning = true;
				startService(new Intent("br.ufsc.cache.CacheCoeherenceService"));
            }
    		
    	});
		
	}
}