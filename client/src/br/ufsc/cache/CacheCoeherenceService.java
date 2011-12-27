package br.ufsc.cache;

import java.net.SocketException;

import android.app.IntentService;
import android.content.Intent;
import android.util.Log;

public class CacheCoeherenceService extends IntentService {

	private static CacheCoeherenceServer server;
	
	public CacheCoeherenceService() {
		super("br.ufsc.cache.CacheCoeherenceService");
	}

	@Override
	protected void onHandleIntent(Intent arg0) {
		try {
			if (server == null) {
				/* The server runs forever, lets not block any android thread.
				   Only one server must be running on the entire system */
			    server = new CacheCoeherenceServer(this);
			    server.start();
			}
		} catch (SocketException e) {
			Log.e("CacheCoeherenceService", "SocketException: " + e.toString() + " : " + e.getMessage());
		}
		
	}

}
