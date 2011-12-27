package br.ufsc.identification;

public class NullIdentification implements Identification {

	public boolean equals(Identification id) {
		// NULL Identification is never equal to any other id.
		return false;
	}

}
