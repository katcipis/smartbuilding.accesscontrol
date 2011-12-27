package br.ufsc.utils;

import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.Enumeration;

public class NetworkUtils {
	
	private static String ip_address = null;
	
	public static String getIpAddress() throws SocketException{
		
		if (ip_address != null) {
			/* If we registered with a ip we must always use that ip, 
			 * so lets guarantee that this function always return the same ip ;-) */
			return ip_address;
		}
		
		Enumeration<NetworkInterface> ifaces =  NetworkInterface.getNetworkInterfaces();
		
		while(ifaces.hasMoreElements()) {
			
			NetworkInterface iface = ifaces.nextElement();
			
			if ((!iface.isLoopback()) && iface.isUp()) {
				
				Enumeration<InetAddress> addrs = iface.getInetAddresses();
				
				while (addrs.hasMoreElements()) {
					
					InetAddress address = addrs.nextElement();
					
					if ((!(address.isAnyLocalAddress() || address.isLoopbackAddress())) && (address instanceof Inet4Address)) {
						ip_address = address.getHostAddress();
						return ip_address;
					}
				}
			} 
		}/* Python is great, look at these braces :-) */
		
		return "NO VALID IP ADDRESS FOUND !!!";
	}
}
