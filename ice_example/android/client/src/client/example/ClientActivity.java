package client.example;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;

public class ClientActivity extends Activity {
	

	// Create an anonymous implementation of OnClickListener
	private OnClickListener printButtonListener = new OnClickListener() {
	    public void onClick(View v) {
	    	// Capture our edit text from layout
	        EditText log = (EditText) findViewById(R.id.log);
	        log.append("Lets call the printer class !!!\n");
	    }
	};

	
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        setContentView(R.layout.main);
        
        // Capture our button from layout
        Button button = (Button)findViewById(R.id.printButton);
        
        // Register the onClick listener with the Activity that implements
        button.setOnClickListener(printButtonListener);
    }
}