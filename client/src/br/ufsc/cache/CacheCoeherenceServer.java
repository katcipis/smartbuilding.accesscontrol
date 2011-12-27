package br.ufsc.cache;

import java.net.SocketException;

import br.ufsc.utils.NetworkUtils;
import android.content.Context;

public class CacheCoeherenceServer extends Thread {
	
	private static final String server_port = "7778";
	
	private Context context;
	private Ice.Communicator iceCommunicator;
	private String server_host;
	
	public CacheCoeherenceServer(Context context) throws SocketException {
		this.context = context;
		this.server_host = NetworkUtils.getIpAddress();
	}

	@Override
	public void run(){
		
		try {
			iceCommunicator = Ice.Util.initialize();
			Ice.ObjectAdapter adapter =
					iceCommunicator.createObjectAdapterWithEndpoints("CacheCoeherenceServerAdapter", "default -h " + server_host +" -p " + server_port);
	        Ice.Object object = new CacheCoeherenceServerI(this.context);
	        adapter.add(object, iceCommunicator.stringToIdentity("CacheCoeherenceServerInstance"));
	        adapter.activate();
	        iceCommunicator.waitForShutdown(); //This will block until destroy is called ;-)
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}
	
	public void destroy(){
		if (iceCommunicator != null) {
			iceCommunicator.destroy();
			iceCommunicator = null;
		}
	}
}
