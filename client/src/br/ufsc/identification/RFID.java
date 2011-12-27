package br.ufsc.identification;

public class RFID implements Identification {

	private String id = "";

	@Override
	public String toString(){
		return id;
	}
	
	public RFID(String id){
		this.id = id;
	}
	
	public RFID(Database.Identification id) {
		this.id = id.data;
	}
	
	public boolean equals(Identification id) {
		if (!(id instanceof RFID)) {
			return false;
		}
		RFID otherId = (RFID) id;
		return otherId.getId().contains(getId()) || getId().contains(otherId.getId());
	}

	private String getId() {
		return id;
	}

}
