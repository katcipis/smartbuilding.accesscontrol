package br.ufsc.register;

import java.net.SocketException;

import br.ufsc.utils.NetworkUtils;
import Database.DeviceRegisterServerPrx;
import Database.DeviceRegisterServerPrxHelper;


public class RegisterClientThread extends Thread {

	private RegisterClientActivity registerActivity;
	private Ice.Communicator ic;
	private String deviceIP;
	private Integer deviceRoom;
	private String serverIP;
	private String serverPort;
	
	RegisterClientThread (String serverIP, 
			              String serverPort,
			              String room,
			              RegisterClientActivity registerActivity) throws SocketException {
		super();
		
		this.registerActivity = registerActivity;
		this.serverIP = serverIP;
		this.serverPort = serverPort;
		
		this.deviceIP = NetworkUtils.getIpAddress();
		this.deviceRoom = Integer.parseInt(room);
	}
	
	@Override
	public void run(){
		try {
            // Create a communicator
            ic = Ice.Util.initialize();
            
            // Create a proxy for the register server
            Ice.ObjectPrx base = ic.stringToProxy("DeviceRegisterServerInstance:default -h " + serverIP + " -p " + serverPort);
        
            if (base == null) {
        	    return;
            }
            
            // Down-cast the proxy to a DeviceRegisterServer proxy
            DeviceRegisterServerPrx server = DeviceRegisterServerPrxHelper.checkedCast(base);
           
            if (server == null){
             	return;
            }
            
            //Register and get allowed persons            
            registerActivity.saveAllowedPersons(server.register(deviceIP, deviceRoom));
            registerActivity.showAllowedPersons();
            registerActivity.startCacheService();
        
            if (ic != null) {
                // Clean up
               ic.destroy();
            }
            
            registerActivity.logMessage("registered");
		} catch (Exception e) {
			registerActivity.logMessage(e.getMessage());
		}
	}
}
