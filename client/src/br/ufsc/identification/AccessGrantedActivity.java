package br.ufsc.identification;

import br.ufsc.register.R;
import android.app.Activity;
import android.os.Bundle;

public class AccessGrantedActivity extends Activity {
	
	/** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.access_granted);
    }

}
