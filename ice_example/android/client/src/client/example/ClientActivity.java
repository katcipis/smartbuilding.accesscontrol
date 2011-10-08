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
	        
	        //Lets do basic ICE stuff
	        Ice.Communicator ic = null;
	        try {
	        	log.append("Initializing ICE\n");
	            ic = Ice.Util.initialize();
	            log.append("Initialized ICE, creating Object proxy\n");
	            
	            Ice.ObjectPrx base = ic.stringToProxy("SimplePrinter:default -p 10000");
	            log.append("Created Object proxy, casting to Printer proxy\n");
	            
	            Demo.PrinterPrx printer = Demo.PrinterPrxHelper.checkedCast(base);
	            log.append("Casted to Printer proxy\n");
	            
	            if (printer == null) {
	            	log.append("Cast to Printer proxy FAILED\n");
	                throw new Error("Invalid proxy");
	            }

	            log.append("Cast to Printer proxy SUCCESS, calling method\n");
	            printer.printString("Hello World from Android !!!");
	            
	        } catch (Ice.LocalException e) {
	            e.printStackTrace();
	            log.append("EXCEPTION: " + e.getMessage());
	        } catch (Exception e) {
	            System.err.println(e.getMessage());
	            log.append("EXCEPTION: " + e.getMessage());
	        }
	        if (ic != null) {
	            // Clean up
	            try {
	            	log.append(" Destroying ic\n");
	                ic.destroy();
	            } catch (Exception e) {
	                System.err.println(e.getMessage());
	                log.append("EXCEPTION: " + e.getMessage());
	            }
	        }

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