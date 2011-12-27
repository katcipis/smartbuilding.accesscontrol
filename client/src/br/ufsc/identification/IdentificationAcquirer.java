package br.ufsc.identification;

import android.app.IntentService;
import android.content.Intent;

public abstract class IdentificationAcquirer extends IntentService {
	
	/* Every identification acquirer service must implement this method. 
	 * It abstracts the way an identification is obtained from a device, such a camera or RFID reader 
	 * */
	protected abstract Identification pollForIdentification();
	
	protected IdentificationAcquirer(String name) {
		super(name);
	}
	
	@Override
	protected void onHandleIntent(Intent arg0) {
		/* poll the RFID reader forever */
		while (true) {
	        Identification id = pollForIdentification();
            AccessGranter.grantAccess(id, this);
		}
	}
}
