package br.ufsc.identification;

public class RFIDAcquirerService extends IdentificationAcquirer {

	public RFIDAcquirerService(){
		super ("br.ufsc.identification.RFIDAcquirerService");
	}
	
	@Override
	protected Identification pollForIdentification() {
		// Will return only if a tag is found		
		try {
			Thread.sleep(5000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		String s = getIdFromReader();
		if (s.contains("Error"))
			return new NullIdentification();
		else
			return new RFID(s);
	}
			
	private native String getIdFromReader();
	
	static{
		System.loadLibrary("usb");
		System.loadLibrary("rfid_handler");
	}
}
